# V47 independent critical assessment — 26 October 2026

## What changed in response to Andrey and the earlier supervisors

1. **Figure 5(c):** replaced the interrupted, ambiguous branch drawing with a **standard circuit-symbol** analogue of two *closed* RF-driven current loops, each containing a resistive term, inductance, a geometric gap capacitance, and an effective bypass switch. The interlayer capacitive connection and labelled magnetic-coupling term are distinct; the figure no longer implies that dotted admittance labels are wires. The original native HFSS 3x3 topology and D1-D4 markers are retained in panels (a) and (b), while the circuit is visibly labelled (c). No circuit element values are invented.
2. **Scientific interpretation:** added a precise statement that each effective modal switch label summarises the four geometric switch locations; it is *not* a physically wired two-diode schematic or an extracted RLC netlist. Incident-field emf symbols are effective RF drives, not laboratory voltage sources. The paper distinguishes topology-level interpretation from quantitative HFSS extraction.
3. **Referencing:** reorganised the bibliography in **strict order of first in-text citation**. The IEEE `cite` package sorts and groups citations numerically. All 37 bibliography entries are cited; removed an uncited legacy entry. The acknowledgement contains an AI-assistance citation for IEEE compliance review.
4. **Editorial efficiency:** compressed redundant descriptions of the circuit’s limitations, clarified the practical meaning of the condition number, shortened an overly explanatory caption, and kept the main result narrative intact. No unsupported extra RF results were introduced.
5. **Quality control:** preserved the Overleaf-portable class and root-level main document. A PDF compositing issue initially clipped the native unit-cell panel; the corrected print asset is 3000 × 2380 pixels and the final manuscript has been re-rendered to verify the complete geometry and circuit appear together.

## Rubric-based harsh university grade

| Actual assessment criterion | Weight | Estimated standard | Weighted points |
|---|---:|---:|---:|
| Research into the field and contribution | 25% | 87/100 | 21.75 |
| Research methodology and justification | 25% | 87/100 | 21.75 |
| Engineering the research | 30% | 79/100 | 23.70 |
| Communicating the research | 20% | 92/100 | 18.40 |
| **Total** | **100%** | | **85.60/100** |

**Harsh estimated band: High Distinction (borderline).** Not a promised examiner mark.

**Deductions that remain:**
- **Research contribution (−13):** no like-for-like RF polarimeter benchmark with identical aperture, carrier and cost constraints. Novelty is mainly in the application-specific instrument and information-aware selection, not in the invention of Fisher information or polarimetric inverses.
- **Methodology (−13):** ideal-bridge HFSS model; the observation covariance is conditional rather than calibrated experimentally, and gain-aware dwell optimisation is a modelled design, not a measured acquisition improvement.
- **Engineering (−21):** finite-panel cross-mesh transfer remains sensitive (95th-percentile errors 72.2%/156.8% in the archived two directions). Weak finite circular response and the actual packaged PIN/bias network are unverified. A physically circuit-extracted fit has not yet been performed; Figure 5(c) is therefore a qualitative physical interpretation.
- **Communication (−8):** dense technical appendices remain; professional layout is strong but the diagram necessarily compresses distributed full-wave physics into two modal loops. The built-in IEEE Access class generates a few non-content box warnings; final production metadata must be assigned by the publisher.

## IEEE Access editorial readiness (informal critical scale)

| Review dimension | Maximum | Estimated |
|---|---:|---:|
| Contribution and differentiation | 20 | 17 |
| Technical correctness / mathematical rigour | 25 | 18 |
| Validation, reproducibility and scope of claims | 25 | 14 |
| Clarity, figures and manuscript structure | 20 | 18 |
| References, attribution and publication compliance | 10 | 9 |
| **Total** | **100** | **76/100** |

**Interpretation:** credible serious candidate for IEEE Access **after substantive scientific and author compliance review**; 76 is not an acceptance probability. IEEE Access uses independent peer review and a binary editorial decision, not percentage grades.

### Publication objections still likely

1. Cross-mesh periodic stability is credible at 1.925 GHz, but the finite $3\times3$ receiving region does not transfer calibration reliably across mesh policies.
2. Circular Stokes $S_3$ is substantially weaker than at least one linear coordinate for the finite receiving model; improving the smallest singular value at the *actual* atomic sampling plane is the highest-value next solver campaign.
3. Ideal conductor bridges omit diode ON resistance, OFF capacitance, bias distribution and manufacturing variability. A modest parametric diode loading study would support practical fabrication claims.
4. The new circuit is much more legible and topologically coherent; however, **it is not an HFSS-extracted reduced-order netlist**. Do not cite the circuit as independent validation or assign its R,L,C parameters quantitative accuracy.
5. No fair matched-aperture baseline against a published programmable microwave polarimeter has been simulated. A baseline at the same frequency and receiving plane would make the novelty easier to evaluate.
6. Author affiliations, authorship, funding statements, author biographies, figure permissions where applicable, and the final IEEE-required AI-writing disclosure/citations need human verification before submission.

## Verification actually performed
- Two successive pdfLaTeX builds of the portable IEEE Access source: **passed**.
- No undefined citations or cross-references detected.
- Ordered-bibliography script: **passed**, 37 first-cited entries.
- C033 standalone matrix-check script: **passed**, rank 4, 15 four-state subsets, best mask 03/06/08/13, condition approximately 9.528, physical cone, circular identity and leave-one-out consistency.
- Figure 5(a,b,c) verified on the **compiled** page 8, including every unit-cell trace and the complete circuit.
- This was an editorial and offline mathematical verification pass, **not a new Ansys HFSS solve or fabrication test**.

### Minimum high-impact next steps

A focused finite-panel convergence campaign and a diode-state parasitic sensitivity sweep would improve the *engineering* score much more than another writing pass. For a publication journal, the most useful single new plot would compare the minimum noise-weighted singular value versus geometry/switch setting under consistent finite-aperture, frequency and mesh conditions. This directly tests whether $S_3$ observability survives realistic receiving conditions.