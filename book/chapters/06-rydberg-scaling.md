# Rydberg quantum defects and scaling laws

**Book:** Rydberg Systems Engineering · **Part:** Atomic physics · **Status:** original educational text, not new experimental evidence.

## Why this matters in our project

For high-n alkali Rydberg levels, the energy relative to ionisation can be approximated E≈−hcR*/(n−δℓj)², where the quantum defect depends on angular state. Classical estimates give radius ∼(n*)²a0, adjacent transition energy ∼(n*)⁻³, polarizability often growing roughly ∼(n*)⁷ in suitable regimes, and radiative lifetime roughly ∼(n*)³ before blackbody/environment effects. These are scaling guides, not calibrated Rb-87 data. Use ARC's published level and lifetime APIs for numerical design.

## Worked problem / research exercise

At n*=70 and 90, the approximate adjacent spacing ratio ΔE90/ΔE70≈(70/90)³≈0.4705. Larger n yields smaller characteristic RF spacings. Check the actual chosen nℓj manifold with ARC before committing a laser wavelength.

## Lab / solver decision checklist

- Record relevant units, basis, frequency, coordinate frame and exact source version.
- Calculate the expected limiting-case behaviour before running expensive software.
- Keep the experimental or solver-native result separate from a numerical illustration.
- Test at least one independent reference, off-state or convergence criterion.

## Questions (attempt before opening the answer)

**Q. Why is hydrogenic energy E∝−1/n² insufficient for a high-accuracy rubidium transition search?**

<details><summary>Reveal worked answer and explanation</summary>

Alkali core penetration creates ℓ,j-dependent quantum defects, and fine/hyperfine interactions plus external fields affect precision. Use state-specific data.

</details>

**Advanced discussion.** State the approximations used in the section, which observable could falsify the current explanation, and which source data you would need to validate a stronger claim. Compare this against the relevant source below.

## Troubleshooting pitfall

Treating scaling laws as an HFSS result; assuming all ℓ states have identical quantum defects; ignoring blackbody lifetimes.

## Source and extension

Gallagher, Rydberg Atoms (Cambridge University Press, DOI 10.1017/CBO9780511524530). [Read the central book reference ledger](../REFERENCES.md). [Return to the syllabus](../README.md).
