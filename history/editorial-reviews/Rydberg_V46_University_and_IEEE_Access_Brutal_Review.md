# V46: Critical university and IEEE Access assessment

**Paper:** *Information-Aware Simulation and Verification of a Two-Face Microwave Stokes Analyser*  
**Basis:** compiled V46 PDF, source, supplied final-thesis rubric, published IEEE Access acceptance/reviewer criteria, and archived numerical data.

## University rubric — estimated 85.2/100 (borderline High Distinction)

| Official rubric criterion | Weight | Score / 100 | Contribution |
|---|---:|---:|---:|
| Research into the subject field to define the contribution | 25% | 87 | 21.75 |
| Research into an appropriate methodology | 25% | 87 | 21.75 |
| Engineering the research | 30% | 79 | 23.70 |
| Communicating the research | 20% | 90 | 18.00 |
| **Weighted estimate** | **100%** | | **85.20** |

This is a critical predicted mark, **not** an official result.

### 1. Research / contribution (87/100)
**What earns marks:** a coherent gap (a fixed-axis receiver lacks independent Stokes information), a precise RF measurement-basis solution, a strong existing-method comparison, an exhaustive subset analysis and gain-aware schedule design. The study is not just an isolated S-parameter peak.

**What costs 13 marks:** novelty is still principally a particular combination and optimisation/application of established Stokes/Fisher concepts. No directly matched numerical benchmark against Chen et al.'s programmable polarimeter (same frequency, aperture, readout and metrics) establishes device-level superiority. The related-work synthesis is strong but could be sharper in measurable comparisons.

### 2. Research methodology (87/100)
**What earns marks:** archived 36-geometry screening, explicit interpolation versus independently adapted HFSS gates, complex Jones-to-Stokes formulation, source provenance, clear variance assumptions for dwell-time claims, and separate finite-aperture study.

**What costs 13 marks:** the study has not jointly optimised circular sensitivity and finite local receiving-field convergence at the same frequency as the periodic optimum; the material/switch implementation model remains idealised; unknown measured detector covariances prevent direct hardware uncertainty projections.

### 3. Engineering the research (79/100)
**What earns marks:** actual archived HFSS solutions and 0.551% periodic intermesh agreement at 1.925 GHz, rank-four instrument, geometry search with 175 to 250 MHz sampled interval, verified equation/operator algebra, exhaustive subset information results, finite-array and aperture calculations, and actual original linear-polarisation hardware reference.

**Why this is the limiting category (21 marks deducted):**
- **Finite calibration transfer is not robust:** 95th-percentile discrepancies of 156.8% and 72.2% in opposite mesh-transfer directions at 1.850 GHz. These cannot be treated as accurate reconstruction of an 82-mm finite panel.
- **Circular information remains weak:** at 5 mm, maximum absolute normalised S3 coefficient 0.191 / 0.174 versus ~0.97 in S1; the fourth singular value is small. Weakness persists in the application-relevant finite receiver, even though rank is four.
- **Hardware viability is not equivalent to fabricated performance:** no PIN-diode parasitics/bias network incorporated into the proven Jones matrices; DRC/fabrication and actual switch impedance/speed unverified.
- **Operating-band transfer is only sampled:** 250 MHz is a discovery-grid acceptance span, not certified continuous bandwidth.

These issues are properly labelled and do not invalidate the periodic HFSS contribution; they do constrain claims about a reliable fabricated receiver.

### 4. Communicating the research (90/100)
**What earns marks:** simulation-specific title; accessible opening explanation of the polarimetric problem; explicitly numbered contributions; disciplined separation of measured, simulated and hypothetical uncertainty results; mathematical proof retained outside the main argument; shorter figure captions; simplified Fig. 13; clearer conclusion.

**What costs 10 marks:** some mathematics/appendix passages remain dense, some multi-panel annotation scales are small at print size, and 23 total Access-formatted pages are a substantial reading commitment (though the main narrative is shorter). The class still produces some formatting warnings, albeit without visually apparent missing content in the reviewed pages.

## IEEE Access peer-review readiness — **74/100** (informal editorial score)

This is **not** an official IEEE score or acceptance probability. It estimates the likely reviewer challenge burden against IEEE Access's stated criteria.

| Test | Max | Mark | Editorial issue |
|---|---:|---:|---|
| Originality and distinction from prior work | 20 | 16 | Clear methodological application; comparative superiority not established |
| Technical evidence and numerical validity | 30 | 18 | Good periodic verification, serious finite calibration-transfer mismatch and weak circular channel |
| Methods, replicability and mathematical soundness | 20 | 18 | Strong derivations, archived code/matrices and condition-specific claims |
| Writing, figures and technical accessibility | 20 | 16 | More coherent, but long and occasionally dense; some figure text small |
| Submission and metadata readiness | 10 | 6 | Author declarations/coauthor approval and final IEEE requirements require signoff |
| **Total** | **100** | **74** | **Credible review candidate; targeted scientific revision still advisable** |

### Remaining actions in priority order
1. **Best single scientific upgrade:** run matched-frequency (1.925 GHz), locally converged finite-array HFSS calibrations, and introduce an S3/minimum-singular-value objective; report independent cross-mesh transfer.
2. **Best manufacturing upgrade:** add measured/vendor-documented diode ON/OFF impedances and bias network to the HFSS model, then perform PCB design-rule checking.
3. **Best novelty upgrade:** a matched-frequency, matched-aperture comparison with a comparable reconfigurable RF analyser on the same metrics.
4. **Best communication upgrade:** one last print-scale check of every axis label at 100% view; keep the appendices/supplemental evidence linked from the main methods.
5. **Administrative publication requirement:** verify coauthors, affiliations, disclosures, funding, data and AI-assistance statements before journal submission.

## Changes specifically made in V46
- Removed repeated explanation of the atomic readout/electromagnetic transfer boundary.
- Reduced five short introductory/theory subdivisions into fewer meaningful sections.
- Removed duplicate methods narrative while preserving solver provenance.
- Rewrote the discussion and conclusion for assessor comprehension.
- Removed Figure 13(c) without concealing any calibration results (numbers remain in text).
- Redesigned Figure 14(b) without an unnecessary bar chart.
- Moved nomenclature out of the opening narrative.
- Left numerical HFSS claims unchanged, because no new solver output was produced in this revision.

## Reviewer bottom line
This is a defensible simulation-led electromagnetics manuscript with a real, reproducible numerical contribution. It should not claim experimentally verified full-Stokes reception or guaranteed fabricated performance. The periodic instrument has stronger evidence than the finite device; that must remain the limiting interpretation even when the narrative foregrounds the positive design results.