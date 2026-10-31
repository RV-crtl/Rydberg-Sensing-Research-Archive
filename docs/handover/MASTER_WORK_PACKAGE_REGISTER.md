# Complete Rydberg research programme — master work-package register

**Edition:** 31 October 2026 · **Project:** Rb-87 Rydberg-EIT microwave receiver and information-aware Stokes analyser · **Source basis:** currently imported thesis and paper material, retained V44 HFSS/field/figure evidence, research posters, verified source files, and separately identified historical Library-discovery records.

This is the cross-disciplinary **handover spine**, not a claim that all historical raw source files have been recovered. For any measurement or numerical result, follow the evidence link to the original. An imported manuscript is a source of the authors' reported conclusions, not a substitute for a missing raw oscilloscope trace, AEDT database, manufacturer receipt or partner correspondence.

## Work-package status key

**Laboratory** = documented experimental RF/optical apparatus or observations; **HFSS** = numerical electromagnetic returns; **Derived** = downstream calculation from original fields; **Design** = engineering geometry or a proposed component; **Scholarly** = reports, posters, papers or reviews; **Archive** = curation and software tooling. “Record exists” does not assert that every individual planned sub-experiment passed.

## A. Atomic and optical RF-sensing programme

| ID | Work package and original scientific purpose | Documentary anchor | Appropriate evidence status |
|---|---|---|---|
| AT-01 | Establish the Rb-87 two-colour EIT ladder (780 nm probe / 480 nm coupling) and optical receiver concept | [June thesis/interim report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf), [atomic SOP](../methods/ATOMIC_MODELLING.md) | Laboratory architecture and report |
| AT-02 | Identify optically accessible Rydberg states and low-GHz microwave-coupled neighbours, including explorations involving 86P3/2 | [Atomic modelling](../software/ATOMIC_MODELLING_AND_WORKBENCH.md), [ARC source](../../research-code/arc/rydberg_tqe_advanced_poster_simulations.py) | Theory/transition-search |
| AT-03 | Characterise laser-frequency and power constraints; compare the 480 nm coarse tuning windows with desired transition accessibility | [Optical receiver dossier](../laboratory/OPTICAL_AND_ATOMIC_RECEIVER.md) | Working instrument constraints; individual wavemeter sweeps need raw files |
| AT-04 | Optical propagation: beam overlap, counter-propagation, lens/fibre coupling, polarisation and rubidium cell arrangement | [Lab methods](../methods/EXPERIMENTAL_SOP.md), [receiver concept slide](../../designs/portable-rydberg-system-proposal.pptx) | Apparatus and optical configuration |
| AT-05 | Probe transmission readout: photodetector/amplifier/oscilloscope configuration, detector bandwidth, backgrounds and lock-point selection | [June report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf) | Experimental framework; individual raw acquisitions incomplete in archive |
| AT-06 | Apply and calibrate magnetic-field bias with single coil and contemplated Helmholtz geometry, including probe/field alignment | [Laboratory dossier](../laboratory/OPTICAL_AND_ATOMIC_RECEIVER.md), [experimental findings](../results/EXPERIMENTS.md) | Preliminary field and apparatus studies |
| AT-07 | Test Zeeman-vector discrimination via ARC/Rydiqule theory and optical/RF experiments; examine whether polarisation coordinates are independently readable | [Atomic-model history](../software/ATOMIC_MODELLING_AND_WORKBENCH.md), [research timeline](../history/DETAILED_RESEARCH_CHRONOLOGY.md) | Explored; complete magnetic full-Stokes demonstration not established |
| AT-08 | Investigate whether peaks around 1.5–1.56 GHz and variable ~2.4 GHz features might represent atomic response or instrument artefacts | [Calibration protocol](../methods/CALIBRATION_AND_RECOVERY_PROTOCOL.md) | Historical exploratory observations; response attribution requires controls |
| AT-09 | Consider lock-in readout and additional calibration to enhance RF-sensitive optical discrimination | [Atomic apparatus dossier](../laboratory/OPTICAL_AND_ATOMIC_RECEIVER.md) | Proposed enhancement, not an established validated noise floor |

### Atomic interpretation

An atomic optical readout changes because microwave coupling modifies an optical quantum response; a voltage from an RF antenna/SDR is a different observable. The completed project provides receiver groundwork and a separate simulated analyser basis. A complete *experimental* linkage—“known input Stokes → PCB state → local Rb coupling → calibrated optical response → measured Stokes”—is a future integrated validation, not a shortcut permitted by a numerical reconstruction plot.

## B. Conventional RF laboratory calibration and polarisation

| ID | Work package | Evidence and correct scope |
|---|---|---|
| RF-01 | Select LPDA/horn/wideband source and receiving antennas and reference them against generator, VNA and spectrum/RF receiver | [Hardware list](../engineering/HARDWARE_AND_BOM.md), [June report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf) |
| RF-02 | Characterise practical steel-rod linear polariser (230 mm-class grid, spacing, orientation, insertion loss) | [Measurements](../laboratory/POLARISATION_MEASUREMENTS.md), [report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf); original 14–15 dB contrast belongs to its own setup |
| RF-03 | Perform/interpret a separate ~2 GHz linear H/V experiment and compare reference polarisation | [Poster](../../presentations/rydberg-rf-polarimetry-poster.png); ~9.7 dB estimate is not the same measured dataset as RF-02 |
| RF-04 | Rotate the linear analyser through multiple angles and repeated sweeps to map cos(2θ)/sin(2θ) response | [Lab analysis](../laboratory/POLARISATION_MEASUREMENTS.md); original complete per-angle acquisition files remain intake targets |
| RF-05 | Interpret equatorial Poincaré states and distinguish linear S1/S2 from circular S3 | [Stokes model derivation](../methods/STOKES_MATHEMATICS_AND_DERIVATION_NOTES.md), [poster plot](../../presentations/linear-polarisation-poincare-equator.png) |
| RF-06 | Plan and investigate circular/elliptical input references, CP antennas, axial ratio and handedness conventions | [RF design lineage](../design/POLARISER_AND_METASURFACE_DESIGN_LINEAGE.md); do not assert a physical CP measurement without its native acquisition |

## C. PCB, polariser and metasurface engineering

| ID | Work package | Representative studies / source |
|---|---|---|
| PCB-01 | Analytical copper-strip and rod-grid linear polarisers, orientation and broadband limits | [Design lineage](../design/POLARISER_AND_METASURFACE_DESIGN_LINEAGE.md) |
| PCB-02 | MATLAB RF PCB Toolbox and Antenna Toolbox: geometries, sweeps and artwork export | [Scientific software](../software/ATOMIC_MODELLING_AND_WORKBENCH.md) |
| PCB-03 | Chiral, spiral, omega and bilayer CP selector candidates to create sensitivity to S3 | [Design lineage](../design/POLARISER_AND_METASURFACE_DESIGN_LINEAGE.md) |
| PCB-04 | CST educational-mesh constrained periodic unit-cell and finite tiling studies | [Software methodology](../software/ATOMIC_MODELLING_AND_WORKBENCH.md) |
| PCB-05 | Practical 200×200 mm in-house copper PCB process, minimum feature/buffer, SVG/Adobe artwork and ferric chloride requirements | [PCB specifications](../engineering/PCB_FABRICATION_SPECIFICATIONS.md) |
| PCB-06 | 70×50 mm sensing region, board aperture versus vapour-cell volume, gap-field versus useful sampled signal | [Metasurface engineering](../engineering/METASURFACE.md), [design lineage](../design/POLARISER_AND_METASURFACE_DESIGN_LINEAGE.md) |
| PCB-07 | SAP18B large two-face switchable concept and tetrahedral four-state metrology candidates | [Design chronology](../design/POLARISER_AND_METASURFACE_DESIGN_LINEAGE.md) |
| PCB-08 | Finite 70×50 mm folded/meander resonator and four ideal switches, including material/thickness distinctions | [HFSS campaign history](../simulations/HFSS_CAMPAIGN_LINEAGE.md) |
| PCB-09 | Single-board/two-face split-loop final research geometry and state selection | [Current manuscript](../../papers/manuscript-source/main.tex), [V44 evidence](../../evidence/hfss/v44-reproducibility/) |
| PCB-10 | Physical PIN diode package, bias isolation, driver/control, DC truth table, RF insertion losses, manufacturing sign-off | [Engineering next steps](TECHNICAL_HANDOVER_NEXT_STEPS.md); complete real-diode implementation is an engineering follow-up |

**Fabrication guard:** Rendered HFSS copper geometry, simulated switch bridges, Gerber intent and a physical manufactured/assembled/tested PCB are four different levels of evidence. Also, a 70×50 mm *cell aperture* does not imply the entire PCB has those dimensions.

## D. Computational physics and native HFSS campaign

| ID | Work package | Verification / anchor |
|---|---|---|
| EM-01 | Match material, copper geometry, frequency, boundaries, excitation Jones basis and switch states | [HFSS SOP](../methods/HFSS_SOP.md) |
| EM-02 | Build Windows automated runners with progress, logs, stop-on-failure, full source bundle and plots | [Campaign history](../simulations/HFSS_CAMPAIGN_LINEAGE.md), [software guide](../software/ATOMIC_MODELLING_AND_WORKBENCH.md) |
| EM-03 | Explore 4-state, tetrahedral, circular and 6-state candidates; screen rank, S3 leverage, gain and κ₂ | [Verification framework](../simulations/VERIFICATION_AND_INFORMATION_MATRIX.md) |
| EM-04 | Perform multi-frequency state exports with *complex* Ex/Ey and phase-consistent receiver observation planes | [Source evidence index](../results/EVIDENCE_INDEX.md) |
| EM-05 | Audit periodic Floquet versus finite 3×3 designs and spatial/axial local E-field ROI | [V44 source archive](../../evidence/hfss/v44-reproducibility/) |
| EM-06 | Independent adapted mesh checks using complex field/matrix disagreement, not simply the solver's convergence flag | [Original source-data checks](../../evidence/hfss/v44-reproducibility/analysis/) |
| EM-07 | Optimise 36 copper geometry candidates, observed sampled 175→250 MHz coverage and selected condition number 9.53 at 1.925 GHz | [Key findings](../results/KEY_FINDINGS.md), [editable paper data](../../papers/manuscript-source/data/) |
| EM-08 | Distinguish rank four from practical estimability, including small singular values and absolute signal gain | [Matrix study](../simulations/VERIFICATION_AND_INFORMATION_MATRIX.md) |
| EM-09 | Study six-state fixed-time measurement allocation and report criterion improvement under stated variance model | [V44 fixed budget output](../../evidence/hfss/v44-reproducibility/analysis/V44_FIXED_BUDGET_RESULTS.json) |
| EM-10 | Reconstruct known polarisation states from simulated instrument matrix; compare physicality, norm, error and finite-model transfer | [Mathematical framework](../methods/STOKES_MATHEMATICS_AND_DERIVATION_NOTES.md) |
| EM-11 | Retain negative/qualifying results from earlier rank-four yet poorly conditioned or mesh-sensitive candidates | [Full HFSS lineage](../simulations/HFSS_CAMPAIGN_LINEAGE.md) |
| EM-12 | Preserve original HFSS .aedt/.aedtresults (if available), state RESULT.json, mesh logs, source complex data, plots, output checksums | [Import backlog](RESEARCH_COMPLETENESS_AND_IMPORTS.md) |

## E. Scientific software and computation

| ID | Work package | Status |
|---|---|---|
| SW-01 | ARC Rydberg transition/dipole/Zeeman and exploratory plotting scripts | [Versioned Python source](../../research-code/arc/rydberg_tqe_advanced_poster_simulations.py) |
| SW-02 | Rydiqule density-matrix and laser/RF coupling studies, solver state/basis definitions | Source intake needed for complete environment |
| SW-03 | MATLAB design/optimisation v1–v1.3 with toolbox paths, RF PCB/cell variations and array studies | Historic originals discoverable in [catalog](../catalog/README.md) |
| SW-04 | CST mesh and angle/frequency screening | Historic originals not fully mirrored |
| SW-05 | PyAEDT/HFSS scripts, geometry generation, exception handling and return bundling | Portions preserved in [native HFSS evidence](../../evidence/hfss/v44-reproducibility/) |
| SW-06 | Desktop Rydberg Workbench (graphical modelling, flexible scope/SDR connections, signal processing and plugin architecture) | [Prototype history](../software/ATOMIC_MODELLING_AND_WORKBENCH.md); original RC2 ZIP indexed for source intake |
| SW-07 | Source figure regeneration, instrument-matrix calculation and paper data integrity | [Paper source](../../papers/manuscript-source/) |
| SW-08 | This research repository, checksum policy, interactive website and continuous validation | [GitHub operations](../governance/GITHUB_RESEARCH_OPERATIONS.md), [website](../../site/explorer.html) |

## F. Scientific communication, administration and external context

| ID | Work package | Evidence |
|---|---|---|
| COM-01 | Structured literature review: Rydberg electrometry, polarisation, magnetic selection, engineered RF surfaces, measurement information | [Thematic research gap](../literature/THEMATIC_LITERATURE_AND_RESEARCH_GAP.md), [original review](../../literature/structured-literature-review-source.txt) |
| COM-02 | Interim experimental report and post-interim experimental research discussion | [Interim report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf) |
| COM-03 | Scientific poster, explanatory slides, presentation speaking notes and supervisor review | [Poster](../../presentations/rydberg-receiver-research-poster.png), [speaker notes](../../presentations/poster-speaking-notes.pdf) |
| COM-04 | ICTON 2026 coauthored invited contribution, DOI and self-citation tracking | [Publication record](../research/PUBLICATIONS.md) |
| COM-05 | APL Photonics to IEEE Access manuscript evolution, figure remediation, mathematical proofs and reviewer responses | [Paper history](../publications/PUBLICATION_AND_PRESENTATION_HISTORY.md) |
| COM-06 | Procurement and quote planning for lasers/detectors/antennas/cell/PCB substrates and equipment | [Equipment history](../operations/EQUIPMENT_PROCUREMENT_FABRICATION_ENGAGEMENT_HISTORY.md) |
| COM-07 | Fabrication planning, copper artwork/Gerber and inspection of practical opto-RF assembly | [Manufacture requirements](../operations/MANUFACTURING.md) |
| COM-08 | University, supervisor, conference and possible industry engagement; verify individual permissions before publication | [Engagement register](../operations/ENGAGEMENT.md) |
| COM-09 | Supervisor assessment response, methodological transparency and independently reviewable engineering documentation | [Rubric evidence](../traceability/RUBRIC_MAPPING.md) |
| COM-10 | Source registry, scientific claims, library metadata discovery, archive integrity and successor handover | [Asset register](../traceability/ASSET_REGISTER.csv), [catalog](../catalog/README.md), [handover](HANDOVER.md) |

## Important scientific qualifications that belong in the handover

- The measured rod-grid ~14–15 dB result and later ~9.7 dB linear contrast are from distinct experimental conditions; averaging or comparing without a reference-plane re-evaluation is misleading.
- The experimental polariser can inform **S1/S2** on a Poincaré equator, not full **S3** without a handedness-sensitive independent channel.
- A simulated six-by-four matrix with rank four does not by itself guarantee noise-robust or hardware-calibrated inversion. Gain and singular spectrum matter.
- The **40.8%** improvement is a calculated fixed-budget information criterion, not measured atomic SNR.
- Periodic and finite 3×3 fields are different observables. Finite-aperture transfer was identified as a principal engineering risk and cannot be glossed over.
- Literature, proposed purchase/manufacture and physical completion are separate evidence classes; confirm order and assembly proofs before adding financial or fabrication completion claims.

## How the next researcher uses this register

Choose a work package ID; open its anchor; identify the actual original data and exact analysis code; verify instrument/solver revision and data provenance; record the outcome with evidence status. For missing originals, use [the historical 1,280-record catalogue](../catalog/README.md) and [completeness tracker](RESEARCH_COMPLETENESS_AND_IMPORTS.md) to recover bytes with a source hash, not just to quote a filename. The technical [continuation SOP](TECHNICAL_HANDOVER_NEXT_STEPS.md) and [verification gates](../simulations/VERIFICATION_AND_INFORMATION_MATRIX.md) then define the next engineering milestones.
