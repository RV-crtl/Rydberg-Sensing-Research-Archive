# HFSS electromagnetic campaign lineage and design decisions

**Primary simulation policy:** Ansys HFSS-derived electromagnetic results are the authoritative simulation observations. Retain solver-generated complex X/Y fields, S-parameters (when solved), setup definitions, mesh histories, independent-mesh data, state definitions, instrument matrices, plots and original return archives. Do not fabricate additional noise or manufacturing tolerances to make a model look “realistic”; those belong to explicitly separate future studies.

## Multiple concurrent version families

The project repeatedly revised both the underlying *physical geometry* and *runner software*. V-numbers are meaningful only **within their branch**; e.g. “V4” of one 70 × 50 mm resonator is unrelated to “V4xx” of a six-state 43 mm cell. Index by design-family ID + geometry hash + solver-case ID + original creation date.

| Campaign branch | Main aim | Evidence / methodological lesson |
|---|---|---|
| MATLAB/CST precursor | Linear/CP design, basic transmission, unit-cell and 200 mm aperture concepts | Analytical/surrogate outputs are not native HFSS |
| SAP18B / four-state PCB (September) | Large switchable panel at ~1.8 GHz; reference H/V and complete instrument matrix | Scripts and unit-test passes do not imply every HFSS case solved; initial screens may be incomplete |
| GEN2 tetrahedral four-state (early October) | Four non-coplanar states with strong Stokes observability and low κ | Some preliminary rank-four responses later showed unacceptable independent mesh disagreement |
| APL TetraStokes V1.x (early October) | Periodic four-state layout plus finite verification | An early REF_25 state could have rank four but κ ~180.67: rank without conditioning was inadequate |
| Standalone folded resonator V5 / V50xx | A finite 70 × 50 mm RO4003C board with four bridge states | One screen tested 17 candidates / 170 successful HFSS solves; no candidate met all targeted condition/S3 gates |
| V7xx / V9.x finite verification | More advanced 4- and 6-state finite response, multiple frequencies | Full rank could coexist with 7–9% independent complex-field disagreement and transfer-sensitive calibration |
| V4xx periodic split-loop / six-state | Native X/Y field exports, six analyser states, improved L-band response | Later studies progressed from ~22.06 κ at 1.85 GHz towards 9.53 at 1.925 GHz in a selected design; **do not equate frequency- or geometry-specific values** |
| V41–V44 information-aware study | Bounded 36-candidate optimisation, mesh validation, finite array, fixed-time information allocation | Current paper evidence, data and scripts preserved in [V44 research archive](../../evidence/hfss/v44-reproducibility/) |

## Documented scientific screens

The research history contains several informative **non-final** results, each tied to its own assumptions:

- An early local circular-sensitive “windmill” type element generated strong near-field handedness contrast, but periodic far-field contrast was much weaker. This differentiates field confinement near the rubidium cell from plane-wave CP transmission.
- A preliminary TetraStokes design had full-rank response but poor angular spread/condition number and required additional finite-board studies; an invertible matrix is not automatically measurement-grade.
- A 17-geometry finite resonator screen reported a candidate condition number around **17.05**, high S3 sensitivity for a *different* candidate, and **zero** simultaneous passes for its joint numerical gates. Optimising only one criterion was inadequate.
- The finite-resonator mesh study around **1.64 GHz** reported a roughly **9.15%** complex-field disagreement in one comparison and material changes in calibration-transfer error. Adaptive convergence alone did not establish the desired complex-field accuracy.
- An intermediate six-state periodic 1.850 GHz case reported κ about **22.06**, rank four, and a 0.749% mesh-matrix difference. This is not the final 1.925 GHz selected design.
- Later V44 manuscript evidence reports **36 geometry candidates**, a **250 MHz accepted sampled band**, rank four, **κ2 = 9.53 at 1.925 GHz**, **0.551%** selected periodic mesh discrepancy, a 3 × 3 finite check, and a **40.8%** modelled fixed-time information criterion gain.
- Finite aperture retained observability in a reported study but the sensitivity along S3 and the transfer of calibration from an ideal periodic cell remained qualified. Avoid claims of seamless atomic full-Stokes hardware transfer.

These historical figures come from their respective modelling branches, not an apples-to-apples model benchmark. The current paper and numeric artefacts are the governing source for *current* research claims.

## Reproducible case identity

Assign every HFSS result a key with:
1. **Geometry**: design ID, material, thickness, copper layer/polygons, switch state, model source hash.
2. **Excitation**: polarisation Jones basis/phase convention, incident direction, port or Floquet definition, input power normalisation.
3. **Observation**: local E-field ROI (e.g. 70 × 50 mm), axial sampling depth (the historical design considered ~10–12 mm), field point grid, any spatial weighting.
4. **Numerics**: AEDT/PyAEDT versions, solver boundary, mesh passes/element count, ΔS or energy residual criteria, port mode conventions, complex field export units.
5. **Validation**: independent adapted mesh, frequency sample set, finite vs periodic state, calibration row transformation, source checksum.
6. **Evidence**: RESULT.json, raw/complex CSV, plots, machine verdict, stdout/log, optional native .aedt and .aedtresults, return ZIP hash.

Keep original HFSS-run files untouched; create downstream derived folders for matrices and paper figures.

## Recommended archive directory layout

For future actual campaigns:

- campaigns/CASE_ID/model/ — native HFSS geometry/project and parameter snapshot;
- campaigns/CASE_ID/raw/ — solver logs, mesh, S-matrix/Jones/complex E-field exports;
- campaigns/CASE_ID/derived/ — A, SVD, rank, condition, Stokes tests;
- campaigns/CASE_ID/figures/ — provenance-labelled figures regenerated from derived inputs;
- campaigns/CASE_ID/VERDICT.json — exact gates, passed/failed/unassessed, source hashes.

The [HFSS SOP](../methods/HFSS_SOP.md) and [native evidence catalogue](../results/EVIDENCE_INDEX.md) specify reproduction steps. The [scientific verification gates](VERIFICATION_AND_INFORMATION_MATRIX.md) define what numerical success means.
