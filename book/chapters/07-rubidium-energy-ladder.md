# Alkali excitation ladders and spectroscopic access

**General Rydberg and optical physics chapter.** Species and apparatus choices are examples, not a report of one project.

## Competencies

Derive the optical and atomic response, identify the real observable, use state-specific data, design controls, and discriminate physical behaviour from technical artefacts.

## 1. Choosing a legitimate ladder

An alkali Rydberg excitation scheme moves population or coherence from the ground state to a highly excited manifold using one or more photons. A common thermal-vapour ladder involves 5S→5P→nS/nD for rubidium, but the actual intermediate and final states depend on isotope, hyperfine level, polarisation and tuning resources. Approximate wavelengths are useful for orientation, never a substitute for a state-specific level table. Some elements require UV sources, two-photon excitation or alternative intermediate levels, and cold platforms may avoid the same ladder architecture entirely.

## 2. Selection rules in every stage

Write each step with n,l,j,F,m where resolved. Apply parity and Δl=±1 to electric-dipole transitions, together with magnetic projection selection under the chosen quantisation axis. A laser nominally tuned to an allowed line may be ineffective when its polarisation projects weakly onto the accessible transition or when optical pumping empties the initial sublevel. The Rabi rate depends on the specific dipole matrix element and electric-field amplitude, not simply the optical power printed on the laser.

## 3. Wavelength, detuning and Doppler reference

The frequency of light in vacuum is f=c/λ; two-photon detuning combines optical frequencies and state energies with their signs. For a moving atom, each beam contributes k·v to its detuning. Whether beams co- or counterpropagate matters to the residual Doppler width. Laser beam crossing angle, cell refractive index, wavemeter calibration and scan nonlinearity should be recorded. A 780 nm laser is hundreds of terahertz in carrier frequency, while scanning a few megahertz concerns a tiny relative shift.

## 4. Coherent and incoherent coupling

An ideal three-state ladder has probe and coupling Rabi frequencies, one-photon and two-photon detunings, intermediate decay and Rydberg dephasing. Strong coupling can dress eigenstates and modify absorption. Incoherent pumping, transit relaxation and hyperfine branching can change population distributions. A single optical trace cannot separately identify every rate without independent controls, making physically informed parameter priors and additional measurements necessary.

## 5. Practical screening with ARC

Begin with a table of candidate Rydberg n,l,j states. Query ARC for actual energies, transition frequencies, dipole matrix elements and lifetime, checking the returned frequency sign and units. Reject inaccessible laser transitions or forbidden magnetic pathways. For a warm-vapour receiver, then calculate Doppler broadening and the optical susceptibility with a consistent density-matrix model. Export source code and a machine-readable table; do not derive all conclusions from a screenshot of an energy-level diagram.

## 6. What to do when nothing appears

Check the ground and intermediate hyperfine lock, optical overlap, beam propagation, coupling polarisation and temperature. Confirm the detector is linear and the scan actually passes through two-photon resonance. Use coupling-off and RF-off baselines, and compare source frequency changes with the optical feature. Only after these controls are verified should unusual physics be invoked.

## 7. Worked wavelength interpretation

For the rubidium D2 transition, accurate spectroscopy tables place the vacuum wavelength near 780.241 nm, while an air wavelength is near 780.033 nm. The difference arises because wavelength depends on the medium but frequency does not. Mistaking the two values, or using a wavemeter configured to a different convention, can confuse coarse tuning and line assignment. Always cite the isotope and vacuum/air convention.

## End-of-chapter questions with answers

### Question 1. Can two lasers with the right approximate wavelengths guarantee EIT?

<details><summary>Reveal the worked answer</summary>

No; transition selection, locks, coherence, beam overlap, Doppler conditions, power and decays must also be correct.

</details>

### Question 2. Why are optical transition frequencies signed in atomic software?

<details><summary>Reveal the worked answer</summary>

They indicate ordering of initial and final energy levels; magnitude is not sufficient to determine the direction of a process.

</details>

### Question 3. How does a counterpropagating geometry affect two-photon Doppler shift?

<details><summary>Reveal the worked answer</summary>

It changes the relative sign of k·v terms and often reduces residual broadening in unequal-wavelength ladders.

</details>

### Question 4. Why can a nominally allowed transition be dark?

<details><summary>Reveal the worked answer</summary>

Population may occupy other magnetic sublevels or light polarisation may not couple the desired projection.

</details>

### Question 5. What is the difference between vacuum and air wavelength?

<details><summary>Reveal the worked answer</summary>

Frequency remains fixed while phase velocity and wavelength depend on refractive index.

</details>

### Question 6. What must an optical ladder table include?

<details><summary>Reveal the worked answer</summary>

State labels, frequency, laser access, dipole projection, detuning, linewidth and lifetime assumptions.

</details>

## Practical scientific assignment

Construct a species-labelled excitation ladder and optical-signal model, calculate the required photon or RF frequency using verified data, and design a control sequence that separates optical drift, detector effects and atomic response. Record assumptions, uncertainties, raw data provenance and expected failure signatures.

## Sources

Foot, *Atomic Physics*; Scully and Zubairy, *Quantum Optics*; Steck spectroscopy data; RydIQule and ARC official guides; and the [book bibliography](../REFERENCES.md).
