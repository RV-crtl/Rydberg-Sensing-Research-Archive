# Matrix rank, singular values and reconstruction

**Book:** Rydberg Systems Engineering · **Part:** Polarimetry · **Status:** original educational text, not new experimental evidence.

## Why this matters in our project

For y=AS+η with m≥4 analyzer states, A∈R^(m×4). Rank(A)=4 is necessary for a unique noiseless least-squares four-coordinate solution. The singular values determine numerical stability: κ2(A)=σmax/σmin, but row normalisation changes the condition measure. Weighted inversion is (AᵀWA)⁻¹ AᵀWy when full rank and assumptions hold. A physically valid Stokes estimate additionally obeys S0≥√(S1²+S2²+S3²) and S0≥0. A numerical test with input S and y=AS only validates the algebra, not the HFSS model or atomic receiver.

## Worked problem / research exercise

Take an orthonormal 4×4 A: κ=1. Repeat one row six times instead of adding independent responses: rank can fall below four, and full Stokes becomes unrecoverable. Compare this with the archived six-mask matrix and identify the smallest singular value after specifying row scaling.

## Lab / solver decision checklist

- Record relevant units, basis, frequency, coordinate frame and exact source version.
- Calculate the expected limiting-case behaviour before running expensive software.
- Keep the experimental or solver-native result separate from a numerical illustration.
- Test at least one independent reference, off-state or convergence criterion.

## Questions (attempt before opening the answer)

**Q. Why is 1,231 recovered Poincaré inputs not equivalent to 1,231 independent HFSS solves?**

<details><summary>Reveal worked answer and explanation</summary>

Those inputs can be generated algebraically through the same finite matrix A. They test inversion consistency under that model, not independent electromagnetic field solutions or hardware observations.

</details>

**Advanced discussion.** State the approximations used in the section, which observable could falsify the current explanation, and which source data you would need to validate a stronger claim. Compare this against the relevant source below.

## Troubleshooting pitfall

Inverting singular matrices; reporting κ without scale convention; omitting full 6×4 source and state order.

## Source and extension

../../docs/results/KEY_FINDINGS.md. [Read the central book reference ledger](../REFERENCES.md). [Return to the syllabus](../README.md).
