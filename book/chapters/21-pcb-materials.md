# Fabrication: Rogers, copper, spacing and switches

**Part:** Hardware · **Type:** educational background, not new experimental data.

## Core explanation

A manufacturable metasurface requires a stackup chosen for its dielectric properties and available process, copper thickness, minimum feature and hole/solder rules. The project explored RO4350B and RO4003C in different design families; they are not interchangeable material identifiers. Board-size limit near 200×200 mm and a 70×50 mm cell aperture refer to different constraints. PIN diode OFF is a frequency-dependent RLC and bias-network state, not the same thing as simply deleting a copper bridge.

## Worked learning / laboratory exercise

For a transmission resonator with effective L,C, f0≈1/(2π√LC). A 5% rise in C lowers resonance by ≈2.4% for small perturbations. Use that *sensitivity* to pick a sweep but validate with the actual HFSS geometry.

## Self-test

**Question:** Why can a perfect-conductor switched bridge overestimate physical polarisation isolation?

<details><summary>Reveal answer and scientific reasoning</summary>

It omits forward on-state resistance/inductance, reverse-state capacitance, bias-line parasitics, substrate/solder losses and physical packaging.

</details>

## Red flags and diagnosis

Mistaking a drawing for a manufactured board; changing dielectric without rerunning fields.

## Validity and reflection

- Identify each approximation or model limitation before reusing the worked example.
- Identify which physical measurement or native HFSS field could falsify the argument.
- Document units, state basis, time convention, calibration reference, exact code and source versions.
- Check sensitivity to numerical errors and state a quantitative acceptance gate before declaring a result.

## Source

Project HFSS findings: ../../docs/results/KEY_FINDINGS.md. [Book references](../REFERENCES.md) · [Syllabus](../README.md).
