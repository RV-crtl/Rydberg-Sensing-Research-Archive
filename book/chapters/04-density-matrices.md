# Density matrices and open quantum systems

*General graduate reference · original educational exposition · no project-specific data used as universal physics.*

## Learning goals

Develop the physical and mathematical background to derive a model, choose observables, test its limiting cases and recognise invalid numerical results. Prerequisites: complex numbers, linear algebra, calculus and SI units. See the [scholarly bibliography](../REFERENCES.md).

## 1. Ensembles and positivity

A density operator ρ=∑pk|ψk⟩⟨ψk| represents an ensemble. It obeys ρ=ρ†, Trρ=1 and ρ≥0. The spectral decomposition of a density matrix expresses it as nonnegative eigenvalue weights, but there can be many other ensemble decompositions of the same physical state. Pure states satisfy Trρ²=1; mixed states generally have lower purity. Populations are diagonal matrix elements in a specified basis and coherences are off-diagonal elements. A population-only rate model cannot generally describe phase-sensitive electromagnetically induced transparency.

## 2. Derivation of coherent density evolution

Differentiate ρ=|ψ⟩⟨ψ| and substitute iℏ∂t|ψ⟩=H|ψ⟩. The result is dρ/dt=−i[H,ρ]/ℏ, where [H,ρ]=Hρ−ρH. The commutator conserves trace and purity. An energy offset proportional to identity does not alter ρ, explaining why absolute energy reference drops out of isolated coherent dynamics. For an optical ladder, different laser couplings create coherences across the relevant states, and their interference can profoundly change probe absorption.

## 3. Lindblad dissipators without hand-waving

A Markovian completely positive master equation adds D[L]ρ=LρL†−(L†Lρ+ρL†L)/2. For spontaneous decay |e⟩→|g⟩ at population decay rate Γ, choose L=√Γ|g⟩⟨e|. Then excited population decays at Γ, while optical coherence typically acquires Γ/2 from that channel. Pure dephasing may suppress coherences without redistributing populations. Be careful about packages that express line widths as half-widths, full widths, angular frequency or cycles per second. A model can be numerically stable and still be physically wrong if dissipators are assigned to the wrong states.

## 4. Stationary solutions, uniqueness and trace constraints

Steady state solves Lρ=0 together with Trρ=1. The Liouvillian superoperator has a zero eigenvalue in a trace-preserving dynamics, but there can be multiple stationary states if the graph is disconnected or preserves a nontrivial invariant subspace. A solver must impose trace independently and should report the residual of the original equation. To check physicality, evaluate the minimum eigenvalue, Hermiticity error and trace error. Small negative eigenvalues may arise from numerical roundoff; larger violations signal an invalid model or numerical failure, not an invitation to clamp the solution silently.

## 5. From atomic coherence to optical transmission

The macroscopic polarisation at the probe frequency is proportional to atomic number density times a transition dipole expectation, often related to ρge. Susceptibility χ follows only after applying the correct dipole normalisation and optical frequency convention. Propagation through a medium depends on the complex refractive index; absorption and phase are distinct observables. A raw coherence plotted against laser detuning is *not* yet an oscilloscope voltage, nor does it include finite optical depth, cell windows, photodetection, beam geometry or servo drift. Distinguish susceptibility, normalised absorption, transmission fraction and calibrated volts in plot titles.

## 6. Thermal averaging and physical rates

A warm vapour contains atoms with velocity v distributed approximately by Maxwell–Boltzmann statistics. Each beam experiences Doppler shifts from k·v, with sign dictated by beam propagation, so a two-photon resonance retains residual Doppler sensitivity when wavelengths differ. Transit broadening depends on beam size and thermal velocity, blackbody transitions couple nearby Rydberg levels and can shorten effective lifetime, and collisions or optical pumping may introduce state-changing rates. Add each mechanism with a justified independent parameter, then perform velocity-grid and truncation convergence tests.

## 7. Worked matrix example

For ρ=[[0.7,0.2],[0.2,0.3]], trace is one, purity is 0.7²+0.3²+2×0.2²=0.66, and eigenvalues are approximately 0.7828 and 0.2172, hence physical. Completely dephase off-diagonal elements while preserving populations: ρ′=diag(0.7,0.3), purity falls to 0.58. A Z-basis measurement sees no change, while an X-basis measurement loses its original coherence-dependent bias. The example shows that incoherent ensembles with the same populations can have different spectroscopic responses.

## 8. A validation ladder for any optical Bloch code

Start with a two-level analytic limit. Add a third state and show the optical-coupling-off limit. Verify positivity, trace and residual at each detuning. Increase truncation until line shapes converge. For a thermal cell, double the Doppler quadrature resolution and report both the velocity span and convergence difference. When using a solver package, record its version, detuning units, decoherence conventions and exact state graph. Only after the physical observable is calibrated against independent data should a fitted RF field be described as a measurement.

## End-of-chapter questions and fully explained answers

### Problem 1. What are the basic physical conditions on ρ?

<details><summary>Reveal the solution</summary>

Hermiticity, positivity and unit trace. Purity is an additional diagnostic of whether a state is mixed.

</details>

### Problem 2. Why does a pure-dephasing jump alter EIT?

<details><summary>Reveal the solution</summary>

It damps coherence needed for interference, potentially destroying transparency even when level populations change little.

</details>

### Problem 3. How can a steady state fail to be unique?

<details><summary>Reveal the solution</summary>

Disconnected or symmetry-protected subspaces can support multiple stationary density matrices; inspect the Liouvillian nullspace.

</details>

### Problem 4. Why is Imρge not automatically equal to photodetector current?

<details><summary>Reveal the solution</summary>

One must calculate susceptibility, propagate the optical field and include detector responsivity, amplification and calibration.

</details>

### Problem 5. How does a Doppler integral differ from adding a constant linewidth?

<details><summary>Reveal the solution</summary>

It averages detuning-dependent responses over physical velocity classes, potentially yielding non-Lorentzian profiles.

</details>

### Problem 6. Why does coherence decay at Γ/2 in simple spontaneous emission?

<details><summary>Reveal the solution</summary>

A population-decay jump attenuates the excited-state amplitude at half the population rate, yielding a Γ/2 optical-coherence damping contribution.

</details>

### Problem 7. What are minimum numerical checks for a solver?

<details><summary>Reveal the solution</summary>

Trace, Hermiticity, positivity, Liouvillian residual, convergence versus basis truncation and the relevant analytic limits.

</details>

### Problem 8. Why must the temperature be specified in a Rydberg lifetime calculation?

<details><summary>Reveal the solution</summary>

Blackbody-induced transitions and thermal populations depend on temperature, so an isolated radiative lifetime need not be the effective experiment lifetime.

</details>

## Advanced practical assignment

Implement a minimal self-contained version of the chapter's central equation. Supply its units, analytic limiting cases, a second independent check, and a reproducible test that fails when a sign or unit is changed. Distinguish generated illustrations from laboratory data. Explain how the model would be extended to a specific atomic species *only after* those foundations are correct.

## References

Use [F1] Foot, [Q1] Scully and Zubairy, [F2] Steck's Quantum and Atom Optics and the numerical analysis sources in [the bibliography](../REFERENCES.md). Consult original primary publications before reusing a parameter as experimental evidence.
