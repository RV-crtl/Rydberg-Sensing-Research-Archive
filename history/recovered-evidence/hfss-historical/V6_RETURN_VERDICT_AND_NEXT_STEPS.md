# Independent V6 return audit — 19 October 2026

**Source archive:** `RETURN_TO_CHATGPT_APL_V6_20261019_014402.zip` (actual HFSS output, not a simulated success flag). **This is a screen, not a finished polarimeter.**

## Current evidence

The V6 controller finished normally and selected V5103, a local modification of V5015. At 1.670, 1.675 and 1.680 GHz, the V5103 gain-normalized, field-derived four-state condition numbers were **14.8128, 14.9668, 15.1658**, respectively. The worst-frequency maximum-state normalized circular contrast was **0.17129**; the adopted exploratory criteria were κ ≤ 12 and η3 ≥ 0.20. V5104 reached η3 ≥ 0.20 but had a condition number ≈ 19.89. Neither meets both gates.

The intended electromagnetic model uses a fixed X-sensitive atomic projection, a uniform 125-point RF interrogation region, a 1.67–1.68 GHz frequency screen and ideal-conductor switching. These assumptions are not a full magnetic-sublevel atomic response or a real PIN diode.

## Numerical fidelity

- **Success:** HFSS completed the independent X/Y and nonbasis cases, and source-linked field files were exported. The latest controller status was `FINISHED`, not a Python failure.
- **P35A versus P35C first-state mesh pilot, 1.675 GHz:** X excitation **7.1046%** raw complex-vector disagreement, Y excitation **4.2971%**. The X test fails the preregistered 5% diagnostic screen, so the eight-state fine-mesh validation was not completed.
- **P35A versus P45A exterior domain, 1.675 GHz:** full instrument-operator disagreement **11.3225%**, also above 5%. The weak X-component from Y incident waves is particularly sensitive; at T3/Y it differs by **38.20%**.
- **Direct independent incident polarisations:** 45-degree, opposite circular-phase and elliptical excitation comparisons to the corresponding X/Y superpositions failed the 5% raw-vector screen. At T1, 1.675 GHz, 45-degree error **5.0664%**, +90 degree **5.6173%**, −90 degree **6.7454%**. Other states reach much larger errors. These discrepancies indicate insufficient numerical/source-normalization closure, not a violation of linear Maxwell superposition.

A 5% engineering screen is not an absolute error bar or a proof of mesh convergence. Two consistent refined solutions do not by themselves prove the continuous Maxwell solution either; source, boundary, finite element and atomic-operator assumptions still matter.

## V6.1 decision and rationale

The most cost-efficient final attempt is **scientific numerical closure of V5103 alone**:

1. Pilot **P35B ↔ P35C** at the most informative T1/X and T1/Y state. If raw complex vector and weak projected-channel differences pass ≤5% at all three frequencies, complete both four-state sets and compare matrices and circular contrast.
2. If the first pilot fails, try the more stringent **P35C ↔ P35D** pilot. On another failure or student-edition mesh limit, STOP: the original geometry is not independently mesh-validated in the available computing regime.
3. Once a full mesh pair passes, compare **matched** 35/45 mm exterior-domain pairs with the same adaptive profile (P35B/P45B or P35C/P45C). Stop if weak fields or operator differ by >5%.
4. Only if these Maxwell gates pass, directly solve 45-degree, both quadrature-handedness and elliptical incident fields at the refined mesh, beginning with problematic T3. Compare **raw** complex-field superposition with the HFSS sources. Record best-fit global gain/phase only to diagnose source normalization; never use it to conceal a raw failure.
5. Finally recompute four-state κ and η3 on the accepted fine mesh. **Neither numerical convergence nor an acceptable Stokes matrix validates a real PIN diode, Rb transition calibration or an optical polarimeter.**

If V6.1 fails at any numerical gate, **stop HFSS within the 48-hour deadline and finalize a theory + independently supported negative/optimization result**, without inventing an experimentally demonstrated full-Stokes device. Full claims require a separate, longer campaign with calibrated Rb spectroscopy, optical weighting, noise and realistic diode switching.

### Critical note about “absolute best”

These are time- and topology-constrained optimizers. The existing V5/V6 results do not prove global optimality or broad-band RF performance. The 1.670–1.680 GHz design screen is narrowband, and the selected atomic transition remains unverified.