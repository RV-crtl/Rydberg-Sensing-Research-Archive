# Research source completeness, backlog and authoritative import checklist

This repository already contains **a preserved 290-file initial evidence package**, an editable paper, early and consolidated reports, original poster assets, an expanded V44 HFSS evidence tree and a project-oriented research microsite. The historical Library catalogue documents hundreds of **additional** candidate assets that were not all in the initial archive. The distinction is intentional: a filename-only index never substitutes for original bytes.

## Evidence completeness by stream

| Stream | Already represented | Additional originals needed for “everything” | Priority |
|---|---|---|---|
| Atomic/lab | June interim report, illustrations and methods | Raw oscilloscope data, EIT/AT scans, camera logs, laser wavelength/power records, cell/coil calibrations, RF source settings, repeats and original plot scripts | High |
| RF polarisation | Prior polariser descriptions, poster and H/V data interpretations | Original angle sweeps for 5 repeats, VNA Touchstone, linear 0/45/90/135 states, signal generator/calibration files, independent circular analyser traces | High |
| HFSS | V44 reproduction data, scripts, original return archives, matrices and figures | Full native .aedt/.aedtresults where recoverable, every earlier campaign's source/return ZIP, X/Y complex source exports, model/material settings, and solver logs | High |
| MATLAB/CST | Method/design descriptions | Editable MATLAB .m project trees, RF PCB Toolbox files, CST projects, optimisers, SVG artwork, Gerber design iterations, results | High |
| ARC/Rydiqule | Advanced Python ARC plotting source + methods | Exact Rydiqule solver scripts, transition tables, magnetic dependence runs, archived Python environment lockfiles | Medium |
| Hardware/manufacture | Specification narrative, BOM working draft, portable receiver proposal | Physical board revisions, raw copper design/verification, Gerber/Excellon, images, etch/manufacture logs, assembly test records, equipment inventories | High |
| Purchases | Hardware candidates, proposal slides and registers | Receipts, orders, quotes, delivery confirmations, supplier/manufacturer correspondence, asset IDs (private/restricted where needed) | Medium |
| External engagement | Academic affiliations, ICTON record and register template | Meeting agendas/minutes, approved stakeholder descriptions, signed permissions, industry correspondence and outcomes | Medium |
| Papers/posters | Interim report, unified report, current editable IEEE Access and poster images | Historical manuscript versions/figure atlases as separate reproducible milestones; final publisher preprints where release permitted | Medium |
| Rydberg Workbench | Software history and model concept | RC1/RC2 desktop source ZIP, setup scripts, test results, GNU Radio/ZeroMQ integration and examples | Medium |
| Governance | Supervisor rubric, SOPs and handover | Formal supervisor sign-offs and any institutional release/IP conditions, if shareable | Medium |

## Import priority and handling

**Tier 1 — irreplaceable primary observations:** raw lab acquisition and original HFSS native databases. Preserve full bytes and hashes, avoid lossy conversion, and link their matching metadata to claims. Large files should use institutional research storage or Git LFS rather than bloating ordinary Git commits.

**Tier 2 — editable source and models:** MATLAB, CST, Rydiqule, ARC, HFSS scripts, CAD/SVG/Gerber, LaTeX source with bibliography and figure generator. Reconstruct pinned environments and include clean setup instructions.

**Tier 3 — communication and administration:** original slides, posters, thesis/report milestones, quotations, supplier records, engagement notes, figures, photo captions. Apply permissions and licensing/redaction before public distribution.

## Required intake manifest format

Use fields: record ID; original filename; research stream; creation/experiment date (distinct from upload date); lab or solver; model/physical origin; source SHA-256; retained path; revision; scientific claim(s) supported; reproducibility steps; release permission; source owner; scope; duplicate/replaced-by links; and review status.

Mark each record: **not available / listed in Library / materialised but not committed / committed unreviewed / evidence validated / external release approved**. Do not replace these statuses with blanket “complete.”

## Reuse guidance for archived HFSS packages

Some ZIPs are only *patch runners* and some are *return archives*. Preserve both, but only the verified return's solver logs and native field data support research findings. Avoid extracting duplicate 20–100 MB ZIP trees repeatedly. Register checksums, run quick manifest-based classification and document provenance chain (runner → case ID → native results → derived matrix → paper figure).

## First 90 minutes of a successor handover

1. Read [Start Here](../START_HERE.md), [complete timeline](../history/DETAILED_RESEARCH_CHRONOLOGY.md) and [scientific status](../results/KEY_FINDINGS.md).
2. Inspect the current source TeX paper and V44 CSV/JSON inputs.
3. Execute the existing local verification and unit-test scripts using a clean Python environment.
4. Trace one plot to raw HFSS inputs and inspect case source/mesh metadata.
5. Review laboratory RF measurement source/uncertainties and unresolved raw-file inventory.
6. Decide on one next experiment or simulation with explicit acceptance criteria.

See [the handover](HANDOVER.md) and [research status policy](../traceability/RECORD_STATUS_POLICY.md).
