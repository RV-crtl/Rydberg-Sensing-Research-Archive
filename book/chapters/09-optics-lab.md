# Optical engineering, detection and alignment

**General Rydberg and optical physics chapter.** Species and apparatus choices are examples, not a report of one project.

## Competencies

Derive the optical and atomic response, identify the real observable, use state-specific data, design controls, and discriminate physical behaviour from technical artefacts.

## 1. Optical power and field amplitude

A Gaussian TEM00 beam with optical power P and waist w0 has peak intensity I0=2P/(πw0²) under the standard 1/e² intensity radius definition. In free space the root-mean-square electric field relates to intensity through I=cε0 E_rms². A Rabi rate follows the transition dipole projection times field amplitude divided by ℏ. If the quoted power is measured before an acousto-optic modulator, cell window or fibre, include losses before predicting on-atom coupling.

## 2. Beam propagation and overlap

Gaussian beam radius evolves as w(z)=w0√(1+(z/zR)²), where zR=πw0²/λ. Lens aberration, astigmatism and clipping can invalidate an ideal paraxial model. In a vapour cell, optical probe and coupling overlap must be maintained over an adequate interaction length; crossing angle affects both volume and Doppler geometry. In a tweezer experiment, high numerical aperture and accurate intensity distribution define trap confinement and addressing fidelity.

## 3. Polarisation preparation

Waveplates produce phase delays between orthogonal optical axes, while polarising beam splitters and analysers distinguish projections. A quarter-wave plate generates ideal circular light only for the correct incident linear state, axis setting and wavelength. Birefringent windows, stress and magnetic-field orientation can change the actual polarisation at the atoms. For magnetic sublevel selection, polarisation must be defined relative to the quantisation axis, not just the appearance of a laboratory arrow.

## 4. Photodetection and electronics

A photodiode current is I_pd=R(λ)P_opt in its linear regime. Transimpedance gain converts current to voltage, while amplifier bandwidth and noise contribute to the measured time series. Overload, feedback instability or a dark offset may distort spectroscopy. Determine whether the oscilloscope is sampling slowly varying optical scan intensity, RF-beat modulation or the raw optical carrier; ordinary photodiodes do not time-resolve hundreds of terahertz optical oscillations.

## 5. Laser frequency stability and diagnostics

Separate fast and slow frequency noise, free-running linewidth, long-term lock drift and absolute reference uncertainty. Saturation absorption, etalon, beat note and wavemeter measurements probe different properties; an in-loop error signal does not independently establish an out-of-loop optical linewidth. Document frequency calibration, scan direction, dwell time, servo state, optical powers and reference frequency for every scientific trace.

## 6. A practical alignment validation sequence

With institutional laser safety controls, identify probe and coupling beam paths separately; verify power, mode quality and detector gain. Establish baseline absorption with probe only, then add coupling at a known resonance and adjust overlap while retaining raw references. Repeat at lower power to test saturation and broadenings. For an RF-controlled experiment, introduce RF only after stable EIT is confirmed, so optical and RF faults do not become entangled in diagnosis.

## End-of-chapter questions with answers

### Question 1. How does peak Gaussian intensity change when w0 halves?

<details><summary>Reveal the worked answer</summary>

It increases fourfold at constant power under an ideal TEM00 model.

</details>

### Question 2. Why is a detector output not an optical carrier waveform?

<details><summary>Reveal the worked answer</summary>

Photodiode bandwidth generally follows envelope/modulation, not the optical hundreds-of-terahertz carrier.

</details>

### Question 3. What changes a waveplate's ideal phase retardance?

<details><summary>Reveal the worked answer</summary>

Wavelength, crystal properties, incidence and temperature may shift the designed retardance.

</details>

### Question 4. Why does a laser lock's error trace not prove absolute frequency stability?

<details><summary>Reveal the worked answer</summary>

It can remain quiet while its reference drifts or common-mode errors occur.

</details>

### Question 5. What optical measurements should precede RF coupling?

<details><summary>Reveal the worked answer</summary>

Stable probe absorption, laser references, coupling-dependent EIT, power, overlap and linear detector response.

</details>

### Question 6. Why can reducing waist worsen EIT in a vapour?

<details><summary>Reveal the worked answer</summary>

Transit time shortens, increasing motional decoherence despite greater intensity.

</details>

## Practical scientific assignment

Construct a species-labelled excitation ladder and optical-signal model, calculate the required photon or RF frequency using verified data, and design a control sequence that separates optical drift, detector effects and atomic response. Record assumptions, uncertainties, raw data provenance and expected failure signatures.

## Sources

Foot, *Atomic Physics*; Scully and Zubairy, *Quantum Optics*; Steck spectroscopy data; RydIQule and ARC official guides; and the [book bibliography](../REFERENCES.md).
