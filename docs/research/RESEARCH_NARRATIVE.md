# Research programme and contribution

## Research question

How can a Rydberg-atom microwave sensing architecture be paired with engineered, polarisation-dependent RF measurement states so that incident polarisation can be inferred, rather than measuring only a scalar field strength?

## Scientific basis

The 780 nm probe and 480 nm coupling beams interrogate a Rb-87 vapour cell through a Rydberg-EIT optical ladder. RF excitation can perturb the prepared Rydberg states, producing an optically readable response. RF front-end design matters because local-field direction, amplitude and phase affect the input seen by an atomic receiver.

A Stokes vector **S = [S0, S1, S2, S3]ᵀ** describes total intensity and three polarisation coordinates. Independent analyser configurations produce an observation vector **y = A S + ε**, where a calibrated instrument matrix **A** connects the incident state to the selected detection observables. Rank four is necessary for recoverability; numerical conditioning and gain affect robustness.

## Work packages

| Package | Core output | Source |
|---|---|---|
| Foundational atomic/microwave literature | Quantum electrometry, EIT/AT, vector sensing, Stokes/Jones modelling | [Literature map](LITERATURE_MAP.md) and [bibliography](../../papers/manuscript-source/ieee_references.tex) |
| Receiver design and laboratory tests | Laser, vapour cell, photodetection, RF polariser and bias-calibration investigations | [Experimental report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf) |
| RF metasurface modelling | Ideal switching-state two-face geometry and solver sweeps | [Engineering overview](../engineering/METASURFACE.md) |
| Source-backed electromagnetic inference | Complex-field extraction, 6 × 4 Stokes response, rank, condition number and mesh comparison | [HFSS evidence](../results/EVIDENCE_INDEX.md) |
| Optimisation and information design | Geometry selection, basis diversity, observation quality and dwell allocation | [Results](../results/KEY_FINDINGS.md) |
| Communication and dissemination | IEEE Access-format draft, presentations and a coauthored IEEE conference paper | [Publications](PUBLICATIONS.md) |

## Contribution statement

The archived manuscript contributes an auditable **information-aware electromagnetic design and verification methodology**: design a switchable two-face microwave analyser, extract its state-dependent complex HFSS fields, construct a Stokes instrument matrix, optimise geometry and switching-state information under explicit criteria, and test numerical stability with independent meshes and finite arrays.

This contribution is specifically **simulation-backed**. Laboratory Rydberg-EIT and linear-polarisation observations form a complementary experimental workstream, with atomic full-Stokes integration reserved for subsequent work.

## Scope of novelty

The work should not claim invention of Stokes polarimetry, Rydberg RF detection, or metasurface polarimeters. The defensible framing is the specific design/verification workflow and simulated measurement-basis arrangement for a prospective atomic receiver. Historical prior-art papers are indexed in the literature map.
