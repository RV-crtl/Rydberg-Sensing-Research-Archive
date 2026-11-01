# Jones, Stokes, Mueller and full-vector polarisation

**General graduate textbook chapter**, applicable to optical, microwave and Rydberg systems without relying on any one research project.

## Outcomes

Derive the core relations, identify measurement conventions, construct a reproducible model, calculate a limiting case and identify a false-positive result.

## 1. What a Jones vector describes

For a monochromatic coherent transverse field propagating along a declared axis, the Jones vector is J=(Ex,Ey)ᵀ with complex phasor components. It captures relative phase and amplitudes but requires a fixed overall phase convention. A detector measuring |Ex|² and |Ey|² alone does not recover their relative phase. An arbitrary partially polarised field is more generally described by a coherency matrix, not a single deterministic Jones vector.

## 2. Derive the Stokes coordinates

One valid convention for e^{−iωt} phasors defines S0=|Ex|²+|Ey|², S1=|Ex|²−|Ey|², S2=2Re(ExEy*), S3=2Im(ExEy*). Some RF and optical references reverse the sign of S3; never mix labels from two conventions without an explicit transformation. For a deterministic pure Jones state, S1²+S2²+S3²=S0². For a partially polarised statistical field, the inequality becomes ≤S0², and the degree of polarisation is the ratio of three-coordinate magnitude to S0.

## 3. Geometric interpretation

Normalized (s1,s2,s3) lies on the Poincaré sphere for pure polarisation and inside it for mixtures. Linear states lie along the equator, circular states at poles and elliptical states between. A linear polariser rotated through all possible angles can constrain some linear projections but cannot resolve the sign of circular handedness by itself. A device claiming full-Stokes must provide enough independent polarization-sensitive measurements and a calibrated forward map.

## 4. Polarisation optics and Mueller matrices

A deterministic Jones matrix transforms field amplitudes, whereas a Mueller matrix transforms Stokes vectors of fields including partial polarization. The latter is a real 4×4 representation but is not simply identical to a classical sensor's arbitrary 6×4 observation matrix. Loss, depolarisation and phase retardation must be modeled appropriately; a diagonal gain factor can shift observed Stokes values without changing the underlying incident polarisation.

## 5. Measurement bases and inverse models

A set of analysed intensity measurements can be written y=AS+ε when a calibrated linear Stokes observation model applies. At least four linearly independent rows are needed to reconstruct four real Stokes coordinates noiselessly; adding more rows may improve noise robustness but not guarantee accuracy. For a partially polarised field, positivity of the coherency matrix imposes S0≥√(S1²+S2²+S3²) and S0≥0. A least-squares solution outside the physical cone signals noise or model error.

## 6. Worked circular-state example

Choose Ex=1/√2 and Ey=i/√2. Under the defined formula, ExEy*=−i/2, so S=(1,0,0,−1). Reversing the sign of Ey flips S3 to +1 while leaving S0,S1,S2 identical. Therefore any measurement insensitive to relative phase cannot distinguish these states; the experiment must add circular/elliptical sensitivity. Helicity naming depends on the propagation and time convention, so the numbers are more reliable than an unlabeled 'RHCP' arrow.

## End-of-chapter questions and explained answers

### Question 1. Why is S3 convention sensitive?

<details><summary>Show complete answer</summary>

Its sign depends on the phasor time dependence and the circular-handedness/propagation definition.

</details>

### Question 2. What is missing from a rotated linear-polarizer measurement?

<details><summary>Show complete answer</summary>

Independent sensitivity to relative phase and thus circular handedness.

</details>

### Question 3. Can a mixed field be described by one Jones vector?

<details><summary>Show complete answer</summary>

Not generally; use the ensemble coherency matrix and Stokes parameters.

</details>

### Question 4. What is the physical cone for Stokes vectors?

<details><summary>Show complete answer</summary>

S0≥0 and S0²≥S1²+S2²+S3².

</details>

### Question 5. Why is a Mueller matrix not identical to any 6×4 detector matrix?

<details><summary>Show complete answer</summary>

The former maps four Stokes coordinates to four Stokes coordinates; a detector matrix maps Stokes coordinates to distinct calibrated observations.

</details>

### Question 6. How do you validate a measured Stokes sign?

<details><summary>Show complete answer</summary>

Use known elliptical/circular reference inputs and a declared propagation/time convention.

</details>

## Numerical and experimental assignment

Implement the physical equation in source code with defined SI units, test the simplest limiting case, then add a second independent calibration or measurement basis. Specify observable, uncertainty, stopping criterion, provenance and limitations. Consult [the source bibliography](../REFERENCES.md) before applying the method to an atomic species or actual hardware.

## Reading

Balanis, *Antenna Theory*; Pozar, *Microwave Engineering*; Collett, *Field Guide to Polarization*; Golub and Van Loan, *Matrix Computations*; [book bibliography](../REFERENCES.md).
