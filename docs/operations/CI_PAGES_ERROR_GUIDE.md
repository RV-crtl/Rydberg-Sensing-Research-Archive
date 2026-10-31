# GitHub Actions and Pages error resolution

## Failure A: Pages setup returned HTTP 404

Two manual website-publishing runs on 31 October 2026 failed at `actions/configure-pages@v5` with **Get Pages site failed: Not Found**. GitHub could not find an enabled Pages site for this repository. This is not an HTML compilation or HFSS-model error. The GitHub Actions token normally **cannot activate Pages for an account/repository without the required administrative permissions**.

**One-time owner action:** Open **Settings → Pages → Build and deployment → Source → GitHub Actions**. Check whether your GitHub plan permits Pages for a **private repository** (GitHub Free normally requires a public repository; GitHub Pro/Team/Enterprise can support private-repository source projects). **Do not make this research repository public merely to activate Pages:** the site contains manuscript figures and historical source filenames. Review publication rights first.

The revised manual deployment workflow now runs a **preflight**: it verifies the standalone site, checks the repository Pages API and deploys only when Pages is configured to use GitHub Actions. When the Pages API returns 403/404 or another publishing source is configured, the workflow explains what to do, skips the deploy job and explicitly states **the site is not published**. It never uploads the entire repository to a Pages artifact.

To preview safely without Pages, run `python -m http.server 8000 --directory site` and visit `http://localhost:8000/`.

## Failure B: Dependency-update pull requests failing integrity check

Dependabot pull requests updated workflow action versions, but the earlier integrity checker demanded that the modified workflow files match outdated **curated-documentation** Git blob IDs from a historical archive snapshot. That wrongly blocked legitimate PRs.

The revised checker still verifies all **234 imported-primary evidence files** with original SHA-256 and byte counts (plus losslessly reversible Windows line-ending normalisation for text). It verifies claim-to-source links and Markdown links. It permits normal review-driven changes to the **55 curated-documentation-or-tool** files, including Actions workflows, without changing any original data checksum.

`docs/traceability/ASSET_REGISTER.csv` remains the preserved historical source manifest; the older `CURATED_DOCUMENT_BLOBS.csv` is a snapshot, **not a rule that all workflow updates must exactly match outdated hashes**. Git tracks changed documentation as immutable commits; the scientific source manifest protects original datasets.

## How to verify the current branch

1. Open **Actions → Research archive checks** and inspect the latest run on `main`, not historical failed interim commits.
2. Run `python scripts/verify_archive.py`, `python -m unittest discover -s tests -v`, `python scripts/verify_site.py`, and `node --test tests/test_site_model.mjs`.
3. Open the Dependabot PR and look for the newly passing checks. Separate major-version compatibility concerns are reviewed per action update.
4. For publishing, run the manual workflow only after source-release approval and the one-time Pages setup. A **successful preflight with deployment skipped is not a live site**.

## Future original data

When new HFSS/AEDT projects, complex Jones fields, laboratory raw measurements, original photographs or paper-source data are imported, compute their SHA-256 and record original source and provenance. Never change an existing source checksum merely to silence a real scientific-data mismatch.
