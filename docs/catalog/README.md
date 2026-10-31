# Historical Rydberg source discovery (2026)

This directory contains **six dated, metadata-only catalogues covering 1,280 distinct named source records** identified across earlier ChatGPT Library files. It complements—**but is not the same as**—the original 290-file evidence archive already committed to this repository.

| Catalogue | Filename | Distinct source records | Source date coverage |
|---|---|---:|---|
| Batch A | [HISTORICAL_SOURCE_INDEX_BATCH_A.csv](HISTORICAL_SOURCE_INDEX_BATCH_A.csv) | 389 | Most recent Library records (October 2026) |
| Batch B | [HISTORICAL_SOURCE_INDEX_BATCH_B.csv](HISTORICAL_SOURCE_INDEX_BATCH_B.csv) | 274 | Before 21 October, September–October |
| Batch C | [HISTORICAL_SOURCE_INDEX_BATCH_C.csv](HISTORICAL_SOURCE_INDEX_BATCH_C.csv) | 222 | Before 27 September |
| Batch D | [HISTORICAL_SOURCE_INDEX_BATCH_D.csv](HISTORICAL_SOURCE_INDEX_BATCH_D.csv) | 238 | 31 August–16 September |
| Batch E | [HISTORICAL_SOURCE_INDEX_BATCH_E.csv](HISTORICAL_SOURCE_INDEX_BATCH_E.csv) | 152 | 5 June–30 August |
| Batch F | [HISTORICAL_SOURCE_INDEX_BATCH_F.csv](HISTORICAL_SOURCE_INDEX_BATCH_F.csv) | 5 | Before 5 June |

A Library record date is an **upload/creation date**, not evidence of when a simulation ran or an item was purchased/manufactured. ZIP packages are often overlapping releases and patches. Titles are a discovery heuristic: generic names like “logs.zip”, unnamed notes or files embedded inside old archives may be absent even though they relate to this work. This is **not an exhaustive count of all original experiments or code**.

## Import status

Every row is **DISCOVERY ONLY**. Actual GitHub files are indexed in [the asset register](../traceability/ASSET_REGISTER.csv), [the evidence catalogue](../results/EVIDENCE_INDEX.md), and the repository itself. Do not cite a source by index row alone.

For a next-stage source migration, retrieve the original bytes, verify source/creation date and context, compute SHA-256, inspect confidentiality and external licences, de-duplicate overlapping ZIPs, classify the file as measurement, native solver, derived calculation, design, manuscript or administration, and commit only when cleared.

## Recommended preservation priorities

1. Irreplaceable raw lab measurements, laser/source settings and original native AEDT projects.
2. Version-pinned source code for MATLAB, CST, ARC/Rydiqule, HFSS and Rydberg Workbench.
3. Fabrication/PCB CAD, BOM/receipts and original images with accurate provenance.
4. Published papers and a useful subset of manuscript/figure-atlas milestones.
5. Historical patch/runner archives as checksum-indexed releases or cold-storage rather than uncontrolled duplicate binary commits.

Follow the [completeness tracker](../handover/RESEARCH_COMPLETENESS_AND_IMPORTS.md), [detailed chronology](../history/DETAILED_RESEARCH_CHRONOLOGY.md) and [record classification policy](../traceability/RECORD_STATUS_POLICY.md).
