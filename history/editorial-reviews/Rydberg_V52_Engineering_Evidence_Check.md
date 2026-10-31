# Numerical and engineering evidence — V52

The manuscript prose and author-edited conclusions were **not rewritten**. These observations support the corrected visuals and provide concise engineering interpretations for any subsequent supervisor-approved revision.

## Source-backed results

1. **Rank and switch-state choice.** The C033 periodic HFSS instrument at 1.925 GHz is 6 × 4 and rank four. Its row-normalised spectral condition number is approximately 9.53. Sorting all 15 distinct four-state subsets by *their actual* condition number identifies masks 03/06/08/13 as best (7.6337). That is better conditioning for the selected four rows, but does **not** imply more total statistical information than all six when the six measurements have independent fixed-variance noise and equal measurement time is not imposed.

2. **Gain and indispensability.** Mask 06 has the smallest raw HFSS row gain, about 0.0550, but deleting it increases the trace-of-inverse information metric by approximately 21.44× if all *raw* outputs have equal variance. If all *row-normalised* outputs are assigned equal variance, the analogous change is about 86.41×. These two values refer to different noise assumptions, not contradictory calibration results. They establish a practical design priority: improve the receiving gain of highly informative states while maintaining their independent polarisation projections.

3. **Fair state-number comparison.** At a fixed total acquisition budget, the best five-state combination is **03/06/08/10/13** under equal dwell and **03/06/08/12/13** under optimised dwell. Figure 11 now selects the best subset separately for each criterion. The four-state subset 03/06/08/13 has a minimum optimised inverse-trace objective of 1020.33 (archive units) versus 1044.82 for the six-state optimum, conditional on the independent variance-per-integration-time model and its 2% dwell floor. Switching dead time, state-dependent noise and atomic dynamics are not included.

4. **Independent mesh evidence.** The frequency-by-frequency mesh archive has both passes and failures. Figure 12 now gives actual passing frequencies filled markers and failed frequencies open markers; a low condition number by itself is not a mesh-agreement pass. This reinforces that the reported 250 MHz discovery interval is a sampled optimisation screen, not an independently validated uninterrupted band.

5. **Bound on performance claims.** Periodic complex-field verification at 1.925 GHz is promising, while the finite 3×3 receiver at 1.850 GHz exhibits weaker circular response and substantial cross-mesh calibration transfer. The latter therefore does not establish the hardware or vapour-cell reconstruction accuracy of the former. Ideal conductor bridges also omit real PIN-diode RF parasitics and bias-line interactions. These limits apply to fabrication-performance predictions but do not invalidate the demonstrated periodic electromagnetic measurement basis.

## What has not been claimed

No new HFSS solution or laboratory measurement was run. The corrected figures are post-processing of already archived matrices and tables. The engineering implications above are analyses of those records, not fabricated experimental confirmation.