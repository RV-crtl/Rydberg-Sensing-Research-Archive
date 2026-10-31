"""
Rydberg polarization-sensing transition screening and forward-model workflow
----------------------------------------------------------------------------
Author-facing purpose:
    Generate the transition table, Zeeman-pathway plots, EIT spectra, RF-detuning maps,
    magnetic-bias maps, and polarization-feature summaries needed to argue a concrete
    experimental plan for a magnetically biased 87Rb Rydberg-EIT polarization receiver.

What this script does:
    1) Uses ARC, if available, to screen 87Rb Rydberg-Rydberg transitions inside the
       lab-accessible RF range (default: 0.85-6.4 GHz).
    2) Falls back to a quantum-defect frequency estimate if ARC is not installed.
       The fallback is only for planning, not final quantitative claims.
    3) Estimates allowed sigma+/pi/sigma- Zeeman pathways and magnetic tuning slopes.
    4) Produces ranked transition candidates based on frequency match, dipole strength,
       Zeeman separability, and practical high-n risk.
    5) Runs a compact four-level ladder-EIT forward model to produce:
         - RF-off/coupling-on baseline EIT spectra
         - RF-coupled spectra versus RF Rabi frequency
         - RF detuning response map
         - magnetic-bias response map
         - polarization comparison: linear, RHCP, LHCP, and B0 reversal
    6) Saves CSVs and figures to ./rydberg_outputs.

Install recommended:
    python -m pip install numpy scipy pandas matplotlib
    python -m pip install arc-alkali-rydberg-calculator
    # Optional if your group wants to build the full graph model later:
    python -m pip install rydiqule

Notes:
    - This script uses ARC for atomic transition screening. RydIQule APIs evolve quickly;
      therefore, the EIT plots here use a transparent analytic/OBE-style model that is
      deliberately easy to inspect and reproduce. Use RydIQule after this to build a more
      complete Doppler-averaged, multi-level model around the selected candidate states.
    - All Rabi frequencies and linewidths in the EIT model are cyclic-frequency units in MHz.
    - The model is for experiment planning. Do not present it as a calibrated digital twin
      until you insert measured laser powers, beam waists, vapor-cell temperature, RF field,
      magnetic-field map, and real transition states.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import math
import itertools
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    from scipy.signal import find_peaks
except Exception:
    find_peaks = None

# -----------------------------------------------------------------------------
# User-editable experimental constraints
# -----------------------------------------------------------------------------
OUTDIR = Path("rydberg_outputs")
OUTDIR.mkdir(exist_ok=True)

CONFIG = {
    # Lab RF availability from current known hardware.
    "rf_min_GHz": 0.85,
    "rf_max_GHz": 6.40,
    "priority_rf_GHz": [1.0, 1.8, 2.4, 5.0],

    # Candidate Rydberg state scan range. Increase n_max if needed, but high-n
    # states become more stray-field-sensitive and experimentally fragile.
    "n_min": 25,
    "n_max": 160,
    "dn_search": 4,  # search n2 around n1 +/- this value for microwave links

    # Optically accessible Rydberg states in a standard 87Rb 5S -> 5P -> nS/nD ladder.
    # l: 0=S, 1=P, 2=D, 3=F
    "optical_rydberg_l_values": [0, 2],

    # Magnetic field scan for forward-model plots.
    "B0_scan_mT": np.linspace(0.0, 2.5, 126),
    "B0_full_mT": np.linspace(0.0, 20.0, 401),

    # Initial EIT model parameters. Replace with measured values later.
    "Omega_p_MHz": 0.05,       # weak probe Rabi frequency
    "Omega_c_MHz": 5.0,        # coupling Rabi frequency
    "gamma_ge_MHz": 6.0,       # optical coherence decay scale
    "gamma_gr_MHz": 0.45,      # ground-Rydberg coherence
    "gamma_gs_MHz": 0.45,      # ground-upper-Rydberg coherence
    "OD": 2.0,                 # effective optical depth, illustrative
    "probe_detuning_MHz": np.linspace(-18.0, 18.0, 901),
    "rf_detuning_MHz": np.linspace(-24.0, 24.0, 401),
    "rf_rabi_examples_MHz": [0.0, 6.0, 10.0, 14.0],

    # Thresholds / ranking weights
    "target_B0_mT_for_zeeman_score": 1.0,
    "max_results": 80,
}

# Constants
MU_B_OVER_H_MHz_PER_mT = 13.99624555  # MHz/mT, mu_B/h
C_LIGHT = 299792458.0
RYD_FREQ_HZ = 3.2898419602508e15  # Rydberg constant * c (approx) in Hz

# Rb quantum defects for fallback estimates. Values are planning-grade only.
# Key: (l, j2) where j2 = 2*j as integer.
RB87_QD = {
    (0, 1): 3.1311804,   # S1/2
    (1, 1): 2.6548849,   # P1/2
    (1, 3): 2.6416737,   # P3/2
    (2, 3): 1.348091,    # D3/2
    (2, 5): 1.346465,    # D5/2
    (3, 5): 0.0165437,   # F5/2 approx
    (3, 7): 0.0165192,   # F7/2 approx
}

L_LETTER = {0: "S", 1: "P", 2: "D", 3: "F", 4: "G"}


def j_values_for_l(l: int):
    """Allowed j values for alkali valence electron with spin 1/2."""
    if l == 0:
        return [0.5]
    return [l - 0.5, l + 0.5]


def state_label(n: int, l: int, j: float) -> str:
    return f"{n}{L_LETTER.get(l, '?')}{int(round(2*j))}/2"


def lande_g(l: int, j: float, s: float = 0.5) -> float:
    """Landé g-factor in LS coupling."""
    if j == 0:
        return 0.0
    return 1.0 + (j*(j+1) + s*(s+1) - l*(l+1)) / (2*j*(j+1))


def mj_values(j: float):
    two_j = int(round(2*j))
    return np.arange(-two_j, two_j + 1, 2) / 2.0


def fallback_energy_Hz(n: int, l: int, j: float) -> float:
    """Approximate Rydberg binding energy relative to ionization, in Hz.

    Energy is negative relative to ionization. This is for fallback screening only.
    """
    j2 = int(round(2*j))
    delta = RB87_QD.get((l, j2), 0.0 if l >= 3 else np.nan)
    if np.isnan(delta):
        return np.nan
    n_eff = n - delta
    return -RYD_FREQ_HZ / (n_eff**2)


def fallback_transition_frequency_Hz(n1, l1, j1, n2, l2, j2) -> float:
    e1 = fallback_energy_Hz(n1, l1, j1)
    e2 = fallback_energy_Hz(n2, l2, j2)
    return abs(e2 - e1)


def get_arc_atom():
    try:
        from arc import Rubidium87
        return Rubidium87(), True
    except Exception as exc:
        print("ARC import failed. Using quantum-defect fallback frequency estimates only.")
        print(f"ARC error: {exc}")
        return None, False


def safe_arc_transition_frequency(atom, n1, l1, j1, n2, l2, j2):
    """Return transition frequency in Hz. ARC returns Hz in current common usage."""
    try:
        val = atom.getTransitionFrequency(n1, l1, j1, n2, l2, j2)
        return abs(float(val))
    except Exception:
        return np.nan


def safe_arc_dipole(atom, n1, l1, j1, mj1, n2, l2, j2, mj2, q):
    """Return dipole matrix element from ARC if possible.

    ARC may return in atomic units for reduced matrix elements depending on function.
    We only use this for relative ranking, so units are not critical here.
    """
    try:
        return abs(float(atom.getDipoleMatrixElement(n1, l1, j1, mj1, n2, l2, j2, mj2, q)))
    except Exception:
        return np.nan


@dataclass
class Pathway:
    q: int
    mj1: float
    mj2: float
    zeeman_slope_MHz_per_mT: float
    dipole_rel: float


@dataclass
class Candidate:
    lower: str
    upper: str
    n1: int
    l1: int
    j1: float
    n2: int
    l2: int
    j2: float
    freq_GHz: float
    min_detuning_to_priority_MHz: float
    max_dipole_rel: float
    sigma_plus_strength: float
    pi_strength: float
    sigma_minus_strength: float
    max_abs_zeeman_slope_MHz_per_mT: float
    zeeman_span_at_1mT_MHz: float
    n_risk: str
    score: float


def analyse_pathways(atom, arc_available, n1, l1, j1, n2, l2, j2):
    g1 = lande_g(l1, j1)
    g2 = lande_g(l2, j2)
    pathways = []
    for mj1 in mj_values(j1):
        for q in [-1, 0, +1]:
            mj2 = mj1 + q
            if mj2 < -j2 or mj2 > j2:
                continue
            slope = MU_B_OVER_H_MHz_PER_mT * (g2 * mj2 - g1 * mj1)
            dip = np.nan
            if arc_available:
                dip = safe_arc_dipole(atom, n1, l1, j1, mj1, n2, l2, j2, mj2, q)
            # If no ARC dipole, give allowed pathways unit relative strength for plotting.
            if not arc_available or np.isnan(dip):
                dip = 1.0
            pathways.append(Pathway(q=q, mj1=mj1, mj2=mj2,
                                    zeeman_slope_MHz_per_mT=slope,
                                    dipole_rel=dip))
    return pathways


def transition_screening():
    atom, arc_available = get_arc_atom()
    rows = []

    for n1 in range(CONFIG["n_min"], CONFIG["n_max"] + 1):
        for l1 in CONFIG["optical_rydberg_l_values"]:
            for j1 in j_values_for_l(l1):
                for l2 in [l1 - 1, l1 + 1]:
                    if l2 < 0 or l2 > 4:
                        continue
                    for n2 in range(max(1, n1 - CONFIG["dn_search"]), n1 + CONFIG["dn_search"] + 1):
                        for j2 in j_values_for_l(l2):
                            if arc_available:
                                f_Hz = safe_arc_transition_frequency(atom, n1, l1, j1, n2, l2, j2)
                            else:
                                f_Hz = fallback_transition_frequency_Hz(n1, l1, j1, n2, l2, j2)
                            if not np.isfinite(f_Hz):
                                continue
                            f_GHz = f_Hz / 1e9
                            if not (CONFIG["rf_min_GHz"] <= f_GHz <= CONFIG["rf_max_GHz"]):
                                continue

                            pathways = analyse_pathways(atom, arc_available, n1, l1, j1, n2, l2, j2)
                            if not pathways:
                                continue

                            max_dip = max(p.dipole_rel for p in pathways)
                            q_strength = {q: sum(p.dipole_rel**2 for p in pathways if p.q == q) for q in [-1, 0, +1]}
                            slopes = np.array([p.zeeman_slope_MHz_per_mT for p in pathways])
                            zeeman_span = float(np.nanmax(slopes) - np.nanmin(slopes)) * CONFIG["target_B0_mT_for_zeeman_score"]
                            priority_detunings = [abs(f_GHz - x) * 1000 for x in CONFIG["priority_rf_GHz"]]
                            min_priority_detuning = float(np.min(priority_detunings))

                            # Practical risk: very high n can be useful but fragile.
                            n_avg = 0.5 * (n1 + n2)
                            if n_avg < 50:
                                n_risk = "low/moderate-n, likely stronger optical control"
                                risk_penalty = 0.0
                            elif n_avg < 100:
                                n_risk = "mid/high-n, monitor stray fields"
                                risk_penalty = 0.8
                            else:
                                n_risk = "very high-n, high stray-field/linewidth risk"
                                risk_penalty = 2.0

                            # Ranking: favour strong dipole, Zeeman separability, and closeness to likely lab frequencies.
                            # log1p handles different dipole units across ARC versions; ranking remains relative.
                            score = (2.0 * math.log10(1.0 + max_dip)
                                     + 0.08 * zeeman_span
                                     - 0.003 * min_priority_detuning
                                     - risk_penalty)

                            rows.append(Candidate(
                                lower=state_label(n1, l1, j1), upper=state_label(n2, l2, j2),
                                n1=n1, l1=l1, j1=j1, n2=n2, l2=l2, j2=j2,
                                freq_GHz=f_GHz,
                                min_detuning_to_priority_MHz=min_priority_detuning,
                                max_dipole_rel=max_dip,
                                sigma_plus_strength=q_strength[+1],
                                pi_strength=q_strength[0],
                                sigma_minus_strength=q_strength[-1],
                                max_abs_zeeman_slope_MHz_per_mT=float(np.nanmax(np.abs(slopes))),
                                zeeman_span_at_1mT_MHz=zeeman_span,
                                n_risk=n_risk,
                                score=score,
                            ))

    df = pd.DataFrame([asdict(r) for r in rows])
    if df.empty:
        raise RuntimeError("No transitions found in requested RF range. Increase n_max/dn_search or check ARC setup.")
    df = df.sort_values("score", ascending=False).reset_index(drop=True)
    df.to_csv(OUTDIR / "transition_candidates_ranked.csv", index=False)
    df.head(CONFIG["max_results"]).to_csv(OUTDIR / "transition_candidates_top.csv", index=False)

    print("\nTop transition candidates:")
    print(df[["lower", "upper", "freq_GHz", "max_dipole_rel", "zeeman_span_at_1mT_MHz", "n_risk", "score"]].head(20).to_string(index=False))
    return df, atom, arc_available


# -----------------------------------------------------------------------------
# EIT forward model
# -----------------------------------------------------------------------------
def rho_ge_four_level(delta_p, Omega_p, Omega_c, Omega_rf, delta_rf,
                      gamma_ge, gamma_gr, gamma_gs, delta_c=0.0):
    """Weak-probe nested-denominator four-level EIT coherence.

    Parameters are cyclic-frequency MHz. This is a compact planning model.
    """
    # Use complex denominator form; sign convention chosen for smooth qualitative EIT spectra.
    D_s = gamma_gs + 1j * (delta_p + delta_c + delta_rf)
    D_r = gamma_gr + 1j * (delta_p + delta_c) + (Omega_rf**2 / 4.0) / D_s
    D_e = gamma_ge + 1j * delta_p + (Omega_c**2 / 4.0) / D_r
    return 1j * Omega_p / 2.0 / D_e


def transmission_from_rho(rho, OD=2.0):
    """Convert coherence to normalized transmission for plotting."""
    absorption = np.imag(rho)
    # Normalize absorption so plots remain readable with arbitrary units.
    absorption = absorption - np.nanmin(absorption)
    if np.nanmax(absorption) > 0:
        absorption = absorption / np.nanmax(absorption)
    T = np.exp(-OD * absorption)
    # Rescale to roughly thesis-friendly 0.1-0.95 range.
    return 0.08 + 0.87 * (T - T.min()) / (T.max() - T.min() + 1e-12)


def eit_spectrum(delta_p, Omega_c=None, Omega_rf=0.0, delta_rf=0.0, OD=None):
    cfg = CONFIG
    Omega_p = cfg["Omega_p_MHz"]
    if Omega_c is None:
        Omega_c = cfg["Omega_c_MHz"]
    if OD is None:
        OD = cfg["OD"]
    rho = rho_ge_four_level(delta_p, Omega_p, Omega_c, Omega_rf, delta_rf,
                            cfg["gamma_ge_MHz"], cfg["gamma_gr_MHz"], cfg["gamma_gs_MHz"])
    return transmission_from_rho(rho, OD=OD)


def extract_basic_features(delta_p, T):
    """Extract simple feature metrics from a spectrum."""
    delta_p = np.asarray(delta_p)
    T = np.asarray(T)
    idx_max = int(np.nanargmax(T))
    idx_min = int(np.nanargmin(T))
    contrast = float(np.nanmax(T) - np.nanmin(T))
    center_MHz = float(delta_p[idx_max])
    # crude width: region above half contrast around max
    half = np.nanmin(T) + 0.5 * contrast
    above = T >= half
    if np.any(above):
        width_MHz = float(delta_p[above][-1] - delta_p[above][0])
    else:
        width_MHz = np.nan
    asym = float(np.trapz(T[delta_p >= 0], delta_p[delta_p >= 0]) - np.trapz(T[delta_p < 0], delta_p[delta_p < 0]))

    splitting = np.nan
    if find_peaks is not None:
        peaks, _ = find_peaks(T, distance=max(3, len(T)//20), prominence=0.02)
        if len(peaks) >= 2:
            # take two highest peaks
            top = peaks[np.argsort(T[peaks])[-2:]]
            splitting = float(abs(delta_p[top[1]] - delta_p[top[0]]))
    return {
        "center_MHz": center_MHz,
        "width_MHz": width_MHz,
        "contrast": contrast,
        "asymmetry_area": asym,
        "splitting_MHz": splitting,
        "max_T": float(np.nanmax(T)),
        "min_T": float(np.nanmin(T)),
    }


def plot_transition_candidates(df):
    top = df.head(60).copy()
    fig, ax = plt.subplots(figsize=(9, 5))
    sc = ax.scatter(top["freq_GHz"], top["zeeman_span_at_1mT_MHz"],
                    s=40 + 10*np.log1p(top["max_dipole_rel"].clip(lower=0)),
                    c=top["score"], cmap="viridis", edgecolor="k", linewidth=0.4)
    ax.set_xlabel("Transition frequency (GHz)")
    ax.set_ylabel("Zeeman pathway span at 1 mT (MHz)")
    ax.set_title("Ranked 87Rb candidate Rydberg-Rydberg transitions")
    for f in CONFIG["priority_rf_GHz"]:
        if CONFIG["rf_min_GHz"] <= f <= CONFIG["rf_max_GHz"]:
            ax.axvline(f, linestyle="--", linewidth=0.8, alpha=0.5)
            ax.text(f, ax.get_ylim()[1]*0.96, f"{f:g} GHz", rotation=90, va="top", ha="right", fontsize=8)
    cbar = fig.colorbar(sc, ax=ax)
    cbar.set_label("Ranking score")
    fig.tight_layout()
    fig.savefig(OUTDIR / "transition_candidate_map.png", dpi=300)
    fig.savefig(OUTDIR / "transition_candidate_map.pdf")
    plt.close(fig)


def plot_zeeman_for_candidate(row):
    g1 = lande_g(int(row.l1), float(row.j1))
    g2 = lande_g(int(row.l2), float(row.j2))
    B = CONFIG["B0_scan_mT"]

    fig, ax = plt.subplots(figsize=(8, 5))
    records = []
    for mj1 in mj_values(float(row.j1)):
        for q in [-1, 0, +1]:
            mj2 = mj1 + q
            if mj2 < -float(row.j2) or mj2 > float(row.j2):
                continue
            slope = MU_B_OVER_H_MHz_PER_mT * (g2*mj2 - g1*mj1)
            shift = slope * B
            lab = {+1: r"$\sigma^+$", 0: r"$\pi$", -1: r"$\sigma^-$"}[q]
            ax.plot(B, row.freq_GHz*1000 + shift, linewidth=1.0, alpha=0.75, label=f"{lab}, mj={mj1:g}->{mj2:g}")
            records.append({"q": q, "mj1": mj1, "mj2": mj2, "slope_MHz_per_mT": slope})
    ax.set_xlabel(r"Magnetic bias $B_0$ (mT)")
    ax.set_ylabel("Transition frequency (MHz)")
    ax.set_title(f"Zeeman-pathway tuning: {row.lower} → {row.upper}")
    # Avoid unreadable legends if many pathways.
    if len(records) <= 10:
        ax.legend(fontsize=7, ncol=2)
    fig.tight_layout()
    fig.savefig(OUTDIR / "selected_candidate_zeeman_paths.png", dpi=300)
    fig.savefig(OUTDIR / "selected_candidate_zeeman_paths.pdf")
    plt.close(fig)
    pd.DataFrame(records).to_csv(OUTDIR / "selected_candidate_zeeman_pathways.csv", index=False)


def plot_eit_baselines():
    dp = CONFIG["probe_detuning_MHz"]
    T_coupling_off = eit_spectrum(dp, Omega_c=0.0, Omega_rf=0.0)
    T_coupling_on = eit_spectrum(dp, Omega_c=CONFIG["Omega_c_MHz"], Omega_rf=0.0)

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(dp, T_coupling_off, "--", linewidth=2, label="Coupling off")
    ax.plot(dp, T_coupling_on, linewidth=2, label="Coupling on")
    ax.set_xlabel(r"Probe detuning, $\Delta_p$ (MHz)")
    ax.set_ylabel("Relative probe transmission")
    ax.set_title("Baseline ladder-EIT response")
    ax.legend()
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUTDIR / "eit_baseline_coupling_on_off.png", dpi=300)
    fig.savefig(OUTDIR / "eit_baseline_coupling_on_off.pdf")
    plt.close(fig)

    pd.DataFrame({"probe_detuning_MHz": dp, "T_coupling_off": T_coupling_off,
                  "T_coupling_on": T_coupling_on}).to_csv(OUTDIR / "eit_baseline_coupling_on_off.csv", index=False)


def plot_rf_coupled_eit():
    dp = CONFIG["probe_detuning_MHz"]
    fig, ax = plt.subplots(figsize=(7, 5))
    data = {"probe_detuning_MHz": dp}
    for Om in CONFIG["rf_rabi_examples_MHz"]:
        T = eit_spectrum(dp, Omega_rf=Om, delta_rf=0.0)
        label = "RF off" if Om == 0 else rf"$\Omega_{{RF}}={Om:g}$ MHz"
        ax.plot(dp, T, linewidth=2, label=label)
        data[f"T_OmegaRF_{Om:g}_MHz"] = T
    ax.set_xlabel(r"Probe detuning, $\Delta_p$ (MHz)")
    ax.set_ylabel("Relative probe transmission")
    ax.set_title("RF-coupled EIT response")
    ax.legend()
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUTDIR / "eit_rf_coupled_spectra.png", dpi=300)
    fig.savefig(OUTDIR / "eit_rf_coupled_spectra.pdf")
    plt.close(fig)
    pd.DataFrame(data).to_csv(OUTDIR / "eit_rf_coupled_spectra.csv", index=False)


def plot_rf_detuning_map():
    dp = CONFIG["probe_detuning_MHz"]
    drf = CONFIG["rf_detuning_MHz"]
    T0 = eit_spectrum(dp, Omega_rf=0.0, delta_rf=0.0)
    M = np.empty((len(drf), len(dp)))
    for i, d in enumerate(drf):
        T = eit_spectrum(dp, Omega_rf=8.0, delta_rf=d)
        M[i, :] = T - T0
    fig, ax = plt.subplots(figsize=(7.2, 5.4))
    im = ax.imshow(M, origin="lower", aspect="auto",
                   extent=[dp.min(), dp.max(), drf.min(), drf.max()],
                   cmap="coolwarm", vmin=-np.nanmax(abs(M)), vmax=np.nanmax(abs(M)))
    ax.set_xlabel(r"Probe detuning, $\Delta_p$ (MHz)")
    ax.set_ylabel(r"RF detuning, $\Delta_{RF}$ (MHz)")
    ax.set_title(r"RF-detuning response, $\Delta T_{RF}$")
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label(r"$\Delta T$")
    fig.tight_layout()
    fig.savefig(OUTDIR / "eit_rf_detuning_response_map.png", dpi=300)
    fig.savefig(OUTDIR / "eit_rf_detuning_response_map.pdf")
    plt.close(fig)
    pd.DataFrame(M, index=drf, columns=dp).to_csv(OUTDIR / "eit_rf_detuning_response_map.csv")


def polarization_weights(kind: str):
    """Return relative RF Rabi weights for sigma-, pi, sigma+ components.

    This assumes k_RF || B0 for circular mapping. If your geometry differs, replace these.
    """
    k = kind.lower()
    if k == "linear_transverse":
        return {-1: 1/np.sqrt(2), 0: 0.0, +1: 1/np.sqrt(2)}
    if k == "rhcp":
        return {-1: 0.0, 0: 0.0, +1: 1.0}
    if k == "lhcp":
        return {-1: 1.0, 0: 0.0, +1: 0.0}
    if k == "pi_linear":
        return {-1: 0.0, 0: 1.0, +1: 0.0}
    raise ValueError(f"Unknown polarization kind: {kind}")


def combined_polarization_spectrum(delta_p, B0_mT, base_rf_rabi_MHz, zeeman_slopes, pol_kind="linear_transverse", reverse_B=False):
    """Combine simplified sigma/pi spectra incoherently for planning.

    zeeman_slopes: dict q -> representative MHz/mT slope.
    """
    weights = polarization_weights(pol_kind)
    out = np.zeros_like(delta_p, dtype=float)
    norm = 0.0
    B_eff = -B0_mT if reverse_B else B0_mT
    for q, w in weights.items():
        if w == 0:
            continue
        # The Zeeman shift changes the RF detuning for that pathway.
        d_rf = -zeeman_slopes.get(q, 0.0) * B_eff
        T = eit_spectrum(delta_p, Omega_rf=base_rf_rabi_MHz * abs(w), delta_rf=d_rf)
        out += (abs(w)**2) * T
        norm += abs(w)**2
    return out / max(norm, 1e-12)


def representative_q_slopes(row):
    """Choose representative high-dipole / max-absolute-slope for q=-1,0,+1."""
    atom, arc_available = get_arc_atom()
    pathways = analyse_pathways(atom, arc_available, int(row.n1), int(row.l1), float(row.j1), int(row.n2), int(row.l2), float(row.j2))
    slopes = {}
    for q in [-1, 0, +1]:
        ps = [p for p in pathways if p.q == q]
        if not ps:
            slopes[q] = 0.0
        else:
            # pick the pathway with largest dipole, then absolute slope
            ps = sorted(ps, key=lambda p: (p.dipole_rel, abs(p.zeeman_slope_MHz_per_mT)), reverse=True)
            slopes[q] = ps[0].zeeman_slope_MHz_per_mT
    return slopes


def plot_magnetic_bias_and_polarization_maps(row):
    dp = CONFIG["probe_detuning_MHz"]
    B = CONFIG["B0_scan_mT"]
    slopes = representative_q_slopes(row)

    T0 = combined_polarization_spectrum(dp, 0.0, 8.0, slopes, pol_kind="linear_transverse")
    M = np.empty((len(B), len(dp)))
    for i, b in enumerate(B):
        T = combined_polarization_spectrum(dp, b, 8.0, slopes, pol_kind="linear_transverse")
        M[i, :] = T - T0

    fig, ax = plt.subplots(figsize=(7.2, 5.4))
    im = ax.imshow(M, origin="lower", aspect="auto",
                   extent=[dp.min(), dp.max(), B.min(), B.max()],
                   cmap="coolwarm", vmin=-np.nanmax(abs(M)), vmax=np.nanmax(abs(M)))
    ax.set_xlabel(r"Probe detuning, $\Delta_p$ (MHz)")
    ax.set_ylabel(r"Magnetic bias, $B_0$ (mT)")
    ax.set_title(r"Zeeman-bias response, $\Delta T_B$")
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label(r"$\Delta T$")
    fig.tight_layout()
    fig.savefig(OUTDIR / "eit_magnetic_bias_response_map.png", dpi=300)
    fig.savefig(OUTDIR / "eit_magnetic_bias_response_map.pdf")
    plt.close(fig)
    pd.DataFrame(M, index=B, columns=dp).to_csv(OUTDIR / "eit_magnetic_bias_response_map.csv")

    # Polarization spectra at a representative bias.
    B_test = 1.0
    pols = ["linear_transverse", "rhcp", "lhcp"]
    fig, ax = plt.subplots(figsize=(7, 5))
    feats = []
    data = {"probe_detuning_MHz": dp}
    for p in pols:
        T = combined_polarization_spectrum(dp, B_test, 8.0, slopes, pol_kind=p)
        ax.plot(dp, T, linewidth=2, label=f"{p}, +B0")
        data[f"T_{p}_plusB"] = T
        f = extract_basic_features(dp, T)
        f.update({"polarization": p, "B0_mT": B_test, "B_reversed": False})
        feats.append(f)
    # RHCP with reversed B0 as a powerful control.
    T = combined_polarization_spectrum(dp, B_test, 8.0, slopes, pol_kind="rhcp", reverse_B=True)
    ax.plot(dp, T, "--", linewidth=2, label="rhcp, -B0")
    data["T_rhcp_minusB"] = T
    f = extract_basic_features(dp, T)
    f.update({"polarization": "rhcp", "B0_mT": B_test, "B_reversed": True})
    feats.append(f)

    ax.set_xlabel(r"Probe detuning, $\Delta_p$ (MHz)")
    ax.set_ylabel("Relative probe transmission")
    ax.set_title(f"Predicted polarization-dependent spectra at B0={B_test:g} mT")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUTDIR / "eit_polarization_comparison_plus_minus_B0.png", dpi=300)
    fig.savefig(OUTDIR / "eit_polarization_comparison_plus_minus_B0.pdf")
    plt.close(fig)

    pd.DataFrame(data).to_csv(OUTDIR / "eit_polarization_comparison_plus_minus_B0.csv", index=False)
    pd.DataFrame(feats).to_csv(OUTDIR / "polarization_feature_summary.csv", index=False)


def write_experimental_plan(top_row):
    text = f"""
Rydberg polarization-sensing simulation summary
==============================================

Selected candidate for initial planning
---------------------------------------
Lower state: {top_row.lower}
Upper state: {top_row.upper}
Transition frequency: {top_row.freq_GHz:.6f} GHz
Max relative ARC dipole metric: {top_row.max_dipole_rel:.4g}
Zeeman pathway span at 1 mT: {top_row.zeeman_span_at_1mT_MHz:.3f} MHz
Risk note: {top_row.n_risk}

Experimental translation
------------------------
1. Verify RF-off ladder EIT first using 780 nm probe + 480 nm coupling.
2. Tune the RF source near {top_row.freq_GHz:.6f} GHz.
3. Use a known linearly polarized LPDA input first. Do not start with RHCP.
4. Sweep RF frequency over at least +/- 20 MHz around the candidate transition.
5. Sweep RF power to check whether the optical feature grows with RF field strength.
6. Apply B0 = 0, 0.5, 1.0, 2.0 mT and repeat spectra.
7. Only after repeatable RF-on response is observed, compare linear/RHCP/LHCP or RHCP with +B0/-B0.
8. Record full probe-transmission spectra T(Delta_p), not single voltage readings.

Decision gates
--------------
Gate 1: EIT baseline exists and coupling-on/off traces differ repeatably.
Gate 2: RF-on feature change exceeds RF-off baseline variation.
Gate 3: B0 sweep produces repeatable feature changes consistent with Zeeman-pathway simulation.
Gate 4: Known polarization states produce feature vectors separated beyond covariance.

Files generated
---------------
- transition_candidates_ranked.csv
- transition_candidates_top.csv
- transition_candidate_map.png/pdf
- selected_candidate_zeeman_paths.png/pdf
- eit_baseline_coupling_on_off.png/pdf/csv
- eit_rf_coupled_spectra.png/pdf/csv
- eit_rf_detuning_response_map.png/pdf/csv
- eit_magnetic_bias_response_map.png/pdf/csv
- eit_polarization_comparison_plus_minus_B0.png/pdf/csv
- polarization_feature_summary.csv

Important caveat
----------------
These simulations provide a transition-screening and measurement-planning basis.
They do not replace experimental EIT verification. The model should be updated with:
laser powers, beam waists, linewidths, vapor-cell length/temperature, measured RF field,
magnetic-field map, selected transition, and actual photodetector gain/noise.
"""
    (OUTDIR / "simulation_summary_and_experimental_plan.txt").write_text(text, encoding="utf-8")
    print(text)


def main():
    print("Running 87Rb transition screening and Rydberg-EIT planning simulations...")
    print(f"Output directory: {OUTDIR.resolve()}")
    df, atom, arc_available = transition_screening()
    plot_transition_candidates(df)
    top = df.iloc[0]
    plot_zeeman_for_candidate(top)
    plot_eit_baselines()
    plot_rf_coupled_eit()
    plot_rf_detuning_map()
    plot_magnetic_bias_and_polarization_maps(top)
    write_experimental_plan(top)
    print("Done. Inspect the rydberg_outputs folder.")


if __name__ == "__main__":
    main()