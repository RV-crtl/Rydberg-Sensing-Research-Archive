# Contributing and updating this research archive

Contributions must maintain **scientific provenance, stable filenames, reviewable changes and clear figure-to-data links**.

1. Work in a named branch; explain research intent and evidence in the PR.
2. Add source files unchanged. Preserve their original filenames, provenance metadata and SHA-256.
3. Update the claim ledger and figure captions whenever a data/result interpretation changes.
4. Keep experimental, numerical HFSS, analytical and reference-only materials clearly separated.
5. Use readable source, recorded versions, comments and tests. No fabricated or interpolated solver data presented as original HFSS output.
6. Run `python scripts/verify_archive.py` and `python -m unittest discover -s tests -v` before merging.
7. Verify all public-release permissions for third-party manuscripts, images, code, supplier documents and personal details.

See [handover intake](docs/handover/SUCCESSOR_ONBOARDING.md) for required metadata fields and naming conventions.
