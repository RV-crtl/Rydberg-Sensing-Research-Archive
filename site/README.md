# Scientific research portfolio and interactive archive

The responsive site is **static, dependency-free HTML/CSS/JavaScript** with source-linked research figures, searchable historical source discovery and an interactive Stokes model. It is a useful scientific presentation layer, not a new experimental result.

## Run locally

```sh
python -m http.server 8000 --directory site
```

Visit `http://localhost:8000/` or `http://localhost:8000/explorer.html`. **Opening `explorer.html` directly from `file://` may block JSON fetch**; use a local HTTP server or the hosted GitHub Pages preview.

## Scientific functionality

- Render a rotatable, projected Poincaré sphere and select H, V, D, A and ±S3 conventional pure input states.
- Show exactly calculated Stokes [S0,S1,S2,S3] and `y = A S` for the six-row **HFSS-derived V42_C033** matrix at 1.925 GHz. The model data has an exact CSV source comparison test.
- Export the calculated responses as a clearly labelled model CSV. No noise is generated and no RF, AEDT or rubidium-cell measurements are made by the browser.
- Show model source rank and the archived fixed-time inverse-trace information criterion (~40.8% modelled reduction).
- Filter timeline by laboratory, design, simulation or publication; search actual tracked GitHub files separately from **historical discovery-only** sources (1,280 records).
- Filter the publication figure gallery with provenance captions.

## GitHub Pages privacy

The Pages workflow is **manual**, not auto-published on every commit. It validates and deploys **only `site/`**. It does not expose raw `evidence/`, `papers/`, `reports/` or `docs/`. The site *does contain project figures, numerical source-derived data, and 1,280 historical file names*; review these for confidentiality and publication rights before manually deploying.

In repository Settings → Pages, set **GitHub Actions** as the build source. The private-repository Pages availability, protection/visibility and deployment URL depend on the owner's GitHub account/settings. The hosted site links to original research sources at GitHub and may require sign-in for access; they are not broken relative parent paths.

## Automated validation

```sh
python scripts/verify_archive.py
python scripts/verify_site.py
python -m unittest discover -s tests -v
node --test tests/test_site_model.mjs
node --input-type=module --check < site/explorer.js
```

`site/data/research-atlas.json` is a **snapshot** of tracked files before the website upgrade, not a live private GitHub index. `site/data/historical-index.json` is source-discovery metadata and must never be reported as 1,280 additional committed binary assets.

Sources: [matrix CSV](../papers/manuscript-source/data/V42_C033_INSTRUMENT_MATRIX.csv), [fixed-budget result](../evidence/hfss/v44-reproducibility/analysis/V44_FIXED_BUDGET_RESULTS.json), [record status policy](../docs/traceability/RECORD_STATUS_POLICY.md).

## Rydberg Academy and lab

- [Textbook website](academy.html), 24 original educational chapters with 1,000 worked-case links.
- [Interactive physics lab and JS code sandbox](lab.html), dimensionally defined weak-probe/EIT illustrative model and SI parameter controls. The sandbox uses an opaque-origin iframe with strict resource CSP and a watchdog; it does not give direct Python/ARC/RydIQule/HFSS execution or physical hardware access.
- [Original diagrams](assets/academy-ladder.svg), [HFSS source workflow](assets/academy-hfss-pipeline.svg), [diagnosis tree](assets/academy-diagnostic-tree.svg), plus authentic archive images already on this site.
- [Research book source](../book/README.md) (in GitHub), [PDF print workflow](../.github/workflows/build-book.yml), [citations](../book/REFERENCES.md).

On GitHub Pages the book and website are site-only; the printed 1,000-case PDF is a verified Actions artifact, not automatically part of the public site.
