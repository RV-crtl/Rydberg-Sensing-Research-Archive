# Doppler dynamics, laser linewidth and spectral broadening

**Independent general reference chapter.** Discusses universally applicable physics and engineering; no project-specific numerical HFSS result is asserted.

## Competencies

Model the system, specify a measurement chain and units, choose appropriate numerical tools, reproduce limiting cases and debug signal/solver failures.

## 1. The velocity distribution of a thermal gas

Atoms in a thermal vapour follow an approximately Maxwell–Boltzmann distribution of velocity components. The one-dimensional root-mean-square thermal velocity is √(kBT/m); the Doppler detuning of one beam is −k·v when the sign convention defines the detuning as laser minus atomic frequency. A finite optical beam samples changing positions and velocities, so transit effects are a separate time-dependent mechanism. Never assign the bulk gas's full three-dimensional thermal speed to the projection along the probe beam without averaging.

## 2. Two-photon Doppler geometry

For a ladder driven by probe and coupling beams, the sum of their signed wavevectors multiplies the atomic velocity in the two-photon Doppler term. Co- and counter-propagating geometries therefore differ, and unequal 780/480-nm wavelengths produce a residual term even under counterpropagation. Beam crossing angles and finite numerical apertures add a distribution of projected k vectors. The residual linewidth is an ensemble property, not the Doppler shift of one atom at an arbitrarily chosen velocity.

## 3. Natural, transit and power broadening

An excited-state population decay Γ leads to a natural homogeneous linewidth under a declared half-width/full-width and rad/s/Hz convention. Optical Rabi power saturation can broaden an absorption line, while atoms leaving the beam experience finite interaction time. Transit broadening is not simply equal to the reciprocal of a full cell length: illuminated beam radius and thermal velocity distribution matter. Collisional dephasing and pressure broadening depend on density, buffer gas and state. Always define what linewidth has been measured: Gaussian standard deviation, Lorentzian HWHM, FWHM, or fit-model decay rate.

## 4. Laser phase noise and scan nonlinearity

Finite laser coherence can be modelled by linewidth or frequency-noise PSD depending on the regime; a single Lorentzian line width is not universal when low-frequency drift dominates. Nonlinear laser-frequency scans can exaggerate apparent splitting at one side of a trace. A stabilized reference laser can have quiet in-loop error but large out-of-loop drift. Characterize spectral scales with an independent optical frequency or etalon reference and record scan direction, lock bandwidth and sample timing.

## 5. Voigt profiles and multilevel line shapes

The convolution of a homogeneous Lorentzian and an inhomogeneous Gaussian produces a Voigt profile for simple absorption, but coherent EIT can create non-Voigt features. A physically valid thermal EIT simulation integrates the complex atomic susceptibility over velocity classes, not just a classical intensity spectrum after taking absolute values. Perform velocity-grid and extent convergence, then calculate optical propagation from the averaged complex susceptibility. Do not fit a Voigt shape to a clearly asymmetric dressed-state spectrum merely for convenience.

## 6. Practical diagnosis and calculated scale

For a single atom moving at 200 m/s projected along a 780 nm probe wavevector, the magnitude of the first-order Doppler shift is approximately v/λ≈256 MHz. That number is not an rms thermal width and not a final two-photon residual Doppler value. Check optical power at atoms, counterpropagation alignment, cell temperature, optical phase noise and the scan-frequency calibration before changing decay rates in a density-matrix fit. Compare spectra under altered beam geometry at otherwise fixed settings.

## End-of-chapter questions and answers

### Question 1. Does v/λ for one atom equal the thermal linewidth?

<details><summary>Read the worked explanation</summary>

No; the linewidth comes from a weighted distribution of projected velocities and the model's optical response.

</details>

### Question 2. Why is counterpropagation not perfect cancellation for 780 and 480 nm?

<details><summary>Read the worked explanation</summary>

The optical wavevector magnitudes differ, so the signed two-photon sum is not zero.

</details>

### Question 3. Why does Voigt broadening not fully predict EIT?

<details><summary>Read the worked explanation</summary>

Quantum coherence and multiple detunings require averaging the complex optical response, not only a scalar intensity profile.

</details>

### Question 4. What physical scale controls transit broadening?

<details><summary>Read the worked explanation</summary>

Beam geometry and distribution of atomic velocities through the illumination region.

</details>

### Question 5. How do laser phase noise and scan drift differ?

<details><summary>Read the worked explanation</summary>

Fast and slow fluctuations have different spectra and effects, and one fitted FWHM may not characterize both.

</details>

### Question 6. Why must linewidth units be declared?

<details><summary>Read the worked explanation</summary>

Decay rates, HWHM and FWHM can differ by factors including two and 2π.

</details>

## Research problem

Build a falsifiable numerical or experimental analysis with correct units and explicitly stated physical observables. Write its independent source and calibration references, convergence thresholds, and diagnostic on/off controls. Test at least one failure case. Never report simulated or illustrative values as new physical measurements.

## Further reading

Foot, *Atomic Physics*; Pozar, *Microwave Engineering*; official Ansys and RydIQule references; [complete bibliography](../REFERENCES.md).
