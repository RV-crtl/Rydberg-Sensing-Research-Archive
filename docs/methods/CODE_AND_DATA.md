# Code, data dictionary and reproducibility

## Code inventory

| Code group | Path | Purpose | Runtime |
|---|---|---|---|
| ARC/Rydberg scientific poster script | [`research-code/arc`](../../research-code/arc/) | Transition/theory figure and Rydberg calculation source as supplied | Python, inspect imports |
| HFSS analysis and verification | [`evidence/hfss/v44-reproducibility/analysis`](../../evidence/hfss/v44-reproducibility/analysis/) | Simulation evidence reduction and verification | Python, campaign-specific numerical dependencies |
| Article figure regeneration | [`papers/manuscript-source/figure_source`](../../papers/manuscript-source/figure_source/) | Produce source-backed paper figures | Python / NumPy / pandas / Matplotlib |
| Manuscript citation and standalone validators | [`papers/manuscript-source/supplementary_data`](../../papers/manuscript-source/supplementary_data/) | Check article assets and bibliography | Python |
| Archive audit | [`scripts/`](../../scripts/) | Hashes, internal links, source inventory, basic statistical summary | Python standard library (optional NumPy for numerical summary) |

## Data dictionary

| Field / file family | Definition and use |
|---|---|
| `Ex`, `Ey`, `Ez` | Complex Cartesian electric field components, source values tied to observation plane/ROI/frequency |
| `S0`, `S1`, `S2`, `S3` | Stokes coordinates, following stated handedness convention |
| `A0`–`A3` | Coefficients of an instrument matrix row mapping Stokes to the observation in a given state |
| `frequency` | Solver frequency; verify Hz/GHz units per native export, do not guess |
| `rank` | Number of independent matrix columns at a selected tolerance |
| `kappa2` / `condition_number` | 2-norm singular-value ratio after specified row or gain normalisation |
| `mesh_stats`, `*.conv` | Solver geometry/convergence evidence; not physical measurements |
| `*_ALL_SUBSETS.csv` | Analysis over combinations of switching states and information objective |

## Clean reproducibility

To inspect the archive with no HFSS license:

```bash
python scripts/verify_archive.py
python scripts/summarise_evidence.py
python -m unittest discover -s tests -v
```

Any numerical plot regeneration must use the underlying **native HFSS-derived source CSV**, not illustrative noise values. If a script uses a stochastic noise model (for example a Monte Carlo uncertainty illustration), label the model assumptions separately from electromagnetic simulation evidence and measured noise.
