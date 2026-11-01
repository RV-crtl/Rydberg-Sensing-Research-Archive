# HFSS modelling from a unit cell to a finite sensor

**Part:** Electromagnetics · **Type:** educational background, not new experimental data.

## Core explanation

In full-wave HFSS, substrate properties, copper boundaries, surface currents, switches, illumination and near-field observation geometry determine the local complex field. A periodic Floquet cell is a different boundary-value problem from a 3×3 finite panel. For the atomic receiver, the relevant observable may be the local E field at the vapour-cell sensing volume, not S21 at a far-field port. Mesh convergence must be checked on the derived Stokes matrix, including phase and S3, not only energy or S11.

## Worked learning / laboratory exercise

Starting from the archived V44 geometry, document true copper state and mesh profile for two independent incident Jones bases. Export complex Ex/Ey (and Ez when atomic coupling requires it) on the same x,y,z coordinates; assemble A only after normalising the observation model and recording phase reference.

## Self-test

**Question:** Why did some historical finite 3×3 results fail although the periodic reference had a small reported mesh mismatch?

<details><summary>Reveal answer and scientific reasoning</summary>

The finite-panel field sampling, edge effects and independent mesh adaptation changed the actual complex response. The project recorded large cross-calibration errors, so periodic success did not prove finite-panel transfer.

</details>

## Red flags and diagnosis

Calling an ideal short a real PIN diode, or judging a full-Stokes device from |S21| only.

## Validity and reflection

- Identify each approximation or model limitation before reusing the worked example.
- Identify which physical measurement or native HFSS field could falsify the argument.
- Document units, state basis, time convention, calibration reference, exact code and source versions.
- Check sensitivity to numerical errors and state a quantitative acceptance gate before declaring a result.

## Source

Project HFSS findings: ../../docs/results/KEY_FINDINGS.md. [Book references](../REFERENCES.md) · [Syllabus](../README.md).
