# Complete research handover

**Programme:** Rydberg-87 RF receiver and information-aware microwave metasurface polarimetry  
**Primary research author:** R. N. Verghese  
**Archive date:** 31 October 2026  
**Handover purpose:** enable a new researcher to understand, validate and extend the work from source evidence rather than reconstructing decisions.

## 1. Executive overview

Two linked technical workstreams have been pursued. The experimental stream covers 780/480 nm Rydberg-EIT reception, polarisation RF hardware and laboratory characterisation. The simulation stream develops a programmable microwave analyser that produces a Stokes measurement basis, with source-backed HFSS data and optimisation/verification scripts. The current paper reports simulation results; it should not be read as a demonstration of a complete experimentally calibrated atomic full-Stokes receiver.

## 2. What is already in this handover

| Deliverable | Location | How a successor uses it |
|---|---|---|
| Experimental report | [`reports/`](../../reports/) | Setup, measured RF/optical work and scientific rationale |
| Current editable IEEE Access manuscript | [`papers/manuscript-source/`](../../papers/manuscript-source/) | Full text, equations, citations, figures and scripts |
| HFSS source evidence and compact native-return archives | [`evidence/hfss/v44-reproducibility/`](../../evidence/hfss/v44-reproducibility/) | Reanalyse electromagnetic evidence and numerical validation |
| Figures, research poster and speaking notes | [`presentations/`](../../presentations/) | Research communication, apparatus and visual context |
| Hardware and portable design | [`docs/engineering/`](../engineering/) and [`designs/`](../../designs/) | Architecture and proposed equipment |
| Code | [`research-code/`](../../research-code/) and analysis folders | Offline reproduction and method extension |
| Traceability index | [`docs/traceability/`](../traceability/) | Link rubric, evidence, assets and design decisions |

## 3. Key results to inherit

The article identifies a selected periodic simulation result at 1.925 GHz with rank 4, κ₂ 9.53 and 0.551% independent mesh discrepancy; the scanned accepted interval reaches 250 MHz and a declared model-based fixed-time information metric improves by 40.8% with optimised state dwell. Finite 3 × 3 results inform calibration transfer and S3 sensitivity. The June experimental report documents RF polarisation characterisation, Helmholtz calibration and exploratory atomic readout. **Numbers must be rechecked against their exact source before being used in a new paper.**

## 4. First-week successor checklist

- Day 1: map the [research narrative](../research/RESEARCH_NARRATIVE.md), [literature](../research/LITERATURE_MAP.md) and [claim ledger](../traceability/CLAIMS.md).
- Day 2: run repository [integrity audit](../../scripts/verify_archive.py), [unit tests](../../tests/) and inspect the manifest.
- Day 3: inspect the actual source files and figure reproducibility using the [simulation SOP](../methods/HFSS_SOP.md).
- Day 4: inspect optics/RF safety documentation, calibration, equipment and [experimental SOP](../methods/EXPERIMENTAL_SOP.md) with an authorised laboratory custodian.
- Day 5: write a precise continuation plan with hypotheses, acceptance gates, instrumentation permissions, candidate validation and reproducibility output list.

## 5. Priority extension work

1. **Source completeness:** import native `.aedt` projects, underlying raw field exports not present in the compact archive, original oscilloscope/VNA raw files and experiment logbooks with metadata.
2. **Model transfer:** refine finite-aperture and circular-component sensitivity; quantify what matters for a rubidium cell ROI and fixed photodetection observable.
3. **Hardware engineering:** formalise manufacturing revision, switching-circuit electrical realism and PCB verification test plan before any fabrication claim.
4. **Atomic integration:** connect the calibrated electromagnetic analyser states to measured optical Rydberg observables, with traceable inversion and independent controlled polarisation inputs.
5. **Evidence communications:** prepare an explicit uncertainty budget and publication-ready cross-links between claims, source data, scripts, plots and design parameters.

## 6. Data ownership and release

Treat original manuscripts, raw laboratory files, suppliers, field datasets and lab photos as controlled records unless authorised for open publication. Follow [release policy](../operations/RELEASE_POLICY.md). No blanket licence has been granted for third-party/publisher assets.

## 7. Scope currently not documented with primary records

The accessible import did not establish actual supplier invoice/payment records, formal fabrication/assembly orders, full AEDT project files, complete laboratory raw waveform/VNA datasets or external industry meeting records. These are **source-completeness items**, not an assertion that such work never occurred. Use the [import intake](SUCCESSOR_ONBOARDING.md) and [asset register](../traceability/ASSET_REGISTER.csv) to add verifiable materials without inventing metadata.
