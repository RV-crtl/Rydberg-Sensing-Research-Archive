# 780/480 nm rubidium EIT ladder

**Book:** Rydberg Systems Engineering · **Part:** Atomic receiver · **Status:** original educational text, not new experimental evidence.

## Why this matters in our project

The documented project uses approximately 780 nm probe light to drive Rb-87 5S→5P and approximately 480 nm coupling light to connect 5P to a Rydberg manifold. A specific nℓj transition is not fixed by quoting 480 nm alone: use measured wavelengths, detunings, polarisation selection and ARC-calculated transition access. Co- or counter-propagating beams have distinct two-photon Doppler behaviour. The photocurrent measures transmitted probe intensity, while EIT arises from driven atomic coherence; an RF field couples Rydberg levels and can alter the optical spectral structure.

## Worked problem / research exercise

Draw states |g⟩→|e⟩→|r⟩ and an RF link |r⟩↔|r'⟩. Label probe/coupling/RF Rabi frequencies, detunings and decay channels. Measure RF-off and coupling-off controls under identical detector gain.

## Lab / solver decision checklist

- Record relevant units, basis, frequency, coordinate frame and exact source version.
- Calculate the expected limiting-case behaviour before running expensive software.
- Keep the experimental or solver-native result separate from a numerical illustration.
- Test at least one independent reference, off-state or convergence criterion.

## Questions (attempt before opening the answer)

**Q. If a transmission feature appears even with coupling light blocked, is it evidence of Rydberg EIT?**

<details><summary>Reveal worked answer and explanation</summary>

Not by itself. With coupling blocked, the Rydberg ladder coherence is absent, so investigate probe absorption, optical etalons, electronics and background before attribution.

</details>

**Advanced discussion.** State the approximations used in the section, which observable could falsify the current explanation, and which source data you would need to validate a stronger claim. Compare this against the relevant source below.

## Troubleshooting pitfall

Confusing a laser wavelength readout with detuning; measuring out-of-band photodetector dynamics; omitted RF-off/coupling-off reference.

## Source and extension

../../docs/laboratory/OPTICAL_AND_ATOMIC_RECEIVER.md. [Read the central book reference ledger](../REFERENCES.md). [Return to the syllabus](../README.md).
