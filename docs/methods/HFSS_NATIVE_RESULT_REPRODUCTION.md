# HFSS native-source export, paper reconstruction and provenance playbook

## Source priority and scope

The authoritative electromagnetic observations in the later paper derive from **Ansys HFSS**; MATLAB/Python calculations *use* the exported complex fields for Jones/Stokes/singular-value analysis. A derived array is not a second independent HFSS run. Preserve the solver's native project/results where available and **never introduce synthetic noise, manufacturing tolerance or unmeasured experimental variations as mandatory substitutes** for solver evidence.

## Stage A — geometry and solver release manifest

Record the CAD project filename / SHA-256; AEDT and PyAEDT versions; design-family ID; cell/board dimensions; material name and exact thickness/εr/tanδ; copper thickness/face and switch-mask truth table; whether switches are ideal conducting bridges or actual RLC/PIN package models. Record frequency range and exact discrete samples, polarisation bases, incidence angle, port integration line/normal, near-field cell position, outer boundary/PML/Floquet, mesh generation method and convergence limits.

Distinct branch examples: earlier 70×50 mm **RO4003C** folded resonator, 200 mm-class **RO4350B** metasurface and 43 mm-class two-face split-loop unit cell. These must not share an undifferentiated parametric-project identity.

## Stage B — source excitation and complex export

For each switch/mask and frequency, solve both independent incident Jones basis excitations with a **known consistent phase reference**. Export complex electric field components Ex/Ey (and Ez where local atomic orientation matters) at matched x,y,z sample coordinates. Store original real/imaginary components, not magnitude-only plots. If using S21/S11, retain complex S-parameters and physical port normalisation; also store near-field maps when the atomic signal depends on local E rather than a far-field transmitted plane wave.

A valid source observation record includes: state, frequency, excitation, x/y/z coordinates, field units, complex component units, mesh ID, solver run ID, project hash, timestamp and file checksum.

## Stage C — build Jones and Stokes instrument response

Construct the two-excitation complex response for each mask at the declared spatial ROI. Define the local quadratic field observation or projected optical-coupling functional and derive the real Stokes measurement row. Maintain a fixed S3 sign/handedness convention and consistent gain/area weighting. Stack the rows into the selected six-by-four matrix. Only from that exact matrix compute singular values, rank, row-normalised κ₂, absolute gain and any fixed-budget information criterion.

A model that has rank four but tiny σmin or negligible S3 leverage does not automatically deliver usable physical estimation. For other frequencies, use **those frequency-specific complex fields**, not a copy of the matrix at 1.925 GHz.

## Stage D — independent mesh and finite panel

Run an independently adapted mesh using changed mesh settings or independent converged refinement, then compare complex fields/matrices on the *same physical sample coordinates* using a stated norm. Contrast each state, not only a favourable aggregate result. Ensure report percentage disagreement means the same metric for every figure. Document periodic Floquet and finite 3×3 separately; local E-field phase/response can change with panel boundary, illumination and depth.

Historical screens included rank-four yet poorly conditioned or mesh-sensitive solutions. The later periodic reference reported rank four and row-normalised κ₂ ≈9.53 at 1.925 GHz with a selected independent-mesh discrepancy ≈0.551%. Finite-array calibration transfer is a separate, qualified result; the reported full-vector median errors at certain 5 mm cross-calibration cases in historical manuscript generations were substantial (~32.9% and ~82.6% depending on direction) and must not be silently suppressed or generalised to other test cases.

## Stage E — frozen paper evidence

The current paper-centred V44 archive contains:

- A bounded 36-candidate geometry screening record; a sampled accepted interval of 250 MHz vs 175 MHz in a comparison design;
- source HFSS field/matrix and mesh exports plus analysis scripts;
- a six-state matrix represented as [V42_C033_INSTRUMENT_MATRIX.csv](../../papers/manuscript-source/data/V42_C033_INSTRUMENT_MATRIX.csv);
- fixed-duration information calculations in [V44_FIXED_BUDGET_RESULTS.json](../../evidence/hfss/v44-reproducibility/analysis/V44_FIXED_BUDGET_RESULTS.json);
- original figure and source-provenance mapping.

These findings are tied to model version and input source files. Any new figure should record its generating script, inputs/hashes, parameter values and plotting choices. See [figure provenance](../results/FIGURE_PROVENANCE.md).

## Stage F — launch, failure and return package

Use one Windows launcher for the configured AEDT installation; log solver/version at start; continue sequential stages automatically; stop only on a genuine failure or essential inspection; write human-readable status and structured JSON verdict; collect all native projects, result directories, complex field exports, plots, CSVs, analysis matrices and the exact logs into a single return ZIP. A ZIP labelled “FINAL” is not a solver-completion certificate: verify its cases, field counts, source hashes and passed gates.

Avoid duplicating huge earlier runner/return packages inside ordinary Git. Prefer original unmodified archive plus its SHA-256 and a slim, reproducible derived set. A patch ZIP must be linked to the base version it modifies.

## Acceptance and scientific interpretation checklist

- [ ] Solver project and parameter set available, or correctly marked missing
- [ ] Six states, both complex basis excitations, all tested frequency samples preserved
- [ ] Units, phase conventions and sample ROI coherent
- [ ] Source hashes, solver mesh and independent adaptation recorded
- [ ] Rank, σmin, κ₂, gain, S3 leverage and frequency band separately calculated
- [ ] Finite-array and periodic matrices reported separately
- [ ] All plots recreate from the source data or are explicitly illustrative
- [ ] Results correctly described as HFSS-derived, not atomically measured
- [ ] Returned ZIP is readable, self-describing and complete under the run manifest

**Start with:** [HFSS SOP](HFSS_SOP.md) · [campaign lineage](../simulations/HFSS_CAMPAIGN_LINEAGE.md) · [V44 source archive](../../evidence/hfss/v44-reproducibility/) · [simulation study](../simulations/VERIFICATION_AND_INFORMATION_MATRIX.md).
