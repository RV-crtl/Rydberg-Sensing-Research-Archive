# Finite-aperture transfer and verification gates

**Part:** Metrology · **Type:** educational background, not new experimental data.

## Core explanation

A periodic source matrix and finite aperture matrix may both have rank four but differ enough that inversion calibrated on one fails on the other. Cross-mesh reconstruction error is a stronger calibration-transfer test than solver's own energy convergence alone. The historical V4.21 records contained large finite-state transfer discrepancies; the V4.22 configuration was a correction plan, not automatic evidence that the corrected solves completed. V44's accepted sampled span is not continuous wideband validation.

## Worked learning / laboratory exercise

Compare A_ref and A_mesh at the same incidence, frequency, volume, state truth table and phase reference. Compute ‖A_ref−A_mesh‖_F/‖A_ref‖_F and holdout Stokes transfer errors in both directions. Record all samples and failures, not only best frequencies.

## Self-test

**Question:** What evidence would permit a robust finite receiver claim?

<details><summary>Reveal answer and scientific reasoning</summary>

Independently converged finite fields at the actual atom sensing volume; measured or physically calibrated response with stable condition and acceptable holdout reconstruction; relevant switch and bias models.

</details>

## Red flags and diagnosis

Treating accepted discrete-frequency samples as a measured continuous band.

## Validity and reflection

- Identify each approximation or model limitation before reusing the worked example.
- Identify which physical measurement or native HFSS field could falsify the argument.
- Document units, state basis, time convention, calibration reference, exact code and source versions.
- Check sensitivity to numerical errors and state a quantitative acceptance gate before declaring a result.

## Source

Project HFSS findings: ../../docs/results/KEY_FINDINGS.md. [Book references](../REFERENCES.md) · [Syllabus](../README.md).
