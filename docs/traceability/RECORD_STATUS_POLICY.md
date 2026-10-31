# Record status, certainty and scientific claim policy

Use these terms consistently across this repository, the website, papers and handover.

| Status | Allowed wording | Minimum supporting record | Not equivalent to |
|---|---|---|---|
| **Measured** | “Recorded with [instrument] under [conditions]” | Raw acquisition, reference/calibration, units, settings, date, analysis script | A plotted simulation, a model assumption |
| **HFSS-computed** | “HFSS predicts/reports under [model]” | HFSS native return/result, solved setup, mesh/configuration, complex data, results checksum | Manufactured hardware or rubidium EIT data |
| **Derived from HFSS** | “Calculated from exported HFSS complex fields” | Input complex data, source code, exact formula, version and outputs | Another independent HFSS solve |
| **Analytical / surrogate** | “Analytical estimate / synthesis-model result” | Assumptions and source script | Full-wave proof |
| **Proposed** | “Designed/considered/planned” | Design proposal, drawing, requirement, date | Fabricated, ordered, tested |
| **Fabricated** | “Board manufactured / assembled” | Manufacturing order, fabrication output/photos, revision and inspection | Simulated board appearance |
| **Purchased** | “Purchased/received” | Order/receipt and delivery record | Supplier quotation, recommended item or planned purchase |
| **Published** | “Published in [journal/conference]” | DOI/indexed publisher record and final author list | Uploaded manuscript draft |
| **Reconstructed history** | “Earlier conversations describe…” | Dated discussion and retrievable original file when possible | Independently reverified source measurement |

## Technical safeguards

- An instrument matrix can have rank four and still be unusably noisy or poorly conditioned. Report both rank and scale-normalised singular values, not only invertibility.
- Idealised PIN switches / metal bridges omit bias networks, package parasitics and manufactured-state variability unless those effects are explicitly modelled.
- Periodic Floquet simulations and a finite 3 × 3 panel answer different electromagnetic questions. A periodic Stokes calibration cannot automatically be transferred to a finite aperture.
- A modelled 40.8% fixed-time criterion improvement is **not** 40.8% measured uncertainty improvement.
- Full-Stokes reconstruction from synthetic input Stokes vectors is a *model consistency test*, not a laboratory demonstration.
- Distinct design branches (RO4003C finite folded meander, RO4350B two-face loop, MATLAB grid and future PCB) should never be described as one continuously manufactured artefact.
- Retain both positive and qualifying evidence. Unvalidated early candidates explain parameter/design choices but should not become headline successes.

## Intake metadata

Every added research source needs: identifier; human-readable title; owner/source; date; source system; stage; instrument/solver; physical units; fabrication/measurement status; material/licence classification; path; SHA-256; related analysis; and permissible release scope.

Existing source-level evidence starts with [asset register](ASSET_REGISTER.csv), [claim evidence register](CLAIM_EVIDENCE.csv), [figure provenance](../results/FIGURE_PROVENANCE.md) and [historical discovery catalogue](../catalog/README.md).
