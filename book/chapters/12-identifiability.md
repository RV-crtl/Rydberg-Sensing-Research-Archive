# Parameter identifiability, matrices and stable reconstruction

**General graduate textbook chapter**, applicable to optical, microwave and Rydberg systems without relying on any one research project.

## Outcomes

Derive the core relations, identify measurement conventions, construct a reproducible model, calculate a limiting case and identify a false-positive result.

## 1. From observations to an inverse problem

Define a forward model y=f(θ,η)+ε, with θ the desired physical parameters and η nuisance variables. Near a chosen operating point, linearize to δy≈Jδθ+ε. The Jacobian's column rank determines local identifiability under noise-free assumptions. The same observable can come from distinct physical conditions, such as a laser detuning shift mimicking a coupling-strength variation; one successful nonlinear fit does not imply uniqueness. Choose additional calibrated measurements that break degeneracies.

## 2. Singular values and condition numbers

For a rectangular sensitivity matrix A=UΣVᵀ, its singular values identify observable input combinations. A full-rank A can still have tiny σ_min and therefore strongly amplify measurement error. A row-normalized condition number differs from an unnormalized gain-aware sensitivity analysis, and both can be useful for different questions. Report the norm, normalization and physical units before comparing κ values between devices.

## 3. Least squares and uncertainty

For full-rank linear Gaussian measurements with covariance C, the generalized least-squares estimator is S_hat=(AᵀC⁻¹A)⁻¹AᵀC⁻¹y. Its model covariance is (AᵀC⁻¹A)⁻¹ if the assumptions hold. When the noise variance depends on signal intensity or acquisition time, the weighting must be adapted. A fitted residual close to zero can coexist with a large systematic calibration error; test against known held-out input states.

## 4. Regularisation and physical constraints

Tikhonov regularisation minimizes ||C⁻1/2(AS−y)||²+λ||LS||². The parameter λ trades variance for bias and should be selected by a defensible cross-validation or prior argument rather than tuned until a particular plot looks smooth. Physical Stokes estimates must be nonnegative intensity and lie inside the polarisation cone. Constraint projection may be useful but should not hide that an unconstrained estimate was invalid.

## 5. Designing independent measurement states

To estimate a vector or quantum state, choose preparation/analyser configurations with complementary sensitivity. State count alone is not a guarantee: six nearly parallel measurement rows can carry less useful information than four well-separated rows. Orthogonal or tetrahedrally distributed measurement bases are useful conceptual guides, but actual system gain, finite aperture, noise and available controls determine whether they are optimal.

## 6. Independent validation and observability maps

Compare prediction y_test=A S_known for known states that were not used in calibration, including the weakest singular direction. Test sensitivity over frequency, position, polarisation and relevant operating conditions. A rank-four matrix obtained from one simulation is evidence of a *model* property, not proof of a physical device; optical transduction and model calibration must be separately established.

## End-of-chapter questions and explained answers

### Question 1. Can six measurements be insufficient for four parameters?

<details><summary>Show complete answer</summary>

Yes; the six rows can be linearly dependent or nearly so.

</details>

### Question 2. What does a tiny singular value imply?

<details><summary>Show complete answer</summary>

Noise and model errors can cause large uncertainty in its associated parameter combination.

</details>

### Question 3. Why is λ in regularisation not free?

<details><summary>Show complete answer</summary>

It controls bias/variance tradeoff and should be justified by prior knowledge or held-out validation.

</details>

### Question 4. Why can a fitted residual be small but a field estimate wrong?

<details><summary>Show complete answer</summary>

The forward model can be miscalibrated or nonunique.

</details>

### Question 5. How should Stokes physicality enter an estimator?

<details><summary>Show complete answer</summary>

Through explicit inequality constraints or a physically parameterized coherency matrix, with violations reported.

</details>

### Question 6. What is a meaningful independent calibration test?

<details><summary>Show complete answer</summary>

A known input outside the fitting set, especially in a weakly observable direction, measured under the same apparatus conditions.

</details>

## Numerical and experimental assignment

Implement the physical equation in source code with defined SI units, test the simplest limiting case, then add a second independent calibration or measurement basis. Specify observable, uncertainty, stopping criterion, provenance and limitations. Consult [the source bibliography](../REFERENCES.md) before applying the method to an atomic species or actual hardware.

## Reading

Balanis, *Antenna Theory*; Pozar, *Microwave Engineering*; Collett, *Field Guide to Polarization*; Golub and Van Loan, *Matrix Computations*; [book bibliography](../REFERENCES.md).
