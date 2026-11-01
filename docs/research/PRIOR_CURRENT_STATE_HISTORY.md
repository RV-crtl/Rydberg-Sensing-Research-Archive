# Prior source-based project state and historical validity — which result should we trust?

**Last scientific baseline reviewed:** V44 paper/HFSS archive, 24 October 2026; archive update 31 October 2026. **Checked:** 1 November 2026. Updating the repo is not the same as running new HFSS simulations.

## Current documented periodic HFSS result — use this first for the paper's numerical claims

- **Case:** C033 six-state, two-face/single-board concept, simulation-derived Stokes instrument basis.
- **Frequency:** 1.925 GHz chosen operating point; selected row-normalised condition number **κ₂≈9.53**, rank **4**.
- **Optimisation:** 36 candidates; a longest **accepted sampled** interval of 250 MHz versus 175 MHz comparison, not a demonstrated continuous RF/hardware band.
- **Mesh:** about **0.551%** disagreement for the reported selected *periodic* adapted-mesh check under its specified metric.
- **Offline inference:** 1,231 algebraic Poincaré tests are not 1,231 independent HFSS field solutions. Modelled 40.8% fixed-time inverse-trace criterion improvement is not a measured atomic SNR improvement.
- **Source:** [main findings](../../docs/results/KEY_FINDINGS.md), [HFSS numerical records](../../evidence/hfss/v44-reproducibility/), [editable manuscript](../../papers/manuscript-source/main.tex).

## Finite-aperture status — do not substitute periodic data

- Historical V4.21 finite **3×3** at 5 mm: matrix discrepancy about **6.18%**, worst cross-mesh transfer about **76.92%**; at 10 mm, about **55.09%** worst transfer. These **failed** the stated finite-calibration-transfer requirements.
- V4.22 documents a corrected HFSS finite-mesh configuration but does not by itself establish that corrected case results were successfully completed.
- The 3×3 finite panel may retain rank four under some models while remaining unreliable to transfer-calibrate. Explicitly separate matrix rank, gain, singular spectrum, mesh and optical signal.
- [Original diagnostic study](../../docs/results/HFSS_V411_V422_ORIGINAL_DIAGNOSTIC_EVIDENCE.md) · [HFSS native-source SOP](../../docs/methods/HFSS_NATIVE_RESULT_REPRODUCTION.md).

## Historical experimental evidence

- The earlier Rb-87 780/480 nm optical RF receiver, rod-grid polariser, antenna and coil studies are **laboratory context**, not a completed full-Stokes Rb-87 receiver.
- The earlier roughly 14–15 dB steel-rod comparison and later roughly 9.7 dB linear-polarisation estimate come from **different RF reference conditions** and should not be averaged or silently interchanged.
- Linear rotated polariser data can constrain **S1/S2** only; physical **S3** requires an independent handedness-sensitive response with source calibration.
- Zeeman-bias strategy was investigated but did not produce a reliable full-Stokes atomic receiver; the programme then emphasised the RF front-end measurement-basis design.
- [Laboratory summary](../../docs/laboratory/POLARISATION_MEASUREMENTS.md) · [interim report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf).

## Historical design streams — preserve, but do not present as the final hardware

Crossed bow-tie/split-ring RO4003C 70×50 mm proposals, RO4350B 200 mm-class etch constraints, SAP18B, tetrahedral, circular spiral selectors, 4-state early screens, and CST/MATLAB explorations each answer different engineering questions. Their date, geometry, substrate, switch representation and calculated observables must travel with their plots.

[Original design history](../../history/README.md) · [Metasurface lineage](../../docs/design/POLARISER_AND_METASURFACE_DESIGN_LINEAGE.md).

## Active scientific tasks

1. Establish full optical and RF reference-state calibration, including circular/elliptical states and signed Jones convention.
2. Verify finite aperture using native complex-field HFSS independent mesh + common physical observation volume and enough independent masks.
3. Implement real switching parasitics/PCB manufacturing acceptance, rather than ideal copper bridge abstractions.
4. Use ARC to screen the actual Rb-87 quantum-state optical/RF access and RydIQule to calculate physically parameterised multilevel spectra; do not invent transitions.
5. Transfer a demonstrably converged finite analyser basis into **measured** optical atomic responses; determine errors from held-out reference states.
6. Preserve all underlying source data, exact solver versions and figure links; report negative results where they constrain acceptance.

## Literature novelty boundary (as of 1 November 2026)

Full 3D atomic RF polarimetry with orthogonal LOs was demonstrated in **2024** (Elgee et al., DOI 10.1103/PhysRevApplied.22.064012). **2026** literature includes Chilcott et al.'s spectroscopic Poincaré polarimetry (arXiv:2605.14529) and Schlossberger et al.'s experimentally validated multilevel elliptic-AT explanation (Phys. Rev. A 114, 033701, DOI 10.1103/w5k9-1mlh). Our contribution must be framed around the engineered measurement basis and its quantified limitations, not as the world's first atomic polarimeter. [References](../../book/REFERENCES.md).
