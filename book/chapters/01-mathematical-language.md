# The mathematical language of quantum science

*General graduate reference · original educational exposition · no project-specific data used as universal physics.*


![A fully coherent two-level state represented by its Bloch-sphere angles (original educational diagram)](../../site/assets/book-quantum-bloch.svg)

*Original scientifically labelled illustration; pedagogical geometry rather than acquired atomic data.*

## Learning goals

Develop the physical and mathematical background to derive a model, choose observables, test its limiting cases and recognise invalid numerical results. Prerequisites: complex numbers, linear algebra, calculus and SI units. See the [scholarly bibliography](../REFERENCES.md).

## 1. What a quantum state actually represents

In a complex Hilbert space the state |ψ⟩ is a unit vector up to a physically irrelevant common phase. For |ψ⟩=a|g⟩+b|e⟩, |a|²+|b|²=1 and measurement in the {|g⟩,|e⟩} basis produces probabilities |a|² and |b|². Complex amplitudes are not the same as the measured voltage from a detector. Relative phase changes interference in a rotated basis, while multiplying both amplitudes by e^{iφ} does not change an expectation value. One should distinguish a pure state, the state vector used to represent it, and a classical ensemble in which the same apparatus prepares different states on different runs.

## 2. Dirac notation and the Born rule

A ket |ψ⟩ is a column vector and its bra ⟨ψ| is the conjugate transpose. An inner product ⟨a|b⟩ describes overlap; it is generally complex. For a normalized projector P=|a⟩⟨a|, the probability of its outcome is ⟨ψ|P|ψ⟩=|⟨a|ψ⟩|². The identity resolution ∑_i |i⟩⟨i|=I holds for a *complete orthonormal* basis. It does not hold for an arbitrary set of nonorthogonal candidates. Real optical experiments acquire ensemble fluorescence or probe transmission, not single-state Born-rule outcomes directly. A forward optical model is needed between microscopic state and macroscopic data.

## 3. Basis rotations, phase and polarisation

A unitary U satisfies U†U=I; it transforms state coordinates as |ψ⟩new=U†|ψ⟩ and observables as Anew=U†AU. Expectations are unchanged, which is a valuable software regression test. For light or RF fields the Cartesian (x,y) basis and the spherical (π,σ±) basis are different coordinate descriptions of the same vector, with helicity sign determined by propagation and time convention. A phase error of π/2 can interchange a linear and circular basis inference. Write down the transformation explicitly before passing complex field components between optical Bloch, atomic-dipole and antenna codes.

## 4. Linear algebra for inverse science

The singular value decomposition A=UΣV† is defined for a rectangular matrix and reveals which parameter combinations are invisible or ill-conditioned. Rank identifies whether a noiseless solution can be unique; a small σmin controls amplification of some perturbations. A numerical condition number only has meaning after declaring units, column scaling and weighting. A transfer matrix mapping incident polarisation into an optical detector does not automatically become a quantum measurement operator. Distinguish the physical process from the numerical instrument-response linearization.

## 5. Calculus and coherent evolution

For a time-independent Hermitian Hamiltonian H the propagator is exp(−iHt/ℏ); its Taylor series involves matrix powers, not element-by-element exponentials. A diagonal Hamiltonian gives each energy eigencomponent a phase exp(−iEjt/ℏ), and interference depends on differences Ej−Ek. For a time-dependent H(t), a single exponential of its integral is invalid unless the Hamiltonians commute at different times. A numerical integrator should preserve norm in a genuinely closed system. Unit-normalised output can still be physically wrong if a time step misses rapid micromotion or if an angular frequency was supplied as cycles/s.

## 6. Statistics and uncertainty with real laboratory data

An average reduces independent, zero-mean noise, but it does not remove systematic calibration error. The sample standard deviation describes scatter; the standard error describes uncertainty of the estimated mean, and a naive 1/√N law fails for serially correlated laser scans. Covariance matters when the same frequency lock, temperature monitor or reference power affects several data channels. Record detector bandwidth and readout gains before comparing datasets. A photodetector output, atomic state variance and RF-field inference uncertainty are three different quantities.

## 7. Worked derivation and numerical checks

Let |ψ⟩=(|0⟩+i|1⟩)/√2. Measuring Z gives p(0)=p(1)=1/2. The Y-basis eigenstate |+y⟩=(|0⟩+i|1⟩)/√2 has overlap 1 and the opposite eigenstate has overlap zero, so ⟨σy⟩=1. Multiply |ψ⟩ by i and repeat: all probabilities stay unchanged. Now replace i with −i; Z-basis probabilities are still equal, but ⟨σy⟩=−1. Thus population measurements in a single basis cannot determine relative phase. Verify all calculations with explicit 2×2 Pauli matrices and complex conjugation in code.

## 8. Experiment-to-model checklist

Before a calculation: (1) state the physical observable and acquisition chain; (2) define your basis, signs and units; (3) write at least one analytically solvable limit; (4) test a change of coordinates; (5) check numerical conservation laws; (6) vary step size or discretisation; (7) record dependencies and raw inputs; (8) distinguish a simulation, measurement and algebraic illustration. These checks apply to virtually every Rydberg apparatus, from Stark spectroscopy to tweezer-array blockade.

## End-of-chapter questions and fully explained answers

### Problem 1. Why can no single-basis population measurement recover relative phase?

<details><summary>Reveal the solution</summary>

It squares amplitudes independently. Phase appears in interference terms once a noncommuting measurement basis mixes them.

</details>

### Problem 2. Which numerical method identifies weakly observable parameters in a six-by-four instrument matrix?

<details><summary>Reveal the solution</summary>

Singular-value decomposition, together with a declared noise metric and column scaling.

</details>

### Problem 3. What changes under a global phase e^{iφ}?

<details><summary>Reveal the solution</summary>

State-vector representation changes but all density matrices and measurement probabilities remain unchanged.

</details>

### Problem 4. Why can a good-looking fit have an invalid uncertainty?

<details><summary>Reveal the solution</summary>

Errors may be correlated, the model may be biased, and fit residuals may violate the assumed likelihood.

</details>

### Problem 5. What is an essential unit check on a Hamiltonian?

<details><summary>Reveal the solution</summary>

All matrix entries must represent the same physical quantity, typically joules or ℏ times angular frequency.

</details>

### Problem 6. Why do inverse-problem condition numbers depend on scaling?

<details><summary>Reveal the solution</summary>

Rescaling parameters or observations changes singular values and their ratio; dimensioned variables must be normalized meaningfully.

</details>

### Problem 7. What must hold for a closed-system numerical propagator?

<details><summary>Reveal the solution</summary>

It should be approximately unitary and preserve the norm of every input state, with errors controlled by a stated tolerance.

</details>

### Problem 8. How can one test a basis transform implementation?

<details><summary>Reveal the solution</summary>

Compute an observable in both frames and show numerical invariance of its expectation under consistent state and operator transformations.

</details>

## Advanced practical assignment

Implement a minimal self-contained version of the chapter's central equation. Supply its units, analytic limiting cases, a second independent check, and a reproducible test that fails when a sign or unit is changed. Distinguish generated illustrations from laboratory data. Explain how the model would be extended to a specific atomic species *only after* those foundations are correct.

## References

Use [F1] Foot, [Q1] Scully and Zubairy, [F2] Steck's Quantum and Atom Optics and the numerical analysis sources in [the bibliography](../REFERENCES.md). Consult original primary publications before reusing a parameter as experimental evidence.
