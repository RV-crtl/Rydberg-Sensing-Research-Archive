# Rydberg Systems Engineering

## A general-purpose, open graduate textbook and laboratory reference

**Quantum fundamentals · atomic structure · coherent optics · Rydberg states · microwave/optical sensing · quantum simulation · scientific computing · reproducible experiment design**

This book is written for a researcher starting from first principles. It is **not** a thesis, not an advertisement for one laboratory, and not a vehicle for presenting one project's HFSS results as universal conclusions. Its chapters apply to alkalis, cold atoms, vapour cells, neutral-atom arrays, cavity-QED platforms and cross-disciplinary quantum research.

**Actual edition status, 1 November 2026:** 36 original instructional chapters, revised physics foundations, 1,000 distinct parameterised numerical problems, original interactive teaching figures, documented ARC and RydIQule Python examples, a reader with interactive questions, and a separate reproducible PDF workbook. The earlier 1,033-page output is predominantly one solved numerical exercise per page; **it is not 1,000 pages of original prose**. This manuscript is a substantially extended *first editorial edition*, not independently peer reviewed or ready for publisher acceptance. See the [honest editorial completion requirements](EDITORIAL_STANDARD.md).

## Deep field guides — design and diagnose real systems

The formal 36-chapter syllabus is supplemented by a practical three-volume, cross-platform reference series. These are **general Rydberg** resources, not examples presented as unique achievements of one laboratory.

| Researcher's question | Start here | Includes |
|---|---|---|
| How do I design laser, vacuum, MOT or tweezer subsystems? | [Laser, vacuum and cold-atom engineering](field-guides/LASERS_VACUUM_AND_COLD_ATOM_SYSTEMS.md) | Optical architecture, calibration, traps, EIT and twelve worked tests |
| What is the rigorous quantum mathematics behind the systems? | [Tensor products and control derivations](field-guides/TENSOR_PRODUCTS_AND_CONTROL_DERIVATIONS.md) | Entanglement, operators, time evolution, frame changes, density matrices and 12 worked answers |
| How do I design a complete atomic system from nothing? | [Design a Rydberg experiment from zero](field-guides/COMPLETE_EXPERIMENT_DESIGN.md) | Platform selection, optical/RF modelling, calibrations, metrology, design gates and 10 fully answered scenarios |
| How do I do deeper state screening, Stark maps and physical solver verification? | [Advanced computational atomic methods](field-guides/ARC_DEEP_COMPUTATIONAL_METHODS.md) | Quantum defects, transition graphs, Doppler convergence, state tracking, fourteen additional worked problems |
| How do I use ARC and RydIQule correctly across problems? | [Computational decision and verification manual](field-guides/ARC_RYDIQULE_MODEL_VERIFICATION.md) | Frequency/units, state rules, numerical checks, thermal/Zeeman limits and 10 worked research diagnostics |
| How can I use blockade and interacting arrays? | [Interactions and neutral-atom design](field-guides/INTERACTING_RYDBERG_ARRAYS.md) | Pair-state models, collective Rabi dynamics, gate-readout considerations and 12 solved problems |
| How do I quantify uncertainty and test model identifiability? | [Metrology and Bayesian inference](field-guides/STATISTICAL_METROLOGY_AND_INFERENCE.md) | Noise likelihoods, Fisher information, validation, inference and 12 full solutions |
| Why did my experiment, simulation or code fail? | [Universal fault-isolation atlas](field-guides/UNIVERSAL_DIAGNOSTIC_ATLAS.md) | Distinct vapour, tweezers, RF, numerical and finite geometry problems plus 15 answered challenges |

The longer practical guides deliberately contain independent design logic, failure controls, implementation gates and source references instead of padding printed pages with repeated numerical variations. **They are substantial extensions, not evidence that the complete 36-chapter manuscript yet satisfies publisher-grade length or independent review.**

![Original Rydberg system selection diagram](../site/assets/book-platform-selection.svg)

*Original research-platform decision diagram. Choose an observable before selecting vapour cells, cold atoms, tweezers or cavity/ionisation detection.*

## Read the book by domain

| Part | Chapter range | Graduate competencies |
|---|---|---|
| I — Mathematics and quantum science | [01](chapters/01-mathematical-language.md)–[04](chapters/04-density-matrices.md) | Dirac notation, observables, uncertainty, driven Hamiltonians, coherence and Lindblad |
| II — Atomic structure and alkali physics | [05](chapters/05-angular-momentum.md)–[08](chapters/08-eit-and-autler-townes.md) | Selection rules, quantum defects, state ladders, Rydberg scaling, EIT and dressed atoms |
| III — Optical/microwave experiments and polarization | [09](chapters/09-optics-lab.md)–[12](chapters/12-identifiability.md) | Gaussian optics, detectors, RF engineering, Jones/Stokes, inverse sensing |
| IV — Numerical atomic modelling and diagnosis | [13](chapters/13-quantum-defect-and-arc.md)–[17](chapters/17-spectroscopy-diagnostics.md) | Actual ARC and RydIQule workflows, Zeeman maps, Doppler, spectroscopy fault isolation |
| V — Electromagnetic/sensor and research methodology | [18](chapters/18-hfss-metasurface.md)–[24](chapters/24-publication-and-future.md) | HFSS theory, information metrics, finite verification, fabrication, numerical inference, publications |
| VI — Interacting Rydberg systems | [25](chapters/25-rydberg-blockade.md)–[28](chapters/28-rydberg-cavity-qed.md) | Blockade and gates, tweezers, multichannel quantum-defect theory, cavity-QED |
| VII — Advanced Rydberg environments | [29](chapters/29-precision-rydberg-electrometry.md)–[32](chapters/32-field-ionisation-and-particle-detection.md) | Quantum electrometry, spin models, Rydberg molecules/collisions, ionisation detectors |
| VIII — Designing the next experiment | [33](chapters/33-lasers-cooling-and-stabilisation.md)–[36](chapters/36-frontiers-and-cross-disciplinary-research.md) | Laser systems, apparatus requirements, Bayesian inference, quantum/Defence research frontier |

## Learn interactively

The [Academy reader](../site/academy.html) contains the actual chapter text, full-text search, collapsible explanations, navigation and worked-case practice. The [live calculation lab](../site/lab.html) demonstrates equations with adjustable settings in an isolated browser sandbox—no native HFSS, ARC or RydIQule is claimed to run in the browser. The [diagnostic companion](../site/diagnostics.html) uses grounded checklists. [Original figure provenance](FIGURE_ATLAS.md) explicitly distinguishes diagrams from photographs or native solver results.

The [source-of-truth chapter generator](../scripts/rebuild_academy.py) builds website text directly from Markdown, so edited chapters cannot silently diverge from the site. [Printable workbook](export_workbook_pdf.py) compiles the chapters and 1,000 individually numbered solved problems. Each exercise has its exact inputs and physical limitations; 1,000 variations do not replace scientific conceptual depth.

## Real runnable code

[ARC state and dipole atlas](examples/arc_transition_atlas.py) uses real installed ARC numerical functions with sign- and units-conscious quantum selection. [RydIQule three-state example](examples/rydiqule_three_level.py) runs the real installed density-matrix solver but explicitly does not claim a calibrated species-specific optical transmission measurement. The software programs are separate from the in-browser illustrative equations. Their offline physics/API interface tests run in CI even without installed scientific packages.

## How to read and use this book responsibly

Start by deriving the core equations and solving the chapter review questions, then test the numerical code and decide what observable a physical experiment would actually acquire. Check primary reference values and current software documentation for the selected species and apparatus. An unverified simulation, a toy spectrum and a measured signal are different evidence categories. Original scientific sources and textbooks are listed in [REFERENCES](REFERENCES.md); equations and figures are reviewed continuously rather than assumed perfect.

### Separate real research archive

The **actual project's** rubidium atomic receiver, HFSS six-state metasurface, experimental rod-grid results, failed finite-mesh cases, manuscript history and version-precedence matrix belong in the [project-specific evidence portal](../docs/research/CURRENT_PROJECT_EVIDENCE_PORTAL.md), and the [historical source library](../history/README.md). They are *not* used as universal evidence in this general book.

### Collaboration, AI and public disclosure

The [automated Australian opportunity monitor](../automation/README.md) watches official ARC/Defence/DSI sources, while a [bounded optional AI co-author](../automation/AI_EDITORIAL_POLICY.md) may create review-only PRs when explicitly configured. Neither verifies unpublished physics, silently changes accepted results or submits applications. This repository is currently public: publication rights and sensitive material must be reviewed.

[Contents and editorial roadmap](EDITORIAL_STANDARD.md) · [General source references](REFERENCES.md) · [Guided labs](TUTORIAL_LABS.md) · [Return to project](../README.md).
