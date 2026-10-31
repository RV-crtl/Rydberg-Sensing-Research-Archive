# Thematic research literature review and gap map

This synthesis is an index to the **original structured-review text** and **paper bibliography**—not a claim that all possible papers or a requested multi-thousand-paper survey have been independently checked. For exact citations, use [the preserved review](../../literature/structured-literature-review-source.txt) and [the manuscript bibliography](../../papers/manuscript-source/ieee_references.tex). Do not invent DOI/title combinations or attribute unpublished project observations to an external source.

## 1. Rydberg-EIT RF electrometry and atomic receivers

**Question:** How does a resonant microwave electric field perturb ladder-EIT probe transmission? Fundamental work addresses a 780 nm probe, 480 nm coupling, Rydberg resonance, Autler–Townes splitting, density-matrix optical susceptibility and SI-traceable RF field strengths. Relevant measurement complications include laser stability, line-width, saturation, vapor conditions and RF-source calibration.

**Project use:** Established physical rationale for the Rb-87 cell and photodetector, low-GHz microwave search and an atomic receiver. See [lab setup](../laboratory/OPTICAL_AND_ATOMIC_RECEIVER.md) and [atomic modelling](../software/ATOMIC_MODELLING_AND_WORKBENCH.md).

**Gap addressed:** Scalar RF sensitivity is insufficient to infer an unknown 4D Stokes vector without enough independent polarisation-sensitive observables.

## 2. Magnetic quantisation and vector selectivity

**Question:** Can applied magnetic bias, optical pumping and selection rules separate the components of incident RF polarisation? Relevant literature includes Zeeman splitting, Δm pathways, quantisation-axis control, RF π/σ± coupling, field homogeneity and lock-in readout.

**Project use:** Early single-coil/Helmholtz thinking, ARC/Rydiqule state calculations, low-GHz transition search and evaluation of bias feasibility.

**Scientific boundary:** A calculated or anticipated Zeeman separation is not an observed polarimetry channel. The research moved to RF-preconditioned multi-state analyser design as a more independently calibratable measurement basis.

## 3. RF antennas, conventional polarimetry and Stokes recovery

**Question:** What references allow S0, S1, S2, S3 to be determined from independent analyser settings? Review Jones calculus, Stokes/Poincaré representation, Mueller matrices, linear/CP antenna calibration, axial ratio, extinction and finite signal-to-noise.

**Project use:** The steel-rod linear grid gave an experimental linear reference; 0°/45°/90° rotation gave equator information; circular/elliptical states motivated independent S3 sensitivity.

**Gap addressed:** Linear-only rotation cannot identify S3. The inverse problem requires rank-four independent measurements with sufficient gain and conditioning, not just a display of a sphere.

## 4. Engineered RF surfaces and chiral metasurfaces

**Question:** How can PCB copper motifs generate polarisation-selective transfer and local field enhancement while satisfying the atom-cell aperture and fabrication envelope? Survey metallic strip grids, split-ring/chiral/omega resonators, bilayer coupling, PIN/varactor switching, low-loss substrate selection and incidence-angle effects.

**Project use:** Linear grids, spiral/CP selectors, X-BSR, SAP18B, TetraVia–Omega and the selected two-face split-loop analyser.

**Gap addressed:** A strongly polarising individual surface may provide nearly redundant measurement states, weak circular leverage or poor finite-aperture transfer. The selected objective measures the information geometry of the *complete analyser state set*.

## 5. Full-wave electromagnetic methods and reproducibility

**Question:** Which simulated RF quantities actually support polarisation reconstruction? Relevant methods include periodic Floquet ports, driven finite structures, two independent complex Jones excitations, spatially averaged local E-fields, S-parameters, field interpolation, convergence, alternative mesh adaptation and source-data provenance.

**Project use:** Native Ansys HFSS as primary numerical evidence; MATLAB/CST for design precursors. The V44 archive retains machine-verifiable downstream data and return bundles.

**Gap addressed:** Local fields at the rubidium-cell volume and a periodic far-field transmission coefficient need not have the same handedness/discrimination. A single solver residual criterion is not proof of phase-sensitive matrix convergence.

## 6. Inverse design, estimation and measurement information

**Question:** Given m analyser states, how should states, gain and dwell time be chosen for stable four-coordinate inversion? Important tools are singular values, rank, condition number, Fisher information, fixed-time design, physically allowable Stokes states and finite-panel calibration transfer.

**Project use:** Six-state 6×4 instrument matrix, candidate/states screening, condition-focused optimiser, periodic and finite comparisons, information-aware dwell allocation.

**Gap addressed:** Rank-four matrices with near-zero smallest singular value are mathematically invertible but poor sensors. Gain-aware estimation can differ from row-normalised conditioning.

## 7. Implementation, manufacturing and research infrastructure

**Question:** What does an electromagnetic proof of principle require before becoming a measured receiver? Topics include RF PCB stack-up, two-faced copper alignment, etched feature repeatability, diode parasitics/bias, coaxial/antenna calibration, laser safety, data acquisition, dataset standards and reproducible software environments.

**Project use:** Constraint-aware CAD and gerber planning, hardware BOM, comparison of 70×50 mm ROI to 200 mm PCB, source-preserving automated HFSS runners, first-stage Rydberg Workbench prototype.

## Research contribution boundary

The defensible current claim is a **simulation-backed, information-aware design and numerical verification of a reconfigurable microwave measurement basis compatible with a Rydberg atomic receiver**. The originality lies in geometry/state selection, full Stokes observability and quantitative numerical verification under stated assumptions; it is not a statement that a complete physical atomic full-Stokes analyser was demonstrated.

## Adding bibliography evidence

For every new study, enter full citation and DOI; wavelength/RF regime; apparatus and material; observable; scalar/vector/Stokes capability; simulation vs experiment; reported error/limits; reproducibility assets; relation to the current project; and a concise critique. Verify publisher metadata and permissions before importing PDFs. See [literature index](../research/LITERATURE_MAP.md) for additional prior context.
