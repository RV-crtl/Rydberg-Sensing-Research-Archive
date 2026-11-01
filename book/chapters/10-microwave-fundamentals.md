# Microwave fields, antennas and reference planes

**Book:** Rydberg Systems Engineering · **Part:** RF engineering · **Status:** original educational text, not new experimental evidence.

## Why this matters in our project

In free space λ0=c/f and k=2π/λ0. At 1.925 GHz, λ0≈155.7 mm, comparable to many of the project's finite-board features. Poynting flux S=Re(E×H*)/2 for peak phasors; RMS and peak amplitude conventions differ by √2. Use calibrated dBm, cable losses and VNA reference planes; near-field coupling may not obey ideal far-field plane-wave assumptions. An antenna orientation sweep does not by itself establish a local E-field at the rubidium atoms.

## Worked problem / research exercise

At f=1.925 GHz, calculate λ0≈0.1557 m. A 70×50 mm receiving aperture spans about 0.45λ0×0.32λ0, which helps explain why a large periodic infinite-surface approximation can differ from a compact finite device.

## Lab / solver decision checklist

- Record relevant units, basis, frequency, coordinate frame and exact source version.
- Calculate the expected limiting-case behaviour before running expensive software.
- Keep the experimental or solver-native result separate from a numerical illustration.
- Test at least one independent reference, off-state or convergence criterion.

## Questions (attempt before opening the answer)

**Q. Why must a finite 3×3 HFSS model not simply inherit a periodic unit cell's S3 sensitivity?**

<details><summary>Reveal worked answer and explanation</summary>

Finite edges, illumination, spatial sampling and complex-field phase change the local response; it requires its own model and calibration.

</details>

**Advanced discussion.** State the approximations used in the section, which observable could falsify the current explanation, and which source data you would need to validate a stronger claim. Compare this against the relevant source below.

## Troubleshooting pitfall

Mistaking dB voltage ratios for power ratios; unspecified phase reference; applying far-field formula in the reactive zone.

## Source and extension

../../docs/results/KEY_FINDINGS.md. [Read the central book reference ledger](../REFERENCES.md). [Return to the syllabus](../README.md).
