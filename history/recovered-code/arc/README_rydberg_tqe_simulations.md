# Advanced Rydberg polarisation poster simulations

## Run
```bash
python -m pip install -r rydberg_tqe_requirements.txt
python rydberg_tqe_advanced_poster_simulations.py --quick
python rydberg_tqe_advanced_poster_simulations.py
```

## Before using the figures on the poster
Edit the configuration block at the top of the script, especially:

1. `COUPLING_LASER_WINDOW_NM` — use the **wavemeter-verified vacuum-wavelength range**. Leave `None` until verified.
2. `RF_K_TO_B_DEG` — actual RF propagation direction relative to the magnetic quantisation axis.
3. `RF_E_PEAK_V_PER_M` — measured/validated electric field at the vapour cell if available.
4. `OMEGA_PROBE_MHZ`, `OMEGA_COUPLING_MHZ`, `GAMMA_R_MHZ`, `EFFECTIVE_OD` — replace planning values with measured/fitted values when available.
5. `COUPLING_OPTICAL_Q` — set only if the 480-nm polarisation relative to B0 and optical-state preparation are known.

## Outputs
- `fig1_arc_three_way_feasibility.*` — ARC transition frequency vs coupling wavelength; DME and Zeeman span encode candidate quality.
- `fig2_arc_zeeman_pathway_fan.*` — sigma-/pi/sigma+ Zeeman branches, weighted by ARC DME, with a coil-current top axis.
- `fig3_equal_power_polarisation_fingerprints.*` — equal-|E| RF states compared using coherent mJ dressing + Doppler-averaged weak-probe EIT.
- `fig4_polarisation_identifiability_map.*` — Jacobian/Fisher-style local identifiability vs B0 and RF detuning; no invented classifier accuracy.
- `fig5_poincare_spectral_manifold.*` — optional PCA/SVD map from Poincare states to simulated spectral manifold.
- CSVs for every figure and `selected_candidate.json`.
- `assumptions_provenance_and_claim_boundary.txt` — read before presenting the results.

## Poster wording
Use **MODELLED RECEIVER BEHAVIOUR** or **SIMULATION-GUIDED FEASIBILITY**, not “experimental results”.

The script intentionally fails if ARC is not installed rather than silently producing approximate quantum-defect data.