# PCB design and manufacturing specification history

These are **documented design constraints from historical project branches**, not blanket final specifications for every HFSS model. Before manufacture, freeze one geometry and reconcile it with exact simulation sources.

## Earlier fabrication envelope

| Constraint | Historical design value | Engineering significance |
|---|---|---|
| Maximum available panel | 200 × 200 mm | RF aperture and process envelope |
| Typical unused edge buffer | 5 mm | Handling and copper clearance |
| Rubidium-cell relevant field region | Approximately 70 × 50 mm | Defines local receive ROI, not automatically board size |
| Rogers laminate | RO4350B, approximately 1.52 mm thick | Candidate dielectric substrate; use correct grade/datasheet for final design |
| Copper | Nominal 35 µm on two sides | Copper thickness for geometry and fabrication |
| Minimum copper feature | 0.5 mm targeted for in-house etching | Process feasibility limit; independent of HFSS mesh |
| Manufacturing exploration | Two-sided artwork and etch process | Process branch separate from current final manuscript simulator |
| RF targets across historical studies | 1–2 GHz and selected alternative ~5.788 GHz | Different branches, **not one broadband validated device** |

## Fabrication-readiness gate

A final board release requires a verified source geometry, exact coordinate system, BOM, material stack-up, verified copper-to-edge/gap dimensions, bias network design, manufacturer DFM acceptance, assembly test plan and test fixture. Simulation switch-bridges must be replaced by a physically characterised switch model before claiming hardware equivalence.

### Handover outputs for each manufactured revision

- Schematic, PCB layout and editable CAD source with explicit revision number.
- Gerbers, drill files, layer stack-up, DFM plots, pick/place data, complete BOM and manufacturer correspondence.
- Fabricated-board photographs, dimensions, unique serial number, continuity and RF-test results.
- Traceability back to matching HFSS parameters and a controlled calibration/verification dataset.

See [manufacturing register](../operations/MANUFACTURING.md), [BOM](../operations/BOM.csv), and [RF model](METASURFACE.md).
