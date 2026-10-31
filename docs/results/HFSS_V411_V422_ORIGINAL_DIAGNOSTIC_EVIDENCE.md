# Historical HFSS numerical verification — source-backed audit

This record is transcribed from original recovered V412, V416, V418, V420 and V422 ZIP members. The ZIPs are checksum-registered in [the binary import ledger](../../history/binary-imports/ORIGINAL_BINARY_SOURCES_TO_IMPORT.csv) but **the original ZIP bytes have not yet been committed to GitHub**. These are case-specific historical HFSS/derived calculations, not Rb-87 atomic measurements.

| Case | Original result | Scientific conclusion |
|---|---|---|
| V4.11 periodic, 1.825 GHz | Condition 32.0349; matrix difference 0.26087%; worst transfer 3.08006% | Periodic dual-mesh screen |
| V4.11 periodic, 1.850 GHz | Condition 22.0560; matrix difference 0.74932%; worst transfer 3.70614% | Separate periodic screen |
| V4.16 early search | One completed screened candidate C000; 175 MHz sampled span | Interim result, not full campaign |
| V4.16 later search | 36 candidates; C033 250 MHz and 11 passing samples | Periodic/interpolating screening; not continuously validated hardware bandwidth |
| V4.18 C033, 1.925 GHz | Rank 4; condition 9.528217; 1,231 algebraic polarisation checks; maximum algebraic error about 5.13×10⁻¹⁵ | Mathematical consistency based on archived HFSS data, not 1,231 independent solver or atomic experiments |
| V4.18 release | 18 offline regression tests passed; new HFSS in release environment NOT RUN; windmill/full-finite simulations PENDING | Offline preflight is not a completed electromagnetic campaign |
| V4.19 finite 3×3 | Only five switch masks available at each of four observation depths | Incomplete for full-Stokes evaluation |
| V4.21 finite at 5 mm | Twelve cases converged; matrix difference 6.17993%; worst cross-mesh transfer 76.9166% | Fails finite calibration-transfer criteria |
| V4.21 finite at 10 mm | Matrix difference 4.85311%; worst transfer 55.0915% | Fails finite transfer |
| V4.22 proposed correction | Change MaxDeltaS to MaxDeltaE=0.02 for plane-wave case; E24/E27 2.4/2.7 mm copper mesh; 24 planned field exports | New strict case results not proven by the patch ZIP alone |

## Critical solver interpretation

The original V422 README identified that the prior finite plane-wave runner had configured an S-parameter-type convergence property rather than the actual energy stopping criterion. It specified two independent strict mesh profiles, minimum eight / maximum 42 passes, three consecutive converged passes, 2% refinement and acceptance requirements of rank four, condition ≤35, matrix discrepancy ≤5% and worst cross-mesh Stokes transfer ≤10%.

Convergence in the solver's adaptive indicator **does not imply phase-sensitive local field or Stokes matrix convergence**. A small periodic V44 difference must not be substituted for large V421 finite-panel transfer errors; these are different models and conditions.

## Native source pointers

- V412 → REFERENCE_EVIDENCE/V411_NATIVE_PERIODIC_VERDICT.json.
- V416 → V416_RESULTS/V416_OPTIMISATION_VERDICT.json.
- V418 → ARCHIVED_HFSS_OFFLINE_EVIDENCE/DATA/C033_EQUATION_VERDICT_1.9250.json and V418_RELEASE_VALIDATION.json.
- V420 → V420_REFERENCE_EVIDENCE/V419_INCOMPLETE_SUMMARY.json.
- V422 → V421_INPUT_VERDICT.json, README_V422_FIRST.md and V422_FINITE_CONFIG.json.

The current V44 evidence and manuscript remain separately documented under [V44](../../evidence/hfss/v44-reproducibility/) and [editable source](../../papers/manuscript-source/main.tex).