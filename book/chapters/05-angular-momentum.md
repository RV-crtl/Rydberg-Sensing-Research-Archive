# Angular momentum, fine structure and selection rules

**Book:** Rydberg Systems Engineering · **Part:** Atomic physics · **Status:** original educational text, not new experimental evidence.

## Why this matters in our project

Orbit ℓ, electron spin s and j=ℓ+s label alkali states; F=j+I adds nuclear spin and mF/mj labels projection. Electric-dipole selection typically requires parity change, Δℓ=±1 and Δm=q∈{−1,0,+1} relative to the chosen quantisation axis. q=0 is π and q=±1 are σ± spherical field components. The sign of a circularly polarised drive depends on the RF propagation and basis convention. A real EIT experiment may involve several coupled magnetic sublevels; one toy three-level ladder is not a full prediction of a Zeeman-sensitive spectrum.

## Worked problem / research exercise

Write a transition table for an illustrative j=1/2→j=3/2 pair at each allowed mj. Enumerate q values and reject endpoints that fall outside |mj|≤j. Recompute after rotating the quantisation axis.

## Lab / solver decision checklist

- Record relevant units, basis, frequency, coordinate frame and exact source version.
- Calculate the expected limiting-case behaviour before running expensive software.
- Keep the experimental or solver-native result separate from a numerical illustration.
- Test at least one independent reference, off-state or convergence criterion.

## Questions (attempt before opening the answer)

**Q. Why does changing the bias-field direction affect which RF polarisation component an atom sees?**

<details><summary>Reveal worked answer and explanation</summary>

The spherical basis is defined about the quantisation axis. Rotating that axis changes how a fixed laboratory RF vector decomposes into π, σ+ and σ− components.

</details>

**Advanced discussion.** State the approximations used in the section, which observable could falsify the current explanation, and which source data you would need to validate a stronger claim. Compare this against the relevant source below.

## Troubleshooting pitfall

Using arbitrary q to force a transition; treating π/σ as Cartesian x/y/z; assuming a field-alignment result without calibration.

## Source and extension

Gallagher, Rydberg Atoms (Cambridge University Press, DOI 10.1017/CBO9780511524530). [Read the central book reference ledger](../REFERENCES.md). [Return to the syllabus](../README.md).
