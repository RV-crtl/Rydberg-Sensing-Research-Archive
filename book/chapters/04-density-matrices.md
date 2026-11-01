# Mixed states and the Lindblad equation

**Book:** Rydberg Systems Engineering · **Part:** Foundations · **Status:** original educational text, not new experimental evidence.

## Why this matters in our project

A density matrix ρ is Hermitian, positive semidefinite, trace one. A pure state has Tr(ρ²)=1; a mixed state generally has Tr(ρ²)<1. Coherent dynamics obey −i[H,ρ]/ℏ and irreversible processes can be represented by Lindblad jump operators: D[L]ρ=LρL†−½{L†L,ρ}. Doppler, dephasing, spontaneous decay and transit effects require mechanisms and parameter choices. A stationary solution solves Lρ=0 with trace one; a numerically stable solver may eliminate one population variable.

## Worked problem / research exercise

For ρ=diag(0.7,0.3), verify Tr(ρ)=1 and Tr(ρ²)=0.58, showing a mixed state. Add dephasing L=√γφ σz and observe that off-diagonal coherence decays while populations remain unchanged.

## Lab / solver decision checklist

- Record relevant units, basis, frequency, coordinate frame and exact source version.
- Calculate the expected limiting-case behaviour before running expensive software.
- Keep the experimental or solver-native result separate from a numerical illustration.
- Test at least one independent reference, off-state or convergence criterion.

## Questions (attempt before opening the answer)

**Q. Does an optical EIT transmission trace alone uniquely determine every density-matrix element?**

<details><summary>Reveal worked answer and explanation</summary>

No. The observable maps the density matrix to a limited set of optical coherences or intensities; multiple internal states may yield the same trace without additional independent observables.

</details>

**Advanced discussion.** State the approximations used in the section, which observable could falsify the current explanation, and which source data you would need to validate a stronger claim. Compare this against the relevant source below.

## Troubleshooting pitfall

Negative populations from a broken solver; failing trace conservation; calling artificial line broadening measured quantum decoherence.

## Source and extension

RydIQule official documentation https://rydiqule.readthedocs.io/en/stable/overview.html. [Read the central book reference ledger](../REFERENCES.md). [Return to the syllabus](../README.md).
