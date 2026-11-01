# RF fabrication, switching and material characterization

**General research engineering textbook.** Applies to independent experiments in optics, quantum sensors, microwave devices and other Rydberg platforms.

## Competencies

Define observables, quantify uncertainties and physical scaling, select an appropriate model, and apply controlled numerical and laboratory validation.

## 1. Physical stackup and electromagnetic behavior

A printed microwave surface is a three-dimensional structure with copper thickness, dielectric permittivity, loss tangent, solder mask, surface roughness and connectors or mounting. Nominal FR-4 is highly variable at microwave frequencies, and different Rogers laminate families must not be substituted without checking their frequency- and temperature-dependent properties. Copper conductivity and skin depth affect high-frequency loss, while substrate thickness changes coupling and modal resonances.

## 2. Fabrication geometry and manufacturability

Set minimum trace/slot width, clearance, via tolerances, drill and registration limits, board outline and copper edge buffers from the actual manufacturer. A parametrically attractive HFSS pattern can become unetchable when its narrow gap is smaller than process limits. Provide Gerber and drill source, layer conventions, fiducials, assembly instructions and copper dimensions that match the simulated model. A 2D SVG copper drawing alone may omit substrate, vias, solder and switching interconnects.

## 3. Switchable surface devices

PIN diodes, varactors and MEMS switches introduce bias-state impedance, nonlinear current/voltage behavior, package inductance, reverse capacitance and thermal dependence. A diode datasheet's RF impedance model must match frequency and bias, and its control circuit can disturb the local microwave field. The RF on/off state truth table belongs in both hardware and simulation. A binary short/open copper model is useful for topology screening but not proof of a manufactured switched device's isolation.

## 4. Measurement with a VNA

A VNA S11 or S21 measurement requires a calibrated reference plane and fixture de-embedding when appropriate. Field polarization selection may require free-space measurements, horn antennas, incidence-angle scans and time-gating to suppress chamber reflections. S parameters are complex, and phase must be aligned if the result is used to reconstruct circular or elliptical polarization. A single pass/reject dB ratio at one angle and frequency does not define broadband full-Stokes capability.

## 5. Resonance and tolerance analysis

For an ideal LC analogue f0=1/(2π√LC), a small capacitance perturbation δC yields δf/f≈−δC/(2C) at fixed L. A feature-size or dielectric shift may change both L and C and invalidate that simple estimate. Tolerance sweeps should use realistic process distributions when these are known, rather than adding arbitrary stochastic noise and presenting the result as measured reliability. Compare at least two mesh settings before optimizing feature-scale parameters.

## 6. Device verification sequence

First verify board dimensions and copper continuity with appropriate instrumentation, then diode bias/control operation, reference fixture calibration, frequency response and polarization angles. Document board revision, substrate batch, stackup, temperature, bias and frequency. If comparing to HFSS, model or de-embed real fixtures so the calibration plane matches the experiment. Hardware release requires electrical, thermal and laser/RF safety checks as applicable.

## End-of-chapter questions with explanations

### Question 1. Why is one laminate permittivity number insufficient?

<details><summary>Reveal answer and reasoning</summary>

Material response varies with frequency, temperature, batch and manufacturer tolerance.

</details>

### Question 2. What does an ideal open-circuit diode model omit?

<details><summary>Reveal answer and reasoning</summary>

Reverse capacitance, package and bias parasitics, leakage and nonlinear effects.

</details>

### Question 3. Why does phase matter for a circular selector?

<details><summary>Reveal answer and reasoning</summary>

Circular components are defined by relative phase and amplitude between orthogonal fields.

</details>

### Question 4. How does a 5% capacitance rise shift ideal resonance?

<details><summary>Reveal answer and reasoning</summary>

Approximately −2.5% in the first-order LC sensitivity estimate.

</details>

### Question 5. What does a PCB fabrication package include beyond a picture?

<details><summary>Reveal answer and reasoning</summary>

Copper/drill layers, board outline, stackup, clearances, registration and assembly details.

</details>

### Question 6. What makes a VNA comparison scientifically valid?

<details><summary>Reveal answer and reasoning</summary>

Matching reference planes, fixtures, polarization, frequency, calibration and physical device revision.

</details>

## Practice and reproducibility challenge

Create a new model or experiment with declared units, physical response and calibration reference. Test its weakest identifiable mode, document uncertainty assumptions and keep at least one control or holdout dataset independent from optimisation. Archive failed cases with the same provenance as accepted cases.

## Sources

Golub and Van Loan, *Matrix Computations*; Kay, *Statistical Signal Processing*; Pozar, *Microwave Engineering*; original documented sources and the [full bibliography](../REFERENCES.md).
