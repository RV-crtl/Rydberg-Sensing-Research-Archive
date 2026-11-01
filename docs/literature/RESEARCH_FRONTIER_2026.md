# Scientific literature horizon and project implications — 1 November 2026

**Evidence rule:** This document cites public scientific sources and separates published experiments, theoretical models and preprints. It does not claim a new study was reproduced or that the project results were experimentally demonstrated. The [automated weekly monitor](../../.github/workflows/weekly-research-watch.yml) finds *candidates* only; critical analysis here remains curated.

## 1. Rydberg polarimetry is not an empty field

**P. K. Elgee et al., “Complete three-dimensional vector polarimetry with a Rydberg-atom rf electrometer,” Physical Review Applied 22, 064012 (3 December 2024)**, DOI https://doi.org/10.1103/PhysRevApplied.22.064012 . That group used three mutually orthogonal RF local oscillators and optical heterodyne signals to infer a 3D polarisation ellipse, including amplitude and relative phase components. Their work established that complete atomic RF polarimetry was experimentally possible before this metasurface project. **Design consequence:** do not position our proposed two-face RF front end as the first complete Rydberg polarimeter. The novelty question is instead whether a limited-cell, switchable and potentially lower hardware-complexity measurement basis can retain robust RF/atomic information.

**M. Chilcott et al., “Quantum-enabled complete RF-polarimetry with an optically-wired atomic sensor,” arXiv:2605.14529 (2026)**, https://arxiv.org/abs/2605.14529 . The preprint describes a spectroscopic framework for arbitrary RF polarisation and Poincaré-sphere mapping through the quantum energy structure. **Design consequence:** compare any simulated Stokes reconstruction against actual spectral fingerprints and independently verify publication status and demonstrated coverage. Do not conflate algorithmic inversion of a metasurface A-matrix with their spectroscopic approach.

## 2. Sublevel physics may explain spectral features that a toy model cannot

**N. Schlossberger et al., “Resolving magnetic-sublevel structure in Rydberg Autler–Townes spectra with arbitrary rf polarization,” Physical Review A 114, 033701 (1 September 2026), DOI https://doi.org/10.1103/w5k9-1mlh .** The reported theory/experiment shows elliptical RF coupling can involve multiple mJ states and produce more than two resolved dressed-state features. **Design consequence:** a three-state or four-state weak-probe teaching graph is not sufficient to validate experimentally observed peaks. Use actual selected magnetic sublevels, field quantisation axis and line-shape model through ARC/RydIQule. When a peak moves with B or input polarisation, check both optical and RF reference controls.

## 3. Information theory and new platforms

**C.-R. Liu et al., “Fisher-based sensitivity framework for Rydberg-atom microwave electrometry,” Physical Review Applied 25, 034052 (16 March 2026), DOI https://doi.org/10.1103/qsmd-yh44 .** This provides a modern scientific context for Fisher-information-based quantum/atomic sensitivity studies. **Design consequence:** derive the relevant noise likelihood for the *actual optical observable* before claiming a metrological advantage from the HFSS matrix's fixed-budget inverse-trace objective.

**“Microwave Electrometry with Quantum-Limited Resolutions in a Rydberg-Atom Array,” Physical Review Letters 136, 110802 (17 March 2026), DOI https://doi.org/10.1103/v5nm-xwp5 .** A distinct tweezer-array platform can provide field mapping and response regimes not directly attainable in a thermal-cell EIT receiver. **Design consequence:** do not generalise a tweezer-array field or speed figure to this vapour-cell apparatus. Use it as a technology comparison and future-methods contrast, not a calibration number.

## 4. What our work actually shows

The project documents measured optical/RF receiver and linear-polariser feasibility, followed by **HFSS-derived** six-state full-rank Stokes analysis and experimental integration planning. The most relevant numerical paper source is the V44 periodic reference: 36 candidates, accepted sampled frequency span, rank 4, κ₂≈9.53 at 1.925 GHz and an approximately 0.551% selected periodic-mesh metric; the finite case's cross-mesh Stokes transfer was much worse. The 40.8% improvement is a modelled allocation criterion, not observed atomic SNR. The design remains distinct from a physically calibrated full-Stokes optical measurement.

[Current versus historical state](../../book/CURRENT_STATE.md) · [HFSS original checks](../results/HFSS_V411_V422_ORIGINAL_DIAGNOSTIC_EVIDENCE.md) · [Book references](../../book/REFERENCES.md).

## 5. Reading-priority matrix for the next real contribution

| Research question | First source to inspect | What would change our design? |
|---|---|---|
| Are RF polarisation components optically observable in the proposed ladder? | Schlossberger 2026; Chilcott 2026; full RydIQule magnetic-manifold model | Real spectrally separable, calibrated lines under the actual B/beam/temperature conditions |
| Is our information-based analyser genuinely metrologically better? | Liu 2026; source V44 matrix and optical noise assumptions | Gain-aware/variance-correct calibration and held-out optical reconstruction |
| Is a different polarimetry architecture necessary? | Elgee 2024; two-face HFSS and switching limits | Compare RF LO complexity versus finite-board conditioning and calibration transfer |
| Are our Rydberg state choices physically accessible? | ARC Rb-87 energies/dipole APIs and 480-nm measured laser range | A complete pair/ladder table with optical access, RF frequency, strength, lifetime and selection rules |
| Is a proposed figure scientifically publishable? | Native HFSS source, exact script, geometry, mesh, dataset/figure provenance | Source-derived plot reproduces and meets predeclared acceptance thresholds |

## 6. A continuously updated research ledger is not self-certifying

A weekly workflow can collect bibliographic metadata with DOI/arXiv links and open an issue for human review. It does not read every manuscript, prove any claim, make legal redistribution decisions or independently run experimental/solver measurements. Any new scientific claim must have a traceable original primary source before being promoted to the front page, textbook or paper.

**Verification:** Published dates/DOIs and summaries here were checked against journal/publisher descriptions on 1 November 2026, and may change through errata/new versions. For publication see the publisher, not a snippet or copied thumbnail.
