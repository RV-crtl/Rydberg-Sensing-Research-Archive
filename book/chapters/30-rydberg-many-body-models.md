# Many-body Hamiltonians and quantum simulation

**Independent textbook chapter / many-body physics**. Original general treatment; no project-specific RF apparatus or HFSS case is presented as universal physics. Read [references](../REFERENCES.md).

## Learning objectives

Explain the core physical mechanism, derive a model with explicit approximations, design a falsifiable measurement, diagnose artefacts and choose validated calculation methods.

## 1. From pair blockade to a lattice Hamiltonian

An interacting Rydberg array can be modelled as two-level pseudo-spins with occupation n_i and site-dependent driving Ω_i, detuning Δ_i and interactions V_ij. In a common rotating frame, H/ℏ=∑_i(Ω_iσ_i^x/2−Δ_i n_i)+∑_{i<j}(V_ij/ℏ)n_i n_j. This is related to a transverse-field Ising model after a shift of variables, but geometry and interaction range matter. Real atoms also have leakage levels, motion, loss and detection imperfections. A six-atom exact diagonalisation may capture small-scale correlations but cannot automatically predict thermodynamic phases.

## 2. Blockade graphs and constrained Hilbert space

Define a graph connecting atom pairs with interaction shifts above a chosen cutoff. In a hard-blockade approximation, forbidden adjacent excitations are removed from the Hilbert space. The resulting constrained dynamics can yield collective oscillations and unusual relaxation. However, a graph cutoff turns a continuous potential into a binary rule; its sensitivity to cutoff and actual positions must be assessed. Near threshold, a full soft interaction can change predicted phase boundaries and defect densities.

## 3. Quenches and adiabatic preparation

A quantum quench changes Hamiltonian parameters faster than the state can adapt, creating non-equilibrium correlations. Adiabatic preparation varies detuning or drive slowly enough to follow a desired eigenstate, subject to a many-body gap that can become small with system size. Landau–Zener estimates from a single pair often underpredict errors in frustrated or large arrays. Define preparation fidelity relative to a measurable reference, and test both ramp direction and ramp speed.

## 4. Correlations and entanglement witness caution

A two-point correlation C_ij=⟨n_i n_j⟩−⟨n_i⟩⟨n_j⟩ can reveal ordering or blockade structure. It is not by itself a proof of quantum entanglement. Readout error correlations, atom loss and data post-selection can produce spurious anti-correlations. When reporting multipartite entanglement, use appropriate witnesses, calibrated measurements in noncommuting bases or more complete tomography as permitted by the apparatus.

## 5. Numerical methods and scaling

An N-spin two-level Hilbert space grows as 2^N; exact dense diagonalisation becomes intractable quickly. Sparse matrix-vector evolution is valuable for small arrays, while matrix-product-state/tensor-network methods exploit limited entanglement structure in one-dimensional settings. Mean-field and truncated-correlation approaches can handle larger systems but may miss critical fluctuations and entanglement. Compare methods on sizes where exact solutions are available, document truncation and quantify finite-size effects.

## 6. Research workflow

First validate single-atom and two-atom dynamics; then characterize 1D chains and 2D geometries under known state preparation. Measure excitation distributions, density correlations and time dependence. Maintain explicit data provenance for each gate, site geometry and imaging correction. A qualitative match between two colorful heatmaps is not a numerical convergence test.

## Review problems with full explanations

### 1. Why does exact Hilbert-space size grow as 2^N?

<details><summary>View worked reasoning</summary>

Each of N independent two-level subsystems contributes two basis choices.

</details>

### 2. What is lost in a hard blockade graph?

<details><summary>View worked reasoning</summary>

The continuous interaction strength and off-threshold double-excitation amplitudes.

</details>

### 3. Why are correlations not identical to entanglement?

<details><summary>View worked reasoning</summary>

Classical mixtures can exhibit similar number correlations; nonclassical witnesses require additional conditions.

</details>

### 4. What checks tensor-network results?

<details><summary>View worked reasoning</summary>

Bond-dimension convergence, finite-size tests and comparison with exact small-system dynamics.

</details>

### 5. Why can a fast adiabatic ramp fail near a phase transition?

<details><summary>View worked reasoning</summary>

The many-body gap can narrow so the ramp violates the adiabatic condition.

</details>

### 6. What does post-selection bias?

<details><summary>View worked reasoning</summary>

The inferred distribution when loss or state readout errors correlate with the selected outcomes.

</details>

## Design and verification assignment

Construct a research protocol for an appropriate species or platform. State what the detector measures, its model assumptions, the control experiment needed, expected scale, uncertainty sources and stopping criteria. Perform an independent computation or published-data comparison before claiming a new observation. Consult the bibliography for exact state constants and validated methods.

## Suggested source pathway

Gallagher, *Rydberg Atoms*; relevant ARC documentation and atomic spectroscopy; the NIST review of atomic electrometry (2024/2025) and field-specific primary literature. See [bibliography](../REFERENCES.md).
