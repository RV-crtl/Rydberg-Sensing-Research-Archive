# Reconstruction regularisation and error bars

**Part:** Metrology · **Type:** educational background, not new experimental data.

## Core explanation

A noisy Stokes inversion should use a declared calibration model and measurement covariance. The Moore–Penrose pseudoinverse returns one least-squares solution but may amplify small singular modes. Weighted least squares, Tikhonov regularisation and physical Stokes-cone projection change bias/variance. The choice must be evaluated on held-out physical/simulation data, not chosen by minimising training reconstruction error alone.

## Worked learning / laboratory exercise

Let A have singular values 1,0.3,0.08,0.01. White-noise variance in the final singular mode amplifies by 10,000 relative to one with σ=1. Compare raw pseudoinverse and ridge inverse with λ>0 and report residual and bias.

## Self-test

**Question:** Why must a negative reconstructed S0 be treated as a diagnosis rather than quietly clipped?

<details><summary>Reveal answer and scientific reasoning</summary>

Physical S0 is nonnegative. A negative estimate reveals calibration, normalisation or noise/model mismatch; clipping can conceal the cause.

</details>

## Red flags and diagnosis

Reporting a visually pretty Poincaré sphere with no holdout or physicality residual.

## Validity and reflection

- Identify each approximation or model limitation before reusing the worked example.
- Identify which physical measurement or native HFSS field could falsify the argument.
- Document units, state basis, time convention, calibration reference, exact code and source versions.
- Check sensitivity to numerical errors and state a quantitative acceptance gate before declaring a result.

## Source

Project HFSS findings: ../../docs/results/KEY_FINDINGS.md. [Book references](../REFERENCES.md) · [Syllabus](../README.md).
