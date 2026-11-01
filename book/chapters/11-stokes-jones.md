# Jones vectors, Stokes coordinates and conventions

**Book:** Rydberg Systems Engineering · **Part:** Polarimetry · **Status:** original educational text, not new experimental evidence.

## Why this matters in our project

For a fully coherent transverse electric Jones vector E=[Ex,Ey]^T, define S0=|Ex|²+|Ey|², S1=|Ex|²−|Ey|², S2=2Re(Ex Ey*), S3=2Im(Ex Ey*) under one explicit time/handedness convention. This S3 sign is not universally shared; preserve the optical/radio convention along with the propagation direction. For an ideal pure input, S1²+S2²+S3²=S0²; partially polarised states lie inside the sphere. Linear analyser rotations alone sample S1,S2 but are insensitive to handedness S3.

## Worked problem / research exercise

Calculate Stokes for Ex=1/√2, Ey=i/√2. With the formula above, ExEy*=−i/2, so S3=−1. Reverse the relative phase and S3 flips. Verify that the project model uses its own stated convention when comparing handedness labels.

## Lab / solver decision checklist

- Record relevant units, basis, frequency, coordinate frame and exact source version.
- Calculate the expected limiting-case behaviour before running expensive software.
- Keep the experimental or solver-native result separate from a numerical illustration.
- Test at least one independent reference, off-state or convergence criterion.

## Questions (attempt before opening the answer)

**Q. Can five repeated linear-angle sweeps prove full-Stokes Rydberg RF sensing?**

<details><summary>Reveal worked answer and explanation</summary>

No. They can improve precision for a linear basis and equatorial projections but cannot independently determine S3 without a circular-sensitive reference or state.

</details>

**Advanced discussion.** State the approximations used in the section, which observable could falsify the current explanation, and which source data you would need to validate a stronger claim. Compare this against the relevant source below.

## Troubleshooting pitfall

Switching S3 sign mid-analysis; declaring a negative power from a model artefact; mixing Jones amplitude normalisations.

## Source and extension

Elgee et al., Physical Review Applied 22, 064012 (2024), DOI 10.1103/PhysRevApplied.22.064012. [Read the central book reference ledger](../REFERENCES.md). [Return to the syllabus](../README.md).
