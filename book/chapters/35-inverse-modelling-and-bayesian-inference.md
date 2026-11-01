# Inverse modelling, Bayesian inference and experimental design

**Graduate general reference / data analysis.** This chapter develops transferable principles rather than an individual laboratory project.

## Competencies

Derive appropriate equations and approximations, identify observables, choose realistic instrumentation, establish numerical and physical controls, and propose a falsifiable research plan.

## 1. The forward model comes first

An inverse problem estimates physical parameters θ from observations y=f(θ,ξ)+ε, where ξ includes nuisance parameters such as laser detuning, gain, linewidth, temperature and field orientation. If two distinct parameter vectors produce essentially identical observables, the inverse problem is non-identifiable. An optimizer can return a precise-looking minimum despite that degeneracy. Inspect Jacobians, singular values, posterior correlations and independent calibration channels before declaring a recovered electric field or atomic rate.

## 2. Likelihoods and noise structure

For independent Gaussian residuals, minus log likelihood is proportional to ∑(y_i−f_i)²/σ_i² plus variance terms. Correlated spectra require a non-diagonal covariance, while photon counts may be better approximated by Poisson statistics. Baseline subtraction changes covariance and can correlate points; fitting a spectrum after smoothing without modelling that filter underestimates uncertainty. Calibration parameters should be included explicitly or propagated into the final inference uncertainty.

## 3. Priors and Bayesian interpretation

Bayes' theorem gives p(θ|y)∝p(y|θ)p(θ). A prior can encode nonnegative rates, known atomic constants or independently measured laser stability, but should not be chosen after seeing the same target data just to manufacture a narrow posterior. Reporting a posterior credible interval requires the likelihood and prior to be disclosed; it is not interchangeable with a frequentist confidence interval. When the likelihood is multimodal, a single best-fit parameter and Hessian approximation may be badly misleading.

## 4. Fisher information and experimental choice

The local Fisher information is the expected negative curvature of the log likelihood; for a linear Gaussian model y=Aθ+ε with fixed covariance C, F=AᵀC^{-1}A. A full-rank F is necessary for local invertibility but small eigenvalues can make uncertainty enormous. Optimising scan frequencies, polarisation states or dwell time should account for actual signal gain and noise, not only algebraic row diversity. Experimental design can target trace(F^{-1}), determinant F or worst-mode error, each answering a different scientific question.

## 5. Model discrepancy and holdout validation

A density-matrix fit with a wrong level graph can compensate by distorting linewidth or Rabi strength. A physically meaningful report should test predictions under new laser powers, detunings or polarisation states that were not used to fit. A poor holdout residual indicates model discrepancy, miscalibration or nonstationarity; adding more fit parameters may reduce training error without improving predictive science. Residual plots should retain time order to reveal drift.

## 6. Posterior predictive checks and reproducibility

Generate predicted observables from posterior draws and compare with held-out experimental distributions. State whether spectra are deterministic simulations, stochastic posterior samples or actual measurements. Archive the inference seed, code version, priors, raw data, calibration and convergence diagnostics. For MCMC, effective sample size, divergent transitions and independent chains matter more than a plot that merely looks Gaussian.

## End-of-chapter questions and explanations

### Question 1. What reveals non-identifiability before fitting?

<details><summary>Read the explained answer</summary>

Multiple parameter directions with near-zero Jacobian singular values or equivalent forward predictions.

</details>

### Question 2. When is a Poisson likelihood preferable?

<details><summary>Read the explained answer</summary>

For photon-count observations where count statistics are relevant and Gaussian approximation is poor.

</details>

### Question 3. Why is a tight posterior not automatically accurate?

<details><summary>Read the explained answer</summary>

An incorrect likelihood or overconfident prior can make a biased conclusion look precise.

</details>

### Question 4. What does a small Fisher eigenvalue imply?

<details><summary>Read the explained answer</summary>

Poor local information about the corresponding parameter combination and large possible estimator variance.

</details>

### Question 5. Why fit on one dataset and test on another?

<details><summary>Read the explained answer</summary>

Independent holdout predictions expose overfitting, nuisance compensation and physical-model discrepancy.

</details>

### Question 6. What does smoothing do to error bars?

<details><summary>Read the explained answer</summary>

It changes the noise covariance and creates correlations, so raw independent-noise error models may no longer apply.

</details>

## Applied learning exercise

Write a fully specified, species-independent experiment proposal for a plausible system. Identify microscopic states, interaction Hamiltonian or rate model, detector observable, units, calibration, expected signal scale, failure controls and validation benchmarks. Use at least one independent source to challenge the expected model. An illustrative calculation is never a substitute for a completed experimental measurement.

## References and next steps

See [the master bibliography](../REFERENCES.md), Gallagher's *Rydberg Atoms*, Foot's *Atomic Physics*, and relevant NIST/open research reviews. State which source supplies each parameter before it is used in a real experiment.
