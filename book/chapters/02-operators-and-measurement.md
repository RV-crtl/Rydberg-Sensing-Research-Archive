# Operators, observables and quantum measurement

**General atomic and quantum physics textbook.** The treatment is not a project-specific apparatus description. Physics constants and state labels must be verified for each chosen species.

## Learning objectives

Derive the central equations, quantify assumptions, compute a simple limiting case, plan an independent experiment and diagnose numerical or laboratory errors.

## 1. Spectral theorem and eigenprojectors

Every finite-dimensional Hermitian observable A admits a spectral decomposition A=∑a_kP_k. Projectors P_k are positive, mutually orthogonal and sum to identity. The probability of outcome k is Tr(ρP_k), and expectation is Tr(ρA). Degeneracy changes the rank of P_k, not the Born rule. Measuring a single basis is generally informationally incomplete: many different coherences yield the same populations. Distinguish a microscopic quantum observable from the measured macroscopic signal, which includes a detector and a forward model.

## 2. Noncommuting observables and uncertainty

The commutator [A,B]=AB−BA determines the Robertson bound ΔAΔB≥|⟨[A,B]⟩|/2. The full Schrödinger uncertainty relation includes covariance and is stronger in many states. The bound is state dependent and should not be confused with classical sampling uncertainty or optical detector noise. One may have very precise technical frequency estimation without preparing an energy eigenstate, because the measurement can integrate coherent signals from many atoms.

## 3. Generalised measurements and loss

Positive operator-valued measures E_k≥0, ∑E_k=I describe detectors with outcomes that need not correspond to orthogonal projections. A finite-efficiency photon detector can be modelled through a calibrated response and losses; including dark counts or saturation may require an extended classical likelihood. An uncalibrated optical current is not an atom state probability. Always state where the atomic model ends and the detector model begins.

## 4. Uncertainty propagation and Fisher information

For an observation y=f(θ)+ε, local parameter sensitivity is J=∂f/∂θ. If ε is Gaussian with covariance C, the local Fisher matrix is F=JᵀC⁻¹J when C is parameter independent. F being invertible is not sufficient for a useful estimator if one eigenvalue is tiny. Spectral noise density has units per square-root bandwidth for amplitude noise and must be integrated through the actual filter; correlations invalidate naive sample-count scaling.

## 5. A worked two-level statistics example

For ρ=diag(0.7,0.3), a σz measurement has mean 0.4, second moment 1 and variance 0.84. If 1000 independently re-prepared atoms are measured, standard deviation of their average is √(0.84/1000)=0.02898. If 1000 recorded detector samples share laser drift, this number is not valid. An honest estimate measures autocorrelation or effective sample size and includes systematic calibration separately.

## 6. Measurement design checklist

Identify whether the desired output is a quantum probability, classical current, phase, spectral frequency or inferred field. Choose a primary physical control, a calibrated detector reference and an independent second measurement basis if phase or vector information is required. Preserve original shots and timestamps, not only an averaged graph. Do not interpret a model's minimum variance as measured sensitivity before testing with laboratory noise.

## End-of-chapter review questions and worked answers

### Question 1. What makes E_k a valid POVM effect?

<details><summary>Show explained solution</summary>

It is positive semidefinite, and all effects sum to identity.

</details>

### Question 2. Why is a single projection basis incomplete?

<details><summary>Show explained solution</summary>

Off-diagonal phases may not affect its populations but change predictions in another basis.

</details>

### Question 3. Does Robertson uncertainty specify the photodiode noise floor?

<details><summary>Show explained solution</summary>

No, it constrains state-observable variances, not electronic or laser noise.

</details>

### Question 4. How does correlation change averaging?

<details><summary>Show explained solution</summary>

Shared noise reduces effective independent sample number, weakening the 1/√N scaling.

</details>

### Question 5. What determines whether F is useful?

<details><summary>Show explained solution</summary>

Its eigenvalues in the calibrated noise and parameter-unit metric, not invertibility alone.

</details>

### Question 6. Why is measurement calibration a model component?

<details><summary>Show explained solution</summary>

Physical states map to voltages or counts through finite efficiency, gain, bandwidth and backgrounds.

</details>

## Graduate practical problem

Develop a reproducible calculation for the principal equation in this chapter, record coordinate frame and units, compare against a separate source or an analytically solvable limit, and describe a controlled measurement that could falsify the model. Explicitly distinguish a derived teaching example from new experimental evidence.

## Scholarly sources

See [the textbook bibliography](../REFERENCES.md), Gallagher (*Rydberg Atoms*), Foot (*Atomic Physics*), Scully and Zubairy (*Quantum Optics*), and official atomic spectroscopy data when applying formulas to an actual species.
