# Spectral diagnosis: false peaks and controls

**Part:** Laboratory · **Type:** educational background, not new experimental data.

## Core explanation

A clean Rydberg RF spectrum needs a reference chain: calibrated laser frequency, optical baseline with the coupling off, dark detector offset, RF generator reference, antenna/cable calibration and repeat scans. A peak that appears at a different RF frequency than the synthesiser may reflect spurs, nonlinear mixing, mains pickup, optical etalons or measurement aliasing. Distinguish amplitude in dBm from electric-field amplitude at the atoms. When coherence disappears, investigate optical overlap, coupling detuning, vapour temperature and power before blaming the metasurface.

## Worked learning / laboratory exercise

Make a four-state experiment table: RF off/on crossed with coupling off/on, while preserving raw traces and identical gain. Compare true RF-sensitive optical features with artefacts common to coupling-off spectra.

## Self-test

**Question:** Why can't a spectrum analyser measurement of the antenna port alone validate a Rydberg EIT RF response?

<details><summary>Reveal answer and scientific reasoning</summary>

The analyser measures an electrical RF observable. A Rydberg response must be demonstrated in optical probe transmission with the atomic ladder active and suitable controls.

</details>

## Red flags and diagnosis

Overinterpreting a peak with no source-off reference; comparing non-identical trace processing.

## Validity and reflection

- Identify each approximation or model limitation before reusing the worked example.
- Identify which physical measurement or native HFSS field could falsify the argument.
- Document units, state basis, time convention, calibration reference, exact code and source versions.
- Check sensitivity to numerical errors and state a quantitative acceptance gate before declaring a result.

## Source

Project apparatus source: ../../docs/laboratory/OPTICAL_AND_ATOMIC_RECEIVER.md. [Book references](../REFERENCES.md) · [Syllabus](../README.md).
