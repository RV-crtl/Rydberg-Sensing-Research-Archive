# Quantum defects, channel mixing and MQDT

**Graduate reference volume:** atomic theory. **Scope:** species-agnostic fundamentals; assumptions and equipment conditions must be specified before applying any formula. [Reference index](../REFERENCES.md).

## Competencies

Derive the basic model, assess approximations, calculate limiting cases, select suitable numerical methods and design a falsifiable experimental check.

## 1. Why alkali spectra are not hydrogenic

Hydrogen-like Rydberg energies scale with effective principal quantum number n*=n−δ, but electron penetration into a multielectron core changes the short-range phase shift. The quantum defect depends on orbital angular momentum, total angular momentum and sometimes energy. High-l circular states may be nearly hydrogenic, while s and p series can have large quantum defects. A fit that reproduces one manifold cannot automatically predict all spin–orbit or hyperfine split states.

## 2. From short-range phases to observed resonances

Quantum-defect theory separates short-range electron–core interactions from long-range Coulomb propagation. The asymptotic phase of an electron radial wavefunction is shifted relative to hydrogen. Bound-state energies can be written in terms of quantum defects, and continuum resonances similarly reflect the underlying scattering phases. MQDT generalises to multiple coupled channels with thresholds and interactions; closed-channel resonances can affect open-channel scattering and spectra. This framework is especially valuable near perturbations by core excitations.

## 3. Fine structure, hyperfine structure and core polarisation

A realistic alkali atom involves electron orbital and spin angular momenta, nuclear spin, relativistic corrections and polarisation of the ionic core. For high n the electron spends much of its time far from the core, but short-range penetration still shifts energies. Angular-momentum coupling bases change when external magnetic fields pass from hyperfine-dominated to uncoupled regimes. Use relevant NIST/ARC reference data rather than forcing a single empirical quantum defect across all levels.

## 4. Stark and Zeeman maps

The perturbations −d·E and μ·B couple manifolds and split degeneracies. In a strongly mixed Stark manifold, a state cannot be characterised by a single n,l,j quantum label without noting the expansion coefficients. Avoided crossings should be tracked by eigenvector overlap as well as energy ordering; a simple sort-by-energy can swap state identities between consecutive field steps. Anomalous jumps in plots may therefore be bookkeeping mistakes rather than physics.

## 5. Spectroscopy and series assignment

Fit multiple known transitions, constrain isotope and hyperfine reference, and evaluate residuals across an entire n series. Check if residual patterns correlate with n, l or j, which can reveal incorrect reference thresholds or omitted channel mixing. A quantum defect is usually inferred from levels, not measured directly by a detector. Propagate calibration of optical frequency to fitted parameters; uncertainty in the ionisation limit can correlate strongly with low-n defect coefficients.

## 6. Computational validation

In ARC, record the exact atomic model, dataset, energy units and state label. For a home-built MQDT routine, test the hydrogenic δ→0 limit, the bound-continuum threshold and orthogonality or flux conservation where applicable. Compare against an independent state table and document whether finite-precision roundoff or basis truncation dominates error.

## End-of-chapter questions and answers

### 1. Why does n*=n−δ matter for optical access?

<details><summary>Reveal the explained answer</summary>

It shifts state-specific transition wavelengths relative to hydrogen, sometimes enough to move outside an available laser tuning window.

</details>

### 2. Can δ be assumed constant for all n and l?

<details><summary>Reveal the explained answer</summary>

No. Quantum defects are manifold dependent and may vary with energy.

</details>

### 3. What makes MQDT different from a single defect fit?

<details><summary>Reveal the explained answer</summary>

It treats coupled short-range channels and thresholds, including closed-channel resonances.

</details>

### 4. Why can energy-sorting a Stark map mislabel states?

<details><summary>Reveal the explained answer</summary>

Avoided crossings exchange energy ordering while physical eigenstate composition evolves continuously.

</details>

### 5. What limit should an MQDT implementation recover?

<details><summary>Reveal the explained answer</summary>

The hydrogenic/Coulomb reference behavior as short-range channel shifts are removed.

</details>

### 6. How can spectroscopic residuals diagnose missing physics?

<details><summary>Reveal the explained answer</summary>

Systematic variation across n,l,j may reveal wrong thresholds, quantum defects, hyperfine structure or channel mixing.

</details>

## Investigation and research methods exercise

Select a published state or apparatus, list its degrees of freedom, write the microscopic Hamiltonian or master equation, and specify an actual measured observable. Compute a limiting case and compare against a separate numerical or experimental check. Document units, versions, control measurements and credible failure modes. A simulation is not automatically a new laboratory result.

## Further study

Gallagher, *Rydberg Atoms*; Foot, *Atomic Physics*; the ARC and RydIQule documentation; and the modern research reviews in the [bibliography](../REFERENCES.md). Figures are original or sourced with permission; no textbook diagrams have been copied.
