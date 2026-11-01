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


---

## Extended metrology and statistical inference tutorial

This is an advanced, general-purpose guide for spectroscopy, RF electrometry, cold-atom control, Rydberg quantum simulators and optical readout. It explains the bridge between a physically calculated signal and a defensible scientific result. It is not a replacement for instrument calibration, institutional quality assurance or independent peer review.

## 1. The difference between a theoretical curve and data

A theory maps a vector of physical parameters θ and controlled settings x into a predicted observable μ(x,θ). A real experiment records y under a distribution of measurement errors and nuisance parameters φ. The complete model is thus a likelihood p(y|x,θ,φ), not simply y=μ. A calibrated state density or electric field estimate requires both the physical transfer function and the statistical model of the detector. Repeated measurements of an uncalibrated observable do not automatically make the estimated electric field accurate.

For example, an optical Rydberg sensor may predict a probe coherence ρge(Δ,Ωc,ΩRF). The photodiode records volts after optical propagation, responsivity, gain, baseline offsets and detector filtering. A parameter such as ΩRF can influence that voltage, but the field estimate requires a calibrated atomic dipole and coupling convention, laser detuning, optical depth, RF polarisation and electronics. If two parameter combinations generate the same optical trace, no numerical optimiser can uniquely identify both without external information.

The first task in an uncertainty analysis is to list all variables controlling the observable and distinguish: **known controls**, **calibrated nuisance quantities**, **scientific parameters of interest**, and **latent unmeasured states**. A coherent likelihood should represent uncertainty where it originates rather than hiding all uncertainty in one additive residual.

## 2. Common likelihoods and what they physically assume

For a calibrated analog photodetector sampled with approximately Gaussian additive noise, one may write y_i∼N(μ_i(θ),σ_i²). If the noise has shared laser drift, use a covariance matrix Σ rather than diagonal independent variances. The Gaussian log likelihood contains (y−μ)^TΣ⁻¹(y−μ)/2, plus the log-determinant normalisation. Using a diagonal Σ when noise is strongly correlated overstates the information gained from repeated samples.

For photon/ion arrival counts with independent events and negligible dead-time effects, a Poisson model N_i∼Poisson(λ_i(θ)) can be appropriate. In real imaging systems, background counts, exposure variations, thresholding and atom loss may violate this simple assumption. Treating counts as continuous Gaussian data when only a handful of events are observed can yield asymmetric or even physically negative intervals.

For a binary trapped-atom fluorescence classification, a Bernoulli/binomial likelihood with preparation and readout confusion probabilities may be needed. If the observed “bright” fraction includes a false-bright probability f_b and false-dark probability f_d, the observed bright probability is p_obs=(1−f_d)p_true+f_b(1−p_true), assuming a simple two-class confusion matrix. An uncorrected bright fraction is not automatically the Rydberg population.

## 3. Derive the Fisher information before optimising a measurement

For a parameter θ and likelihood p(y|θ), Fisher information is F(θ)=E[(∂θ ln p)^2], or the appropriate matrix of expected score outer products. Under independent Gaussian observations of known constant variance σ_i², F=Σ_i (∂μ_i/∂θ)^T(∂μ_i/∂θ)/σ_i². If μ=Aθ and covariance Σ is fixed, F=A^TΣ⁻¹A. The Cramér–Rao bound gives a local covariance lower bound F⁻¹ for unbiased estimators under regularity conditions and invertibility.

These conditions matter. Noise that depends on θ contributes additional Fisher terms; correlated noise modifies Σ; an estimator can be biased; and a poorly identified model can have singular F. A computed Fisher improvement under an idealised noise distribution is a theoretical design metric, not automatically a measured sensitivity improvement.

For a vector field, there may be several physical parameters beyond the four Stokes coordinates. The measurement matrix could be rank four yet the total physical model remains nonidentifiable because unknown gain and field amplitude are confounded. A separate calibration or reference can turn an unidentifiable model into an identifiable one.

## 4. Singular-value analysis and experiment design

Linearise the forward model near a reference: μ(θ+δθ)≈μ(θ)+Jδθ with Jacobian J=∂μ/∂θ. The singular values of the noise-whitened Jacobian Σ^(-1/2)J reveal locally weak parameter directions. A small singular value means a perturbation in some combination of parameters creates little detectable change. Repeating the same observation may increase information along existing directions, but cannot create a missing one. An additional measurement with a different atomic state, detuning, time point, magnetic field or polarisation can add an independent row and resolve the degeneracy.

A good experiment-design objective should state what is optimised: determinant of F (D-optimal volume), trace of F⁻¹ (A-optimal uncertainty), largest eigenvalue of F⁻¹ (worst-case criterion), or an application-specific weighted loss. An optimum can change dramatically if the assumed nuisance uncertainties or signal gains change. Report the chosen objective and sensitivity to uncertain assumptions.

## 5. Bayesian inference without magical certainty

Bayesian inference combines a likelihood and a prior: p(θ|y)∝p(y|θ)p(θ). Priors may encode physically known constraints such as positive rates, finite beam waists, and calibrated magnetic field bounds, but cannot rescue a fundamentally uninformative experiment without affecting the conclusion. Report how posterior results change under reasonable alternative priors. A narrow posterior may reflect a narrow prior rather than high experimental information.

Posterior predictive checks compare replicated data under the inferred model to actual measured residual structure. If simulated posteriors reproduce mean line shape but not scan-direction hysteresis, drift or peak asymmetry, the model is incomplete. MCMC convergence diagnostics, effective sample sizes and chains matter if sampling is used; an optimiser that returns a maximum a posteriori estimate is not by itself a full uncertainty calculation.

An observable can also be nonidentifiable through parameter symmetries. For an ideal two-level system with no external phase reference, changing a drive sign may leave a measured population trace unchanged. A prior that arbitrarily selects a sign does not constitute experimental sign sensitivity; a phase-sensitive reference or additional observable is needed.

## 6. A practical uncertainty-budget example

Assume an ideal resonant two-level RF angular Rabi rate Ω=μE/ℏ, and estimate field E=ℏΩ/μ using independently calibrated Ω and dipole μ. For small independent relative uncertainties, (σE/E)²≈(σΩ/Ω)²+(σμ/μ)². Thus a 2% relative uncertainty on Ω and 3% on μ produce √(0.02²+0.03²)=3.61% relative uncertainty on E. This excludes detuning, polarisation projection, systematics, correlations and frequency-scale conventions.

If Ω and μ estimates are correlated, the relative covariance term enters with a minus sign because μ is in the denominator: Var(lnE)=Var(lnΩ)+Var(lnμ)−2Cov(lnΩ,lnμ). Ignoring covariance can either exaggerate or underestimate field uncertainty. For nonlinear inversions near a weak signal, first-order propagation may fail and a Monte Carlo/posterior analysis is preferable.

## 7. Calibration transfer and validation

Calibration is a physical relationship between an instrument output and a reference. It needs a valid operating range and uncertainty, not simply a fit on convenient input states. If a RF analyser is calibrated at one frequency, beam profile, atom position or polarisation, transfer to another condition must be tested. A matrix fitted using one electromagnetic mesh and inverted on simulated data generated by the same mesh can show almost perfect “reconstruction,” but this is algebraic self-consistency. The test of transfer is to hold out independently computed or measured states, with model discrepancies preserved.

For a finite microwave device, local complex E fields vary spatially. If the detector integrates over a cell volume, one point-sampled Jones vector may be an invalid replacement. Model the actual observation weight in a volume integral, propagate phase correctly and compare finite models or independent measurements. A numerical field simulation is not by itself a calibration of atomic optical response.

## 8. Design a decision-quality research experiment

Begin by stating the decision: accept or reject a transition, validate a polarisation basis, choose a trap spacing, measure a field, demonstrate a gate. Predefine the smallest physically meaningful effect, the nuisance quantities that can mimic it, and an external reference. Choose settings to distinguish competing hypotheses rather than to maximise the prettiest plotted signal. Register a control/holdout plan, stop criteria and raw data storage before large data collection.

For iterative model development, separate a training dataset, a validation dataset for design decisions and a final holdout test. The precise statistical design can differ for physical experiments where resources are scarce, but the principle remains: parameter tuning and performance assessment should not rely on the exact same information without a correction. Preserve negative results and the original acceptance threshold.

## 9. Twelve solved and conceptual exercises

<details><summary>1. If two independent relative errors are 2% and 3%, what is their quadrature total?</summary>

√(0.02²+0.03²)=0.03606, or 3.61%. This propagation is first order and assumes independent uncertainty components.

</details>
<details><summary>2. Why is 1000 times the same identical signal not the same as 1000 independent measurement bases?</summary>

Repeats can reduce variance along the existing sensitivity direction but do not change the rank of the Jacobian. Independent bases change the parameter dependence and can resolve nonidentifiability.

</details>
<details><summary>3. For y=Aθ with two parameters, A=[[1,1],[2,2]], can θ be uniquely reconstructed?</summary>

No. The second row is twice the first, rank(A)=1. Any change (δ,−δ) leaves y unchanged. A new independent measurement is needed.

</details>
<details><summary>4. What is the Fisher information for the mean μ of one Gaussian observation with known variance σ²?</summary>

Fμμ=1/σ², because ∂μ ln p=(y−μ)/σ² and E[(y−μ)²]=σ². For n independent observations, F=n/σ².

</details>
<details><summary>5. What changes if all observations share an unknown common offset?</summary>

That offset acts as a nuisance parameter, and the effective information for the desired physical parameter may decrease; include it in the model or calibrate independently. Treating common offset drift as independent zero-mean noise is incorrect.

</details>
<details><summary>6. Why can an uninformative spectrum yield a narrow Bayesian posterior?</summary>

A restrictive prior can dominate the posterior. Sensitivity to reasonable alternative priors and posterior predictive checks must be shown before claiming data-driven precision.

</details>
<details><summary>7. A detector registers 120 counts against mean background 20. Is the raw signal exactly 100 with zero error?</summary>

No. Subtracting a measured or estimated background introduces uncertainty from both signal counts and background estimate, and detector dead-time/readout effects may matter. Use an appropriate count model.

</details>
<details><summary>8. What is the first check when two parameter-fit algorithms return different linewidths?</summary>

Verify they use the same line-shape definition, units, detector baseline, noise likelihood, data weighting and parameter constraints. A different FWHM/decay-rate convention can explain disagreement without new physics.

</details>
<details><summary>9. Can a rank-four Stokes matrix still make S3 unmeasurable in practice?</summary>

Yes. If its S3-sensitive singular direction has negligible absolute gain relative to noise or is unstable to calibration transfer, physical estimation may be impractical despite algebraic full rank.

</details>
<details><summary>10. What does a positive covariance between lnΩ and lnμ do to Var(lnE) for E∝Ω/μ?</summary>

It reduces the first-order variance through −2Cov(lnΩ,lnμ), provided the covariance is correctly estimated. The sign matters and must not be dropped.

</details>
<details><summary>11. Why should a calibration be tested on changed conditions?</summary>

A fitted calibration may fail under altered frequency, temperature, geometry, position, time or detector gain. Independent conditions reveal transfer errors that same-condition algebra cannot.

</details>
<details><summary>12. What is the distinguishing feature of an empirical discovery rather than a good simulation?</summary>

Independent, calibrated observation that meets predeclared acceptance and uncertainty criteria, with raw evidence and reproducible controls. A simulation may be scientifically important but supports a different claim.

</details>

## Further reading

S. M. Kay, *Fundamentals of Statistical Signal Processing: Estimation Theory*; Gelman et al., *Bayesian Data Analysis*, CRC Press; Golub and Van Loan, *Matrix Computations*; JCGM 100:2008 measurement uncertainty, https://www.bipm.org/en/committees/jc/jcgm/publications ; Scully and Zubairy, *Quantum Optics*. Consult [the book's annotated references](../REFERENCES.md).
