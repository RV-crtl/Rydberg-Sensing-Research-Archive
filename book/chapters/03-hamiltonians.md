# Hamiltonians and rotating frames

**Book:** Rydberg Systems Engineering · **Part:** Foundations · **Status:** original educational text, not new experimental evidence.

## Why this matters in our project

The Schrödinger equation iℏ ∂t|ψ⟩=H|ψ⟩ maps energy to dynamics. For a two-level system under a coherent drive and rotating-wave approximation, H/ℏ=[[-Δ/2,Ω/2],[Ω*/2,Δ/2]] in a declared basis. Here Δ and Ω are angular frequencies (rad/s). If a library requests MHz instead, first check whether it means cycles/s or angular-frequency units. A frame transformation changes the representation, not the underlying experiment.

## Worked problem / research exercise

For a resonant drive Ω=2π×1 MHz, the ideal population Rabi cycle has period 2π/Ω=1 μs. Off resonance, Ωeff=√(Ω²+Δ²). Compare the slow drive, finite detuning and transit-broadening timescales.

## Lab / solver decision checklist

- Record relevant units, basis, frequency, coordinate frame and exact source version.
- Calculate the expected limiting-case behaviour before running expensive software.
- Keep the experimental or solver-native result separate from a numerical illustration.
- Test at least one independent reference, off-state or convergence criterion.

## Questions (attempt before opening the answer)

**Q. Why can replacing 2π×10 MHz with 10 MHz in a Hamiltonian lead to incorrect dynamics?**

<details><summary>Reveal worked answer and explanation</summary>

Because Ω is often angular frequency; 10 MHz in cycles/s corresponds to 2π×10 million rad/s. Verify the interface convention, rather than assuming.

</details>

**Advanced discussion.** State the approximations used in the section, which observable could falsify the current explanation, and which source data you would need to validate a stronger claim. Compare this against the relevant source below.

## Troubleshooting pitfall

An unexplained factor of 2π; inconsistent sign for detuning; rotating-wave approximation outside its validity range.

## Source and extension

RydIQule official documentation https://rydiqule.readthedocs.io/en/stable/overview.html. [Read the central book reference ledger](../REFERENCES.md). [Return to the syllabus](../README.md).
