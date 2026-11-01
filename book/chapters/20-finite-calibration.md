# Model transfer, finite geometry and independent validation

**General research engineering textbook.** Applies to independent experiments in optics, quantum sensors, microwave devices and other Rydberg platforms.

## Competencies

Define observables, quantify uncertainties and physical scaling, select an appropriate model, and apply controlled numerical and laboratory validation.

## 1. A good model is not automatically a good instrument

A computational model predicts a physical observable under chosen boundaries, source conditions and parameters. Transferring its calibration to a real apparatus requires the modeled observable to match the measurement location, spatial integration and detector response. Periodic and finite electromagnetic devices can have different edge currents and local fields; likewise a single stationary atom and a thermal ensemble have different response functions. Validation is therefore a sequence of domain transfers, not one global yes/no 'converged' flag.

## 2. Discretization versus physical-model error

A refined finite-element mesh can reduce discretization error for the equations being solved, but cannot fix incorrect material properties, missing hardware, wrong boundary conditions or unmodeled atomic dynamics. Distinguish mesh-convergence studies from model-discrepancy studies. Independently adapted meshes must be compared on the same observation coordinates, and phase must remain referenced consistently. A small energy-residual number is not sufficient to certify a highly phase-sensitive derived observable.

## 3. Complex-field and calibration matrix transfer

Suppose A_ref is calibrated on one model, while the actual device has A_real. Inverting y=A_real S with A_ref can introduce systematic error even when both matrices have full rank. A transfer test generates known S inputs through A_real and reconstructs with A_ref; the maximum error depends on matrix difference and inverse conditioning. Perform this in both directions for independent meshes, field positions and relevant incident polarisation bases. Report failed inputs and frequencies rather than only an average metric.

## 4. Gain, phase and physical observation volume

An optical receiver samples a physical volume; a point probe in simulation may not represent that average. If incident field phases vary across the cell or detector response is spatially weighted, integrating complex amplitudes before versus after taking intensity can produce different results. Define whether the atomic model senses local RF intensity, spherical Rabi components or another nonlinear optical response. Sampling exactly at a surface may yield strong mesh artifacts not representative of a finite atom cloud.

## 5. Transfer acceptance thresholds

Declare pass/fail metrics before selecting frequencies: relative complex-field error, matrix discrepancy, smallest singular value, calibration holdout error and absolute signal. Different thresholds may be appropriate for a concept screen versus a manufactured sensor, but they must not be changed silently after seeing bad results. Include uncertainty due to RF source reference, material parameters and manufacturing variation only when appropriately modeled or measured.

## 6. Designing a validation campaign

Create independent validation levels: analytic electromagnetic sanity checks; periodic unit-cell calculations; finite array on two distinct adapted meshes; extracted Jones/Stokes response; optical atomic forward-model transfer; and eventually real calibration against reference field states. Every level includes raw native source, code, geometry, spectral bandwidth and a decision log. A failure can be scientifically useful because it specifies exactly which model transfer assumption was false.

## End-of-chapter questions with explanations

### Question 1. Can two full-rank matrices produce unreliable calibration transfer?

<details><summary>Reveal answer and reasoning</summary>

Yes; their physical response rows may differ enough to introduce large reconstruction bias.

</details>

### Question 2. Does numerical mesh convergence certify material correctness?

<details><summary>Reveal answer and reasoning</summary>

No, it only tests discretisation under the specified physical model.

</details>

### Question 3. Why compare the same observation volume between meshes?

<details><summary>Reveal answer and reasoning</summary>

Otherwise field differences may be due to sampling different physical locations instead of numerical error.

</details>

### Question 4. Why must finite edges matter?

<details><summary>Reveal answer and reasoning</summary>

They change boundary currents, diffraction, source illumination and near-field phase.

</details>

### Question 5. What is a holdout transfer test?

<details><summary>Reveal answer and reasoning</summary>

Use known inputs not used in calibration through an independent response model or experiment, then reconstruct with the calibrated model.

</details>

### Question 6. Why preserve failed solver cases?

<details><summary>Reveal answer and reasoning</summary>

Failures identify model regimes and validity boundaries that a best-case plot cannot reveal.

</details>

## Practice and reproducibility challenge

Create a new model or experiment with declared units, physical response and calibration reference. Test its weakest identifiable mode, document uncertainty assumptions and keep at least one control or holdout dataset independent from optimisation. Archive failed cases with the same provenance as accepted cases.

## Sources

Golub and Van Loan, *Matrix Computations*; Kay, *Statistical Signal Processing*; Pozar, *Microwave Engineering*; original documented sources and the [full bibliography](../REFERENCES.md).
