# Operators, eigenstates and uncertainty

**Book:** Rydberg Systems Engineering · **Part:** Foundations · **Status:** original educational text, not new experimental evidence.

## Why this matters in our project

A Hermitian observable A has real eigenvalues and expectation ⟨A⟩=⟨ψ|A|ψ⟩. The variance is ⟨A²⟩−⟨A⟩². If A and B do not commute, ΔAΔB≥|⟨[A,B]⟩|/2. Spectral optical detection reads a response of an ensemble, not a direct projective measurement of a single Rydberg state. Measurement bandwidth and integration affect uncertainty but are distinct from a quantum uncertainty bound.

## Worked problem / research exercise

Represent σ_z as diag(1,−1). For |+x⟩=(|g⟩+|e⟩)/√2, predict 50:50 outcomes for σ_z, ⟨σ_z⟩=0 and variance 1.

## Lab / solver decision checklist

- Record relevant units, basis, frequency, coordinate frame and exact source version.
- Calculate the expected limiting-case behaviour before running expensive software.
- Keep the experimental or solver-native result separate from a numerical illustration.
- Test at least one independent reference, off-state or convergence criterion.

## Questions (attempt before opening the answer)

**Q. What is the distinction between a photodetector's electronic noise and intrinsic quantum state uncertainty?**

<details><summary>Reveal worked answer and explanation</summary>

Electronic noise is a property of a physical readout chain; quantum uncertainty describes incompatible observable statistics for a specified state. They need separate models and calibrations.

</details>

**Advanced discussion.** State the approximations used in the section, which observable could falsify the current explanation, and which source data you would need to validate a stronger claim. Compare this against the relevant source below.

## Troubleshooting pitfall

Reporting an rms error in volts as an atomic density-matrix uncertainty; assuming quantum projection noise dominates without an experiment.

## Source and extension

Gallagher, Rydberg Atoms (Cambridge University Press, DOI 10.1017/CBO9780511524530). [Read the central book reference ledger](../REFERENCES.md). [Return to the syllabus](../README.md).
