# Advanced mathematical foundations: from complex vector spaces to atomic measurement

## Tensor products and why “two atoms” is not “one atom with twice as many states”

An isolated qubit has a two-dimensional Hilbert space. For two distinguishable two-level atoms the joint space is the tensor product H_A⊗H_B and has dimension four, with basis |gg⟩,|ge⟩,|eg⟩,|ee⟩. The coefficient of a joint basis state is a complex amplitude, and the four squared moduli sum to one. In a three-atom array there are eight basis states; with N two-level atoms, dimension 2^N grows exponentially. This scaling is the first reason exact many-body simulation becomes expensive even when each atom looks simple.

A separable product state has form |ψ_A⟩⊗|ψ_B⟩. Its four amplitudes factor as products of two local amplitude vectors. A state such as |Φ+⟩=(|gg⟩+|ee⟩)/√2 cannot be written as a product: there are perfect correlations in its computational-basis statistics, but each atom alone has equal ground/excited probability. The distinction between classical correlation and quantum entanglement requires checking whether the density operator can be expressed as a mixture of product states. For pure states, nonfactorisability is sufficient to identify entanglement.

The reduced density operator of atom A is ρ_A=Tr_B(ρ_AB), where the partial trace sums over a complete basis of B. For |Φ+⟩, ρ_A=I/2, a maximally mixed single-atom state, even though ρ_AB is pure. This is not a contradiction: the local subsystem can have uncertain outcomes because it is entangled with another subsystem. A numerical implementation should test that Tr(ρ_A)=Tr(ρ_AB)=1 and preserve positivity after the partial trace. The tensor-product basis order is part of the software interface; changing it without changing operator construction can silently swap control and target atoms.

For a pair of Rydberg atoms, the state |rr⟩ acquires an interaction-dependent shift. An operator acting only on atom A has matrix A⊗I; one acting only on B is I⊗B. The pair interaction is often represented by V(R)|rr⟩⟨rr|. It must be added in the correct energy or angular-frequency units. Once these elementary operators are reliable, more complicated pair-state mixing and quantum gate pulses can be derived instead of implemented as opaque matrix entries.

## Projectors, positive operator-valued measurements and detectors

A projective measurement with orthogonal projectors P_k satisfies P_k=P_k†, P_k²=P_k and ΣP_k=I. The Born-rule probability is p_k=Tr(ρP_k). Real sensors often include inefficient, ambiguous or continuous-valued readouts that cannot be described as perfect projectors on the atomic system. A more general positive operator-valued measure (POVM) consists of positive operators E_k≥0 summing to I, with p_k=Tr(ρE_k). The operators E_k need not each be projectors.

As an illustrative state-classification detector, suppose the true bright outcome B is reported bright with probability 1−f_d, and the true dark outcome D is falsely reported bright with probability f_b. The effective bright POVM element is E_bright=(1−f_d)|B⟩⟨B|+f_b|D⟩⟨D|. If the true bright population is p, the observed bright probability is (1−f_d)p+f_b(1−p). The calibration of f_b and f_d is part of the measurement model, not a correction to be guessed after results are collected.

For optical transmission through an ensemble, the detector is usually measuring a field intensity integrated over time, optical propagation and spatial modes. A density-matrix solver computes microscopic coherences or populations; obtaining a detector voltage requires a physically justified optical susceptibility and electronics transfer. Conversely, a photoelectric voltage alone rarely gives enough information to reconstruct every microscopic atomic density-matrix component. It is a map from a high-dimensional state to a much smaller observable.

## Unitary evolution, generators and exponential matrices

The formal solution of a time-independent Schrödinger equation is U(t)=exp(−iHt/ℏ). If H is Hermitian, U†U=I and norm is preserved. This exponential can be calculated through diagonalisation when H has a reliable eigenbasis or by numerical matrix exponential methods when numerical conditioning demands it. It is generally unsafe to replace exp(A) with an elementwise scalar exponential: a matrix exponential is a power series of matrix products, exp(A)=I+A+A²/2!+….

For a simple resonant two-level Hamiltonian H=(ℏΩ/2)σ_x, use σ_x²=I to separate even and odd terms. One obtains U(t)=cos(Ωt/2)I−i sin(Ωt/2)σ_x. Starting in |g⟩, the excited amplitude is −i sin(Ωt/2), so the probability is sin²(Ωt/2). This derivation immediately exposes the angular-rate convention: a π pulse requires Ωt=π, whereas the full population oscillation period is 2π/Ω. The sign of the off-diagonal complex amplitude can matter in interference experiments even when the population trace does not.

With detuning Δ under a rotating-wave approximation, a common Hamiltonian is (ℏ/2)(Ωσ_x+Δσ_z). The generalized Rabi angular rate is Ω_eff=√(Ω²+Δ²). For an initially unexcited atom, the maximum excitation probability is Ω²/Ω_eff² and occurs at times satisfying Ω_eff t=(2k+1)π, neglecting decay. Large detuning suppresses transfer; this is a valuable limiting case for source code. The exact sign of Δ and basis ordering change the Hamiltonian representation, so independent regression tests should compare physical populations rather than just hard-coded matrix entries.

## Rotating frames and the interaction picture

A time-dependent drive can be simplified with a rotating frame. If the laboratory state is |ψ_lab⟩ and define a unitary R(t) such that |ψ_rot⟩=R†(t)|ψ_lab⟩, then H_rot=R†HR−iℏR†dR/dt. The derivative term is essential. Omitting it produces a frame-dependent prediction, which is an algebraic error rather than new physics. For a near-resonant two-level drive, this transformation isolates a slowly changing detuning and allows the rotating-wave approximation to neglect counter-rotating terms where justified.

The rotating-wave approximation requires a hierarchy: coupling and detuning small relative to optical/RF carrier angular frequencies, and no nearby counter-rotating resonance that strongly affects the observable. At strong drives or unusual spectra, Bloch–Siegert and other beyond-RWA effects can matter. A numerical comparison to the laboratory-frame Hamiltonian at increasing drive strength is a useful validation study.

When several optical or RF drives couple a multilevel atom, a consistent frame may involve a set of laser frequencies and phase conventions. Inappropriate rotating-frame choices can create artificial time dependence or apparently inconsistent detunings around closed coupling loops. Document each phase in the original lab frame, then transform systematically.

## Density matrices, commutators and relaxation

For a closed quantum system the Liouville–von Neumann equation is dρ/dt=−(i/ℏ)[H,ρ]. The commutator ensures trace preservation since Tr([H,ρ])=0. A master equation can add dissipative channels in Lindblad form: D[L]ρ=LρL†−1/2{L†L,ρ}. This structure can preserve trace and complete positivity for physical rates. Arbitrarily subtracting a linewidth from a coherence without regard to populations and positivity can create a mathematically inconsistent “decay model.”

For spontaneous relaxation of a two-level atom, use L=√Γ|g⟩⟨e|. The excited population decays with rate Γ in the absence of coherent drive. Off-diagonal coherence decays at Γ/2 in this simple model without additional pure dephasing. A separate pure-dephasing channel can suppress coherence without changing the populations. Consequently, “population lifetime,” “coherence time” and “optical linewidth” are not interchangeable experimental numbers.

A coherent optical ladder may require several such channels: intermediate-state spontaneous emission, Rydberg state decay, transit loss and perhaps laser phase diffusion. In a thermal vapour, Doppler averaging is often an ensemble average over coherent responses at different velocities; it is not always adequately represented by a single Lindblad dephasing operator. A model that reproduces a linewidth with an arbitrary scalar Γ might still be wrong about the signal's dependence on optical power or velocity geometry.

## Rotations in ordinary space versus quantum state space

A three-dimensional field vector rotates under an ordinary spatial rotation, while a spin-j atomic state rotates through the corresponding unitary representation. A Cartesian microwave field must be decomposed into spherical components relative to the quantisation axis to determine magnetic-sublevel couplings. For an axis along z, a common convention is E_{±1}=∓(E_x±iE_y)/√2 and E_0=E_z. Other sign or time conventions occur, so a scientific calculation must declare its choice.

The quantum angular-momentum ladder operators satisfy J_±|j,m⟩=ℏ√[j(j+1)−m(m±1)]|j,m±1⟩. These square-root factors are why different magnetic-sublevel transitions can have different strengths even under the same field amplitude. Selection rules identify which couplings vanish exactly in the ideal basis, but the angular coefficients determine how strongly allowed transitions are driven. The choice of magnetic field direction therefore changes which lab field component contributes to a given atomic transition.

Do not equate the photon propagation direction with the quantisation axis unless the experiment establishes that geometry. In a weak or poorly controlled bias field, the physical eigenbasis may be ambiguous or mixed. This is a substantial source of misleading circular-polarisation claims.

## Eigenvectors, avoided crossings and numerical continuity

In a slowly varied external field, a state energy can be tracked as a function of field strength. The eigenvalues of a Hermitian Hamiltonian are real, but their numerical ordering can change near crossings. If states mix, an eigenvector's label based solely on sorted energy may jump to a different physical branch. A robust Stark/Zeeman-map code should examine overlap |⟨ψ_i(B_k)|ψ_j(B_{k+1})⟩|², relevant expectation values and convergence under a larger basis.

At an avoided crossing, the minimum energy gap provides evidence of coupling between nominally crossing bare states. A gap can be resolved in theory but experimentally obscured by Doppler width, decay, probe selection rules or detector noise. The most beautiful eigenvalue diagram may therefore not correspond to an observable EIT peak. Always connect the state map to a physical excitation pathway and detection transfer function.

## A mathematical reproducibility checklist

For every piece of atomic-physics numerical software: verify basis ordering; test Hermiticity of H; verify normalisation and trace; check positivity of density operators; track Hz/rad/s; test an exact two-level limit; compare spectra under zero drive, zero detuning and large detuning; check independent state-basis truncation; include a phase-convention test; record library version and reference. Each test should fail on a deliberately introduced known error, such as a swapped matrix index or missing conjugation. A test that never fails may be a decorative test rather than protection.

## Advanced end-of-chapter questions with complete answers

<details><summary>Q21. What is the dimension of the Hilbert space of six distinguishable two-level atoms?</summary>

Each contributes a dimension-two space, so the tensor product dimension is 2^6=64. This does not count additional leakage or motional degrees of freedom, which increase the physical dimension.

</details>

<details><summary>Q22. Find the reduced state of atom A in |Φ+⟩=(|gg⟩+|ee⟩)/√2.</summary>

Form ρ=|Φ+⟩⟨Φ+|. Sum over the second atom's ground and excited basis. Cross terms vanish under the partial trace, leaving ρ_A=(|g⟩⟨g|+|e⟩⟨e|)/2=I/2. Purity of the reduced state is 1/2, although the joint state is pure.

</details>

<details><summary>Q23. Why can't a matrix exponential be evaluated elementwise?</summary>

Matrix powers in exp(A)=I+A+A²/2!+… involve products that mix entries. Elementwise exponentials omit these products and generally fail to preserve the correct unitary evolution.

</details>

<details><summary>Q24. Derive the ideal resonant π-pulse duration for Ω=2π×2 MHz.</summary>

A π pulse satisfies Ωt=π, hence t=π/(2π×2×10^6)=0.25 μs. It transfers a ground-state atom to the excited population in the ideal coherent model.

</details>

<details><summary>Q25. Why does a pure phase change sometimes alter interferometry but not population?</summary>

A common global phase cancels all observables. A relative phase between components or a phase relative to a reference beam changes interference terms while leaving certain individual basis populations unchanged.

</details>

<details><summary>Q26. What happens to population transfer if |Δ|≫|Ω| in a detuned two-level drive?</summary>

The maximum excited population approaches Ω²/Δ², which is small. The generalized oscillation frequency grows approximately as |Δ|, but the oscillation amplitude decreases.

</details>

<details><summary>Q27. What term appears in the Hamiltonian when changing to a time-dependent rotating frame?</summary>

With |ψ_rot⟩=R†|ψ_lab⟩, H_rot=R†HR−iℏR†dot R. The additional term accounts for the basis's time dependence.

</details>

<details><summary>Q28. For spontaneous decay with jump L=√Γ|g⟩⟨e| and no drive, how does ρee change?</summary>

It obeys dρee/dt=−Γρee, so ρee(t)=ρee(0)e^{-Γt}. Off-diagonal coherence decays at Γ/2 absent other dephasing channels.

</details>

<details><summary>Q29. A quantum-state solver returns purity 1.07 for a normalized two-level density matrix. What is wrong?</summary>

For a physical density matrix, Tr(ρ²)≤1. A value 1.07 is nonphysical and signals a numerical or model error, incorrect normalisation or an object that is not a density operator.

</details>

<details><summary>Q30. Why is state tracking by sorted eigenvalue alone unreliable at an avoided crossing?</summary>

Energy-ordered eigenvectors can exchange character under mixing. Overlap-based tracking and physical expectation values are needed to identify states consistently across the parameter sweep.

</details>

<details><summary>Q31. What physical assumption is required to use E_{±1}=∓(Ex±iEy)/√2 for a magnetic transition?</summary>

The quantisation axis must coincide with the declared laboratory z axis, and the spherical-basis/time convention must match the atomic matrix elements. Rotating B changes the decomposition.

</details>

<details><summary>Q32. A detector bright probability is p_obs=(1−f_d)p+f_b(1−p). Solve for true p.</summary>

Rearrange: p_obs=f_b+(1−f_d−f_b)p, giving p=(p_obs−f_b)/(1−f_d−f_b), provided the denominator is nonzero and confusion rates are calibrated. If f_b+f_d≈1, the readout becomes poorly conditioned.

</details>

## References and independent checks

Foot, *Atomic Physics* (Oxford University Press); Scully and Zubairy, *Quantum Optics* (Cambridge University Press); Steck, *Quantum and Atom Optics* <https://steck.us/teaching/>; Gallagher, *Rydberg Atoms*, DOI <https://doi.org/10.1017/CBO9780511524530>; Golub and Van Loan, *Matrix Computations*. Each derivation should be independently checked against the declared phase convention and numerical limit before being used in a published research calculation.
