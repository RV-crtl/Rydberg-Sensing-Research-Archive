# Equipment, sourcing, manufacturing and external engagement — complete working history

This page separates **apparatus present/reported**, **design-specified hardware**, **candidate quotations**, **orders mentioned in research discussions** and **delivered/manufactured evidence**. It does not infer purchase or fabrication from specifications. Primary equipment references: [June interim report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf), [hardware inventory](../engineering/HARDWARE_AND_BOM.md), [portable receiver proposal](../../designs/portable-rydberg-system-proposal.pptx), and [BOM.csv](BOM.csv).

## Optical, RF and laboratory hardware

| Area | Item / historical specification | Evidence-status guidance |
|---|---|---|
| Optical source | 780 nm DL PRO probe laser | Recorded setup/platform; confirm serial/owned inventory |
| Optical source | 480 nm DL PRO coupling laser, several explored coarse tuning windows | Recorded setup; distinguish tuning range from calibrated line |
| Atomic media | Rb-87 vapour cell, approximately 70 × 50 mm optical/RF aperture region | Document cell length, temperature, fill/serial and holder |
| Detector | Optical photodetector and amplifier (DET025M/related candidates) | Platform report; multiple models were considered |
| Detector proposal | Thorlabs DET025AFC 2 GHz Si FC/PC photodetector | Portable-system slide proposed ~USD 359.72; **quotation/design reference only**, not proof of purchase |
| Laser proposal | Thorlabs DBR 780 nm component | Portable-system proposal listed ~USD 7,202.81; **price example, not confirmed expenditure** |
| RF generation | Windfreak synthesiser (historical 12.5 MHz–6.4 GHz reference) | Setup/equipment record |
| RF capture | SDR (Ettus B210), oscilloscope and RF measurement receiver | Refer to exact run-specific configuration |
| RF transmission/reception | 1.8 GHz LPDAs, wideband antenna, linear rods/grid | Reported / examined in RF experiments |
| Circular RF candidate | approximately 6 dBi wideband PCB CP antenna | Earlier discussions describe an order; purchase/delivery record not yet imported |
| Magnetic bias | initial single coil; later Helmholtz/field homogeneity planning | Distinguish built/installed and designed/tested arrangements |
| Near-cell polariser | 230 × 230 mm steel-rod grid (6 mm rod, 30 mm pitch) | Earlier physical RF reference design; dimensions should be checked against report |

**Procurement reconciliation:** Supplier correspondence, POs, tax receipts, packing lists, asset numbers and warranty records are missing from the published archive unless individually imported. No total project expenditure, vendor relationship or receipt date is inferred.

## PCB/material/manufacturing branches

Historical process: Rogers RO4350B nominal 1.52–1.60 mm with 35 μm copper, or FR-4 1.6 mm for an alternative model; artwork prepared for two copper faces; intended board maximum 200 × 200 mm, 5 mm clearance and ≥0.5 mm etch features; SVG/Adobe workflows; a two-stage ferric chloride chemical-etch method was discussed. One exploratory 220 mm TetraVia–Omega and 500 mm wideband grids exceeded the smaller manufacturing envelope and must not be labelled fabrication-release-ready.

Manufacturing records to preserve for each revision: design revision and material lot; HFSS/source geometry hash; actual Gerber/Excellon/drill set; fabrication drawing; manufacturer DFM and stack-up sign-off; quote/order; assembled PCB front/back images; component and PIN diode identification; driver and bias board; dimensional inspection; DC continuity and RF VNA verification; optical clearances; safety/etch procedures and waste-disposal records.

For existing simulation-only designs, original copper geometry files and an “illustrative design view” caption are appropriate; a rendered PCB should not be called a photograph of a manufactured board.

## Research engagement and dissemination

- **Academic context:** University of New South Wales Canberra engineering/research group; collaboration/coauthorship and supervisor direction shaped the research plan, figure choices, technical verification and communication.
- **External conference dissemination:** ICTON 2026 invited coauthored paper, *Quantum Radio-Frequency Rydberg Sensors and mid-infrared photodetectors*, DOI 10.1109/ICTON71309.2026.11704868. This is a conference contribution, not proof that the present six-state analyser paper has been accepted.
- **Application-facing engagement:** Earlier project documents/discussions referenced defence/research application awareness including DSTG and Panop. Do **not** present this as funded sponsorship, institutional endorsement, supplied test data or a signed partnership without corresponding permission/records.
- **Suppliers/fabricators:** Portable-receiver optical sourcing and PCB-fabrication options were studied. Company identifiers, quotations and emails should be added only with provenance and release screening.
- **Peer and research communication:** Poster, scientific presentation, seminar, thesis/interim report and evolving manuscript versions constitute distinct deliverables.

## Administrative control

Use [the existing engagement register](ENGAGEMENT_REGISTER.csv) for authorised contacts and source documents. Keep confidential correspondence in a permission-managed private area, not GitHub Pages. Add each invoice/manufacturing order only after checking personal addresses, supplier terms and institutional IP. The primary public-facing bibliography is [publications](../research/PUBLICATIONS.md); project-specific poster and manuscript records belong to [publication history](../publications/PUBLICATION_AND_PRESENTATION_HISTORY.md).

## Next evidence intake

Check [missing source register](../handover/RESEARCH_COMPLETENESS_AND_IMPORTS.md), [manufacturing guidance](../engineering/PCB_FABRICATION_SPECIFICATIONS.md) and [record-status policy](../traceability/RECORD_STATUS_POLICY.md). This archive intentionally records the work and actionable requirements, not correspondence grievances.
