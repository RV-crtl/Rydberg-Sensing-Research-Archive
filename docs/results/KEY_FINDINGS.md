# Results and engineering interpretation

## Laboratory experiments and receiver feasibility

The earlier report documents a Rb-87 EIT receiver setup, optical readout, antenna/polariser investigations, VNA RF-front-end comparisons and a coil-based magnetic calibration. In that report a **custom steel-rod linear polariser** is described as producing approximately **14–15 dB** pass/reject contrast under its RF reference conditions, and magnetic calibration is reported as **R² ≈ 0.981**. Later poster/manuscript figures describe a separate linear-polarisation measurement condition with approximately **9.7 dB** contrast. These are *not* the same calibrated dataset and must not be combined or averaged without a common measurement protocol.

Refer to the [experimental report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf) and [experimental result notes](EXPERIMENTS.md).

## HFSS simulation and polarimetric information

The current manuscript reports the following **simulation-derived** summary:

| Metric | Reported result | Interpretation / source |
|---|---:|---|
| Candidate copper geometries examined | 36 | Optimisation search described in current article |
| Longest accepted sampled frequency interval | 250 MHz | Increased from 175 MHz under the paper's acceptance criteria |
| Selected periodic-design frequency | 1.925 GHz | Numerical operating point for reported metrics |
| Instrument matrix rank | 4 | Full column rank for four Stokes coordinates under the simulation observation model |
| Row-normalised 2-norm condition number | 9.53 | Conditioning of selected simulated analyser instrument matrix |
| Independently adapted mesh disagreement | 0.551% | Reported numerical verification at selected periodic case |
| Fixed-time, equal-variance dwell allocation improvement | 40.8% | Reduction of inverse-trace uncertainty *criterion* under explicitly stated model |
| Finite array | 3 × 3 cells | Observability retained in investigated case, with reduced S3 sensitivity and calibration-transfer dependence on mesh |

Source: [current article](../../papers/current-manuscript-draft.pdf), [editable paper data](../../papers/manuscript-source/data/) and [HFSS evidence archive](EVIDENCE_INDEX.md). A numerical objective reduction is not an observed 40.8% experimental instrument-noise reduction.

## Evidence interpretation

- **Observed in the laboratory:** receiver/antenna/polariser measurements and Rydberg-EIT-related work described in the experimental report.
- **Computed in HFSS:** electric fields, state-dependent analyser responses, candidate selection, matrix rank/conditioning and finite-array electromagnetic behaviour.
- **Calculated offline from HFSS fields:** instrument matrix, Stokes and information metrics, and model-dependent optimal dwell allocation.
- **Next-stage integration:** calibration of a real optical Rydberg atomic receiver against the RF analyser basis for full-Stokes inference.

The 3 × 3 study should remain visible in scientific reporting rather than being hidden behind periodic-unit-cell metrics: finite geometry is what a future physical receiver must use.
