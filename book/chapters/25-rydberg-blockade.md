# Rydberg blockade and interacting-atom Hamiltonians

**Graduate reference volume:** many-body. **Scope:** species-agnostic fundamentals; assumptions and equipment conditions must be specified before applying any formula. [Reference index](../REFERENCES.md).

## Competencies

Derive the basic model, assess approximations, calculate limiting cases, select suitable numerical methods and design a falsifiable experimental check.

## 1. The physical mechanism

A pair of atoms is blockaded when an atom excited to a Rydberg state shifts the doubly excited pair state far enough off resonance that a second resonant excitation is strongly suppressed. The basic two-atom states include |gg⟩, |gr⟩, |rg⟩ and |rr⟩. Resonant drive couples these states while interaction contributes V(R)|rr⟩⟨rr|. In the strongly blockaded symmetric subspace the singly excited bright state (|gr⟩+|rg⟩)/√2 couples collectively to |gg⟩ at enhanced √2 Ω, while antisymmetric dark states may be inaccessible for symmetric illumination. The blockade is finite, frequency-dependent and susceptible to positional and excitation inhomogeneity.

## 2. Dipole–dipole versus van der Waals interactions

Two Rydberg atoms interact through dipole–dipole coupling Vdd=[d1·d2−3(d1·Rhat)(d2·Rhat)]/(4πε0R³). At sufficiently large detuning from Förster resonance, second-order perturbation leads to effective van der Waals shifts C6/R^6. Near resonant pair manifolds, a simple C6 fit may fail because the interaction is nonperturbative, anisotropic and state dependent. Zeeman and Stark fields alter the channel structure and angular couplings. ARC pair-state interaction routines should be used to identify the actual eigenstates and potential curves before relying on a single coefficient.

## 3. Defining the blockade radius

A frequently used scale satisfies |V(Rb)|≈ℏΩeff, with the precise criterion depending on protocol and acceptable double-excitation error. For a van der Waals law and known C6, Rb≈(|C6|/(ℏΩeff))^(1/6). This is a *scale*, not a hard boundary: double excitation is continuously suppressed with detuning and finite linewidth. If Ω doubles and C6 is fixed, Rb shrinks by 2^(−1/6), about 11 percent. Laser dephasing and motional spread change effective blockade in experiments.

## 4. Quantum gates and simulation

A Rydberg controlled-phase gate uses conditional shifts to accumulate phase on one two-qubit basis state. A neutral-atom array can implement Ising-like models with laser drive Ω, detuning Δ and Rydberg number operators n_i: H/ℏ=∑(Ω_iσx_i/2−Δ_i n_i)+∑V_ij n_i n_j/ℏ. Spatial geometry, state preparation, coherent control, readout and inhomogeneous detuning define actual simulator fidelity. Benchmark single-atom Rabi oscillations, pairwise blockade, crosstalk and then collective dynamics; do not infer gate fidelity solely from a strong theoretical V(R).

## 5. Calculating realistic pair spectra

ARC computes single-atom energies and pair-interaction matrices under specified angular-momentum truncations. Record n, l, j, m_j, quantisation axis, B/E fields, pair separation and angle, basis cutoffs, laser coupling and signs. Test convergence with both principal-quantum-number range and angular channels. A divergent or discontinuous C6 near a resonant pair state can be a sign to diagonalise the coupled pair manifold rather than an ARC software error.

## 6. Failure modes and quantitative readout

Poor blockade can arise from too-large spacing, wrong pair-state near-resonance, stray DC electric field, polarization leakage, optical frequency noise, laser intensity variation and finite Rydberg lifetime. Double-excitation probability must be corrected for imperfect state detection and atom loss. An apparent spatial anti-correlation is not automatically entanglement; witness or state-tomography methods and detector calibration are needed.

## End-of-chapter questions and answers

### 1. Why does the symmetric state have an enhanced Rabi frequency?

<details><summary>Reveal the explained answer</summary>

Two indistinguishable excitation pathways add coherently, producing a √2 enhancement of the coupling amplitude.

</details>

### 2. Why is Rb not a physical brick-wall boundary?

<details><summary>Reveal the explained answer</summary>

Suppression is continuous and depends on interaction shift relative to drive, linewidth and acceptable error.

</details>

### 3. When is C6/R^6 inadequate?

<details><summary>Reveal the explained answer</summary>

Near Förster resonances, strong state mixing or angularly dependent avoided crossings.

</details>

### 4. What does doubling Ω do to blockade radius at fixed C6?

<details><summary>Reveal the explained answer</summary>

Rb scales as Ω^(−1/6), so it is reduced by a factor 2^(−1/6).

</details>

### 5. What must be recorded for a two-atom interaction calculation?

<details><summary>Reveal the explained answer</summary>

Atomic states, separation, relative angle, fields, interaction basis and truncation convergence.

</details>

### 6. Can suppression of double excitation alone prove entanglement?

<details><summary>Reveal the explained answer</summary>

No. Correlations can be classical or detector-induced; additional quantum-state evidence is needed.

</details>

## Investigation and research methods exercise

Select a published state or apparatus, list its degrees of freedom, write the microscopic Hamiltonian or master equation, and specify an actual measured observable. Compute a limiting case and compare against a separate numerical or experimental check. Document units, versions, control measurements and credible failure modes. A simulation is not automatically a new laboratory result.

## Further study

Gallagher, *Rydberg Atoms*; Foot, *Atomic Physics*; the ARC and RydIQule documentation; and the modern research reviews in the [bibliography](../REFERENCES.md). Figures are original or sourced with permission; no textbook diagrams have been copied.
