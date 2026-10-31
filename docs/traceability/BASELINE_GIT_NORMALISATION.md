# Original asset checksum vs Git checkout verification

The **initial research archive** was assembled as a ZIP with 289 SHA-256-registered assets. The original asset manifest is intentionally retained, unchanged, at [ASSET_REGISTER.csv](ASSET_REGISTER.csv). When the files were uploaded through GitHub Desktop, Git's existing [attribute rules](../../.gitattributes) normalised some source text (CSV/JSON/Python/Markdown/TeX) from Windows CRLF to LF. This does **not** change numeric values, but it changes byte-level SHA-256 values and file sizes.

The new verifier uses three strictly defined checks:

1. **Exact original match**: SHA-256 and byte length equal the original recorded manifest.
2. **Losslessly reversible Git line-ending change**: the checkout's LF bytes must reconstruct the *exact* initial CRLF bytes by replacing LF with CRLF, and the reconstructed file must match **both** original SHA-256 and byte count. Arbitrary content changes fail.
3. **Explicitly edited curated documents/scripts**: original asset manifest still records the baseline, while current bytes are verified against the current committed **Git blob object SHA-1** in [CURATED_DOCUMENT_BLOBS.csv](CURATED_DOCUMENT_BLOBS.csv). Git's blob identity covers full exact bytes including the content-length prefix. Any change without manifest update fails.

Source scientific data, original PDFs and ZIPs are **not exempted** from source verification. Do not replace a changed scientific CSV's hash in the original manifest to silence the verifier. Preserve original return ZIPs and numeric source data; use new versioned derived files for modifications. The auditor checks ZIP internal integrity, referenced claims and local Markdown links as before.

To verify: run `python scripts/verify_archive.py`, `python -m unittest discover -s tests -v`, and inspect GitHub Actions. This procedure documents checkout normalisation transparently rather than claiming byte-for-byte identical Git data for CRLF-normalised text.
