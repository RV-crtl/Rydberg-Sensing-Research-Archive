# Research design decision log

| Decision | Basis | Trade-off and trace |
|---|---|---|
| Adopt Stokes / Jones and instrument-matrix framework | RF polarisation contains phase/handedness information that scalar readout alone does not resolve | Multiple independent states needed; see [literature map](../research/LITERATURE_MAP.md) |
| Evaluate polarisation-selective hardware alongside atomic receiver | RF conditioning controls the field before atomic optical readout | Separate calibration of RF hardware and optical response; [experimental report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf) |
| Build a two-face switch-programmable analyser | Reconfigurable geometric response produces distinct measurement basis | Requires explicit state geometry and switching assumptions; [manuscript](../../papers/manuscript-source/main.tex) |
| Choose rank, conditioning and gain-aware information objectives | Recoverability depends on independent rows and reliable signal | Must test mesh/finite transfer, not rank alone; [HFSS SOP](../methods/HFSS_SOP.md) |
| Retain native solver-return evidence and field provenance | Reviewer and successor require inspection and reproducibility | Includes source hashes, scripts and numerical CSV; [evidence](../results/EVIDENCE_INDEX.md) |
| Optimise state time allocation under declared model | States differ in information content | 40.8% improvement is a model objective, not experimental measurement; [results](../results/KEY_FINDINGS.md) |
| Separate experimental and HFSS conclusions | Different validation modalities | More accurate science and future independent calibration; [claims](CLAIMS.md) |

Add a date, approver, alternatives and linked decision-specific datasets to this ledger as future source records are imported. Historical decision dates are not inferred from file versions.
