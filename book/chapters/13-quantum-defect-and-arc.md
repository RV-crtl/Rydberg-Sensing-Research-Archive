# ARC: an auditable transition atlas

**Part:** Atomic software · **Type:** educational background, not new experimental data.

## Core explanation

ARC is a numerical library for alkali Rydberg energies, dipoles, Stark maps and lifetimes. Use the Rubidium87 class, not generic hydrogen, when screening a proposed laser/RF ladder. Constrain optical access to measured 480-nm settings, the RF frequency to available sources and antennas, and the detector's optical modulation capability. Query levels and the difference of energies with `getTransitionFrequency`; query strength through state-specific dipole matrix elements, selection rules and lifetimes. Store code, environment version, quantum numbers and method calls, not just a screenshot of a transition table.

## Worked learning / laboratory exercise

Install `python -m pip install ARC-Alkali-Rydberg-Calculator`. In Python: `from arc import Rubidium87; a=Rubidium87(); print(a.getTransitionFrequency(86,1,1.5,87,0,0.5))`. This is an *illustrative* pair, not automatically the project-approved RF transition. Compare to ARC's documented quantum numbers and frequency sign convention before ranking.

## Self-test

**Question:** Why are a high dipole moment and correct RF frequency not sufficient to choose the receiver transition?

<details><summary>Reveal answer and scientific reasoning</summary>

The same state pair also needs a physically accessible optical ladder, available power and bandwidth, compatible selection rules, useful coherence lifetime and an experimentally resolvable optical observable.

</details>

## Red flags and diagnosis

A screenshot of an ARC Stark map cannot substitute for source code and inputs.

## Validity and reflection

- Identify each approximation or model limitation before reusing the worked example.
- Identify which physical measurement or native HFSS field could falsify the argument.
- Document units, state basis, time convention, calibration reference, exact code and source versions.
- Check sensitivity to numerical errors and state a quantitative acceptance gate before declaring a result.

## Source

ARC official documentation: https://arc-alkali-rydberg-calculator.readthedocs.io/en/latest/alkali_atom_functions.html. [Book references](../REFERENCES.md) · [Syllabus](../README.md).
