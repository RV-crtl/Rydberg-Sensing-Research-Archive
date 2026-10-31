# Start here: Rydberg research archive

**Audience:** research assessors, successor students, collaborators, engineers and future maintainers.

1. For a 10-minute understanding, read [the narrative](research/RESEARCH_NARRATIVE.md) and [results](results/KEY_FINDINGS.md).
2. For a 30-minute scientific audit, follow the [claim-to-source ledger](traceability/CLAIMS.md), [figure provenance](results/FIGURE_PROVENANCE.md) and the manuscript's `main.tex`.
3. For an engineering handover, follow [the complete handover](handover/HANDOVER.md), [setup SOP](methods/EXPERIMENTAL_SOP.md), [simulation SOP](methods/HFSS_SOP.md) and [code/data index](methods/CODE_AND_DATA.md).
4. For project administration, inspect the [hardware/BOM](engineering/HARDWARE_AND_BOM.md), [procurement register](operations/PROCUREMENT.md), [fabrication register](operations/MANUFACTURING.md) and [engagement record](operations/ENGAGEMENT.md).
5. For the four supervisor criteria, consult the [rubric-aligned evidence matrix](traceability/RUBRIC_MAPPING.md).

## Scientific status at handover

- Laboratory programme: Rydberg optical/RF apparatus and characterisation reported in the 2026 experimental report.
- Simulation programme: HFSS evidence archive supports the reconfigurable analyser, rank, numerical conditioning and finite-array studies.
- Native electromagnetic field outputs and solver logs: preserve source checksums and compact HFSS-return evidence; full AEDT project databases have **not** been included in the imported set.
- Full atomic-receiver Stokes calibration: a planned integration/verification step, not a reported completion.

Use the [asset register](traceability/ASSET_REGISTER.csv) to identify exactly what is packaged. Do not infer a purchase from an equipment list or infer experimental validation from an HFSS plot.

## Full research corpus (expanded 31 October 2026)

- **End-to-end history:** [Detailed programme timeline](history/DETAILED_RESEARCH_CHRONOLOGY.md) and [historical file discovery](catalog/README.md).
- **Physical investigations:** [Optical receiver and EIT](laboratory/OPTICAL_AND_ATOMIC_RECEIVER.md), [linear RF measurements](laboratory/POLARISATION_MEASUREMENTS.md) and [equipment / sourcing](operations/EQUIPMENT_PROCUREMENT_FABRICATION_ENGAGEMENT_HISTORY.md).
- **Scientific design:** [Metasurface design lineage](design/POLARISER_AND_METASURFACE_DESIGN_LINEAGE.md), [HFSS campaign lineage](simulations/HFSS_CAMPAIGN_LINEAGE.md), [measurement matrix and verification](simulations/VERIFICATION_AND_INFORMATION_MATRIX.md), [formal Stokes notes](methods/STOKES_MATHEMATICS_AND_DERIVATION_NOTES.md).
- **Scientific ecosystem:** [Literature themes](literature/THEMATIC_LITERATURE_AND_RESEARCH_GAP.md), [ARC / Rydiqule / MATLAB / CST and Workbench](software/ATOMIC_MODELLING_AND_WORKBENCH.md), [publications and poster history](publications/PUBLICATION_AND_PRESENTATION_HISTORY.md).
- **Reliable continuation:** [Evidence-status policy](traceability/RECORD_STATUS_POLICY.md), [stream matrix](traceability/RESEARCH_STREAM_STATUS.csv), [completeness / import tracker](handover/RESEARCH_COMPLETENESS_AND_IMPORTS.md), [technical continuation](handover/TECHNICAL_HANDOVER_NEXT_STEPS.md).

Dated Library indexes are **not** statements that every binary is mirrored. Keep original experimental and solver records and permissions distinct from narrative reconstruction.

## Advanced research explorer and reproducibility guides

- [Interactive Stokes, archive and research-history explorer](../site/explorer.html) (source HFSS matrix; not a new solver run or atomic measurement).
- [Master 55-work-package register](handover/MASTER_WORK_PACKAGE_REGISTER.md): experiments, atomic models, RF/PCB, native HFSS, software, papers and operations.
- [End-to-end experimental calibration and RF controls](methods/CALIBRATION_AND_RECOVERY_PROTOCOL.md).
- [Native HFSS export and results reproduction](methods/HFSS_NATIVE_RESULT_REPRODUCTION.md).
- [GitHub research infrastructure and release](governance/GITHUB_RESEARCH_OPERATIONS.md).

The historical 1,280-name catalogue represents discovery metadata for source recovery; only file objects already tracked in GitHub count as imported assets.

## Recovered original research and source code

- **[Recovered historical source library](../history/README.md)** — original planning documents, X-BSR designs, atomic workflow, MATLAB/CST scripts, Workbench validation, thesis source and past HFSS cases.
- [Original binary source checksums and import status](../history/binary-imports/README.md) — 13 preserved original archives awaiting the final Git binary import; not equivalent to tracked data.
- [Repeatable source atlas generator](../scripts/rebuild_research_atlas.py) — builds a current search index of committed source files for the website.

Keep HFSS results, experiment measurements, numerical models and design proposals in their distinct evidence classes.
