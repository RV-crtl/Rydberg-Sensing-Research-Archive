# GitHub operations for a source-preserving scientific programme

## Branches and review

The `main` branch holds the curated handover baseline. Work in descriptive topic branches (`feat/`, `fix/`, `docs/`, `evidence/`); merge through a PR after automated checks. Attach a concise evidence declaration for any scientific figure, material properties, Maxwell solve or stated experimental outcome. Keep manuscript version changes distinct from source-data changes.

## Built-in features configured

- Issue forms for a **lab experiment**, **HFSS scientific case**, and **repository/website bug**, plus existing primary-evidence intake.
- CODEOWNERS and a release-notes classifier (owner and labels can be adjusted if the team expands).
- Monthly Dependabot checks for GitHub Actions and CI coverage for Python provenance, numerical model, source page links and JavaScript tests.
- Manually initiated, site-only GitHub Pages deployment to avoid copying the entire private research archive into a public website artifact.
- A searchable *committed-file* register separate from the historical *discovery* index; the latter cannot substitute for raw-source import.

## GitHub-specific capabilities requiring owner setup

GitHub app permissions for this repository do not automatically configure **branch protection**, **rulesets**, **Pages source**, **Discussions**, **Projects** or domain/DNS settings. Recommended manual Settings choices: require a passing `research-integrity` check on `main`, disallow force pushes, require at least one code review for manuscript/solver changes, use GitHub Actions as Pages source only after release approval, and protect the Pages environment if available.

## Scientific quality control

New numerical results should include original source hashes, geometry/state ID, solver settings, units, exact basis/order convention, downstream code and acceptance thresholds. A plot can be visually correct yet scientifically mismatched to the reported project; check each figure's actual input data before merging. Separate measured, HFSS-computed, derived, proposed, fabricated and published outcomes. The [record status policy](../traceability/RECORD_STATUS_POLICY.md) and [completeness tracker](../handover/RESEARCH_COMPLETENESS_AND_IMPORTS.md) are mandatory reference points.

## Website development

Use `python -m http.server 8000 --directory site`, then visit `/explorer.html`. The scientific model is dependency-free JavaScript and loads immutable source-derived JSON; it does **not** call HFSS or the atomic receiver. Run the Actions tests, confirm the Poincaré conventions and visually review media on desktop and mobile. The site links to GitHub sources; private links require sign-in and are never broken relative `../` paths.

## Release and privacy

The Pages workflow is intentionally manual. Its asset contains only `site/`. The website's historic metadata index reveals historical filenames: approve that metadata before a public launch. Never treat a passing CI status as redistribution permission. Keep source data protected even if an excerpt appears on the website.
