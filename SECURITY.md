# Security, data access and responsible disclosures

This repository holds research assets, some of which may be unpublished or subject to institutional and supplier constraints. **Do not** open a public issue containing API tokens, laboratory access credentials, personally identifiable correspondence, proprietary quotes, restricted drawings, unpublished research records or sensitive partner details.

For a security flaw in project code or a suspected accidental disclosure, contact the repository owner through a private GitHub channel. Avoid publishing a reproducer with real research records. Keep any remediation on a review branch, revoke accidentally exposed credentials and document affected files and Git history.

## Data hygiene

- Keep the research archive **private by default** until institutional, coauthor, image and supplier rights are confirmed.
- GitHub Pages is a separate **manual** release step. Its workflow copies only `site/`, never `papers/`, `evidence/`, `reports/` or `docs/` into the Pages artifact. Review the filenames and derived numerical data in `site/data/` as well as figures before running it.
- Neither the source catalogue nor the website proves all files may be redistributed.
- Use private institutional storage or approved Git LFS for large proprietary AEDT models, raw lab measurements, photos with identifiable people, invoice data or embargoed datasets.
- Use SHA-256, instrument configuration and provenance metadata for each new physical measurement; never silently edit an original source file.
- User-supplied code and archived solver returns must be scanned for unsafe executables, credentials and external endpoints before reuse.
