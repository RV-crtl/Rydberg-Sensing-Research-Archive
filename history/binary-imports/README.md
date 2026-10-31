# Unimported original binary source bundle

This register tracks **13 real recovered historical files** totaling **44,617,349 original bytes**. All files are present in the preserved separate archive **`Rydberg_Additional_Original_Source_Import_2026-10-31.zip`**, which is available to the researcher in the prior ChatGPT delivery and working download environment. **The original binary bytes are NOT yet tracked in this GitHub repository.** Filenames in this register must not be treated as GitHub evidence.

Source values and SHA-256 digests were copied from the verified original-source ZIP manifest. Nine nested ZIPs include original Python, MATLAB/HFSS-related scripts, solver-return files, models, logs, plots, manuscript source, and/or evidence. **None of these archives is automatically proof of a completed HFSS run.** See [import CSV](ORIGINAL_BINARY_SOURCES_TO_IMPORT.csv).

## Reproducible intake

1. In a private staging directory, extract the prior delivery ZIP. It contains the nested `history/source-imports/` hierarchy and the original `SOURCE_IMPORT_MANIFEST.csv`/`CHECKSUMS.sha256`.
2. Review each source for third-party material, unpublished paper rights, laboratory photographs and personal details before publication.
3. Verify each original against the exact SHA-256 in this register. For large datasets use Git LFS or institutional storage with a checksum manifest as appropriate; preserve original raw archives without silently re-compressing them.
4. Copy the `history/source-imports/` folder into the repository using GitHub Desktop. Commit and push. This is an **additional binary import**, independent of the recovered plain-text scripts currently in `history/recovered-code/`.
5. Amend status from `UNIMPORTED_ORIGINAL_BINARY` only after verifying the actual Git file and native source lineage, and link any corresponding claim/figure. Duplicate source files should be indexed by checksum, not repeatedly extracted.
6. Preserve license/simulation status (proposed, original runner, solver return, HFSS-derived calculation, draft paper) in the claim ledger.

**Key risk:** archive files often carry a “final” or “paper-ready” label despite partial, failed or mesh-sensitive results. Inspect source content and solver logs before reporting published performance.

[Research completeness tracker](../../docs/handover/RESEARCH_COMPLETENESS_AND_IMPORTS.md) · [HFSS original evidence policy](../../docs/methods/HFSS_NATIVE_RESULT_REPRODUCTION.md).
