# Rydberg cavity QED and microwave photons

**Graduate reference volume:** quantum optics. **Scope:** species-agnostic fundamentals; assumptions and equipment conditions must be specified before applying any formula. [Reference index](../REFERENCES.md).

## Competencies

Derive the basic model, assess approximations, calculate limiting cases, select suitable numerical methods and design a falsifiable experimental check.

## 1. Cavity modes and atom-field coupling

A resonator supports discrete electromagnetic modes with field per photon set by mode volume and energy. A Rydberg transition can couple strongly to microwave photons because its electric dipole matrix element is large. A minimal Jaynes–Cummings Hamiltonian has H/ℏ=ωc a†a+(ωa/2)σz+g(a†σ−+aσ+), where g is the single-photon coupling frequency. The rotating-wave approximation and two-level truncation require validation for the chosen atom, cavity and drive.

## 2. Dressed-state spectrum

On resonance, each excitation manifold contains coherent superpositions of |e,n⟩ and |g,n+1⟩ separated by a frequency proportional to 2g√(n+1). The vacuum Rabi splitting arises already at n=0, revealing single-photon field sensitivity. Cavity and atom frequencies may be shifted by temperature, geometry, Stark fields or mechanical changes. Simply seeing two classical peaks cannot prove strong coupling without calibrated linewidth and density dependence.

## 3. Strong versus weak coupling

The relevant loss rates include cavity photon leakage κ, atomic decay γ and pure dephasing γφ. Strong coupling requires coherent exchange to compete favourably with these decoherence channels; exact conventional inequalities vary by observable and definition. Cooperativity C∼g²/(κγ) is a useful dimensionless measure under a declared convention. A device with large g but even larger κ can remain a broad, weakly coupled sensor.

## 4. Dispersive regime and nondemolition concepts

When |Δ|≫g√(n+1), virtual exchanges shift the atom or cavity frequency by terms of order g²/Δ. Such shifts can enable photon-number sensing or conditional phase interactions. Derivations neglect counter-rotating terms and higher atomic levels only under known inequalities. A dispersive approximation fails near resonance or large photon occupation, where exact diagonalisation or multilevel modelling is necessary.

## 5. Experimental design and calibration

Choose cavity geometry, polarization, mode volume, Q factor, atom trajectory, magnetic control and readout before predicting signal. Measure the empty-cavity linewidth and its drift; characterise atomic transition without the cavity; then study the coupled system. Separate thermal occupation from coherent injected photons. Rydberg atoms can be destroyed or shifted by nearby dielectrics and charged surfaces; map DC stray fields.

## 6. Error diagnosis

A missing avoided crossing may result from wrong cavity polarization, weak state preparation, excessive atomic velocity spread, mode mismatch, frequency calibration error or low Q. Reproduce known empty-cavity mode frequencies and single-atom spectroscopy separately. Only when both components pass should the coupled-system parameter g be inferred.

## End-of-chapter questions and answers

### 1. Why is a large electric dipole not sufficient for strong cavity coupling?

<details><summary>Reveal the explained answer</summary>

Mode overlap, vacuum field, cavity loss and atomic decoherence determine the ratio of coherent exchange to damping.

</details>

### 2. What does the √(n+1) dependence express?

<details><summary>Reveal the explained answer</summary>

Bosonic photon-number enhancement of the coherent coupling within an excitation manifold.

</details>

### 3. When does dispersive approximation fail?

<details><summary>Reveal the explained answer</summary>

When detuning is not large compared with coupling and relevant photon-number-dependent matrix elements.

</details>

### 4. What does κ describe in cavity QED?

<details><summary>Reveal the explained answer</summary>

Cavity field/photon decay, with a convention-dependent linewidth relationship that must be defined.

</details>

### 5. Why is thermal photon occupation relevant?

<details><summary>Reveal the explained answer</summary>

A microwave cavity at finite temperature may contain substantial background photons that change observed spectra.

</details>

### 6. How is vacuum Rabi splitting distinguished from an artefact?

<details><summary>Reveal the explained answer</summary>

Check detuning-dependent anticrossing, linewidth dependence, density, mode coupling and independently calibrated cavity/atom controls.

</details>

## Investigation and research methods exercise

Select a published state or apparatus, list its degrees of freedom, write the microscopic Hamiltonian or master equation, and specify an actual measured observable. Compute a limiting case and compare against a separate numerical or experimental check. Document units, versions, control measurements and credible failure modes. A simulation is not automatically a new laboratory result.

## Further study

Gallagher, *Rydberg Atoms*; Foot, *Atomic Physics*; the ARC and RydIQule documentation; and the modern research reviews in the [bibliography](../REFERENCES.md). Figures are original or sourced with permission; no textbook diagrams have been copied.
