# Project-specific visual atlas: exact project evidence versus original teaching diagrams

**Priority:** use the actual source images already in the research archive. Do not use unrelated stock laboratory imagery, random CAD copper topology or a fabricated spectral trace to fill visual space.

## A — Actual optical and RF experiments

### Optical laboratory apparatus (experimental photograph)

![Optical Rb-87 laser and RF research setup from documented lab source](../site/assets/lab-optical-bench.png)

**Source:** [Original manuscript laboratory Figure 1](../papers/manuscript-source/figures/F01_REAL_LAB_PHOTO.pdf). **Claim supported:** documented apparatus layout. It is not by itself evidence of a fully calibrated optical full-Stokes receiver.

### Measured linear-polarisation response

![Measured linear polariser experiment in the research manuscript](../site/assets/linear-polarisation-experiment.png)

**Source:** [Original measured linear polariser research figure](../papers/manuscript-source/figures/FINAL_F06_LINEAR_EXPERIMENT.pdf). **Claim supported:** linear polarisation only. A physical S3 state is not independently measured by rotating a linear reference.

## B — Native HFSS and derived scientific figures

### Candidate optimisation

![HFSS electromagnetic candidate optimisation figure](../site/assets/hfss-optimisation.png)

**Source:** [Paper figure F07](../papers/manuscript-source/figures/FINAL_F07_OPTIMISATION.pdf). Model-based 36-candidate screening with frequencies and criteria tied to the versioned source.

### Independently adapted periodic mesh

![HFSS mesh validation study](../site/assets/hfss-adapted-mesh.png)

**Source:** [Paper figure F08](../papers/manuscript-source/figures/FINAL_F08_ADAPTED_RESULTS.pdf). This is the specific periodic mesh result; it cannot replace a failed finite-array cross-calibration check.

### Stokes instrument response

![Derived six-state complex field Stokes response](../site/assets/stokes-instrument-response.png)

**Source:** [Paper figure F09](../papers/manuscript-source/figures/FINAL_F09_STOKES_AB_VECTOR.pdf). Source-determined simulation-derived response, not a measured Rb-87 optical output.

### Finite observation distance

![Numerical finite-panel distance and response analysis](../site/assets/finite-distance-sensitivity.png)

**Source:** [Paper figure F10](../papers/manuscript-source/figures/FINAL_F10_FINITE_DISTANCE.pdf). Check actual cell observation plane, mask and mesh before claiming finite transfer.

## C — New original and editable research-teaching schematics

### Quantum optical / microwave ladder

![Original conceptual Rydberg EIT optical and microwave ladder](../site/assets/academy-ladder.svg)

**Type:** conceptual SVG. Illustrates 780/480 nm steps, an RF-coupled neighbouring level and the measured optical observable. The exact measured nℓj and magnetic states must be obtained from ARC and experiment; line spacing is not to scale.

### Source-to-claim analysis pipeline

![Original source-aware HFSS to Stokes data flow](../site/assets/academy-hfss-pipeline.svg)

**Type:** conceptual SVG with grounded project metrics and limitations. Source complex fields, instrument A, periodic and finite cases must not be conflated.

### Original laboratory diagnosis decision tree

![Source-aware atomic/RF/HFSS fault isolation](../site/assets/academy-diagnostic-tree.svg)

**Type:** workflow SVG derived from source-specific calibration and verification protocols, not a screenshot of a completed experiment.

## Rules for adding the next figure

1. Add the native image/drawing and source project path; if a personal/supplier photo, obtain release approval first.
2. Record **measured, HFSS-native, derived, proposed or illustrative** modality, date, design revision, frequency and actual observation plane.
3. Associate code, original complex fields/raw trace, figure units, and source checksum in [the figure provenance ledger](../docs/results/FIGURE_PROVENANCE.md).
4. Use meaningful screen-reader alt text and avoid mismatched captions.
5. In publication, a unit cell artwork is not proof that a full finite board was fabricated or calibrated.

[Book home](README.md) · [Project figure provenance](../docs/results/FIGURE_PROVENANCE.md) · [Lab diagrams](../site/lab.html) · [Current status](CURRENT_STATE.md).
