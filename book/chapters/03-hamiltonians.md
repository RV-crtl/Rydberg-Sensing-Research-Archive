# Hamiltonians, rotating frames and coherent control

**General atomic and quantum physics textbook.** The treatment is not a project-specific apparatus description. Physics constants and state labels must be verified for each chosen species.

## Learning objectives

Derive the central equations, quantify assumptions, compute a simple limiting case, plan an independent experiment and diagnose numerical or laboratory errors.

## 1. The interaction Hamiltonian

Begin with H=H0−d·E(t). The dipole moment d is an operator; its matrix elements connect allowed atomic states according to angular-momentum selection rules. In a two-state rotating-wave model, H/ℏ can be written as (−Δσz+Ωσx)/2 after specifying basis order, phase and detuning sign. The Rabi frequency Ω is an angular rate in rad/s when H is divided by ℏ. A rotating frame changes coordinates but cannot change physical probabilities.

## 2. Where the RWA comes from

Expanding E0cos(ωt+φ) into exponentials produces near-resonant and counter-rotating terms. Transforming to a frame rotating with the laser reveals one slowly varying component and another rotating near twice the carrier. Neglect of the fast term is justified only if drive and detuning are sufficiently small compared with carrier frequency. Ultrastrong coupling, rapid modulation and Floquet-assisted Rydberg spectroscopy may require retaining counter-rotating dynamics.

## 3. Exact Rabi oscillations

For an atom initially in the lower state, P_e(t)=(Ω²/(Ω²+Δ²))sin²(√(Ω²+Δ²)t/2). The probability's first maximum is at t=π/√(Ω²+Δ²), not necessarily π/Ω; its height is reduced when Δ≠0. If Ω/2π=2 MHz and Δ/2π=1 MHz, the maximum is 0.8. A textbook calculation is not a measured time-domain Rydberg coherence; spontaneous decay, Doppler effects and finite atom motion may change the result.

## 4. Three-level coherence and dressed states

EIT and coherent population trapping arise from interference between excitation pathways. In an idealised lambda system a dark state proportional to Ωc|g⟩−Ωp|r⟩ decouples from a shared excited state at two-photon resonance. A ladder EIT system has its own decay and state structure; do not assume all lambda-system formulas transfer unchanged. Adding an RF-coupled fourth state modifies the dressed eigenvalues and can generate Autler–Townes features under suitable linewidth conditions.

## 5. Numerical propagation and error checks

For time-independent H, U(t)=exp(−iHt/ℏ) is unitary. For H(t), time-ordering is required if H at different times does not commute. Explicit integration must converge with step size, preserve norm in the closed limit and recover Ω→0, Δ→0 and far-detuned limits. When adding dissipation, transition to a density-matrix/Lindblad solver instead of manually renormalising a decaying wavefunction without a physical model.

## 6. Design and diagnosis

Build a drive-frequency/state diagram and write the actual sign of each complex coupling. Check selection rules, numerical angular-frequency conversions, phase references and branch choice. A simulated avoided crossing is not an experimental field calibration; spectroscopy requires independent frequency and detector controls.

## End-of-chapter review questions and worked answers

### Question 1. What is the difference between Ω and Ω/2π?

<details><summary>Show explained solution</summary>

Ω is angular frequency in rad/s, while Ω/2π is cycles/s; mixing them creates an erroneous 2π.

</details>

### Question 2. Why does RWA fail for sufficiently strong RF?

<details><summary>Show explained solution</summary>

Counter-rotating terms no longer average away and may modify energies or sidebands.

</details>

### Question 3. How much transfer occurs for Δ=Ω/2?

<details><summary>Show explained solution</summary>

Maximum transfer is Ω²/(Ω²+Ω²/4)=0.8.

</details>

### Question 4. Can a three-state dark vector predict a full thermal spectrum?

<details><summary>Show explained solution</summary>

No; dissipative dynamics, Doppler classes, density and optical propagation must be added.

</details>

### Question 5. Which identity tests a propagator?

<details><summary>Show explained solution</summary>

U†U=I to numerical tolerance in a closed system.

</details>

### Question 6. Why are relative phases meaningful?

<details><summary>Show explained solution</summary>

Coupled pathways interfere and their relative phases determine coherent probabilities.

</details>

## Graduate practical problem

Develop a reproducible calculation for the principal equation in this chapter, record coordinate frame and units, compare against a separate source or an analytically solvable limit, and describe a controlled measurement that could falsify the model. Explicitly distinguish a derived teaching example from new experimental evidence.

## Scholarly sources

See [the textbook bibliography](../REFERENCES.md), Gallagher (*Rydberg Atoms*), Foot (*Atomic Physics*), Scully and Zubairy (*Quantum Optics*), and official atomic spectroscopy data when applying formulas to an actual species.
