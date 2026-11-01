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


## Extended derivation: interference from complex amplitudes

A complex number is not an optional decoration on a classical probability. Its phase determines how alternative quantum pathways combine. Suppose a system admits two alternative coherent paths from its initial state to a final measurement state, contributing amplitudes a₁ and a₂. The probability is |a₁+a₂|²=|a₁|²+|a₂|²+2Re(a₁a₂*). The final interference term is absent from the classical sum of two exclusive probabilities. Therefore adding probabilities prematurely destroys experimentally observable relative-phase effects. When laser-induced coherence and microwave-induced coupling participate in a Rydberg spectroscopic feature, this distinction is central: the optical probe signal can respond to phase-sensitive atomic coherences, even though the final photodetector output is real.

Take a₁=1/2 and a₂=e^{iφ}/2. Then the interference probability is (1+cosφ)/2, varying from 0 to 1 as relative phase changes. Multiplying both amplitudes by the same e^{iθ} leaves this probability unchanged. An optical intensity measurement is often insensitive to the overall optical phase, whereas a heterodyne measurement with a known reference can convert a relative phase into a detected intensity oscillation. Identifying what is measurable requires specifying the reference, not simply writing a complex state.

## Extended derivation: uncertainty and compatible measurements

For Hermitian A and B, define centred operators ΔA=A−⟨A⟩ and ΔB=B−⟨B⟩. Cauchy–Schwarz applied to ΔA|ψ⟩ and ΔB|ψ⟩ yields ΔA²ΔB²≥|⟨ΔA ΔB⟩|². The imaginary part of this covariance is ⟨[A,B]⟩/(2i), yielding the Robertson lower bound ΔAΔB≥|⟨[A,B]⟩|/2. This lower bound can be zero even for noncommuting operators when the particular state makes the expected commutator zero; a zero bound does not imply all observables can be known sharply in that state.

For spin-1/2, [σx,σy]=2iσz. In an eigenstate of σz with eigenvalue +1, the variances of σx and σy both equal one, saturating the spin-form bound ΔσxΔσy≥1. But an experimental detector's output voltage may have far larger variance due to electronic and environmental noise, and calibration uncertainty is a separate systematic component. Do not label all observed noise “quantum uncertainty.” In practice, shot noise, projection noise, laser phase noise and classical technical noise require different likelihood models.

## Extended derivation: change of basis without changing physics

Let the computational basis be |g⟩=(1,0)^T and |e⟩=(0,1)^T. Define |+⟩=(|g⟩+|e⟩)/√2 and |−⟩=(|g⟩−|e⟩)/√2. The unitary whose columns are these new basis states is U=(1/√2)[[1,1],[1,−1]]. To represent the same physical state in the new coordinates, use |ψ⟩new=U†|ψ⟩. The operator must transform consistently as Anew=U†AU. The expectation ⟨ψ|A|ψ⟩ is then invariant because U U†=I. Transforming the state but not the operator produces spurious dependence on software basis ordering.

A numerical regression test should choose a random normalised state, a Hermitian observable and a known unitary, then check expectation invariance within tolerance. Repeat with a complex rotation, not only a real matrix, so a missing conjugation is caught. The same reasoning becomes crucial for atomic spherical bases: a field written in laboratory x/y components does not directly determine q=±1 coupling strengths until it is transformed relative to the magnetic quantisation axis.

## Extended derivation: density operators as probabilities over preparations

A source that produces state |ψₖ⟩ with classical probability pₖ is represented by ρ=Σₖpₖ|ψₖ⟩⟨ψₖ|. For any observable A, the ensemble mean is Tr(ρA). A different ensemble decomposition can produce the same ρ and is therefore indistinguishable using only measurements on the system. This is a crucial identifiability limit: what a model calls its constituent “preparations” need not be uniquely inferred from the measured optical response.

For a two-level system, ρ=(I+r·σ)/2 with real Bloch vector r and |r|≤1. A pure state has |r|=1 and Tr(ρ²)=1; the maximally mixed state has r=0 and purity 1/2. A fitted Bloch vector with norm above one implies a nonphysical state unless the reported quantities are not actually normalised Bloch coordinates. This mathematical physicality test can be applied before any specific atomic species is introduced.

## Extended derivation: forward and inverse problems

Suppose a system maps unknown parameter θ to measured data y through y=f(θ)+ε. A forward model predicts y for a known θ. An inverse model estimates θ given y. In general f may not be one-to-one. If two parameter sets produce the same observable, no amount of noiseless repetition can distinguish them without an additional measurement basis or prior restriction. In linear form y=Aθ, full column rank is necessary for unique noiseless inversion. Even when rank is complete, singular values close to zero make inversion unstable.

This has two distinct implications for Rydberg systems. First, an optical spectrum may depend on combinations of RF amplitude, detuning, linewidth and atomic density; fitting one spectrum can therefore produce correlated parameters. Second, spatially and polarisation-resolved measurements may require multiple independent configurations before a vector field can be recovered. A clever optimiser cannot create information absent from the forward map. A researcher should inspect parameter identifiability through a Jacobian ∂f/∂θ or a physically motivated Fisher matrix and then design new measurements to resolve the weak directions.

## Unit discipline and dimensional reasoning

Every numerical routine should decide whether the state evolution Hamiltonian is expressed in joules, angular frequency rad/s or cycle frequency Hz. If H is in joules, iℏd|ψ⟩/dt=H|ψ⟩. If the reduced Hamiltonian H/ℏ is in rad/s, its eigenvalues are angular rates. A detuning reported as 10 MHz often means Δω=2π×10⁷ rad/s, but a software package may instead define internal detunings in multiples of 2π MHz or scaled units. The correct procedure is to inspect official documentation, trace the conversion and test a known Rabi period.

Dimensional consistency is an inexpensive but powerful diagnostic. The matrix element dE has dimensions (C·m)(V/m)=J. Dividing by ℏ gives s⁻¹ (angular frequency), while dividing by h gives Hz. A reported coherence time is not a frequency; its inverse has frequency dimensions, with numerical π/2 factors depending on how linewidth is defined (amplitude decay, population decay, FWHM). Using generic “gamma=1” values without units prevents a reproducible line-shape prediction.

## Further extended exercises

<details><summary>Q9. Two coherent paths have amplitudes 0.3 and 0.4 e^{iφ}. Find the probability for φ=0 and φ=π.</summary>

For φ=0, P=|0.7|²=0.49. For φ=π, P=|−0.1|²=0.01. Adding separate probabilities would give 0.09+0.16=0.25 and miss interference. These amplitudes may be components of an outcome within a larger normalised state; their total is not automatically a complete measurement probability distribution.

</details>

<details><summary>Q10. Compute the purity of a diagonal qubit state with probabilities 0.8 and 0.2.</summary>

Tr(ρ²)=0.8²+0.2²=0.68. Because the purity is below one, it is mixed. A different physical classical preparation may produce the same density operator.

</details>

<details><summary>Q11. Transform σz into the |+⟩,|−⟩ basis.</summary>

Using the Hadamard U above, U†σzU=σx. The state coordinates must also transform. Computing the same expectation in both bases gives equal values.

</details>

<details><summary>Q12. Explain why a measured 10 MHz line splitting is not automatically a Rabi angular rate of 10 million rad/s.</summary>

The frequency splitting is in cycles/s. If the simple resonant model maps that splitting directly to Ω/(2π), Ω would be 2π×10⁷ rad/s. In an actual multilevel, Doppler-broadened atomic spectrum, the mapping must be verified and may not be exact.

</details>

<details><summary>Q13. A computed Bloch vector is (0.7,0.8,0.2). Is it physical?</summary>

Its squared norm is 0.49+0.64+0.04=1.17, exceeding one. A qubit density matrix built as (I+r·σ)/2 would have a negative eigenvalue. Inspect normalisation or inversion errors rather than clipping silently.

</details>

<details><summary>Q14. Give a concrete criterion for when an inverse model cannot uniquely identify its parameters.</summary>

If f(θ₁)=f(θ₂) for distinct admissible θ₁,θ₂, then y=f(θ) does not uniquely identify the input. For a linear model this is equivalent to a nontrivial nullspace of A: A v=0 with v≠0.

</details>

<details><summary>Q15. Why does increasing the sample count not necessarily fix a nonidentifiable experiment?</summary>

Repeating an identical measurement can reduce statistical variance but cannot resolve a missing independent response direction. Change the measurement basis, geometry, time dependence or reference observable.

</details>

<details><summary>Q16. Derive the photon energy for 780 nm and report eV.</summary>

E=hc/λ=(6.62607015×10⁻³⁴ J·s)(299792458 m/s)/(780×10⁻⁹ m)≈2.546×10⁻¹⁹ J. Divide by 1.602176634×10⁻¹⁹ J/eV to obtain ≈1.589 eV.

</details>

<details><summary>Q17. Why does a unitary basis change preserve density-matrix purity?</summary>

ρ'=U†ρU and Tr((ρ')²)=Tr(U†ρUU†ρU)=Tr(U†ρ²U)=Tr(ρ²) by unitarity and cyclic trace. A numerical purity discrepancy indicates an implementation or rounding problem.

</details>

<details><summary>Q18. What mathematical feature reveals poor parameter sensitivity near a best fit?</summary>

Small singular values of the Jacobian or a near-singular Fisher information matrix indicate directions along which the observable changes little. The precise interpretation depends on the likelihood, scaling and nuisance parameters.

</details>

<details><summary>Q19. Can a state have no intrinsic spin-uncertainty in σz and also no uncertainty in σx?</summary>

Not as a pure simultaneous eigenstate of both noncommuting Pauli operators. A σz eigenstate has a definite z outcome but an equal distribution of x outcomes; Δσx=1.

</details>

<details><summary>Q20. What independent software regression would catch a missing complex conjugation?</summary>

Compare ⟨ψ|A|ψ⟩ in two randomly chosen complex unitary bases using U† on both state and operator. A transpose in place of conjugate transpose generally breaks expectation invariance.

</details>

## Expanded references

- Foot, *Atomic Physics*, Oxford University Press, for state and measurement foundations.
- Scully and Zubairy, *Quantum Optics*, Cambridge University Press, for density operators and coherent optical interference.
- Steck, *Quantum and Atom Optics*, https://steck.us/teaching/ for detailed graduate quantum methodology.
- Golub and Van Loan, *Matrix Computations*, for rank, singular values and numerical stability.
