
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
