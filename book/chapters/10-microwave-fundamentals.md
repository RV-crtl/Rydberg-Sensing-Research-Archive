# Electromagnetic waves, RF hardware and atomic field coupling

**General graduate textbook chapter**, applicable to optical, microwave and Rydberg systems without relying on any one research project.

## Outcomes

Derive the core relations, identify measurement conventions, construct a reproducible model, calculate a limiting case and identify a false-positive result.

## 1. From Maxwell equations to plane waves

Maxwell equations relate electric displacement, magnetic flux, conduction current and charge. In a homogeneous lossless medium, a monochromatic plane wave has k=ω√(με), its transverse E and H fields are related through impedance η=√(μ/ε), and free-space wavelength is λ0=c/f. The time-averaged Poynting flux of peak phasors is Re(E×H*)/2; using RMS field phasors omits the one-half factor. This convention matters when converting calibrated power into a local electric-field amplitude.

## 2. Near field versus far field

A source does not produce a uniform plane wave at every distance. Reactive and radiative field components decay differently; the geometric relationship between antenna size, wavelength and observation distance controls whether a plane-wave or far-field approximation is justified. A compact cell near a radiating element can experience complex spatially varying fields and longitudinal components. The plane-wave port S parameters of an isolated microwave component do not by themselves determine the atom-local electric field.

## 3. Network analyzers and reference planes

Scattering parameters relate incident and reflected travelling-wave amplitudes at specified characteristic impedances. A vector network analyzer must be calibrated to a reference plane through cables, connectors and fixtures. S21 magnitude gives transmission under its port and load conventions; a polarisation-sensitive local-field model also needs complex phase and vector components. Incoherent subtraction of dB values or mixing power and voltage logarithms can give wrong extinction ratios.

## 4. Power calibration and antenna pattern

For power P in watts, dBm=10log10(P/1mW). A 3 dB power change is approximately a factor two in power but only √2 in electric-field amplitude for fixed impedance. Antenna gain, polarisation mismatch and path loss must be applied in their correct domains. A high-gain antenna pointed at a cell is not proof of an incident plane-wave field: scattering from optical mounts and cell windows may substantially change local direction and handedness.

## 5. RF coupling to an atomic dipole

The coupling is Ω=|⟨i|d·E|j⟩|/ℏ. The complex vector E includes phase and orientation, and the transition dipole is defined in an atomic state basis. Rotating the magnetic quantisation axis changes which spherical component drives a particular m transition. RF polarization, noise and frequency modulation can therefore alter atomic optical spectra even at the same total received RF power.

## 6. Hardware fault isolation

When an optical atomic response seems absent, independently inspect source generator power/carrier, antenna/cable reference, RF detuning from the atomic transition, field orientation and optical EIT. Avoid blaming an antenna solely from a zero optical detector contrast; atoms may be prepared in an uncoupled sublevel or the optical linewidth may be too broad. Preserve VNA calibration kits, source spectra, power units, layout drawings and detector data separately.

## End-of-chapter questions and explained answers

### Question 1. What does S21 measure?

<details><summary>Show complete answer</summary>

Complex port transmission under a specified impedance and calibration reference, not necessarily local atom-cell field.

</details>

### Question 2. What is free-space wavelength at 2 GHz?

<details><summary>Show complete answer</summary>

Approximately 0.150 m using c/f.

</details>

### Question 3. Why can a dB voltage ratio use 20log but a power ratio 10log?

<details><summary>Show complete answer</summary>

Power is quadratic in field/voltage for a fixed impedance.

</details>

### Question 4. Why might atoms see different field polarisation from an antenna datasheet?

<details><summary>Show complete answer</summary>

Nearby structures and finite observation geometry can scatter the field and change complex components.

</details>

### Question 5. How does RF field orientation enter atomic Rabi frequency?

<details><summary>Show complete answer</summary>

Through the vector dipole projection and allowed spherical components.

</details>

### Question 6. What must be written beside a VNA plot?

<details><summary>Show complete answer</summary>

Reference planes, S-parameter definition, ports/impedance, calibration state, frequency and phase conventions.

</details>

## Numerical and experimental assignment

Implement the physical equation in source code with defined SI units, test the simplest limiting case, then add a second independent calibration or measurement basis. Specify observable, uncertainty, stopping criterion, provenance and limitations. Consult [the source bibliography](../REFERENCES.md) before applying the method to an atomic species or actual hardware.

## Reading

Balanis, *Antenna Theory*; Pozar, *Microwave Engineering*; Collett, *Field Guide to Polarization*; Golub and Van Loan, *Matrix Computations*; [book bibliography](../REFERENCES.md).
