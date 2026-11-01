# Scientific code, environments and reproducibility

**Part:** Scientific software · **Type:** educational background, not new experimental data.

## Core explanation

Record exact Python/toolbox/AEDT versions, solver executables, source hashes and input datasets. Separate generated figures from raw data. Use unit tests for the 2π convention, Jones/Stokes signs, matrix order and numerical physicality. Never use a random synthetic dataset and label it optical data. Archive return packages need full failure logs as well as successful plots, including interrupted HFSS attempts.

## Worked learning / laboratory exercise

Run `python -m unittest discover -s tests -v` on the repository and inspect the original HFSS manifest for every figure. Attempt a deliberate column-order swap in a *copy* of a test matrix and verify that the test detects it.

## Self-test

**Question:** What makes a source archive scientifically reusable beyond merely containing a ZIP?

<details><summary>Reveal answer and scientific reasoning</summary>

A clear manifest, source origin, exact scripts/versions, units, computational assumptions, reproducible run commands, integrity hashes and clear distinctions between raw/derived outputs.

</details>

## Red flags and diagnosis

Renaming an archive FINAL without inspecting solver results or its parent dependencies.

## Validity and reflection

- Identify each approximation or model limitation before reusing the worked example.
- Identify which physical measurement or native HFSS field could falsify the argument.
- Document units, state basis, time convention, calibration reference, exact code and source versions.
- Check sensitivity to numerical errors and state a quantitative acceptance gate before declaring a result.

## Source

Project HFSS findings: ../../docs/results/KEY_FINDINGS.md. [Book references](../REFERENCES.md) · [Syllabus](../README.md).
