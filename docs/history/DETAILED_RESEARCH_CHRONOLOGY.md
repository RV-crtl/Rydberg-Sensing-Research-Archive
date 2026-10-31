# Comprehensive research chronology (2026)

> **Evidence rule.** This timeline combines dated artefacts already preserved in this repository with milestones documented in earlier research discussions. A dated design proposal is not evidence of fabrication; a solver package name is not proof of a completed solve. Manuscript versions are editorial history, not independent experimental datasets. For verified quantities use the [key findings](../results/KEY_FINDINGS.md), [experimental report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf), [HFSS source catalogue](../results/EVIDENCE_INDEX.md), and [current editable manuscript](../../papers/manuscript-source/main.tex).

## Research phases at a glance

| Period | Research direction | Deliverables / evidence | Maturity |
|---|---|---|---|
| March–April 2026 | Feasibility, literature scoping and atomic receiver architecture | Scoping presentation; theoretical EIT/Rydberg sensing framework; project specification | Architecture and literature |
| April–June 2026 | Rubidium ladder EIT, field/polarisation calibration and magnetic-bias studies | June experimental report; optical and RF setup; early ARC/Rydiqule exploration | Physical apparatus and exploratory measurements |
| July–August 2026 | Linear polariser characterisation, atomic RF polarimetry interpretation, PCB concepts | Measured linear-angle/equator interpretation; MATLAB grids, CP/chiral cells, CST investigation | Measured linear reference; other architectures simulated/proposed |
| August–September 2026 | Manufacture-constrained RF metasurfaces and research communication | FR-4/RO4350B board studies, Gerber/SVG plans, posters, presentations | Design studies and partial demonstrations |
| September–early October 2026 | Reconfigurable analyser and end-to-end HFSS automation | SAP18B, tetrahedral/bank-switched ideas, AEDT runners and return bundles | Screening and numerical verification stages |
| Mid–late October 2026 | HFSS-native finite/periodic comparison, mesh verification, information-aware multi-state optimisation | V4xx/V5xx campaigns, V44 reproducibility package, 6×4 Stokes matrix, figures and full manuscripts | Simulation-backed research |
| Late October 2026 | IEEE Access-format manuscript, evidence alignment and handover | Editable full LaTeX project, draft PDF, supervisor rubric, figures and research handover | Manuscript draft and curated archive |

## 1. Scientific inception and rationale — March–April

The initial investigation asked whether an optically read rubidium Rydberg-atom receiver could do more than detect the magnitude of a microwave field: could it estimate or discriminate the **polarisation** of an incident RF signal? The working thesis title was **“Magnetically-biased Rydberg Microwave Receiver for Polarization Estimation.”** Early literature explored Rydberg-EIT/Autler–Townes electrometry, vector RF sensing, Zeeman-bias selection rules, atomic optical pumping, low-GHz transitions, antenna polarimetry and RF front-end calibration.

The initial engineering chain was **780 nm probe + 480 nm coupling → rubidium vapour cell → probe transmission/photodetector**, while a reference RF chain supplied known microwave states. ARC and Rydiqule were chosen for atomic structure and density-matrix feasibility work. The targeted RF region was principally around 1.8 GHz, with later higher-frequency exploration limited by laboratory readout and sources.

## 2. Experimental receiver studies — May–June

An exploratory laboratory configuration used counter-propagating optical beams and a magnetic coil near the vapour cell. A single-coil arrangement was evaluated before investigation of a more homogeneous Helmholtz approach. Magnetic biasing did not yield a sufficiently clear experimental basis for complete polarisation reconstruction. The project therefore progressively emphasised deterministic, external **RF polarisation conditioning**, which can be calibrated without treating a difficult atomic Zeeman observable as the sole information source.

A steel-rod linear polariser and wideband antennas were used for baseline RF analysis. The earlier experimental-stage report describes a roughly 23 × 23 cm, 6 mm rod / 30 mm pitch polariser, optical receiver components, instrument measurements, VNA comparisons and magnetic calibration. Some reported pass/reject contrasts are 14–15 dB under one reference configuration. Later approximately **9.7 dB** results are from a distinct measurement setup/condition: neither should be substituted for the other or represented as measured circular polarimetry. See [lab records](../laboratory/OPTICAL_AND_ATOMIC_RECEIVER.md) and [polarisation data interpretation](../laboratory/POLARISATION_MEASUREMENTS.md).

## 3. Linear basis to Stokes geometry — July–September

Linear polariser rotation experiments were interpreted on the **Poincaré equator**. Horizontal/vertical and diagonal sensitivity can constrain components of the polarisation state, but the circular coordinate S3 requires an independent handedness-sensitive observation. A future computer-estimated Stokes state cannot create missing independent information. This insight motivated multi-state measurement-basis design, rank testing and explicitly calibrated analyser matrices.

Proposed fabrication paths covered analytical grid polarisers, double-sided copper strip grids, chiral/circular selectors, spiral or split-loop cells, finite apertures and one-board two-face reconfigurable meta-atoms. MATLAB RF PCB/Antenna Toolbox and CST educational studies were explored before native Ansys HFSS became the principal electromagnetic evidence source.

Research posters, a seminar and repeated editorial reviews communicated the core distinction between **demonstrated linear discrimination** and **proposed full-Stokes reconstruction**. The current poster and presentation assets are preserved in [presentations](../../presentations/).

## 4. Automated simulation programme — September–October

Ansys HFSS became the primary solver for complex field outputs, polarisation Jones response, finite-aperture effects, switch-state comparisons, mesh verification and downstream Stokes/information computations. Multiple automated packages and return archives were built to cover startup, geometry creation, solver runs, result export, plots, diagnostics and one final evidence ZIP. The numbered sequences overlap across different design families: **do not infer a single monotonic design lineage from version numbers alone**.

Earlier candidate families included large low-frequency frequency-bank boards, RO4350B PIN-via concepts and 70 × 50 mm finite folded resonators. Separate branches screened four-state and six-state measurements. Some candidates achieved rank four but had poor condition numbers, weak circular sensitivity, finite-aperture changes or independent-mesh disagreement. These scientifically useful screens informed the later instrument design; they must not be reported as validated complete atomic full-Stokes measurements.

## 5. Consolidated information-aware analyser — October

The later paper-centred lineage uses a **two-face copper split-loop arrangement** with a small number of idealised switch configurations, from which **six analyser states** are selected. The model evaluates four Stokes coordinates through a real **6 × 4** instrument matrix derived from two-mode electromagnetic responses. The V44 evidence records the best-paper-selected candidate among **36** parameter candidates, an accepted sampled bandwidth of **250 MHz** (versus 175 MHz for the predecessor), full-rank response and row-normalised condition number **9.53 at 1.925 GHz**. The documented independent mesh discrepancy was **0.551%** at the selected periodic reference. Simulated 3 × 3 finite arrays and fixed-duration measurement-information allocation were also evaluated.

These claims are tied to the [V44 original HFSS return evidence](../../evidence/hfss/v44-reproducibility/) and [current manuscript](../../papers/manuscript-source/main.tex). They are **simulation-conditional**, not claims that hardware or a full-Stokes atomic receiver was physically demonstrated.

## 6. Reports, manuscripts, software and handover

The writing lineage proceeded from interim thesis/report and posters through APL Photonics-style research drafts, then a refined IEEE Access-format article. Archived manuscript generations and figure atlases are discoverable through the [historical source catalogue](../catalog/README.md). A Rydberg Workbench desktop simulator was developed in parallel as a potential flexible RF/atomic research environment; it is a **separate software project**, not evidence that its virtual instrument observations are physical HFSS or atomic measurements.

For new researchers, begin with [the handover](../handover/HANDOVER.md); review [the evidence status policy](../traceability/RECORD_STATUS_POLICY.md) before adding fresh claims. This chronology intentionally records constructive development and final scientific conclusions rather than editorial/frustration logs.

## Source anchors

- [June experimental report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf)
- [October unified research report](../../reports/2026-10-unified-rydberg-polarimetry-report.pdf)
- [Current editable manuscript](../../papers/manuscript-source/main.tex)
- [V44 HFSS data, scripts and returns](../../evidence/hfss/v44-reproducibility/)
- [Source asset provenance](../traceability/ASSET_REGISTER.csv)
- [Design lineage](../design/POLARISER_AND_METASURFACE_DESIGN_LINEAGE.md) and [solver lineage](../simulations/HFSS_CAMPAIGN_LINEAGE.md)

**Reconstruction status:** partly source-grounded, partly reconstructed from dated project discussion; a raw file should be imported and checksum-registered whenever an older design needs to be independently reproduced.
