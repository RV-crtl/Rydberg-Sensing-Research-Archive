# RF polariser and metasurface design lineage

The programme investigated **multiple independent design families**. Dimensions, substrate material, operating frequency and switch counts below describe *historical individual candidates*, not one fabricated board. Before reproducing, consult the exact source geometry, electrical model and return archive.

## Design-family comparison

| Family / period | Geometry and construction | Target / rationale | Verification |
|---|---|---|---|
| Laboratory wire/rod grid (May–June) | ~230 × 230 mm grid with 6 mm steel rods and ~30 mm pitch | Practical low-GHz linear H/V discrimination | RF reference measurements in experimental report |
| Analytical strip grid (Aug) | double-sided copper grids on Rogers RO4350B, including a 500 × 500 mm exploratory 1–20 GHz concept, ~0.75 mm pitch, 0.45 mm strip, 0.30 mm gap | Broad linear extinction and fabricability research | MATLAB analytical/surrogate branch; **not** proof of 1–20 GHz full-wave performance |
| In-house 200 × 200 mm polariser (Aug) | FR-4 or RO4350B, 1.6 mm nominal, two-sided 35 μm copper | RF PCB Toolbox/Antenna Toolbox, SVG artwork, finite aperture and laser clearance | Analytical and manufacturing-design study |
| Chiral CP selector (Aug–Sep) | two copper faces; split loops/spirals/chiral geometry; RF handedness response | Add S3-sensitive analyser axis beyond the linear equator | MATLAB/CST/HFSS candidate screening, not a measured circular selector |
| X-BSR 70 × 50 mm design basis | crossed/bowtie split-ring design, local field enhancement near cell | Contrast available finite aperture vs field-volume gain | Design basis and proposed fabrication package; no inferred manufactured batch |
| SAP18B four-state board (Sep) | 200 × 200 mm RO4350B; recorded CAD specification included 726 copper polygons, 754 gaps, 230 ideal/switch sites and 825 sample points in the atom ROI | Multi-state full-Stokes observability at 1.8 GHz | Automated HFSS setup/screening; synthetic offline unit tests alone were **not** HFSS proof |
| TetraVia–Omega concept (Sep) | 220 × 220 × 1.524 mm RO4350B, 8 × 8 cells, chiral/omega, PIN/via states | Four-state tetrahedron-inspired analyser | Concept/source-Gerber stage; outside some 200 mm manufacture limits; “seed” data not fabrication release |
| V5xx finite resonator (Oct) | ~70 × 50 mm Rogers RO4003C (0.813 mm), 35 μm copper; four-arm folded/meander resonator with four ideal bridges | Compact, local, four-state polarisation readout | HFSS candidate mesh/response runs; limited validation transfer and S3 tradeoffs |
| Later two-face six-state split-loop (Oct) | double-sided copper on ~1.6 mm dielectric; four ideal switch locations, six selected states; a periodic reference cell ~43 mm in some evidence | Conditioned six-row Stokes projection over an L-band sampled interval | HFSS evidence in preserved V44 archive; periodic/finite qualifications |

**Material consistency:** RO4003C and RO4350B are not interchangeable. Values such as εr ≈3.48–3.55, loss tangent, 1.524/1.6/0.813 mm thickness and the 35 μm copper must be taken from the exact candidate's simulation project, not normalised away in retrospective writing.

## Engineering design objectives

### Linear discriminator
A conventional strip/rod grid should transmit one linear field component with acceptable insertion loss and attenuate the orthogonal component. Design studies examined strip pitch, copper coverage, resonance and aperture effects. Use frequency-resolved complex transmission and reflection, linear extinction, orientation and incidence-angle checks. A single ideal analytic dB estimate is not a calibrated measured 200 mm board.

### Circular/elliptical discriminator
To access the missing Stokes coordinate S3, the analyser needs independent circular-handedness sensitivity or a measurement basis containing non-coplanar analyser vectors. Chiral/spiral/split-loop geometries and two-face coupled resonators were considered. Axial ratio, RHCP/LHCP transmission and local field projections must be checked with a fixed handedness convention and phase-sensitive Jones components. Full-Stokes observability does not automatically mean low-noise S3 estimation.

### Reconfigurable multi-state measurement basis
Rather than assuming that a large circular-selectivity score alone solves the inverse problem, the later work optimised the *measurement instrument* A. For a vector S = (S0,S1,S2,S3)^T and calibrated observations y, use y ≈ A S + b. Check whether A has full column rank; then condition number, singular spectrum, gain/dwell information, spatial averaging and physical state compatibility. A good state subset must remain distinct after finite-aperture and mesh effects.

## Fabrication constraints and output gates

Historical in-house constraints were at most **200 × 200 mm**, a **5 mm edge/optics buffer**, minimum process feature **≥0.5 mm**, two-sided copper, nominal **35 μm** foil, PCB artwork export to SVG/Adobe workflow, and a two-step ferric-chloride etch process (approximately 0.5 L discussed). A 500 × 500 mm concept and some 220 mm candidates are **outside that stated in-house board size**; they remain historical studies, not approved drawings.

The physical rubidium-cell aperture of approximately **70 × 50 mm** is a *sensing region*, not necessarily the board outline. A 3 × 3 finite tile and a 200 mm-class panel are also not electrically equivalent. Biasing a practical PIN network requires DC/RF isolation, insertion/series resistance, package capacitance, drive state truth table, vias, spacing and heat/current budget—none should be silently replaced by an ideal conducting bridge in a fabrication release.

## Where to continue

- [Current engineering overview](../engineering/METASURFACE.md)
- [PCB specification and manufacture gates](../engineering/PCB_FABRICATION_SPECIFICATIONS.md)
- [Manufacturing register](../operations/MANUFACTURING.md)
- [HFSS campaign lineage](../simulations/HFSS_CAMPAIGN_LINEAGE.md)
- [V44 HFSS numerical inputs](../../evidence/hfss/v44-reproducibility/data/)
- [Historical asset discovery](../catalog/README.md)
