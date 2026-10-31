<div align="center">

# RYDBERG RF SENSING
### Atomic receivers · Microwave polarimetry · Information-aware metasurfaces

**Research portfolio / source evidence / reproducible analysis / technical handover**

[**Explore the Research**](docs/START_HERE.md) · [**Engineering Handover**](docs/handover/HANDOVER.md) · [**Evidence Catalogue**](docs/results/EVIDENCE_INDEX.md) · [**Browse the Website**](site/index.html)

![Experimental Rydberg optical bench, from the manuscript's documented laboratory figure](site/assets/lab-optical-bench.png)

*Experimental apparatus image sourced from the editable Rydberg manuscript (Figure 1).*

</div>

---

## Complete project history and technical dossiers

The original source-backed article and V44 numerical evidence are only part of the programme. The expanded archive also reconstructs the prior atomic-receiver experiments, systematic design progression, simulation campaigns, original communication and research software. Start with:

| Dossier | What is preserved / explained |
|---|---|
| [Complete chronology](docs/history/DETAILED_RESEARCH_CHRONOLOGY.md) | March–October research phases, experimental-to-simulation progression, scientific decisions and source anchors |
| [Atomic receiver and laboratory](docs/laboratory/OPTICAL_AND_ATOMIC_RECEIVER.md) · [linear measurements](docs/laboratory/POLARISATION_MEASUREMENTS.md) | 780/480 nm Rb-EIT platform, RF references and Stokes equator distinction |
| [RF design lineage](docs/design/POLARISER_AND_METASURFACE_DESIGN_LINEAGE.md) | Rod grids, analytical PCB polarisers, chiral CP selectors, SAP18B, TetraVia–Omega, finite folded and six-state surfaces |
| [HFSS campaign history](docs/simulations/HFSS_CAMPAIGN_LINEAGE.md) · [verification criteria](docs/simulations/VERIFICATION_AND_INFORMATION_MATRIX.md) | Multi-branch V1–V44 development, complex-field evidence, mesh, conditioning and finite aperture |
| [Atomic modelling and Workbench](docs/software/ATOMIC_MODELLING_AND_WORKBENCH.md) | ARC, Rydiqule, MATLAB, CST, automated HFSS and desktop scientific software |
| [Literature synthesis](docs/literature/THEMATIC_LITERATURE_AND_RESEARCH_GAP.md) · [Stokes derivation](docs/methods/STOKES_MATHEMATICS_AND_DERIVATION_NOTES.md) | Thematic background, research gaps and mathematical conventions |
| [Equipment and engagement](docs/operations/EQUIPMENT_PROCUREMENT_FABRICATION_ENGAGEMENT_HISTORY.md) | Components, PCB processes, quotation-versus-purchase evidence, academic and external engagement |
| [Publication history](docs/publications/PUBLICATION_AND_PRESENTATION_HISTORY.md) | Interim thesis, posters, ICTON conference, APL/IEEE manuscript evolution |
| [Historical asset catalogues](docs/catalog/README.md) | **1,280 additional named Library records discovered**; indexed for retrieval, not misrepresented as GitHub-imported files |
| [Source completeness](docs/handover/RESEARCH_COMPLETENESS_AND_IMPORTS.md) · [next steps](docs/handover/TECHNICAL_HANDOVER_NEXT_STEPS.md) | Import gates, primary evidence gaps, instructions for a successor |
| [Evidence status](docs/traceability/RECORD_STATUS_POLICY.md) · [research stream matrix](docs/traceability/RESEARCH_STREAM_STATUS.csv) | Explicit measured vs simulated vs proposed vs fabricated/purchased/published controls |

**Archive count clarity:** the original release contained 290 actual files. The discovery catalogue lists 1,280 *additional historical source records*, many overlapping/versioned. Their filenames are not automatically original GitHub assets; consult the source-completeness register before claiming a complete byte-for-byte historical mirror.

## The research in one minute

This archive documents a microwave sensing programme combining **rubidium-87 Rydberg electromagnetically induced transparency (EIT)**, RF polarisation conditioning and **HFSS-designed, switch-programmable metasurfaces**. The objective is to understand how multiple known analyser states can convert polarisation-dependent responses into a well-conditioned Stokes measurement basis compatible with an atomic receiver.

Work spans literature synthesis, optical/RF system design, laboratory characterisation, numerical modelling, electromagnetic design, polarimetric inference, simulation validation, visual communication and research dissemination.

> **Evidence key:** Experimental measurements and electromagnetic-simulation results are separate. HFSS-derived results are not described as rubidium-cell full-Stokes measurements. Procurement proposals are not treated as purchase confirmations.

## Research highlights

| Research stream | Documented outcome | View evidence |
|:---|:---|:---|
| Rydberg-EIT experimental receiver | Rubidium optical readout, RF-front-end evaluation, magnetic calibration and exploratory experimental work | [Experimental report](reports/2026-06-magnetically-biased-rydberg-receiver.pdf) |
| Polarisation conditioning | Laboratory linear-polarisation contrasts, RF front-end comparisons and Poincaré-equator interpretation | [Experimental evidence](docs/results/EXPERIMENTS.md) |
| HFSS metasurface engineering | Two-face, switch-programmable design and 6 × 4 Stokes instrument using complex simulated fields | [Design and methodology](docs/engineering/METASURFACE.md) |
| Simulation optimisation | 36 geometry candidates; simulated accepted sampled interval of 250 MHz; at 1.925 GHz: rank 4, row-normalised κ₂ = 9.53, independent mesh disagreement 0.551% | [Results](docs/results/KEY_FINDINGS.md) |
| Measurement design | Fixed-time dwell-allocation criterion improved by 40.8% under the article's stated statistical model | [Analysis sources](papers/manuscript-source/data/) |
| Research communication | Research poster, editable technical manuscript, interim research report, publication record and handover documents | [Papers and talks](docs/research/PUBLICATIONS.md) |

## Navigate by purpose

| I want to... | Start here |
|:---|:---|
| Understand the scientific gap and intellectual contribution | [Research overview](docs/research/RESEARCH_NARRATIVE.md) · [Literature map](docs/research/LITERATURE_MAP.md) · [Chronology](docs/research/RESEARCH_CHRONOLOGY.md) |
| Rebuild the experimental setup | [Hardware inventory](docs/engineering/HARDWARE_AND_BOM.md) · [Experimental SOP](docs/methods/EXPERIMENTAL_SOP.md) · [Atomic modelling](docs/methods/ATOMIC_MODELLING.md) |
| Trace the HFSS evidence and reproduce paper figures | [HFSS SOP](docs/methods/HFSS_SOP.md) · [Figure provenance](docs/results/FIGURE_PROVENANCE.md) |
| Inspect source code, measurements and datasets | [Code index](docs/methods/CODE_AND_DATA.md) · [Evidence catalogue](docs/results/EVIDENCE_INDEX.md) |
| Find procurement, fabrication or collaborators | [Procurement](docs/operations/PROCUREMENT.md) · [Fabrication](docs/operations/MANUFACTURING.md) · [Engagement](docs/operations/ENGAGEMENT.md) |
| Take over the research project | [Research handover](docs/handover/HANDOVER.md) · [Successor onboarding](docs/handover/SUCCESSOR_ONBOARDING.md) |
| Inspect what meets the supervisor assessment rubric | [Assessment evidence matrix](docs/traceability/RUBRIC_MAPPING.md) · [Claims ledger](docs/traceability/CLAIMS.md) |

## Project process

```mermaid
flowchart LR
  A[Literature and gap mapping] --> B[Requirements and RF/atomic architecture]
  B --> C[Laboratory EIT / RF characterisation]
  B --> D[HFSS candidate design and verification]
  C --> E[Calibration and polarisation interpretation]
  D --> F[Complex fields and Jones / Stokes analysis]
  E --> G[Research evidence and publications]
  F --> G
  G --> H[Handover and research continuation]
```

## Repository structure

```text
.
├── README.md                       Research overview and navigation
├── docs/                           Narrative, decisions, methods and handover
├── papers/manuscript-source/       Fully editable LaTeX article and figure source
├── papers/current-manuscript-draft.pdf
├── reports/                        Earlier experimental research report
├── presentations/                  Posters and presentation material
├── literature/                     Retained structured-review source
├── designs/                        Portable receiver and hardware proposals
├── evidence/hfss/                   HFSS-derived numerical data, logs and native-return ZIPs
├── research-code/                   Rydberg/ARC scientific source code
├── site/                            Portable, responsive research microsite
├── governance/                      Original assessment rubric
├── scripts/                         Integrity / navigation / evidence checks
└── tests/                           Automated archive and math checks
```

## Reuse and publication

The repository is a **preserved research handover** and a **publication-ready documentation structure**, not a statement that all artefacts have public-release permission. Check institutional IP rules, photograph permissions, proprietary supplier material, third-party licenses and unpublished manuscript status before publishing a public fork. See [release and data policy](docs/operations/RELEASE_POLICY.md). Avoid publishing internal commercial invoices and personal contact details.

**Maintainer:** R. N. Verghese · **Archive assembled:** 31 October 2026 · **Status:** curated from accessible project records; import register tracks additional sources.
