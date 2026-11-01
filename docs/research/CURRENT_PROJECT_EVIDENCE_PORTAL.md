# Rydberg Sensing Research Archive — where to find the real work

**Last editorial review: 1 November 2026.** This portal is project-specific. Universal atomic physics belongs in the [separate general Rydberg Systems Engineering textbook](../../book/README.md). Use this page to find original evidence quickly and to determine **which result is the latest supported one for a particular scientific question**. Last edited is not the same thing as last experimentally validated.

## Scientific source of truth, organized by question

| Need to know | Start here | Evidence maturity and supersession |
|---|---|---|
| **What was the latest documented full-Stokes HFSS concept?** | [Current conclusions](../results/KEY_FINDINGS.md) · [V44 native numeric data](../../evidence/hfss/v44-reproducibility/) · [editable paper](../../papers/manuscript-source/main.tex) | **V44 periodic, simulation-derived** six-state analysis; most recent main-paper numerical baseline. |
| **What is actually proven numerically at the selected point?** | [Selected 6×4 matrix](../../papers/manuscript-source/data/V42_C033_INSTRUMENT_MATRIX.csv) · [fixed-budget results](../../evidence/hfss/v44-reproducibility/analysis/V44_FIXED_BUDGET_RESULTS.json) | Rank 4, row-normalised κ≈9.53 at 1.925 GHz; 40.8% *modelled* inverse-trace criterion reduction; sampled 250 MHz acceptance under declared criteria. |
| **What is the most serious finite-model limitation?** | [Original historical finite evidence and corrective strategy](../results/HFSS_V411_V422_ORIGINAL_DIAGNOSTIC_EVIDENCE.md) | Finite 3×3 cross-mesh transfer **failed** previously: worst ~76.92% at 5 mm and ~55.09% at 10 mm. V422 corrected *configuration* does not prove a successful subsequent native finite solve. |
| **What was built and investigated in the actual laboratory?** | [Optical atomic receiver](../laboratory/OPTICAL_AND_ATOMIC_RECEIVER.md) · [linear RF polarimetry](../laboratory/POLARISATION_MEASUREMENTS.md) · [experimental June report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf) | Rb-87 780/480-nm EIT, antenna and linear-polariser measurements, investigated Zeeman bias; *not* a hardware full-Stokes atomic receiver. |
| **Why were designs revised?** | [Full metasurface geometry lineage](../design/POLARISER_AND_METASURFACE_DESIGN_LINEAGE.md) · [research decisions](../traceability/DECISION_LOG.md) · [chronology](../history/DETAILED_RESEARCH_CHRONOLOGY.md) | Early grids, circular selectors, SAP18B, folded/finite boards and six-state information-aware optimisation answer different historical questions. |
| **Which HFSS scripts/results should be reproduced?** | [Native result reproducibility](../methods/HFSS_NATIVE_RESULT_REPRODUCTION.md) · [HFSS campaign lineage](../simulations/HFSS_CAMPAIGN_LINEAGE.md) · [original source checksums](../../evidence/hfss/v44-reproducibility/data/SOURCE_HFSS_CHECKSUMS.json) | Compare exact model, solver, complex Ex/Ey, mask, frequency, observation volume, mesh and data provenance before reporting a number. |
| **How to compute atomic transition candidates?** | [Prior ARC/Workbench work](../software/ATOMIC_MODELLING_AND_WORKBENCH.md) · [historical original code](../../history/recovered-code/atomic/rydberg_polarization_simulation_workflow.py) | Original exploratory state-screening code. For transferable general algorithms use the independent [ARC textbook example](../../book/examples/arc_transition_atlas.py). |
| **Which raw files were really recovered?** | [Actual imported source library](../../history/README.md) · [binary import checksum ledger](../../history/binary-imports/README.md) · [discovery inventory](../catalog/README.md) | Only Git-tracked raw files count as imported. The 13 binary bundles in the ledger remain an import queue; 1,280 discovered filenames are not independently Git-imported sources. |
| **What figures are defensible?** | [Figure-source ledger](../results/FIGURE_PROVENANCE.md) · [current manuscript source](../../papers/manuscript-source/) · [source visual atlas](../../book/FIGURE_ATLAS.md) | Distinguish authentic optical photograph, measured linear RF curve, HFSS-native fields and illustrative theory diagrams. |
| **Who can reproduce and extend it?** | [55 work packages](../handover/MASTER_WORK_PACKAGE_REGISTER.md) · [handover](../handover/HANDOVER.md) · [test/repair protocol](../methods/CALIBRATION_AND_RECOVERY_PROTOCOL.md) | Handover to a successor, detailed risk gates, source audit and automation procedures. |

## Version-selection rule

**Prefer the newest source that is validated for the *same scientific quantity* and physical model.** V44 periodic information results must supersede weaker early periodic screens when reporting current periodic performance, but cannot overwrite a V421 **finite-panel** failure: the latter answers a different boundary-value problem and cannot be promoted to a pass until corresponding independent finite-model evidence exists. Similarly, a newer formatted paper does not supersede an actual optical measurement when the question concerns observed data.

When comparing numbers, annotate: **measured** / **HFSS-native simulated** / **offline derived from native fields** / **proposed** / **historical preliminary** / **published externally**. Never average different rod-grid experiments simply because they both report extinction dB.

## Search and operations

The [interactive research explorer](../../site/explorer.html) searches committed files and historical metadata and visualises actual imported 6×4 analysis. The [diagnostic assistant](../../site/diagnostics.html) provides source-linked RF/EIT/HFSS fault isolation and a reporting worksheet. Public-source [Australian quantum and Defence collaboration monitor](../../automation/README.md) produces issue-based review candidates; it is not an authority to disclose restricted data or contact third parties.

## Current highest-value research gates

1. Independently verify finite 3×3/physical aperture complex-field response with true state geometry and two distinct adapted meshes at the cell sensing volume.
2. Validate handedness sensitivity and full-Stokes reference basis with calibrated independent RF states, not algebraic pseudoinverse tests alone.
3. Incorporate physical PIN diode and copper-stack parameters if predicting manufactured device switching.
4. Build a fully parameterised RydIQule optical model for the selected real Rb-87 manifold, and ARC-verified accessible laser/RF transition, then cross-check with controlled laboratory traces.
5. Integrate a real atomic readout and analyser basis and quantify error against held-out optical/RF reference states, with a complete native-data ZIP.
6. Document limitations transparently and update this status portal only after source-backed independent validation.

The [general textbook](../../book/README.md) deliberately does not contain these case-specific scientific claims.
