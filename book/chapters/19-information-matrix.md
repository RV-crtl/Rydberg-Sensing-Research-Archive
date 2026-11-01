# Fisher information, time budgets and conditioning

**Part:** Metrology · **Type:** educational background, not new experimental data.

## Core explanation

With independent Gaussian measurements y_i=a_i·S+η_i of known variance σ_i²/t_i, the Fisher information for S is F=Aᵀ diag(t_i/σ_i²) A. The inverse diagonal traces can express a weighted estimation criterion when F is nonsingular. Optimising t_i for fixed total time may reduce a modelled uncertainty criterion; it does not report experimental SNR gain. If noise is correlated or signal dependent, the weights and objective must be re-derived.

## Worked learning / laboratory exercise

Reproduce the archived V44 six-mask equal-allocation and optimised-allocation results, noting the reported ~40.8% inverse-trace criterion reduction. Hold the same matrix, normalisation and total acquisition time. Repeat with doubled σ for one channel and observe how the optimum changes.

## Self-test

**Question:** Why can a device with lower κ still produce worse estimation than another?

<details><summary>Reveal answer and scientific reasoning</summary>

Normalising each row may hide absolute gain. A less conditioned but higher-signal array may carry more information under a specific noise model; inspect F with physical noise units.

</details>

## Red flags and diagnosis

Comparing two values of κ computed under different row scaling.

## Validity and reflection

- Identify each approximation or model limitation before reusing the worked example.
- Identify which physical measurement or native HFSS field could falsify the argument.
- Document units, state basis, time convention, calibration reference, exact code and source versions.
- Check sensitivity to numerical errors and state a quantitative acceptance gate before declaring a result.

## Source

Project HFSS findings: ../../docs/results/KEY_FINDINGS.md. [Book references](../REFERENCES.md) · [Syllabus](../README.md).
