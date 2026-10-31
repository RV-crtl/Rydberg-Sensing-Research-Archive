# Successor onboarding, source intake and project operations

## Source intake

For every new artefact: record the owner, date, instrument or software, original filename, source/repository location, SHA-256, access classification, experiment or case ID, derived outputs and associated claims. Never overwrite raw files. Use a descriptive path and register the file in the evidence manifest.

**Recommended categories:** `experiments/`, `evidence/hfss/`, `manufacturing/`, `procurement-private/` (restricted only), `collaborations/` (redacted public index), `papers/`, `designs/`, `research-code/`.

## Naming pattern

`YYYYMMDD_<stream>_<setup-or-case>_<content>_rNN.<extension>`; for example, `20261031_hfss_periodic_P8E_Efield_complex_r01.csv`. Do not rename native exports without preserving the original name in metadata.

## Reproduction steps

1. Clone or extract the repository and run `python scripts/verify_archive.py`.
2. Read [SOPs](../methods/HFSS_SOP.md) and [code/data dictionary](../methods/CODE_AND_DATA.md).
3. Identify the **exact campaign**, mesh and geometry branch before launching a solver.
4. Compare newly computed results with archived condition number, source matrices and cross-mesh tests at the same sampling locations.
5. Version all changed parameters, publish scripts and controlled output hashes and update [`CLAIM_EVIDENCE.csv`](../traceability/CLAIM_EVIDENCE.csv).

## Required import metadata template

```json
{
  "record_id": "EXP-or-HFSS-YYYYMMDD-case",
  "modality": "experiment | hfss | analytical | reference",
  "original_filename": "<original name>",
  "sha256": "<hash calculated from original file>",
  "acquired_at": "YYYY-MM-DD or unknown",
  "instrument_or_software": "<model and version>",
  "settings": {},
  "observables_and_units": {},
  "derived_from": [],
  "claim_ids": [],
  "access": "private | restricted | public-cleared"
}
```

GitHub is the living index; large native project databases and controlled supplier/industry records may require university-managed storage, Git LFS or a versioned release archive.

## Publishing to GitHub

Create an **empty** GitHub repository named `Rydberg-Sensing-Research-Archive`, then from inside the extracted folder run:

```bash
git init
git add .
git commit -m "docs: import Rydberg sensing research archive and evidence"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Rydberg-Sensing-Research-Archive.git
git push -u origin main
```

Replace `YOUR_USERNAME` with the account that owns the target repository; check access/permissions and public-release policy first. Existing unrelated repositories should not be used as a destination. A repository owner can subsequently enable the **manual** GitHub Pages workflow after release review.
