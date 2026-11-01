# Doppler averaging, linewidth and coherence

**Part:** Atomic physics · **Type:** educational background, not new experimental data.

## Core explanation

A room-temperature vapour ensemble has a Maxwell–Boltzmann velocity distribution; each class experiences Doppler shifts k·v that differ for 780/480 nm probe and coupling propagation directions. Co/counter-propagation changes the residual two-photon Doppler width. Other linewidth sources include natural decay, power broadening, laser phase noise, collisions, transit time and detector bandwidth. A single broadening slider in a toy graph cannot be represented as a real Rb linewidth measurement.

## Worked learning / laboratory exercise

For illustrative transverse thermal velocity v=200 m/s, compute single-photon shifts ∆f≈v/λ. At λ=780 nm, that is about 256 MHz. The actual projected velocity distribution, orientation and two-photon detuning must be modeled.

## Self-test

**Question:** What experimental evidence distinguishes Doppler broadening from laser-frequency jitter?

<details><summary>Reveal answer and scientific reasoning</summary>

Change beam geometry/temperature while separately measuring laser frequency stability and scan timing, then fit a physically derived model rather than retuning a Lorentzian width.

</details>

## Red flags and diagnosis

Ignoring counter-propagation sign in the two-photon Doppler term.

## Validity and reflection

- Identify each approximation or model limitation before reusing the worked example.
- Identify which physical measurement or native HFSS field could falsify the argument.
- Document units, state basis, time convention, calibration reference, exact code and source versions.
- Check sensitivity to numerical errors and state a quantitative acceptance gate before declaring a result.

## Source

RydIQule documentation: https://rydiqule.readthedocs.io/en/stable/overview.html. [Book references](../REFERENCES.md) · [Syllabus](../README.md).
