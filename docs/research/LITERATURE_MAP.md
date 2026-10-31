# Living literature review and reading roadmap

**Primary reference source:** the 36 editable entries in [`ieee_references.tex`](../../papers/manuscript-source/ieee_references.tex), supported by the theory and background sections of [`main.tex`](../../papers/manuscript-source/main.tex) and the earlier experimental report. Citation metadata should be cross-checked against publishers before submission.

| Theme | Representative literature already cited | Relevance and design consequence | Next reading priority |
|---|---|---|---|
| Atomic microwave electrometry and metrology | Sedlacek et al. (2012, 2013); Holloway et al. (2014); Schlossberger et al. (2024) | Optical atomic RF readout, vector measurement and calibration | High: apparatus-to-observable mapping |
| Atomic mixers, phase and receive architectures | Jing et al. (2020); Holloway et al. (2019); Berweger et al. (2024) | A scalar atomic response need not imply phase or complete polarisation recovery | High: compatible detection observables |
| Rydberg vector and polarisation methods | Elgee et al. (2024); Cloutman et al. (2024); Yin et al. (2024) | Prior polarimetric/vector approaches and alternative experimental bases | Critical: novelty and state-of-art comparison |
| Jones–Stokes theory and optimal analyzers | Jones (1941); Azzam (1988, 1990); Tyo (2002); Goldstein (2011) | Measurement-matrix construction, rank, condition number, information | Critical: matrix derivation and design objective |
| Metasurface full-Stokes sensing | Arbabi et al. (2018); Basiri et al. (2019); Rubin et al. (2019); Lin et al. (2019) | Alternative optical metasurface analyzers and detector architectures | High: transferable ideas and distinctions |
| Atomic simulation and physical feasibility | Gallagher (1994); method references in the manuscript | Transition/dipole-selection and realistic Rydberg observables | Medium/high: follow-on atomic integration |

[Archived structured-review source draft](../../literature/structured-literature-review-source.txt) is also preserved. It complements, but does not supersede, the current publication bibliography and literature map.

## Traceable gap-to-decision connections

| Gap / constraint | Decision | Evidence entry |
|---|---|---|
| Scalar readout loses polarisation detail | Introduce multiple RF analyser states rather than infer polarisation from scalar strength alone | [Manuscript](../../papers/current-manuscript-draft.pdf), Theory |
| Arbitrary Stokes recovery needs sufficient independent observations | Construct six-state 6 × 4 instrument and check rank, singular values, conditioning | [Matrix CSV](../../papers/manuscript-source/data/V42_C033_INSTRUMENT_MATRIX.csv) |
| Numerical results can depend on mesh and finite geometry | Preserve independent-mesh checks, finite array and sensitivity analyses | [Evidence archive](../results/EVIDENCE_INDEX.md) |
| Different switching states carry different information | Examine state combinations and dwell allocation using stated objective functions | [Subset CSV](../../papers/manuscript-source/data/V44_FIXED_BUDGET_ALL_SUBSETS.csv) |

## Research search protocol for successors

Search IEEE Xplore, Web of Science, Scopus, APS, AIP, Optica, NIST and arXiv using combinations of `Rydberg electrometry`, `atomic receiver polarisation`, `full Stokes microwave`, `reconfigurable metasurface polarimetry`, `Stokes instrument conditioning`, `Rydberg mixer phase` and `circular discrimination`. Record title, DOI, year, platform, measurement basis, frequency, experimental/simulation modality, demonstrated S3 response, limitations and a relevance score. Deduplicate by DOI, map each new source to one question, and log every design decision it changes.

The bibliography is **version-controlled**; individual database search dates and screening totals were not available in the imported project files, so no PRISMA-style systematic-search claim is made.
