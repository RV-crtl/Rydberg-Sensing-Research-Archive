# Optical alignment, power and detection

**Book:** Rydberg Systems Engineering · **Part:** Laboratory · **Status:** original educational text, not new experimental evidence.

## Why this matters in our project

Laser alignment should begin with documented interlocks, beam paths, eyewear requirements and instrument reference settings. A photodetector's voltage is related to optical power via responsivity R(λ) and transimpedance gain; electronic bandwidth, saturation and offset must be checked. Optical density OD=−log10(T) and Beer–Lambert intensity T≈exp(−αL) are different expressions of the same attenuation when the assumptions hold. For an Rb vapour-cell EIT system, document laser locks, power drift, polarisation, temperature and probe coupling before changing RF geometry. Never infer line strength from a plot with uncalibrated vertical scaling.

## Worked problem / research exercise

For an illustrative diode with R=0.55 A/W and 10 µW detected, calculate 5.5 µA photocurrent. At 100 kΩ ideal transimpedance, the signal magnitude is 0.55 V before bandwidth, feedback stability and offset constraints.

## Lab / solver decision checklist

- Record relevant units, basis, frequency, coordinate frame and exact source version.
- Calculate the expected limiting-case behaviour before running expensive software.
- Keep the experimental or solver-native result separate from a numerical illustration.
- Test at least one independent reference, off-state or convergence criterion.

## Questions (attempt before opening the answer)

**Q. Why should detector bandwidth be recorded for Rydberg optical spectra?**

<details><summary>Reveal worked answer and explanation</summary>

A bandwidth limit filters transmitted intensity variations and may alter observed modulation/spectral scan dynamics; it is not interchangeable with RF carrier reception bandwidth.

</details>

**Advanced discussion.** State the approximations used in the section, which observable could falsify the current explanation, and which source data you would need to validate a stronger claim. Compare this against the relevant source below.

## Troubleshooting pitfall

Detector saturation, ADC clipping, false laser lock, wavelength mismatch or a changed neutral-density filter.

## Source and extension

../../docs/laboratory/OPTICAL_AND_ATOMIC_RECEIVER.md. [Read the central book reference ledger](../REFERENCES.md). [Return to the syllabus](../README.md).
