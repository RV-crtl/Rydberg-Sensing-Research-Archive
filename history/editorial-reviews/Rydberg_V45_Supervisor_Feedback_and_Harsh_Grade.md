# V45 IEEE Access — Supervisor-feedback implementation and critical assessment

## Revision basis
Source manuscript: V44 IEEE Access (`main_access.tex`). No new full-wave HFSS simulations or hardware measurements have been claimed. The scientific numerical results are those already preserved in the V44 archived evidence package.

## Response to the six supervisor comments

1. **Title over-promises constructed hardware — resolved.** The title now begins **"Simulation-Based Design..."** and the abstract, discussion and conclusion consistently distinguish simulation, measured linear-polariser references and proposed hardware integration.
2. **List contributions — resolved.** Five explicit contributions appear early in the Introduction: two-face geometry, six-state Stokes instrument, condition/gain-based optimisation, finite-array/calibration analysis and proposed Rydberg-receiver compatibility. Each is bounded to its actual evidence level.
3. **Explain condition numbers — resolved.** The results include the singular-value definition, relative-error bound, an accessible 1%/9.53 illustration, and a physical comparison of selected periodic results at 1.750, 1.925 and 1.975 GHz. Clarification: 9.53 is *not* a percentage accuracy; 0.551% periodic matrix agreement is *not* the resulting Stokes-error percentage. The project's numerical criterion of 35 is a screening rule, not a universal performance specification.
4. **Conclusion — resolved.** Explicitly organised as achievements, limitations and future work, with numerical findings and actionable implementation steps.
5. **Repetition — substantially reduced.** Duplicated discussions of the sampled bandwidth metric and receiver transfer boundary were consolidated; orphan headings removed; the discussion was rewritten to focus on evidence and design implications.
6. **Write for nonspecialist assessors — improved.** The opening introduces the measurement-information problem using physically intuitive examples; core polarimetric results now explain *why* a numerical result matters before proceeding to the deeper derivations.

## Scientific and document QA
- IEEE Access LaTeX source compiled successfully after repeated runs; final PDF **24 pages**.
- No undefined LaTeX citations or cross-references; figures exist, labels are unique.
- Original simulation checks reproduced **PASS** for two finite 6-by-4 matrices, rank four, Gram admissibility, source switch masks and cross-mesh reconstruction consistency.
- Additional analysis reproduced **PASS** for the 15 four-state subsets, independent C033 rank/condition, Sherman–Morrison state-removal identity and circular-response identity.
- Rendered pages inspected using PDF page images (especially opening pages, result interpretation and conclusion).
- Original figure graphics preserved; no fabricated experiment photographs, HFSS solves, optical spectra or numerical performance improvements were introduced.

## Harsh UNSW Final Thesis Report Rubric 4 estimate

| Official criterion | Weight | Estimated mark | Weighted contribution | Principal justification and deduction |
|---|---:|---:|---:|---|
| Research field and contribution | 25% | 87/100 | 21.75 | Clearer high-value gap and explicit five-part contribution; still lacks matched numerical advantage over published microwave polarimeters. |
| Methodology | 25% | 87/100 | 21.75 | Transparent 36-candidate HFSS search, complex receiving operators, independent periodic meshes and reproducible state-selection tests; finite calibration variance is not mitigated. |
| Engineering the research | 30% | 79/100 | 23.70 | Source-defined electromagnetic topology, strong periodic matrix result, optimisation, measured linear reference and independent computational checks; the finite 3-by-3 cross-mesh transfer remains unstable and ideal switches have not been physically verified. |
| Communicating the research | 20% | 89/100 | 17.80 | Explicit objectives, accessible numerical explanation, IEEE Access presentation and direct achieved/limitation/future-work conclusion; main article remains long and technically dense. |
| **Total** | **100%** | | **85.00/100** | **Borderline High Distinction estimate, not an official mark.** |

### Remaining review concerns
The finite receiving results still show 6.18% matrix discrepancy at 5 mm and large deterministic cross-mesh Stokes reconstruction differences. The simulated PIN switch states remain ideal conductor bridges, with no fabricated bias network or measured end-to-end receiver. The additional textual clarity cannot by itself remove these engineering limits. A publication submission would also need final author, conflicts, funding, ethics (where relevant) and data-availability checks, and the Access template's publication metadata must remain blank until assigned by the publisher.