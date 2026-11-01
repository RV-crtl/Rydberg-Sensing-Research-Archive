# Rydberg blockade and interacting-atom Hamiltonians

**Graduate reference volume:** many-body. **Scope:** species-agnostic fundamentals; assumptions and equipment conditions must be specified before applying any formula. [Reference index](../REFERENCES.md).


![Two-atom blockade scale and interaction criterion, original conceptual physics drawing](../../site/assets/book-rydberg-blockade.svg)

*Original scientifically labelled illustration; pedagogical geometry rather than acquired atomic data.*

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


---

## Extended interacting-atom and many-body laboratory design

This self-contained reference is applicable to cold clouds, optical tweezer arrays, cavity-assisted systems and deliberately engineered many-body simulators. It is not a claim that a particular laboratory has implemented these experiments.

## 1. Why isolated-atom intuition eventually fails

For one atom, a microwave or optical field connects internal states through dipole matrix elements. For two excited Rydberg atoms, their huge electric multipole moments introduce an interaction energy that depends on separation, orientation, selected quantum states, electric and magnetic fields, and nearby pair-state resonances. A two-atom basis must include states of both atoms, and exchange symmetry can become essential. “Large dipole” is therefore an incomplete predictor of blockade; the actual interaction eigenstructure can change sign or magnitude near Förster resonances.

In the perturbative van der Waals regime one often writes V(R)=C6/R^6; near a resonant dipole-dipole channel the characteristic scaling may instead resemble C3/R^3. Neither power law is universal across all states, angles and separations. A good calculation reports the state manifold, pair-state defects, total angular-momentum projections, field and the minimum R at which its truncation remains reliable.

## 2. Derive a useful blockade criterion

Suppose the target state |rr⟩ is detuned from independent double excitation by interaction energy V(R). Let the single-atom drive have angular rate Ω, and compare |V|/ℏ with Ω. If |V|/ℏ≫Ω, simultaneous excitation becomes off-resonant: the system is in a blockade regime under the model. The conventional blockade radius solves |V(Rb)|/ℏ≈Ω; for V=C6/R^6 this gives Rb≈(|C6|/(ℏΩ))^(1/6). A sixth-root dependence means a hundredfold interaction coefficient change increases Rb by only 100^(1/6)≈2.15 under otherwise equal assumptions.

This is a screening radius, not a measured device acceptance metric. A real two-qubit gate must consider leakage, finite excitation bandwidth, motional Doppler effects, spontaneous decay, differential AC Stark shift, technical phase errors and state preparation and measurement (SPAM). If the blockade is marginal over the tails of the motional distribution, a mean-distance calculation overstates robust performance.

## 3. The coherent two-atom Hamiltonian

For identical resonantly driven atoms, consider basis {|gg⟩,|gr⟩,|rg⟩,|rr⟩}. Under a coherent drive applied to each atom, the Hamiltonian includes separate σx terms and an interaction shift V|rr⟩⟨rr|. The symmetric single-excitation state |W⟩=(|gr⟩+|rg⟩)/√2 couples to |gg⟩ with a √2-enhanced collective Rabi amplitude, whereas the antisymmetric combination is dark to a uniform in-phase drive. This simple fact predicts the expected enhancement in the ideal strongly blockaded two-atom limit.

A model that predicts the same oscillation period as a single atom in the perfectly uniform blockade limit may have omitted the collective coupling or used a different Ω definition. Before running a many-body simulator, diagonalise this 4×4 example analytically or numerically. Add decay only after its coherent limit passes.

## 4. Förster channels and angular structure

A near-degenerate pair-state manifold such as |nℓ,nℓ⟩↔|n'ℓ',n''ℓ''⟩ can make the interaction stronger than a single far-detuned C6 fit predicts. Its energy defect depends on state quantum defects, external fields and magnetic projections. “Tuning the Förster resonance” is therefore a separate experimental problem from changing the optical drive: field control and calibration become part of the target Hamiltonian.

Angular dipolar interactions contain a factor proportional to (1−3cos²θ) in a simple aligned classical picture. Around the “magic angle” cos²θ=1/3, that particular term vanishes. However, a full quantum pair-state interaction is tensorial and can retain other channels; a single magic-angle argument cannot prove that all Rydberg interactions disappear.

## 5. Single-atom addressing and experimental workflow

To make a tweezer array, define trapping wavelength, target atom species, optical waist, depth, loading rate, imaging cycle and steering/rearrangement strategy. Rydberg states often experience different trap potentials from ground states. Whether traps are extinguished during excitation changes both motion and AC Stark detuning; the pulse sequence must record that fact.

Calibrate trap spacing using a physical length standard and imaging scale. Calibrate single-site Rabi rates and differential detunings before a multi-site gate. Run Ramsey and spin-echo sequences to separate coherent detuning from irreversible decoherence, then measure the pair blockade response versus R and angle. The final result should contain an uncertainty model for readout and losses; postselection can artificially inflate a quoted fidelity if atoms that were lost are excluded.

## 6. Validation for many-body simulation

A constrained Rydberg spin Hamiltonian may be expressed as H/ℏ=Σ_i Ω_i σ_i^x/2−Σ_i Δ_i n_i+Σ_{i<j} V_ij n_i n_j/ℏ. For small N, exact diagonalisation provides a reference. As N grows, the Hilbert space dimension 2^N rapidly becomes prohibitive, and approximate methods become necessary. A valid approximation should report its truncation, conserved symmetries, convergence and independent small-N comparison.

Observables include Rydberg density, excitation correlations g2(R), blockade signatures, entanglement witnesses and dynamical structure factors. None is interchangeable with “gate fidelity.” A high-contrast correlation image may coexist with preparation errors or laser drift. For every quantity, define whether it is measured site-by-site, inferred from fluorescence, or reconstructed using a model.

## 7. A system-development gate structure

**Gate 1: atomic feasibility.** Choose actual Rydberg states, optical access, lifetimes and field tolerance; verify energies through ARC and published spectroscopy.

**Gate 2: optical source quality.** Demonstrate linewidth, frequency tuning, phase stability and addressing uniformity against the intended operation time.

**Gate 3: isolated-atom dynamics.** Recover single-site coherent and decoherence limits; calibrate detection and loss.

**Gate 4: interaction verification.** Measure a distance-dependent pair response and compare to an angularly resolved pair-state calculation.

**Gate 5: multi-atom task.** Define a specific gate or simulation observable and quantify its state-preparation, readout, leakage, drift and modelling errors.

**Gate 6: reproducibility.** Share sufficient code, calibration and original data under appropriate institutional permissions so the result can be independently checked.

Do not advance from Gate 2 to a claimed quantum-advantage result purely because an idealised Hamiltonian numerically produces an entangled state.

## Twelve graduated problems and answers

<details><summary>1. Derive the van der Waals blockade-radius dependence on C6 and Ω.</summary>

From |C6|/Rb^6=ℏΩ, rearrange to Rb=(|C6|/(ℏΩ))^(1/6). The result assumes a single effective isotropic interaction and that this equality is the chosen threshold.

</details>
<details><summary>2. What happens to Rb if Ω increases by a factor of 64 while C6 stays fixed?</summary>

Rb scales as Ω^(-1/6), so it decreases by 64^(-1/6)=1/2.

</details>
<details><summary>3. Why is the collective |gg⟩↔|W⟩ drive enhanced?</summary>

Two indistinguishable paths excite atom 1 or atom 2. For equal coherent phases, the amplitudes add, producing √2 enhancement relative to a single path for the normalized symmetric state.

</details>
<details><summary>4. Is the antisymmetric single-excitation state always dark?</summary>

No. It is dark to an exactly uniform, equal-phase drive under the simple identical-atom model. Unequal phases, Rabi strengths, detunings or symmetry-breaking couplings can drive it.

</details>
<details><summary>5. Why can a simple C6/R6 model fail near a Förster resonance?</summary>

The perturbative elimination of nearby pair states becomes invalid when the pair-state energy defect approaches the dipole-dipole coupling. Diagonalise the coupled pair manifold instead.

</details>
<details><summary>6. Is θ≈54.7° proof of no interaction?</summary>

Only a particular aligned dipolar tensor component vanishes in the simple model. Additional quantum channels, angular momentum mixing and higher multipoles can remain.

</details>
<details><summary>7. Why should ground-state trap loading and Rydberg excitation be calibrated independently?</summary>

Poor loading changes the observed atom count even when excitation is perfect, while excitation errors can occur with fully loaded traps. Combined signals cannot isolate the two without independent controls.

</details>
<details><summary>8. A two-atom model predicts perfect blockade but the measured correlation is weak. What should be tested first?</summary>

Verify actual trap spacing, state labels, Rabi bandwidth, field drift, atom loss and detection errors; test whether the chosen pair interaction manifold yields the expected V(R).

</details>
<details><summary>9. How can site-selective light shift mimic an interaction-induced shift?</summary>

A local intensity-dependent detuning varies with site and preparation sequence. Run independent single-site controls with the same illumination and no Rydberg neighbour excitation.

</details>
<details><summary>10. Why must exact diagonalisation be used before approximating a large spin array?</summary>

Small-N solutions are a reference to detect state-order, sign and energy-unit mistakes; an approximate method's output alone lacks that independent numerical anchor.

</details>
<details><summary>11. A published gate excludes all lost atoms in postprocessing. What must be reported?</summary>

Both conditional performance and unconditional success including loss, with explicit SPAM, postselection and survival definitions. Otherwise cross-platform comparisons are misleading.

</details>
<details><summary>12. Why is a strongly interacting atomic state not automatically a useful sensor?</summary>

It must encode the target parameter into a measurable observable with sufficient Fisher information under realistic preparation, decoherence and readout costs. Strong interaction alone establishes neither high bandwidth nor low uncertainty.

</details>

## References

Gallagher, *Rydberg Atoms*; Browaeys and Lahaye, *Many-body physics with individually controlled Rydberg atoms*, Nature Physics **16**, 132–142 (2020), https://doi.org/10.1038/s41567-019-0733-z ; Saffman, Walker and Mølmer, *Quantum information with Rydberg atoms*, Reviews of Modern Physics **82**, 2313–2363 (2010), https://doi.org/10.1103/RevModPhys.82.2313 ; ARC interaction/PerturbativeC6 documentation https://arc-alkali-rydberg-calculator.readthedocs.io/en/latest/ .
