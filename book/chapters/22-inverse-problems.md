# Reliable inversion, regularisation and physical parameter inference

**General graduate research textbook.** Cross-disciplinary methods; the original user's experiment histories remain in separate project evidence and research folders.

## Learning objectives

Develop reproducible scientific methods, diagnose invalid conclusions and plan experiments with independent verification and proper uncertainty models.

## 1. Why inversion is often ill posed

A forward model maps physical parameters into observables, but multiple parameter values may generate nearly indistinguishable signals. The Hadamard requirements of existence, uniqueness and stability provide a useful starting point for diagnosing inverse problems. In atomic spectra, different laser detunings, decoherence rates or microwave couplings can compensate each other. A nonlinear optimiser producing a small residual does not prove that the inferred Rydberg field or atomic decay rate is uniquely determined.

## 2. Normal equations and robust computation

For linear data y=Aθ+ε with fixed covariance C, weighted least squares formally yields θhat=(AᵀC⁻¹A)⁻¹AᵀC⁻¹y when full rank holds. In numerical code, do not form explicit inverse matrices unnecessarily; solve the linear least-squares problem by QR or SVD after whitening. Normal equations square the condition number and can magnify roundoff. A suitable cross-check compares residual norms and solutions computed with different stable factorizations.

## 3. Tikhonov and Bayesian regularisation

A regularized estimate minimizes ||C⁻1/2(Aθ−y)||²+λ||L(θ−θ0)||². In one interpretation this is a maximum a posteriori estimate with a Gaussian prior. The parameter λ trades variance against bias and must be chosen using a justified method such as holdout cross-validation, independent calibration or prior noise statistics. Fitting λ until the preferred physical field value appears is not scientific inference.

## 4. Constraints and physically meaningful solutions

Many estimated quantities have physical bounds: decay and population rates are nonnegative, density matrices are positive semidefinite, and a Stokes vector lies inside a positive polarization cone. Constraint enforcement can improve stability, but it should not quietly hide a large unconstrained model violation. Report the unconstrained residual, constrained residual and reason for the constraint. In density-matrix parameter estimation, a parametrization through a positive factor can avoid unphysical updates.

## 5. Sensitivity, confidence intervals and model discrepancy

A local Jacobian can predict uncertainty near a fit minimum when the model and noise are valid. Multimodal likelihoods, correlated drift, unmodelled line shapes or discrete transition assignments can defeat Gaussian Hessian error bars. Run posterior predictive checks or held-out validation; perturb laser intensity, magnetic field and RF detuning experimentally when possible. If predictions fail away from the training scan, the model may have compensated for missing physics.

## 6. Worked singular value argument

Consider a toy response A=diag(1,0.1,0.01). With equal independent observation noise σ, the third component's variance under an unregularized inverse is σ²/(0.01²)=10000σ², while the first is σ². A weighted penalty can lower output variance but introduces bias. Acquiring additional measurements with strong sensitivity to the third parameter is generally a more informative physical remedy than clipping its noisy reconstruction.

## 7. Audit and reproducibility

Preserve calibrated observations, covariance model, forward code, solver tolerances, parameter bounds, initialization, fit residuals and random seeds. Perform tests at known synthetic *educational* parameters but never mix the synthetic curve into a measured dataset. Declare which confidence intervals are model-based and which are empirically tested. A publishable result should be reproducible on independent starting guesses and meaningful holdout conditions.

## Questions and complete explanations

### Question 1. Why avoid forming (AᵀA)⁻¹ directly?

<details><summary>Reveal reasoning</summary>

Normal equations can square the condition number; stable QR/SVD solvers are preferred.

</details>

### Question 2. What does regularisation do?

<details><summary>Reveal reasoning</summary>

It trades estimator variance for bias under an explicit penalty/prior assumption.

</details>

### Question 3. Why can a small residual still be incorrect?

<details><summary>Reveal reasoning</summary>

Wrong model or degeneracy can fit the observed data without identifying true parameters.

</details>

### Question 4. What physical constraints govern Stokes reconstruction?

<details><summary>Reveal reasoning</summary>

Nonnegative S0 and S0≥√(S1²+S2²+S3²).

</details>

### Question 5. What does a holdout experiment test?

<details><summary>Reveal reasoning</summary>

Predictive transfer to new calibrated inputs not used in fitting or tuning.

</details>

### Question 6. How can one expose compensating linewidth and RF coupling?

<details><summary>Reveal reasoning</summary>

Measure independent scans at varied RF powers/laser conditions, then inspect joint sensitivity and posterior correlations.

</details>

## Advanced research assignment

Choose a real published experimental or computational method. Create a reproducibility checklist, data/provenance manifest, independent limiting-case test and a claim-to-evidence table. Include a realistic failure case and a diagnostic remedy. Distinguish your own numerical illustration from any published measurement.

## References

Consult [the annotated bibliography](../REFERENCES.md) and discipline-specific journal, instrumentation and software primary sources. Rights to source images and datasets must be checked before release.
