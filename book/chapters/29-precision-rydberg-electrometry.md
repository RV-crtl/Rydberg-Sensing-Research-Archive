# Precision Rydberg electrometry and traceability

**Independent textbook chapter / metrology**. Original general treatment; no project-specific RF apparatus or HFSS case is presented as universal physics. Read [references](../REFERENCES.md).

## Learning objectives

Explain the core physical mechanism, derive a model with explicit approximations, design a falsifiable measurement, diagnose artefacts and choose validated calculation methods.

## 1. Electric-field observables across the spectrum

Rydberg sensors respond to DC and oscillating electric fields through different mechanisms. A static or far-detuned field produces Stark shifts related to polarizability, whereas near-resonant microwave coupling can produce dressed-state splitting, changes in EIT and heterodyne sidebands. A frequency measurement can be intrinsically precise, but converting that frequency shift to the external incident electric field requires an accurate dipole matrix element, selection rule, field orientation and local-field model. A vapour-cell wall may perturb the field; 'SI traceable' describes a calibrated measurement chain, not every arbitrary Rydberg setup.

## 2. Resonant Autler–Townes and phase sensitivity

The simplest resonant two-state dressed splitting is ΩRF, and ΩRF=|μ·E|/ℏ for a specified matrix element and field amplitude convention. An optical splitting extracted from an EIT spectrum can differ from ΩRF because multi-level Zeeman coupling, Doppler averaging, propagation and finite linewidth reshape peaks. When the RF field is too weak to resolve a doublet, a local-oscillator or frequency-modulated detection scheme can increase sensitivity by converting phase/amplitude into optical sideband observables. A model that predicts amplitude only cannot be used to certify RF phase retrieval.

## 3. Field-vector and polarisation observability

A complex electric field has vector amplitude and relative phases. A single scalar transition dipole projection only responds to one linear combination of the field; multiple independent atomic selection-rule pathways, rotated quantisation axes or known polarisation-sensitive references may be needed for vector reconstruction. An instrument matrix can be full rank but still poorly conditioned or insensitive in practice if its smallest singular mode is below noise. Circular helicity must be tied to a declared propagation axis and Fourier sign.

## 4. Sensitivity and noise-equivalent field

Define a calibration slope K=∂V/∂E and output amplitude spectral density S_V^{1/2}; then a local small-signal noise-equivalent electric-field density is S_E^{1/2}=S_V^{1/2}/|K|. Units are V·m^−1·Hz^−1/2, not simply 'volts'. This linearisation assumes stable slope, bandwidth, optical powers and noise spectrum. Shot noise, laser drift, RF local-oscillator phase noise and cell environmental perturbations must be considered separately. An apparent improvement under different sampling time is not a device sensitivity comparison.

## 5. Traceability, uncertainty and interference

Establish frequency calibration against appropriate references, confirm the state-specific μ using ARC/atomic spectroscopy, characterise incident RF polarization and local field distortions, and propagate uncertainties including correlations. A strong field may shift levels enough to invalidate the weak-field approximation or cause electromagnetically induced absorption. A nearby RF spur can produce an optical response indistinguishable from the intended source without controlled RF-off/reference tests.

## 6. Design recipe

Choose whether the measurement target is amplitude, frequency, phase, polarisation, spatial field or modulation content; each requires a different observable and transfer function. Select an accessible atomic species/transition, estimate linewidth and field coupling, select laser paths and readout, and design calibration with at least two independent references. Use simulations only after specifying testable pass/fail criteria and preserve the raw signals as well as derived field estimates.

## Review problems with full explanations

### 1. Why is AT splitting not a universal field meter without calibration?

<details><summary>View worked reasoning</summary>

The observed optical feature depends on multilevel structure, linewidth, line shape, field projection and optical propagation; a valid mapping to μE/ℏ needs those assumptions.

</details>

### 2. What does sensitivity in V/m/√Hz require?

<details><summary>View worked reasoning</summary>

A calibrated voltage-to-field slope and output noise spectral density at a specified frequency and bandwidth.

</details>

### 3. What can make a full-rank polarimeter poor?

<details><summary>View worked reasoning</summary>

Low absolute gain, ill-conditioned modes relative to noise, model mismatch or unstable field reference.

</details>

### 4. Why can SI traceability fail despite accurate frequency measurement?

<details><summary>View worked reasoning</summary>

Dipole, orientation, local-field correction and measurement transfer factors may be uncertain.

</details>

### 5. Why do RF phase measurements require an appropriate reference?

<details><summary>View worked reasoning</summary>

Absolute phase has no standalone observable; coherence/relative phase is inferred against a known local oscillator or reference pathway.

</details>

### 6. How do you separate a source spur from an atomic line?

<details><summary>View worked reasoning</summary>

Use calibrated RF-port characterisation and source-off/coupling-off optical controls plus frequency tracking.

</details>

## Design and verification assignment

Construct a research protocol for an appropriate species or platform. State what the detector measures, its model assumptions, the control experiment needed, expected scale, uncertainty sources and stopping criteria. Perform an independent computation or published-data comparison before claiming a new observation. Consult the bibliography for exact state constants and validated methods.

## Suggested source pathway

Gallagher, *Rydberg Atoms*; relevant ARC documentation and atomic spectroscopy; the NIST review of atomic electrometry (2024/2025) and field-specific primary literature. See [bibliography](../REFERENCES.md).
