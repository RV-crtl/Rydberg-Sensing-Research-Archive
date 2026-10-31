# Original Rydberg research history and recoverable source library

This research archive now preserves **34 committed historical source/index files**, recovered from the original project file Library rather than reconstructed from summaries. The imported materials cover initial Rb-87 optical and Zeeman modelling, laboratory polarisation analysis, MATLAB and CST, split-ring/X-BSR geometry studies, HFSS candidate evaluation, scientific software testing, the interim thesis and successive manuscript reviews.

**Provenance ledger:** [Original recovered source hashes](RECOVERED_SOURCE_PROVENANCE.csv) records each extracted text source's Git blob ID and its historical—not independently remeasured—status. The [history-specific integrity validator](../scripts/verify_history_sources.py) checks these records in CI. These files remain distinct from the 234 SHA-256-protected original imported primary assets.

**Scientific provenance:** A recovered .m/.py script or review is original research history, but does not establish that every associated measurement, simulated figure or solver run was validated. Files in `recovered-evidence/` contain *historical* case-specific verdicts; cite the full case ID and original solver data. The final main-paper V44 numerical evidence remains under [evidence/hfss/v44-reproducibility](../evidence/hfss/v44-reproducibility/). These imported text files are faithful Library text extractions, not a claim of byte-for-byte parity with an earlier ZIP's original encoding.

## Browse original source by discipline

### Verified byte-level intake manifest for unimported historical binaries (2 files)

- [`ORIGINAL_BINARY_SOURCES_TO_IMPORT.csv`](../history/binary-imports/ORIGINAL_BINARY_SOURCES_TO_IMPORT.csv) — 2,821 bytes
- [`README.md`](../history/binary-imports/README.md) — 2,481 bytes

### Original technical and manuscript assessments (4 files)

- [`Rydberg_V45_Supervisor_Feedback_and_Harsh_Grade.md`](../history/editorial-reviews/Rydberg_V45_Supervisor_Feedback_and_Harsh_Grade.md) — 4,840 bytes
- [`Rydberg_V46_University_and_IEEE_Access_Brutal_Review.md`](../history/editorial-reviews/Rydberg_V46_University_and_IEEE_Access_Brutal_Review.md) — 7,460 bytes
- [`Rydberg_V47_Critical_University_and_Publication_Review.md`](../history/editorial-reviews/Rydberg_V47_Critical_University_and_Publication_Review.md) — 6,967 bytes
- [`Rydberg_V52_Engineering_Evidence_Check.md`](../history/editorial-reviews/Rydberg_V52_Engineering_Evidence_Check.md) — 3,253 bytes

### Original architecture and metasurface design plans (3 files)

- [`2026-09-28_APL_PHOTONICS_RESEARCH_PLAN.md`](../history/original-research-plans/2026-09-28_APL_PHOTONICS_RESEARCH_PLAN.md) — 37,998 bytes
- [`2026-09-28_XBSR_70x50_DESIGN_BASIS.md`](../history/original-research-plans/2026-09-28_XBSR_70x50_DESIGN_BASIS.md) — 47,880 bytes
- [`2026-09-28_XBSR_MANUFACTURABLE_DESIGN_STUDY.md`](../history/original-research-plans/2026-09-28_XBSR_MANUFACTURABLE_DESIGN_STUDY.md) — 32,804 bytes

### Original MATLAB, atomic, CST, Workbench and figure code (17 files)

- [`arc/README_rydberg_tqe_simulations.md`](../history/recovered-code/arc/README_rydberg_tqe_simulations.md) — 1,990 bytes
- [`atomic/rydberg_polarization_simulation_workflow.py`](../history/recovered-code/atomic/rydberg_polarization_simulation_workflow.py) — 29,059 bytes
- [`cst/cp_fullwave_results_TEMPLATE.csv`](../history/recovered-code/cst/cp_fullwave_results_TEMPLATE.csv) — 200 bytes
- [`cst/CST2025_FIRST_RUN_CARD.txt`](../history/recovered-code/cst/CST2025_FIRST_RUN_CARD.txt) — 1,251 bytes
- [`cst/README_CST2025.md`](../history/recovered-code/cst/README_CST2025.md) — 7,274 bytes
- [`figures/APL_FIGURE_RULES.md`](../history/recovered-code/figures/APL_FIGURE_RULES.md) — 1,664 bytes
- [`figures/generate_v90_apl_plots.py`](../history/recovered-code/figures/generate_v90_apl_plots.py) — 13,052 bytes
- [`figures/HFSS_POSTER_COPY.md`](../history/recovered-code/figures/HFSS_POSTER_COPY.md) — 2,404 bytes
- [`matlab/02_generate_matlab_poster_figures.m`](../history/recovered-code/matlab/02_generate_matlab_poster_figures.m) — 14,515 bytes
- [`matlab/03_replot_arc_outputs_in_matlab.m`](../history/recovered-code/matlab/03_replot_arc_outputs_in_matlab.m) — 5,325 bytes
- [`matlab/analyse_new_polariser_data.m`](../history/recovered-code/matlab/analyse_new_polariser_data.m) — 12,512 bytes
- [`matlab/plot_digitized_rydberg_data.m`](../history/recovered-code/matlab/plot_digitized_rydberg_data.m) — 9,129 bytes
- [`matlab/plot_verified_rydberg_figures_v3.m`](../history/recovered-code/matlab/plot_verified_rydberg_figures_v3.m) — 7,463 bytes
- [`matlab/plot_verified_rydberg_figures.m`](../history/recovered-code/matlab/plot_verified_rydberg_figures.m) — 9,083 bytes
- [`workbench/Rydberg_Workbench_v0.4_Validation.md`](../history/recovered-code/workbench/Rydberg_Workbench_v0.4_Validation.md) — 6,447 bytes
- [`workbench/Rydberg_Workbench_v1.0_RC1_SetupFix_Validation.md`](../history/recovered-code/workbench/Rydberg_Workbench_v1.0_RC1_SetupFix_Validation.md) — 1,545 bytes
- [`workbench/Rydberg_Workbench_v1.0_RC1_Validation.md`](../history/recovered-code/workbench/Rydberg_Workbench_v1.0_RC1_Validation.md) — 1,523 bytes

### Historical HFSS campaign returns, diagnostic and derived-law values (5 files)

- [`earlier_laws/final_law_results.csv`](../history/recovered-evidence/earlier_laws/final_law_results.csv) — 1,405 bytes
- [`earlier_laws/LAW_VERDICT.json`](../history/recovered-evidence/earlier_laws/LAW_VERDICT.json) — 618 bytes
- [`hfss-historical/APL_V4_1_EVIDENCE_AND_V5_DESIGN_GATES.md`](../history/recovered-evidence/hfss-historical/APL_V4_1_EVIDENCE_AND_V5_DESIGN_GATES.md) — 8,535 bytes
- [`hfss-historical/LATEST_RETURN_5.json`](../history/recovered-evidence/hfss-historical/LATEST_RETURN_5.json) — 413 bytes
- [`hfss-historical/V6_RETURN_VERDICT_AND_NEXT_STEPS.md`](../history/recovered-evidence/hfss-historical/V6_RETURN_VERDICT_AND_NEXT_STEPS.md) — 4,416 bytes

### Original thesis, seminar and laboratory reporting drafts (3 files)

- [`2026-06-revised-interim-report-original.tex`](../history/recovered-reports/2026-06-revised-interim-report-original.tex) — 136,343 bytes
- [`Rydberg_Polarimetry_SPEAKER_TRANSCRIPT.md`](../history/recovered-reports/Rydberg_Polarimetry_SPEAKER_TRANSCRIPT.md) — 8,312 bytes
- [`Rydberg_Thesis_Methods_Draft.md`](../history/recovered-reports/Rydberg_Thesis_Methods_Draft.md) — 8,832 bytes

## Current source completeness

- **Committed and directly accessible:** the files listed above and the original 234 primary evidence files already in the main repository.
- **Source bundle verified, not yet committed:** 13 recovered native/binary archives, including V412, V416, V418, V420, V422 and V43 HFSS-related packages, editable Rydberg Workbench RC2, manuscript versions and an antenna/metasurface report. Their [checksum/source manifest](binary-imports/ORIGINAL_BINARY_SOURCES_TO_IMPORT.csv) includes exact sizes and SHA-256.
- **Historical Library discovery only:** 1,280 originally indexed filename records, which can overlap and should not be claimed as imported data. [Search the catalogue](../docs/catalog/README.md).
- **Still requiring acquisition:** untransferred original oscilloscope traces/laser log records, unpublished POs/receipts, native AEDT databases if available and additional MATLAB/CST projects. [Completeness tracker](../docs/handover/RESEARCH_COMPLETENESS_AND_IMPORTS.md).

## Avoid false certainty

A scientific runner, a condition-number plot, an initial validation report and a measured rubidium EIT trace describe different forms of evidence. Explicitly use *proposed*, *analytic*, *HFSS-computed*, *derived*, *measured*, *manufactured*, or *published*. For every new original, add model/experiment revision, physical units, apparatus or solver settings, source location and checksum.

## Reproduction sequence

Read [master work-package register](../docs/handover/MASTER_WORK_PACKAGE_REGISTER.md), recover the appropriate real primary data in its original source format, run the source code in its recorded environment, and compare native outputs against the corresponding [claim-to-evidence register](../docs/traceability/CLAIM_EVIDENCE.csv). Older MATLAB and Python scripts may require toolbox installations and missing input CSV files; their presence here does not imply they all run standalone.
