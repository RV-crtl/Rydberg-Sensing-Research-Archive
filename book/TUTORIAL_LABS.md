# Guided laboratory and software tutorials — from basics to native evidence

Every lab has an **expected result**, **source**, **check**, **extension**, and **common failure**. Examples are educational unless a specific imported source is cited; no tutorial creates synthetic “measured” data.

## Lab 1 — State vector sanity

Represent `|+x⟩=(|g⟩+|e⟩)/√2`. Check norm exactly one; use a complex off-diagonal phase and compute Pauli expectations. Expected: ⟨σz⟩=0, state purity one. Failure: phase-conjugation or normalization mistake. [Chapter 01](chapters/01-mathematical-language.md).

## Lab 2 — Selection rules and optical access

Construct a state sheet from actual `n,ℓ,j,mj/F,mF`. Enumerate `Δℓ=±1, Δm=q` and optical ladder paths. Run ARC Rubidium87 `getTransitionFrequency` and dipole APIs; preserve numbers and version. Expected: only physically allowed transitions survive *before* ranking candidates by strength. [ARC chapter](chapters/13-quantum-defect-and-arc.md).

## Lab 3 — RydIQule pure steady-state solver

Use the official minimal three-state `rq.Sensor(3)` graph with two optical couplings and transit broadening. Run `solve_steady_state`, check returned shape, trace/purity and sensitivity to detuning, then switch to a physical Rb Cell and appropriate optical observable. Expected: qualitative EIT window/weak-probe limits; *not* measured Rb data. [RydIQule chapter](chapters/14-rydiqule-lab.md).

## Lab 4 — Optical and RF-on/off experiment

Define a four-condition matrix: RF on/off × coupling on/off. Collect same photodetector settings and raw, unmodified traces with laser reference. Expected: changes attributable specifically to the Rydberg ladder are absent when the coupling is blocked. Failure: peaks persisting under coupling-off conditions require artefact investigation. [Spectral diagnosis](chapters/17-spectroscopy-diagnostics.md).

## Lab 5 — Three-angle polariser plus missing S3

Measure linear H, V, +45°, −45° states after calibrating orientation. Compute S1,S2 and show that changing relative Jones phase can alter S3 while leaving the linear basis measurement ambiguous in suitable cases. Expected: the inverse problem lacks circular information until independent handedness-sensitive states are introduced. [Chapter 11](chapters/11-stokes-jones.md).

## Lab 6 — Native HFSS six-state matrix

Inspect [V42_C033_INSTRUMENT_MATRIX.csv](../papers/manuscript-source/data/V42_C033_INSTRUMENT_MATRIX.csv). Recompute rank and row-normalised SVD, compare with documented 1.925 GHz results and reference the actual source field provenance. No random Gaussian noise; do not claim that 1,231 algebraic input points are 1,231 HFSS solves. [HFSS chapter](chapters/18-hfss-metasurface.md).

## Lab 7 — Finite mesh failure

Compare documented V4.21 finite cross-mesh values against accepted criteria. Explain why the periodic 0.551% result does not rescue the finite 5 mm worst transfer discrepancy near 76.92%. Expected: *fail finite transfer* until a new independent mesh and sample-volume comparison is performed. [Finite chapter](chapters/20-finite-calibration.md).

## Lab 8 — Research evidence and publication

Choose one figure and write a provenance chain: native source → original complex field → matrix → numerical plot → labelled caption → manuscript claim → validation gate. Expected: each link references the same run/geometry/states, and no “final” file label replaces an actual acceptance test. [Chapter 24](chapters/24-publication-and-future.md).

## Lab 9 — Real-time sandboxed code

Open the [interactive code lab](../site/lab.html). Adjust frequency, RF field, optical linewidth or Stokes azimuth and inspect the live model plot. Use the **optional browser Python runtime** only for user-initiated safe educational examples. This runs in-browser, cannot access actual HFSS or hardware and is not a general server-side compiler. The numerical outputs are illustrations with explicit equations and sources.

## Lab 10 — Scientific literature review

Open the weekly GitHub Actions research watch, take one paper's DOI/arXiv reference, verify journal/preprint status and underlying method, and write a factual claim matrix: what was experimentally measured, what was modelled, what remains limited and how it changes the project's novelty boundary. Do not merge metadata-only claims into the scientific book as verified facts.

## Reflective end-of-part questions

- What does an atomic optical spectrum measure, and how does it differ from direct RF antenna output?
- What assumption transforms a complex Jones response into a real Stokes projection row?
- How would you prove the circular coordinate is identifiable despite frequency drift and nonuniformity?
- Which mesh adaptation produces an independent finite-array check?
- How do current accepted periodic simulations differ from planned hardware work?

**Answers:** See the linked chapters, in particular [Chapter 12](chapters/12-identifiability.md), [Chapter 17](chapters/17-spectroscopy-diagnostics.md), [Chapter 20](chapters/20-finite-calibration.md) and [current evidence ledger](CURRENT_STATE.md).
