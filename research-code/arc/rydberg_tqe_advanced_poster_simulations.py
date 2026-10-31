#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced simulation workflow for a magnetically-biased 87Rb Rydberg RF receiver
for polarisation estimation.

Purpose
-------
Generate publication/poster-grade figures that answer four linked thesis questions:

    Fig. 1  Is there a physically plausible 87Rb transition that simultaneously fits
            the RF hardware and the verified 480-nm coupling-laser tuning window?
    Fig. 2  How does magnetic bias separate the sigma-/pi/sigma+ RF pathways?
    Fig. 3  At equal RF field magnitude, do different polarisation states generate
            distinguishable optical spectral fingerprints?
    Fig. 4  At what (B0, RF detuning) operating point is the spectrum locally most
            informative about the two polarisation degrees of freedom?

An optional Fig. 5 maps a grid of Stokes states into a low-dimensional spectral
manifold using SVD/PCA, useful for a poster or website.

Scientific scope / claim boundary
---------------------------------
* Atomic frequencies, transition wavelengths, magnetic sublevels, dipole matrix
  elements and state lifetimes are calculated with ARC. There is deliberately NO
  quantum-defect fallback: if ARC is absent, the script stops instead of producing
  approximate numbers that might be mistaken for final results.
* The RF-dressed Rydberg manifold is treated coherently across all m_J sublevels.
  Arbitrary elliptical RF polarisation is decomposed into spherical q = -1,0,+1
  components relative to B0 and the corresponding ARC matrix elements are used.
* Optical readout uses a transparent weak-probe dressed-state EIT model with 1-D
  thermal Doppler averaging (Gauss-Hermite quadrature). It is suitable for
  simulation-guided feasibility and relative spectral fingerprints.
* It is NOT a calibrated digital twin until measured optical powers/beam waists,
  optical polarisation preparation, RF electric field at the cell, magnetic-field
  map, detector noise and verified laser tuning range are inserted.
* A Rydiqule cross-check is recommended before publication-level quantitative
  claims; the figures produced here are explicitly labelled MODEL.

Units
-----
ARC DME: e a0
ARC transition frequency: Hz
ARC transition wavelength: vacuum m
ARC Zeeman shift: J for B in tesla
Hamiltonian / detunings in this script: cyclic-frequency MHz (NOT Mrad/s)
B0: mT
RF electric field: peak V/m

Install
-------
    python -m pip install numpy scipy matplotlib
    python -m pip install "ARC-Alkali-Rydberg-Calculator>=3.8,<4"

Optional validation:
    python -m pip install "rydiqule>=2.1,<3"

Run
---
    python rydberg_tqe_advanced_poster_simulations.py
    python rydberg_tqe_advanced_poster_simulations.py --quick

Outputs are written to ./rydberg_tqe_outputs.

IMPORTANT BEFORE POSTER USE
---------------------------
Set COUPLING_LASER_WINDOW_NM below to the range VERIFIED on your wavemeter / laser,
not a catalogue or remembered value. If left as None, the script still screens and
plots candidates but clearly marks optical access as UNVERIFIED and does not call any
candidate fully feasible.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import warnings
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from scipy.constants import h, k as k_B, physical_constants, atomic_mass
from numpy.polynomial.hermite import hermgauss


# =============================================================================
# 0. USER-EDITABLE CONFIGURATION
# =============================================================================

OUTDIR = Path("rydberg_tqe_outputs")

# ---- Hardware / thesis bands -------------------------------------------------
# Practical radiated search band. Edit if your antenna/feed chain is narrower.
RF_HARDWARE_BAND_GHZ = (0.40, 6.40)
# Original thesis emphasis; shown as context, not used as a hard gate.
THESIS_TARGET_BAND_GHZ = (1.00, 2.00)
# Frequencies you may want annotations near; NOT forced targets.
REFERENCE_RF_GHZ = (1.80, 2.40, 2.45, 5.00)

# VERIFIED coupling-laser tuning window in VACUUM wavelength, nm.
# Example syntax ONLY: COUPLING_LASER_WINDOW_NM = (479.45, 479.75)
# Leave None until independently verified with the wavemeter.
COUPLING_LASER_WINDOW_NM: Optional[tuple[float, float]] = None

# ---- ARC screening -----------------------------------------------------------
N_MIN = 35
N_MAX = 130
DN_RF_SEARCH = 6
# 5P3/2 -> Rydberg E1 access: primarily S and D manifolds.
OPTICALLY_PREPARED_L = (0, 2)
# Ignore very weak branches relative to the strongest branch of each transition.
PATHWAY_RELATIVE_DME_CUTOFF = 1e-4
MAX_CANDIDATES_TO_ANNOTATE = 8

# Optional manual state override. Set to a tuple
# ((n_r,l_r,j_r), (n_s,l_s,j_s)); otherwise a balanced feasible candidate is chosen.
SELECT_TRANSITION = None
# Example only (DO NOT use unless independently re-verified):
# SELECT_TRANSITION = ((71, 2, 2.5), (72, 1, 1.5))

# ---- Magnetic bias -----------------------------------------------------------
B0_RANGE_MT = (0.0, 2.50)
B0_POINTS_FAN = 251
# Interim local coil calibration (measured): B0[mT] = a*I[A] + b.
COIL_A_MT_PER_A = 2.302
COIL_B_MT = 0.028
COIL_B_RMSE_MT = 0.103

# ---- RF geometry and magnitude ----------------------------------------------
# B0 defines +z. RF wavevector lies in x-z plane at this angle to +z.
# 45 deg is deliberately general: all q components can contribute. Replace with
# the measured geometry of your experiment for final claims.
RF_K_TO_B_DEG = 45.0
# Equal peak |E| is used for every compared polarisation state.
# This is an explicit planning value until the field at the cell is calibrated.
RF_E_PEAK_V_PER_M = 0.20
RF_FIELD_PROVENANCE = "ASSUMED planning value; replace with measured/validated E at vapour cell"

# ---- Optical / EIT model -----------------------------------------------------
# Apparatus/reference values. These are not all measured calibrations.
TEMPERATURE_K = 297.35
CELL_LENGTH_M = 0.075
PROBE_WAVELENGTH_NM_FALLBACK = 780.0
OMEGA_PROBE_MHZ = 0.05
OMEGA_COUPLING_MHZ = 5.0
GAMMA_GE_MHZ = 6.0
GAMMA_R_MHZ = 0.45
EFFECTIVE_OD = 2.0
DELTA_COUPLING_MHZ = 0.0
# Coupling-laser optical preparation. None means an unresolved/incoherent average
# over all accessible 5P3/2 mJ and q paths. Set -1,0,+1 only if geometry/polarisation
# relative to B0 is known.
COUPLING_OPTICAL_Q: Optional[int] = None

# Spectral grids
PROBE_DETUNING_MHZ = (-45.0, 45.0)
PROBE_POINTS_HERO = 1201
PROBE_POINTS_MAP = 241
HERMITE_NODES_FULL = 61
HERMITE_NODES_QUICK = 25

# Identifiability map
B0_MAP_POINTS_FULL = 45
RF_DETUNING_MAP_MHZ = (-30.0, 30.0)
RF_DETUNING_MAP_POINTS_FULL = 61
B0_MAP_POINTS_QUICK = 21
RF_DETUNING_MAP_POINTS_QUICK = 25
# Local polarisation around which the Fisher/Jacobian identifiability is evaluated.
# psi = orientation angle; chi = ellipticity angle. Both in degrees.
IDENTIFIABILITY_REFERENCE_PSI_DEG = 22.5
IDENTIFIABILITY_REFERENCE_CHI_DEG = 12.0
IDENTIFIABILITY_STEP_DEG = 1.0

# Optional Poincare spectral manifold (can take extra time)
MAKE_POINCARE_MANIFOLD = True
POINCARE_PSI_POINTS = 13
POINCARE_CHI_POINTS = 9

# Figure export
EXPORT_PNG_DPI = 600
EXPORT_SVG = True
EXPORT_PDF = True

# TQE-like figure dimensions (inches): ~IEEE single- and double-column widths.
FIG_SINGLE = (3.50, 2.55)
FIG_DOUBLE = (7.16, 4.35)
FIG_DOUBLE_TALL = (7.16, 5.10)


# =============================================================================
# 1. CONSTANTS AND STYLE
# =============================================================================

EA0_C_M = physical_constants["elementary charge"][0] * physical_constants["Bohr radius"][0]
RB87_MASS_KG = 86.909180531 * atomic_mass
L_LETTER = {0: "S", 1: "P", 2: "D", 3: "F", 4: "G", 5: "H"}

# Restrained palette inspired by clean IEEE/TQE figures.
IEEE_BLUE = "#00629B"
IEEE_DARK = "#202020"
IEEE_ORANGE = "#D55E00"
IEEE_GREEN = "#009E73"
IEEE_PURPLE = "#7B2CBF"
IEEE_GREY = "#7F7F7F"
LIGHT_GREY = "#E9ECEF"

Q_COLORS = {-1: IEEE_BLUE, 0: IEEE_DARK, +1: IEEE_ORANGE}
Q_LABEL = {-1: r"$\sigma^{-}$", 0: r"$\pi$", +1: r"$\sigma^{+}$"}


def set_tqe_style(font_scale: float = 1.0) -> None:
    """Compact, publication-clean styling guided by the user's IEEE TQE manuscript."""
    base = 8.0 * font_scale
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "Times", "Nimbus Roman No9 L", "STIXGeneral", "DejaVu Serif"],
        "mathtext.fontset": "stix",
        "font.size": base,
        "axes.labelsize": base,
        "axes.titlesize": base,
        "legend.fontsize": 7.2 * font_scale,
        "xtick.labelsize": 7.2 * font_scale,
        "ytick.labelsize": 7.2 * font_scale,
        "axes.linewidth": 0.8,
        "lines.linewidth": 1.25,
        "xtick.major.width": 0.7,
        "ytick.major.width": 0.7,
        "xtick.minor.width": 0.5,
        "ytick.minor.width": 0.5,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.top": True,
        "ytick.right": True,
        "legend.frameon": False,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.025,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })


def clean_axes(ax):
    ax.tick_params(which="both", direction="in", top=True, right=True)
    for s in ax.spines.values():
        s.set_linewidth(0.8)


def panel_label(ax, label: str):
    ax.text(-0.13, 1.04, label, transform=ax.transAxes,
            ha="left", va="bottom", fontweight="bold")


def save_figure(fig, stem: str):
    OUTDIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTDIR / f"{stem}.png", dpi=EXPORT_PNG_DPI)
    if EXPORT_PDF:
        fig.savefig(OUTDIR / f"{stem}.pdf")
    if EXPORT_SVG:
        fig.savefig(OUTDIR / f"{stem}.svg")
    plt.close(fig)


# =============================================================================
# 2. BASIC HELPERS / IO
# =============================================================================


def write_dict_csv(path: Path, rows: list[dict]):
    if not rows:
        return
    fields = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            clean = {}
            for k_, v in r.items():
                if isinstance(v, np.generic):
                    v = v.item()
                clean[k_] = v
            w.writerow(clean)


def write_matrix_csv(path: Path, row_name: str, row_values, col_name: str, col_values, matrix):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([f"{row_name}\\{col_name}"] + list(col_values))
        for rv, row in zip(row_values, matrix):
            w.writerow([rv] + list(row))


def state_label(n: int, l: int, j: float) -> str:
    return f"{n}{L_LETTER.get(l, '?')}{int(round(2*j))}/2"


def j_values_for_l(l: int) -> list[float]:
    return [0.5] if l == 0 else [l - 0.5, l + 0.5]


def mj_values(j: float) -> np.ndarray:
    two_j = int(round(2 * j))
    return np.arange(-two_j, two_j + 1, 2, dtype=float) / 2.0


def arc_atom_or_die():
    try:
        from arc import Rubidium87
    except Exception as exc:
        raise RuntimeError(
            "ARC is required for this final-quality workflow. Install with:\n"
            "  python -m pip install 'ARC-Alkali-Rydberg-Calculator>=3.8,<4'\n"
            "No approximate quantum-defect fallback is used by design."
        ) from exc
    return Rubidium87()


def robust_minmax(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, float)
    good = np.isfinite(x)
    out = np.zeros_like(x)
    if good.sum() < 2:
        return out
    lo, hi = np.nanpercentile(x[good], [5, 95])
    if hi <= lo:
        return out
    out[good] = np.clip((x[good] - lo) / (hi - lo), 0, 1)
    return out


# =============================================================================
# 3. ARC TRANSITION SCREENING
# =============================================================================

@dataclass
class Pathway:
    q: int
    mj_r: float
    mj_s: float
    dme_ea0: float
    strength_ea0_sq: float
    shift_at_1mT_MHz: float
    slope_MHz_per_mT: float


@dataclass
class Candidate:
    lower: str
    upper: str
    n_r: int
    l_r: int
    j_r: float
    n_s: int
    l_s: int
    j_s: float
    rf_frequency_GHz: float
    coupling_wavelength_nm: float
    max_abs_dme_ea0: float
    total_dme2_ea0_sq: float
    sigma_minus_fraction: float
    pi_fraction: float
    sigma_plus_fraction: float
    q_entropy: float
    zeeman_span_1mT_MHz: float
    lower_lifetime_us_300K: float
    upper_lifetime_us_300K: float
    min_lifetime_us_300K: float
    avg_n: float
    rf_access: bool
    optical_access: bool
    thesis_band: bool
    fine_structure_warning: bool
    balanced_score: float = 0.0
    spectral_vector_score: float = 0.0
    selection_score: float = 0.0


def arc_transition_frequency_Hz(atom, a, b) -> float:
    n1, l1, j1 = a
    n2, l2, j2 = b
    return abs(float(atom.getTransitionFrequency(n1, l1, j1, n2, l2, j2)))


def arc_transition_wavelength_nm(atom, a, b) -> float:
    n1, l1, j1 = a
    n2, l2, j2 = b
    return abs(float(atom.getTransitionWavelength(n1, l1, j1, n2, l2, j2))) * 1e9


def arc_lifetime_us(atom, state, temperature_K=TEMPERATURE_K) -> float:
    n, l, j = state
    try:
        return float(atom.getStateLifetime(n, l, j, temperature=temperature_K)) * 1e6
    except TypeError:
        return float(atom.getStateLifetime(n, l, j)) * 1e6
    except Exception:
        return float("nan")


def zeeman_shift_MHz(atom, state, mj: float, B_mT: float) -> float:
    """ARC linear paramagnetic Zeeman shift in cyclic MHz."""
    n, l, j = state
    # ARC method depends on l,j,mj, not n, in the linear regime.
    dE_J = float(atom.getZeemanEnergyShift(l, j, mj, B_mT * 1e-3))
    return dE_J / h / 1e6


def dipole_ea0(atom, r, mr: float, s, ms: float, q: int) -> float:
    nr, lr, jr = r
    ns, ls, js = s
    try:
        return float(atom.getDipoleMatrixElement(nr, lr, jr, mr,
                                                 ns, ls, js, ms, q))
    except Exception:
        return 0.0


def allowed_pathways(atom, r, s, B_probe_mT: float = 1.0) -> list[Pathway]:
    jr, js = r[2], s[2]
    rows: list[Pathway] = []
    for mr in mj_values(jr):
        for q in (-1, 0, +1):
            ms = mr + q
            if ms < -js - 1e-9 or ms > js + 1e-9:
                continue
            d = dipole_ea0(atom, r, mr, s, ms, q)
            if not np.isfinite(d) or abs(d) < 1e-14:
                continue
            shift = (zeeman_shift_MHz(atom, s, ms, B_probe_mT)
                     - zeeman_shift_MHz(atom, r, mr, B_probe_mT))
            rows.append(Pathway(q=q, mj_r=float(mr), mj_s=float(ms),
                                dme_ea0=float(d), strength_ea0_sq=float(abs(d)**2),
                                shift_at_1mT_MHz=float(shift),
                                slope_MHz_per_mT=float(shift / B_probe_mT)))
    if rows:
        mx = max(p.strength_ea0_sq for p in rows)
        rows = [p for p in rows if p.strength_ea0_sq >= PATHWAY_RELATIVE_DME_CUTOFF * mx]
    return rows


def q_fraction_entropy(pathways: list[Pathway]):
    qsum = {q: 0.0 for q in (-1, 0, +1)}
    for p in pathways:
        qsum[p.q] += p.strength_ea0_sq
    total = sum(qsum.values())
    if total <= 0:
        fr = {q: 0.0 for q in qsum}
        return fr, 0.0
    fr = {q: qsum[q] / total for q in qsum}
    vals = np.array([fr[-1], fr[0], fr[+1]], float)
    nz = vals[vals > 0]
    entropy = -np.sum(nz * np.log(nz)) / np.log(3.0)
    return fr, float(entropy)


def fine_structure_splitting_MHz(atom, state) -> float:
    n, l, j = state
    if l == 0:
        return float("inf")
    j_alt = l + 0.5 if abs(j - (l - 0.5)) < 1e-9 else l - 0.5
    try:
        return abs(float(atom.getTransitionFrequency(n, l, j, n, l, j_alt))) / 1e6
    except Exception:
        return float("nan")


def candidate_fine_structure_warning(atom, r, s) -> bool:
    """Flag if max linear Zeeman scale approaches nearby fine-structure splitting.

    This does NOT model J-mixing. It prevents a linear-J model from being silently
    trusted in a regime where that assumption becomes questionable.
    """
    Bmax = B0_RANGE_MT[1]
    max_z = 0.0
    for st in (r, s):
        for m in mj_values(st[2]):
            max_z = max(max_z, abs(zeeman_shift_MHz(atom, st, float(m), Bmax)))
    fs = min(fine_structure_splitting_MHz(atom, r), fine_structure_splitting_MHz(atom, s))
    if not np.isfinite(fs) or fs <= 0:
        return False
    return max_z > 0.20 * fs


def screen_candidates(atom) -> tuple[list[Candidate], dict[tuple, list[Pathway]]]:
    candidates: list[Candidate] = []
    pathway_cache: dict[tuple, list[Pathway]] = {}

    for nr in range(N_MIN, N_MAX + 1):
        for lr in OPTICALLY_PREPARED_L:
            for jr in j_values_for_l(lr):
                r = (nr, lr, jr)
                # coupling laser: 5P3/2 -> r
                try:
                    lam_nm = arc_transition_wavelength_nm(atom, (5, 1, 1.5), r)
                except Exception:
                    continue

                for ls in (lr - 1, lr + 1):
                    if ls < 0 or ls > 5:
                        continue
                    for js in j_values_for_l(ls):
                        # E1 total-J selection rule (0<->0 excluded automatically here)
                        if abs(js - jr) > 1.0001:
                            continue
                        for ns in range(max(1, nr - DN_RF_SEARCH), nr + DN_RF_SEARCH + 1):
                            s = (ns, ls, js)
                            if s == r:
                                continue
                            try:
                                f_GHz = arc_transition_frequency_Hz(atom, r, s) / 1e9
                            except Exception:
                                continue
                            if not (RF_HARDWARE_BAND_GHZ[0] <= f_GHz <= RF_HARDWARE_BAND_GHZ[1]):
                                continue

                            paths = allowed_pathways(atom, r, s, 1.0)
                            if not paths:
                                continue
                            key = (r, s)
                            pathway_cache[key] = paths
                            fr, ent = q_fraction_entropy(paths)
                            shifts = np.array([p.shift_at_1mT_MHz for p in paths])
                            zspan = float(np.ptp(shifts)) if len(shifts) > 1 else 0.0
                            maxd = max(abs(p.dme_ea0) for p in paths)
                            td2 = sum(p.strength_ea0_sq for p in paths)
                            tau_r = arc_lifetime_us(atom, r)
                            tau_s = arc_lifetime_us(atom, s)
                            min_tau = np.nanmin([tau_r, tau_s])

                            if COUPLING_LASER_WINDOW_NM is None:
                                optical_ok = False
                            else:
                                lo, hi = sorted(COUPLING_LASER_WINDOW_NM)
                                optical_ok = lo <= lam_nm <= hi

                            candidates.append(Candidate(
                                lower=state_label(*r), upper=state_label(*s),
                                n_r=nr, l_r=lr, j_r=jr,
                                n_s=ns, l_s=ls, j_s=js,
                                rf_frequency_GHz=f_GHz,
                                coupling_wavelength_nm=lam_nm,
                                max_abs_dme_ea0=maxd,
                                total_dme2_ea0_sq=td2,
                                sigma_minus_fraction=fr[-1], pi_fraction=fr[0],
                                sigma_plus_fraction=fr[+1], q_entropy=ent,
                                zeeman_span_1mT_MHz=zspan,
                                lower_lifetime_us_300K=tau_r,
                                upper_lifetime_us_300K=tau_s,
                                min_lifetime_us_300K=min_tau,
                                avg_n=0.5 * (nr + ns),
                                rf_access=True,
                                optical_access=optical_ok,
                                thesis_band=(THESIS_TARGET_BAND_GHZ[0] <= f_GHz <= THESIS_TARGET_BAND_GHZ[1]),
                                fine_structure_warning=candidate_fine_structure_warning(atom, r, s),
                            ))

    if not candidates:
        raise RuntimeError("ARC screening found no candidates in the configured RF band.")

    # Balanced multi-objective score: no single assumed engineering weight dominates.
    d = robust_minmax(np.log10(np.array([c.max_abs_dme_ea0 for c in candidates]) + 1e-30))
    z = robust_minmax(np.log10(np.array([c.zeeman_span_1mT_MHz for c in candidates]) + 1e-6))
    t = robust_minmax(np.log10(np.array([c.min_lifetime_us_300K for c in candidates]) + 1e-6))
    e = np.array([c.q_entropy for c in candidates])
    # Maximin rewards candidates that are not catastrophically weak in one metric.
    balance = np.minimum.reduce([d, z, t, e])
    for c, b in zip(candidates, balance):
        # Keep score interpretable: 0..1 balanced feasibility diagnostic.
        c.balanced_score = float(b)

    candidates.sort(key=lambda c: c.balanced_score, reverse=True)
    write_dict_csv(OUTDIR / "arc_transition_candidates.csv", [asdict(c) for c in candidates])
    return candidates, pathway_cache


def fast_vector_screen_score(atom, c: Candidate, B_mT: float = 1.0) -> float:
    """Fast coherent-mJ screening score for vector sensitivity.

    This is NOT a final EIT simulation. It converts the ARC-based dressed poles and
    optical weights for four canonical SOPs into a common Lorentzian stick spectrum,
    then returns the minimum pairwise RMS separation. It is used only to avoid
    automatically selecting transitions whose angular-momentum response is nearly
    rotationally invariant.
    """
    x = np.linspace(-35.0, 35.0, 401)
    gamma = max(GAMMA_R_MHZ, 0.25)
    curves = []
    for _, psi, chi, _ in canonical_polarisations():
        d = build_rf_dressed_manifold(atom, c, B_mT, 0.0, psi, chi, RF_E_PEAK_V_PER_M)
        y = np.zeros_like(x)
        for e0, w0 in zip(d["energies_MHz"], d["optical_weights"]):
            if w0 <= 1e-10:
                continue
            y += w0 * gamma**2 / ((x - e0)**2 + gamma**2)
        # One common normalization scale based on integrated optical weight.
        curves.append(y)
    dists = []
    for i in range(len(curves)):
        for j in range(i + 1, len(curves)):
            dists.append(float(np.sqrt(np.mean((curves[i] - curves[j])**2))))
    return min(dists) if dists else 0.0


def add_vector_screening_scores(atom, candidates: list[Candidate], max_evaluate: int = 60):
    """Add a coherent angular-response score to the strongest balanced candidates."""
    # Evaluate optically eligible candidates first when a verified window exists.
    pool = [c for c in candidates if (c.optical_access or COUPLING_LASER_WINDOW_NM is None)
            and not c.fine_structure_warning]
    pool = sorted(pool, key=lambda c: c.balanced_score, reverse=True)[:max_evaluate]
    print(f"Computing fast coherent vector-sensitivity screen for {len(pool)} candidates...")
    for i, c in enumerate(pool, 1):
        try:
            c.spectral_vector_score = fast_vector_screen_score(atom, c)
        except Exception as exc:
            warnings.warn(f"Vector screening failed for {c.lower}->{c.upper}: {exc}")
            c.spectral_vector_score = 0.0
        if i % 10 == 0 or i == len(pool):
            print(f"  vector screen: {i}/{len(pool)}")

    vnorm = robust_minmax(np.log10(np.array([c.spectral_vector_score for c in candidates]) + 1e-12))
    for c, vn in zip(candidates, vnorm):
        # Geometric blend requires both atomic/RF balance and actual angular response.
        c.selection_score = float(math.sqrt(max(c.balanced_score, 0.0) * max(vn, 0.0)))

    candidates.sort(key=lambda c: c.selection_score, reverse=True)
    write_dict_csv(OUTDIR / "arc_transition_candidates.csv", [asdict(c) for c in candidates])


def select_candidate(candidates: list[Candidate]) -> Candidate:
    if SELECT_TRANSITION is not None:
        r_req, s_req = SELECT_TRANSITION
        for c in candidates:
            if (c.n_r, c.l_r, c.j_r) == tuple(r_req) and (c.n_s, c.l_s, c.j_s) == tuple(s_req):
                return c
        raise RuntimeError(f"Requested SELECT_TRANSITION={SELECT_TRANSITION} not found in screening output.")

    if COUPLING_LASER_WINDOW_NM is not None:
        eligible = [c for c in candidates if c.optical_access and not c.fine_structure_warning]
        if eligible:
            return max(eligible, key=lambda c: c.selection_score)
        warnings.warn("No candidate passes the VERIFIED optical window + model-validity gate; selecting best RF candidate for modelling only.")

    # Optical access unverified: choose a balanced RF candidate, but never call it fully feasible.
    eligible = [c for c in candidates if not c.fine_structure_warning]
    return max(eligible or candidates, key=lambda c: c.selection_score)


# =============================================================================
# 4. FIGURE 1 — THREE-WAY FEASIBILITY LANDSCAPE
# =============================================================================


def plot_candidate_landscape(candidates: list[Candidate], selected: Candidate):
    set_tqe_style()
    fig, ax = plt.subplots(figsize=FIG_DOUBLE)

    f = np.array([c.rf_frequency_GHz for c in candidates])
    lam = np.array([c.coupling_wavelength_nm for c in candidates])
    dme = np.array([c.max_abs_dme_ea0 for c in candidates])
    zspan = np.array([c.zeeman_span_1mT_MHz for c in candidates])

    # Context region: original 1–2 GHz thesis band.
    ax.axvspan(*THESIS_TARGET_BAND_GHZ, color=LIGHT_GREY, alpha=0.65, zorder=0,
               label="Original 1–2 GHz thesis band")

    # Point size = Zeeman pathway span, colour = log DME.
    size = 14 + 65 * robust_minmax(np.log10(zspan + 1e-3))
    good = np.isfinite(lam) & np.isfinite(f) & np.isfinite(dme)
    sc = ax.scatter(f[good], lam[good], s=size[good],
                    c=np.log10(dme[good] + 1e-30), cmap="viridis",
                    edgecolors="white", linewidths=0.35, alpha=0.82, rasterized=True)

    # Verified optical region if known.
    if COUPLING_LASER_WINDOW_NM is not None:
        lo, hi = sorted(COUPLING_LASER_WINDOW_NM)
        ax.axhspan(lo, hi, color=IEEE_GREEN, alpha=0.08, zorder=0)
        ax.hlines([lo, hi], RF_HARDWARE_BAND_GHZ[0], RF_HARDWARE_BAND_GHZ[1],
                  colors=IEEE_GREEN, linestyles="--", linewidth=0.8)
        ax.text(0.99, 0.98, "verified coupling-laser window", transform=ax.transAxes,
                ha="right", va="top", color=IEEE_GREEN, fontsize=7)
    else:
        ax.text(0.99, 0.98, "OPTICAL ACCESS UNVERIFIED\n(set COUPLING_LASER_WINDOW_NM)",
                transform=ax.transAxes, ha="right", va="top", color=IEEE_ORANGE,
                fontsize=7, fontweight="bold",
                bbox=dict(facecolor="white", edgecolor=IEEE_ORANGE, linewidth=0.7, pad=2.5))

    # Selected candidate.
    ax.scatter([selected.rf_frequency_GHz], [selected.coupling_wavelength_nm],
               s=135, facecolors="none", edgecolors=IEEE_ORANGE, linewidths=1.6,
               marker="o", zorder=6)
    ax.scatter([selected.rf_frequency_GHz], [selected.coupling_wavelength_nm],
               s=34, c=IEEE_ORANGE, marker="*", zorder=7)

    # Annotate balanced top candidates with spacing guard.
    ann = sorted(candidates, key=lambda c: c.selection_score, reverse=True)[:MAX_CANDIDATES_TO_ANNOTATE]
    for i, c in enumerate(ann):
        ax.annotate(f"{c.lower}→{c.upper}",
                    (c.rf_frequency_GHz, c.coupling_wavelength_nm),
                    xytext=(5, 5 + (i % 2) * 5), textcoords="offset points",
                    fontsize=6.4, color=IEEE_DARK,
                    arrowprops=dict(arrowstyle="-", lw=0.45, color=IEEE_GREY))

    cb = fig.colorbar(sc, ax=ax, pad=0.015)
    cb.set_label(r"$\log_{10}\max|d_q|$  ($ea_0$)")

    ax.set_xlim(RF_HARDWARE_BAND_GHZ)
    pad_nm = max(0.015, 0.04 * np.ptp(lam[good]))
    ax.set_ylim(np.nanmin(lam[good]) - pad_nm, np.nanmax(lam[good]) + pad_nm)
    ax.set_xlabel("Rydberg–Rydberg transition frequency (GHz)")
    ax.set_ylabel(r"$5P_{3/2}\rightarrow nL_J$ coupling wavelength (nm, vacuum)")
    clean_axes(ax)
    panel_label(ax, "(a)")

    # Compact legend note (size variable).
    ax.text(0.015, 0.02,
            "marker area ∝ Zeeman-pathway span at 1 mT\n"
            "colour ∝ strongest ARC dipole matrix element",
            transform=ax.transAxes, ha="left", va="bottom", fontsize=6.4,
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.82, pad=1.2))

    save_figure(fig, "fig1_arc_three_way_feasibility")


# =============================================================================
# 5. RF POLARISATION GEOMETRY AND COHERENT DRESSED MANIFOLD
# =============================================================================


def transverse_basis(theta_deg: float):
    """Return k, e1, e2 for k in x-z plane, B0 along z.

    e1 lies in the k-z plane and e2=+y; both are orthogonal to k.
    """
    th = np.deg2rad(theta_deg)
    k_hat = np.array([np.sin(th), 0.0, np.cos(th)])
    e1 = np.array([np.cos(th), 0.0, -np.sin(th)])
    e2 = np.array([0.0, 1.0, 0.0])
    return k_hat, e1, e2


def jones_from_psi_chi(psi_deg: float, chi_deg: float) -> np.ndarray:
    """Normalized Jones vector in the local transverse (e1,e2) basis.

    Convention:
        S1 = cos(2chi) cos(2psi)
        S2 = cos(2chi) sin(2psi)
        S3 = sin(2chi)
    The handedness label therefore depends on the declared +k and +B0 axes.
    """
    psi = np.deg2rad(psi_deg)
    chi = np.deg2rad(chi_deg)
    j1 = np.cos(psi) * np.cos(chi) - 1j * np.sin(psi) * np.sin(chi)
    j2 = np.sin(psi) * np.cos(chi) + 1j * np.cos(psi) * np.sin(chi)
    J = np.array([j1, j2], dtype=complex)
    return J / np.linalg.norm(J)


def stokes_from_psi_chi(psi_deg: float, chi_deg: float):
    psi = np.deg2rad(psi_deg)
    chi = np.deg2rad(chi_deg)
    return np.array([1.0,
                     np.cos(2*chi) * np.cos(2*psi),
                     np.cos(2*chi) * np.sin(2*psi),
                     np.sin(2*chi)])


def spherical_field_components(E_peak: float, psi_deg: float, chi_deg: float,
                               k_to_B_deg: float = RF_K_TO_B_DEG) -> dict[int, complex]:
    """Complex peak electric-field components E_q relative to B0 (+z)."""
    _, e1, e2 = transverse_basis(k_to_B_deg)
    J = jones_from_psi_chi(psi_deg, chi_deg)
    E = E_peak * (J[0] * e1 + J[1] * e2)
    Ex, Ey, Ez = E
    # Standard spherical-basis convention.
    return {
        +1: -(Ex + 1j*Ey) / np.sqrt(2),
         0: Ez,
        -1: (Ex - 1j*Ey) / np.sqrt(2),
    }


def rf_component_fractions(psi_deg: float, chi_deg: float):
    eq = spherical_field_components(1.0, psi_deg, chi_deg)
    p = {q: abs(v)**2 for q, v in eq.items()}
    s = sum(p.values())
    return {q: p[q] / s for q in (-1, 0, +1)}


def candidate_states(c: Candidate):
    return (c.n_r, c.l_r, c.j_r), (c.n_s, c.l_s, c.j_s)


def optical_lower_mj_weights(atom, c: Candidate) -> dict[float, float]:
    """Incoherent optical-preparation weights for the lower Rydberg mJ states.

    If COUPLING_OPTICAL_Q is None, sum DME^2 over all 5P3/2 mJ and q pathways.
    This is intentionally conservative when the actual optical pumping/polarisation
    distribution has not been measured.
    """
    r, _ = candidate_states(c)
    weights = {float(mr): 0.0 for mr in mj_values(c.j_r)}
    qset = (-1, 0, +1) if COUPLING_OPTICAL_Q is None else (COUPLING_OPTICAL_Q,)
    for me in mj_values(1.5):
        for q in qset:
            mr = me + q
            if mr < -c.j_r - 1e-9 or mr > c.j_r + 1e-9:
                continue
            try:
                d = float(atom.getDipoleMatrixElement(5, 1, 1.5, float(me),
                                                      c.n_r, c.l_r, c.j_r, float(mr), q))
            except Exception:
                d = 0.0
            weights[float(mr)] += abs(d)**2
    total = sum(weights.values())
    if total <= 0:
        # Only a fail-safe for unexpected ARC conventions; report it loudly.
        warnings.warn("Could not construct optical mJ weights from ARC; using equal lower-mJ weights.")
        return {m: 1.0 / len(weights) for m in weights}
    return {m: w / total for m, w in weights.items()}


def build_rf_dressed_manifold(atom, c: Candidate, B_mT: float,
                              rf_detuning_MHz: float,
                              psi_deg: float, chi_deg: float,
                              E_peak_V_m: float = RF_E_PEAK_V_PER_M):
    """Coherent Rydberg RF Hamiltonian across every mJ sublevel.

    rf_detuning_MHz = f_RF(source) - f0(ARC) in cyclic MHz.
    Rotating-frame diagonal:
        lower r: Zeeman_r
        upper s: Zeeman_s - rf_detuning
    Coupling H_rs = Omega_rs/2, with Omega = d*E_q/h in MHz.
    """
    r, s = candidate_states(c)
    mr_list = [float(x) for x in mj_values(c.j_r)]
    ms_list = [float(x) for x in mj_values(c.j_s)]
    n_r = len(mr_list)
    n_s = len(ms_list)
    N = n_r + n_s
    H = np.zeros((N, N), dtype=complex)

    for i, mr in enumerate(mr_list):
        H[i, i] = zeeman_shift_MHz(atom, r, mr, B_mT)
    for j, ms in enumerate(ms_list):
        H[n_r + j, n_r + j] = zeeman_shift_MHz(atom, s, ms, B_mT) - rf_detuning_MHz

    Eq = spherical_field_components(E_peak_V_m, psi_deg, chi_deg)
    transitions = []
    for i, mr in enumerate(mr_list):
        for q in (-1, 0, +1):
            ms = mr + q
            if ms not in ms_list:
                continue
            j = ms_list.index(ms)
            d = dipole_ea0(atom, r, mr, s, ms, q)
            if abs(d) < 1e-15:
                continue
            # Complex cyclic Rabi frequency in MHz.
            Omega = d * EA0_C_M * Eq[q] / h / 1e6
            H[i, n_r + j] += Omega / 2.0
            H[n_r + j, i] += np.conjugate(Omega) / 2.0
            transitions.append((mr, ms, q, d, Omega))

    evals, evecs = np.linalg.eigh(H)
    prep = optical_lower_mj_weights(atom, c)
    optical_weights = np.zeros(N, float)
    for kidx in range(N):
        w = 0.0
        for i, mr in enumerate(mr_list):
            w += prep[mr] * abs(evecs[i, kidx])**2
        optical_weights[kidx] = w
    if optical_weights.sum() > 0:
        optical_weights /= optical_weights.sum()

    return {
        "energies_MHz": evals.real,
        "optical_weights": optical_weights,
        "H_MHz": H,
        "mr_list": mr_list,
        "ms_list": ms_list,
        "transitions": transitions,
        "E_q": Eq,
    }


# =============================================================================
# 6. DOPPLER-AVERAGED WEAK-PROBE DRESSED-STATE EIT MODEL
# =============================================================================


def gauss_hermite_velocities(T_K: float, n_nodes: int):
    x, w = hermgauss(n_nodes)
    sigma = math.sqrt(k_B * T_K / RB87_MASS_KG)
    v = math.sqrt(2.0) * sigma * x
    weights = w / math.sqrt(math.pi)
    return v, weights


def probe_wavelength_nm_from_arc(atom) -> float:
    try:
        return arc_transition_wavelength_nm(atom, (5, 0, 0.5), (5, 1, 1.5))
    except Exception:
        return PROBE_WAVELENGTH_NM_FALLBACK


def two_level_reference_absorption(delta_p_MHz: np.ndarray,
                                   lambda_probe_nm: float,
                                   n_hermite: int) -> np.ndarray:
    v, vw = gauss_hermite_velocities(TEMPERATURE_K, n_hermite)
    dop_p = v / (lambda_probe_nm * 1e-9) / 1e6
    dpv = delta_p_MHz[None, :] - dop_p[:, None]
    rho = 1j * OMEGA_PROBE_MHZ / 2.0 / (GAMMA_GE_MHZ + 1j * dpv)
    rho_avg = np.sum(vw[:, None] * rho, axis=0)
    return np.maximum(np.imag(rho_avg), 0.0)


def dressed_eit_spectrum(atom, c: Candidate, delta_p_MHz: np.ndarray,
                         B_mT: float, rf_detuning_MHz: float,
                         psi_deg: float, chi_deg: float,
                         E_peak_V_m: float,
                         n_hermite: int,
                         return_details: bool = False):
    """Doppler-averaged relative probe transmission for one RF polarisation.

    The model treats the RF-dressed Rydberg eigenmodes as poles in the upper
    ladder susceptibility. This captures coherent magnetic-sublevel dressing and
    Doppler averaging while remaining auditable.
    """
    dressed = build_rf_dressed_manifold(atom, c, B_mT, rf_detuning_MHz,
                                        psi_deg, chi_deg, E_peak_V_m)
    eps = dressed["energies_MHz"]
    wk = dressed["optical_weights"]
    keep = wk > 1e-8
    eps = eps[keep]
    wk = wk[keep]

    lam_p_nm = probe_wavelength_nm_from_arc(atom)
    lam_c_nm = c.coupling_wavelength_nm
    v, vw = gauss_hermite_velocities(TEMPERATURE_K, n_hermite)
    dop_p = v / (lam_p_nm * 1e-9) / 1e6
    # Counter-propagating coupling beam: k_c points opposite to k_p.
    dop_c = -v / (lam_c_nm * 1e-9) / 1e6

    dpv = delta_p_MHz[None, :] - dop_p[:, None]
    dcv = DELTA_COUPLING_MHZ - dop_c[:, None]
    two_photon = dpv + dcv

    # Sum dressed poles. Shapes: velocity x probe x pole.
    den_r = GAMMA_R_MHZ + 1j * (two_photon[:, :, None] - eps[None, None, :])
    self_energy = (OMEGA_COUPLING_MHZ**2 / 4.0) * np.sum(
        wk[None, None, :] / den_r, axis=2
    )
    den_e = GAMMA_GE_MHZ + 1j * dpv + self_energy
    rho = 1j * OMEGA_PROBE_MHZ / 2.0 / den_e
    rho_avg = np.sum(vw[:, None] * rho, axis=0)
    absorption = np.maximum(np.imag(rho_avg), 0.0)

    # One common two-level reference scale preserves relative differences across
    # all RF polarisation cases; spectra are NOT individually normalized.
    Aref = two_level_reference_absorption(delta_p_MHz, lam_p_nm, n_hermite)
    A0 = max(float(np.nanmax(Aref)), 1e-15)
    T = np.exp(-EFFECTIVE_OD * absorption / A0)

    if return_details:
        return T, dressed
    return T


# =============================================================================
# 7. FIGURE 2 — ZEEMAN PATHWAY FAN
# =============================================================================


def plot_zeeman_fan(atom, c: Candidate, optimum_rf_detuning_MHz: float = 0.0):
    set_tqe_style()
    fig, ax = plt.subplots(figsize=FIG_DOUBLE)
    r, s = candidate_states(c)
    B = np.linspace(*B0_RANGE_MT, B0_POINTS_FAN)
    paths = allowed_pathways(atom, r, s, 1.0)
    max_strength = max(p.strength_ea0_sq for p in paths)
    used_label = set()

    records = []
    for p in paths:
        shifts = []
        for b in B:
            ds = zeeman_shift_MHz(atom, s, p.mj_s, float(b))
            dr = zeeman_shift_MHz(atom, r, p.mj_r, float(b))
            shifts.append(ds - dr)
        shifts = np.asarray(shifts)
        lw = 0.45 + 2.0 * math.sqrt(p.strength_ea0_sq / max_strength)
        alpha = 0.28 + 0.72 * math.sqrt(p.strength_ea0_sq / max_strength)
        label = Q_LABEL[p.q] if p.q not in used_label else None
        used_label.add(p.q)
        ax.plot(B, shifts, color=Q_COLORS[p.q], lw=lw, alpha=alpha, label=label)
        records.append({
            "q": p.q, "mj_r": p.mj_r, "mj_s": p.mj_s,
            "dme_ea0": p.dme_ea0, "slope_MHz_per_mT": p.slope_MHz_per_mT,
        })

    ax.axhline(optimum_rf_detuning_MHz, color=IEEE_PURPLE, ls="--", lw=1.0,
               label=rf"selected $\Delta_{{RF}}={optimum_rf_detuning_MHz:.1f}$ MHz")
    ax.set_xlabel(r"Magnetic bias, $B_0$ (mT)")
    ax.set_ylabel(r"RF transition shift, $f_{m_Jm'_J}(B_0)-f_0$ (MHz)")
    clean_axes(ax)
    ax.legend(loc="best", ncol=4, handlelength=2.0, columnspacing=1.0)
    panel_label(ax, "(b)")

    # Experiment-actionable secondary axis using measured interim coil calibration.
    def B_to_I(BmT):
        return (BmT - COIL_B_MT) / COIL_A_MT_PER_A
    def I_to_B(I):
        return COIL_A_MT_PER_A * I + COIL_B_MT
    sec = ax.secondary_xaxis("top", functions=(B_to_I, I_to_B))
    sec.set_xlabel("Coil current from interim local calibration, I (A)", labelpad=4)
    sec.tick_params(direction="in")

    info = (f"{c.lower} → {c.upper};  $f_0$={c.rf_frequency_GHz:.6f} GHz\n"
            f"line width ∝ |d|; coil-field RMSE ≈ {COIL_B_RMSE_MT:.3f} mT")
    ax.text(0.015, 0.985, info, transform=ax.transAxes, ha="left", va="top",
            fontsize=6.7, bbox=dict(facecolor="white", edgecolor="none", alpha=0.84, pad=1.5))

    if c.fine_structure_warning:
        ax.text(0.985, 0.02,
                "WARNING: linear-J Zeeman model approaches fine-structure scale;\n"
                "use a mixed-state Stark/Zeeman Hamiltonian before quantitative claims.",
                transform=ax.transAxes, ha="right", va="bottom", fontsize=6.5,
                color=IEEE_ORANGE, fontweight="bold")

    save_figure(fig, "fig2_arc_zeeman_pathway_fan")
    write_dict_csv(OUTDIR / "fig2_zeeman_pathways.csv", records)


# =============================================================================
# 8. IDENTIFIABILITY / FISHER MAP — FIGURE 4 (computed before Fig. 3)
# =============================================================================


def local_polarisation_jacobian(atom, c: Candidate, dp: np.ndarray,
                                B_mT: float, rf_det_MHz: float,
                                psi0_deg: float, chi0_deg: float,
                                step_deg: float, n_hermite: int):
    d = step_deg
    Tpp = dressed_eit_spectrum(atom, c, dp, B_mT, rf_det_MHz,
                               psi0_deg + d, chi0_deg, RF_E_PEAK_V_PER_M, n_hermite)
    Tpm = dressed_eit_spectrum(atom, c, dp, B_mT, rf_det_MHz,
                               psi0_deg - d, chi0_deg, RF_E_PEAK_V_PER_M, n_hermite)
    Tcp = dressed_eit_spectrum(atom, c, dp, B_mT, rf_det_MHz,
                               psi0_deg, chi0_deg + d, RF_E_PEAK_V_PER_M, n_hermite)
    Tcm = dressed_eit_spectrum(atom, c, dp, B_mT, rf_det_MHz,
                               psi0_deg, chi0_deg - d, RF_E_PEAK_V_PER_M, n_hermite)
    drad = np.deg2rad(d)
    dT_dpsi = (Tpp - Tpm) / (2 * drad)
    dT_dchi = (Tcp - Tcm) / (2 * drad)
    J = np.column_stack([dT_dpsi, dT_dchi])
    # Normalize by sqrt(N) so the metric does not grow merely because more pixels
    # are sampled on the spectrum.
    return J / math.sqrt(len(dp))


def compute_identifiability_map(atom, c: Candidate, quick: bool):
    nb = B0_MAP_POINTS_QUICK if quick else B0_MAP_POINTS_FULL
    nd = RF_DETUNING_MAP_POINTS_QUICK if quick else RF_DETUNING_MAP_POINTS_FULL
    nh = HERMITE_NODES_QUICK if quick else max(31, HERMITE_NODES_FULL // 2)
    Bvals = np.linspace(*B0_RANGE_MT, nb)
    Dvals = np.linspace(*RF_DETUNING_MAP_MHZ, nd)
    dp = np.linspace(*PROBE_DETUNING_MHZ, PROBE_POINTS_MAP)

    worst = np.full((nb, nd), np.nan)
    condition = np.full((nb, nd), np.nan)
    volume = np.full((nb, nd), np.nan)

    total = nb * nd
    count = 0
    for ib, b in enumerate(Bvals):
        for jd, det in enumerate(Dvals):
            J = local_polarisation_jacobian(
                atom, c, dp, float(b), float(det),
                IDENTIFIABILITY_REFERENCE_PSI_DEG,
                IDENTIFIABILITY_REFERENCE_CHI_DEG,
                IDENTIFIABILITY_STEP_DEG, nh
            )
            sv = np.linalg.svd(J, compute_uv=False)
            s1, s2 = float(sv[0]), float(sv[-1])
            worst[ib, jd] = s2
            condition[ib, jd] = s1 / max(s2, 1e-15)
            volume[ib, jd] = s1 * s2
            count += 1
            if count % max(1, total // 20) == 0:
                print(f"  identifiability map: {100*count/total:5.1f}%")

    # A robust optimum rewards worst-direction sensitivity while avoiding severe
    # anisotropy. No invented detector noise or classifier accuracy is used.
    objective = worst / np.sqrt(np.maximum(condition, 1.0))
    idx = np.unravel_index(np.nanargmax(objective), objective.shape)
    optimum = {
        "B0_mT": float(Bvals[idx[0]]),
        "rf_detuning_MHz": float(Dvals[idx[1]]),
        "worst_direction_sensitivity": float(worst[idx]),
        "condition_number": float(condition[idx]),
        "spectral_area_sensitivity": float(volume[idx]),
    }

    write_matrix_csv(OUTDIR / "fig4_worst_direction_sensitivity.csv",
                     "B0_mT", Bvals, "rf_detuning_MHz", Dvals, worst)
    write_matrix_csv(OUTDIR / "fig4_condition_number.csv",
                     "B0_mT", Bvals, "rf_detuning_MHz", Dvals, condition)
    (OUTDIR / "predicted_operating_point.json").write_text(
        json.dumps(optimum, indent=2), encoding="utf-8")
    return Bvals, Dvals, worst, condition, optimum


def plot_identifiability_map(Bvals, Dvals, worst, condition, optimum):
    set_tqe_style()
    fig, axes = plt.subplots(1, 2, figsize=FIG_DOUBLE_TALL, constrained_layout=True)

    # Panel a: worst-direction local sensitivity.
    W = np.log10(np.maximum(worst, 1e-12))
    im = axes[0].pcolormesh(Dvals, Bvals, W, shading="auto", cmap="viridis")
    cb = fig.colorbar(im, ax=axes[0], pad=0.015)
    cb.set_label(r"$\log_{10}\,\sigma_{\min}(J)$  (relative transmission rad$^{-1}$)")
    axes[0].plot(optimum["rf_detuning_MHz"], optimum["B0_mT"], marker="*",
                 ms=9, mfc="white", mec=IEEE_DARK, mew=0.8)
    axes[0].set_xlabel(r"RF detuning, $\Delta_{RF}=f_{RF}-f_0$ (MHz)")
    axes[0].set_ylabel(r"Magnetic bias, $B_0$ (mT)")
    clean_axes(axes[0]); panel_label(axes[0], "(a)")

    # Panel b: condition number; lower is better. Clip for readable dynamic range.
    C = np.clip(condition, 1.0, np.nanpercentile(condition[np.isfinite(condition)], 97))
    im2 = axes[1].pcolormesh(Dvals, Bvals, np.log10(C), shading="auto", cmap="magma_r")
    cb2 = fig.colorbar(im2, ax=axes[1], pad=0.015)
    cb2.set_label(r"$\log_{10}\kappa(J)$  (1 = isotropic sensitivity)")
    axes[1].plot(optimum["rf_detuning_MHz"], optimum["B0_mT"], marker="*",
                 ms=9, mfc="white", mec=IEEE_DARK, mew=0.8)
    # A useful visual contour: condition number 10, only if present.
    try:
        axes[1].contour(Dvals, Bvals, condition, levels=[10], colors=[IEEE_BLUE], linewidths=0.8)
    except Exception:
        pass
    axes[1].set_xlabel(r"RF detuning, $\Delta_{RF}=f_{RF}-f_0$ (MHz)")
    axes[1].set_ylabel(r"Magnetic bias, $B_0$ (mT)")
    clean_axes(axes[1]); panel_label(axes[1], "(b)")

    fig.text(0.5, 0.005,
             "Local spectral identifiability from the Jacobian of the full simulated spectrum with respect to "
             r"polarisation orientation $\psi$ and ellipticity $\chi$; no classifier accuracy is invented.",
             ha="center", va="bottom", fontsize=6.5)
    save_figure(fig, "fig4_polarisation_identifiability_map")


# =============================================================================
# 9. FIGURE 3 — HERO POLARISATION-RESOLVED SPECTRAL FINGERPRINTS
# =============================================================================


def canonical_polarisations():
    # Defined in the local transverse basis; equal total |E| for every case.
    return [
        ("Linear 0°", 0.0, 0.0, IEEE_BLUE),
        ("Linear 90°", 90.0, 0.0, IEEE_DARK),
        ("RHCP*", 0.0, +45.0, IEEE_ORANGE),
        ("LHCP*", 0.0, -45.0, IEEE_GREEN),
    ]


def plot_polarisation_fingerprints(atom, c: Candidate, optimum: dict, quick: bool):
    set_tqe_style()
    dp = np.linspace(*PROBE_DETUNING_MHZ, PROBE_POINTS_HERO)
    nh = HERMITE_NODES_QUICK if quick else HERMITE_NODES_FULL
    B = optimum["B0_mT"]
    det = optimum["rf_detuning_MHz"]

    # Same-B RF-off reference: isolates RF-induced structure from common magnetic/optical shifts.
    T_off = dressed_eit_spectrum(atom, c, dp, B, det,
                                 0.0, 0.0, 0.0, nh)

    fig, axes = plt.subplots(2, 2, figsize=FIG_DOUBLE_TALL, sharex=True, sharey=True,
                             constrained_layout=True)
    data_rows = []

    for ax, (name, psi, chi, color), lab in zip(axes.flat, canonical_polarisations(), ["(a)", "(b)", "(c)", "(d)"]):
        T, details = dressed_eit_spectrum(atom, c, dp, B, det,
                                          psi, chi, RF_E_PEAK_V_PER_M, nh,
                                          return_details=True)
        dT = T - T_off
        ax.plot(dp, T_off, color=IEEE_GREY, lw=0.85, ls="--", label="RF off")
        ax.plot(dp, T, color=color, lw=1.5, label=name)
        # Light differential fill shows exactly where RF changes the optical trace.
        ax.fill_between(dp, T_off, T, color=color, alpha=0.10, linewidth=0)

        # Dressed-pole rug at top; height/alpha reflects optical weight.
        eps = details["energies_MHz"]
        wk = details["optical_weights"]
        ylim = (min(np.nanmin(T_off), np.nanmin(T)), max(np.nanmax(T_off), np.nanmax(T)))
        yrange = ylim[1] - ylim[0]
        for e0, w0 in zip(eps, wk):
            if w0 < 0.01 or e0 < dp.min() or e0 > dp.max():
                continue
            ax.vlines(e0, ylim[1] - 0.08*yrange, ylim[1], color=color,
                      lw=0.5 + 2.0*w0, alpha=0.30 + 0.65*w0)

        frac = rf_component_fractions(psi, chi)
        ax.text(0.02, 0.04,
                rf"$|E_{{-1}}|^2={frac[-1]:.2f}$,  $|E_0|^2={frac[0]:.2f}$,  $|E_{{+1}}|^2={frac[+1]:.2f}$",
                transform=ax.transAxes, fontsize=6.2, ha="left", va="bottom")
        ax.legend(loc="best", handlelength=2.2)
        clean_axes(ax); panel_label(ax, lab)

        for x, y, yoff in zip(dp, T, T_off):
            data_rows.append({"polarisation": name, "psi_deg": psi, "chi_deg": chi,
                              "probe_detuning_MHz": float(x), "T_RF_on": float(y),
                              "T_RF_off": float(yoff), "delta_T": float(y-yoff)})

    for ax in axes[1, :]:
        ax.set_xlabel(r"Probe detuning, $\Delta_p$ (MHz)")
    for ax in axes[:, 0]:
        ax.set_ylabel("Relative probe transmission")

    # Figure-level model conditions, compact enough for TQE/poster use.
    fig.text(0.5, 0.995,
             f"Equal RF field magnitude: E_peak={RF_E_PEAK_V_PER_M:.3g} V/m; "
             f"B0={B:.3f} mT; ΔRF={det:.2f} MHz; k_RF∠B0={RF_K_TO_B_DEG:.0f}°",
             ha="center", va="top", fontsize=7.0)
    fig.text(0.5, 0.006,
             "*RHCP/LHCP follow the stated +k/+B0 Jones convention; reverse propagation or B0 reverses the handedness mapping.",
             ha="center", va="bottom", fontsize=6.2)

    save_figure(fig, "fig3_equal_power_polarisation_fingerprints")
    write_dict_csv(OUTDIR / "fig3_polarisation_fingerprints.csv", data_rows)


# =============================================================================
# 10. OPTIONAL FIGURE 5 — POINCARE-TO-SPECTRUM MANIFOLD
# =============================================================================


def plot_poincare_spectral_manifold(atom, c: Candidate, optimum: dict, quick: bool):
    if not MAKE_POINCARE_MANIFOLD:
        return
    set_tqe_style()
    nh = HERMITE_NODES_QUICK if quick else max(31, HERMITE_NODES_FULL // 2)
    dp = np.linspace(*PROBE_DETUNING_MHZ, PROBE_POINTS_MAP)
    psis = np.linspace(0, 180, POINCARE_PSI_POINTS, endpoint=False)
    chis = np.linspace(-45, 45, POINCARE_CHI_POINTS)

    X, S = [], []
    labels = []
    for chi in chis:
        for psi in psis:
            T = dressed_eit_spectrum(atom, c, dp, optimum["B0_mT"], optimum["rf_detuning_MHz"],
                                     float(psi), float(chi), RF_E_PEAK_V_PER_M, nh)
            # Shape rather than absolute DC offset dominates PCA.
            X.append(T - np.mean(T))
            S.append(stokes_from_psi_chi(float(psi), float(chi)))
            labels.append((psi, chi))
    X = np.asarray(X)
    S = np.asarray(S)
    Xc = X - X.mean(axis=0, keepdims=True)
    U, sv, Vt = np.linalg.svd(Xc, full_matrices=False)
    scores = U[:, :3] * sv[:3]
    explained = sv**2 / np.sum(sv**2)

    fig = plt.figure(figsize=FIG_DOUBLE)
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(scores[:, 0], scores[:, 1], scores[:, 2], c=S[:, 3], cmap="coolwarm",
                    s=24, edgecolors="white", linewidths=0.25, alpha=0.92)
    cb = fig.colorbar(sc, ax=ax, pad=0.08, shrink=0.78)
    cb.set_label(r"Stokes $S_3/S_0$ (ellipticity)")
    ax.set_xlabel(f"PC1 ({100*explained[0]:.1f}%)")
    ax.set_ylabel(f"PC2 ({100*explained[1]:.1f}%)")
    ax.set_zlabel(f"PC3 ({100*explained[2]:.1f}%)")
    ax.tick_params(labelsize=6.7)
    ax.grid(False)
    fig.text(0.02, 0.98, "(e)", ha="left", va="top", fontweight="bold")
    save_figure(fig, "fig5_poincare_spectral_manifold")

    rows = []
    for (psi, chi), st, scv in zip(labels, S, scores):
        rows.append({"psi_deg": psi, "chi_deg": chi,
                     "S0": st[0], "S1": st[1], "S2": st[2], "S3": st[3],
                     "PC1": scv[0], "PC2": scv[1], "PC3": scv[2]})
    write_dict_csv(OUTDIR / "fig5_poincare_spectral_manifold.csv", rows)


# =============================================================================
# 11. PROVENANCE / VALIDITY REPORT
# =============================================================================


def provenance_report(c: Candidate, optimum: dict, n_candidates: int):
    optical_text = (
        f"VERIFIED window {COUPLING_LASER_WINDOW_NM[0]:.6f}–{COUPLING_LASER_WINDOW_NM[1]:.6f} nm"
        if COUPLING_LASER_WINDOW_NM is not None else
        "UNVERIFIED (COUPLING_LASER_WINDOW_NM=None)"
    )
    status = "FULL THREE-WAY FEASIBILITY GATE PASSED" if c.optical_access else "RF/ATOMIC MODEL CANDIDATE ONLY — OPTICAL ACCESS NOT VERIFIED"

    text = f"""ADVANCED RYDBERG POLARISATION SIMULATION — PROVENANCE AND CLAIM BOUNDARY
================================================================================

Selected transition
-------------------
Lower Rydberg state : {c.lower}
Upper Rydberg state : {c.upper}
ARC RF frequency    : {c.rf_frequency_GHz:.9f} GHz
ARC coupling lambda : {c.coupling_wavelength_nm:.9f} nm (vacuum)
Max |DME|           : {c.max_abs_dme_ea0:.6g} e a0
Zeeman span @1 mT   : {c.zeeman_span_1mT_MHz:.6g} MHz
Min lifetime @ {TEMPERATURE_K:.2f} K : {c.min_lifetime_us_300K:.4g} us
q fractions         : sigma-={c.sigma_minus_fraction:.3f}, pi={c.pi_fraction:.3f}, sigma+={c.sigma_plus_fraction:.3f}
Fine-structure flag : {c.fine_structure_warning}
Screened candidates : {n_candidates}
STATUS              : {status}

Experimental/hardware gates
---------------------------
RF hardware band            : {RF_HARDWARE_BAND_GHZ[0]}–{RF_HARDWARE_BAND_GHZ[1]} GHz
Original thesis context band: {THESIS_TARGET_BAND_GHZ[0]}–{THESIS_TARGET_BAND_GHZ[1]} GHz
Coupling-laser window       : {optical_text}
Magnetic calibration        : B0[mT] = {COIL_A_MT_PER_A} I[A] + {COIL_B_MT}, RMSE={COIL_B_RMSE_MT} mT
RF geometry                 : k_RF angle to B0 = {RF_K_TO_B_DEG} deg (EDIT TO MATCH LAB)
RF peak E field             : {RF_E_PEAK_V_PER_M} V/m — {RF_FIELD_PROVENANCE}

Optical/EIT model parameters
----------------------------
Temperature                 : {TEMPERATURE_K} K
Cell length                 : {CELL_LENGTH_M} m
Probe Rabi                  : {OMEGA_PROBE_MHZ} MHz (model input; replace if measured)
Coupling Rabi               : {OMEGA_COUPLING_MHZ} MHz (model input; replace if measured)
gamma_ge                    : {GAMMA_GE_MHZ} MHz
gamma_R                     : {GAMMA_R_MHZ} MHz
Effective optical depth     : {EFFECTIVE_OD}
Coupling optical q          : {COUPLING_OPTICAL_Q} (None = unresolved/incoherent preparation approximation)

Predicted model operating point
-------------------------------
B0                           : {optimum['B0_mT']:.6g} mT
RF detuning f_RF-f0          : {optimum['rf_detuning_MHz']:.6g} MHz
Worst-direction sensitivity : {optimum['worst_direction_sensitivity']:.6g} rel. transmission/rad
Jacobian condition number    : {optimum['condition_number']:.6g}

Interpretation
--------------
1. ARC-derived frequency/wavelength/DME/linear Zeeman/lifetime values are atomic-data/model outputs.
2. Figure 3 compares equal |E| polarisation states and uses one common transmission scale; traces are not
   independently normalized, so spectral separation is visible without manufacturing contrast artificially.
3. Figure 4 is a local identifiability metric from the spectrum Jacobian with respect to psi and chi. It is NOT
   a claimed classifier accuracy and does not invent detector noise.
4. Absolute agreement with experiment requires measured laser powers/beam waists, optical polarisation and
   pumping, RF electric field at the cell, full B-field vector map, detector transfer function and repeated
   baseline covariance.
5. ARC getZeemanEnergyShift is a linear paramagnetic-J model. If the fine-structure warning is True, use a
   mixed-state Hamiltonian / StarkMap / full validated Rydiqule model before quantitative poster claims.
6. The RF spherical-component decomposition uses the coordinate convention B0=+z and k_RF in the x-z plane.
   RHCP/LHCP labels reverse under propagation-axis or B0 reversal depending on convention.

Recommended poster wording
--------------------------
"MODELLED RECEIVER BEHAVIOUR — ARC atomic data + coherent mJ dressing + Doppler-averaged weak-probe EIT model."
"Predicted spectral fingerprints require experimental validation; simulation is used for transition selection and
measurement design, not as a substitute for measured polarimetry."
"""
    (OUTDIR / "assumptions_provenance_and_claim_boundary.txt").write_text(text, encoding="utf-8")


# =============================================================================
# 12. MAIN
# =============================================================================


def print_top_candidates(candidates: list[Candidate], n=15):
    print("\nTop balanced ARC candidates")
    print("-" * 126)
    hdr = f"{'transition':26s} {'fRF/GHz':>10s} {'lambda/nm':>11s} {'|d|max':>10s} {'Zspan@1mT':>12s} {'tau_min/us':>11s} {'Hq':>6s} {'vec':>8s} {'opt':>5s} {'FSwarn':>7s} {'score':>7s}"
    print(hdr)
    print("-" * 126)
    for c in candidates[:n]:
        tr = f"{c.lower}->{c.upper}"
        print(f"{tr:26s} {c.rf_frequency_GHz:10.6f} {c.coupling_wavelength_nm:11.6f} "
              f"{c.max_abs_dme_ea0:10.2f} {c.zeeman_span_1mT_MHz:12.2f} "
              f"{c.min_lifetime_us_300K:11.2f} {c.q_entropy:6.3f} {c.spectral_vector_score:8.3g} "
              f"{str(c.optical_access):>5s} {str(c.fine_structure_warning):>7s} {c.selection_score:7.3f}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quick", action="store_true",
                        help="smaller B0/RF-detuning grids and fewer Doppler nodes for iteration")
    args = parser.parse_args()

    OUTDIR.mkdir(parents=True, exist_ok=True)
    set_tqe_style()

    print("Loading ARC 87Rb model...")
    atom = arc_atom_or_die()
    print("Screening transitions using ARC (no approximate fallback)...")
    candidates, pathway_cache = screen_candidates(atom)
    add_vector_screening_scores(atom, candidates)
    print_top_candidates(candidates)
    selected = select_candidate(candidates)

    print("\nSelected for forward modelling:")
    print(json.dumps(asdict(selected), indent=2))
    (OUTDIR / "selected_candidate.json").write_text(json.dumps(asdict(selected), indent=2), encoding="utf-8")

    if COUPLING_LASER_WINDOW_NM is None:
        warnings.warn(
            "COUPLING_LASER_WINDOW_NM is not verified. Candidate is NOT being claimed optically accessible. "
            "Enter the wavemeter-verified tuning window before using Fig. 1 as a feasibility claim."
        )

    print("Creating Fig. 1: ARC three-way feasibility landscape...")
    plot_candidate_landscape(candidates, selected)

    print("Computing Fig. 4 first to determine a model operating point...")
    Bvals, Dvals, worst, condition, optimum = compute_identifiability_map(atom, selected, args.quick)
    plot_identifiability_map(Bvals, Dvals, worst, condition, optimum)
    print("Predicted model operating point:", optimum)

    print("Creating Fig. 2: Zeeman pathway fan...")
    plot_zeeman_fan(atom, selected, optimum_rf_detuning_MHz=optimum["rf_detuning_MHz"])

    print("Creating Fig. 3: equal-power polarisation spectral fingerprints...")
    plot_polarisation_fingerprints(atom, selected, optimum, args.quick)

    if MAKE_POINCARE_MANIFOLD:
        print("Creating optional Fig. 5: Poincare-to-spectrum manifold...")
        plot_poincare_spectral_manifold(atom, selected, optimum, args.quick)

    provenance_report(selected, optimum, len(candidates))

    print("\nDone.")
    print(f"Outputs: {OUTDIR.resolve()}")
    print("Before poster use, read assumptions_provenance_and_claim_boundary.txt")


if __name__ == "__main__":
    main()
