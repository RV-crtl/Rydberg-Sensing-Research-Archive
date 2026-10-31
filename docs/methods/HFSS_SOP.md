# Standard operating procedure: HFSS metasurface verification

## Scope and environment

Reproduce work only using an appropriately licensed version of Ansys Electronics Desktop / HFSS matching the project's verified solver model. Historical scripts include PyAEDT/HFSS workflows; pin their versions in each campaign. This archive includes numerical source exports but does **not** contain the full native `.aedt` databases needed to recreate every solve automatically.

## End-to-end process

1. **Select the exact campaign:** determine geometry branch, substrate, excitation basis, switching states, periodic vs finite modelling, units and analysed frequency band. Do not splice different branches.
2. **Recreate/inspect geometry:** review metal objects, minimum gap, dielectric and sheet assignments, ideal bridge positions and local receiver ROI.
3. **Configure solver:** record boundary types, plane-wave wavevector and Jones excitations, radiation/PML settings, ports if present, analysis setup, mesh and convergence stop rule.
4. **Run the specified excitation cases:** preserve separate X/Y complex fields (and any circular reference solutions used for checks), one record per state and frequency.
5. **Export authoritative results:** complex Ex/Ey/Ez, observation points, S-parameters where modelled, solver convergence, mesh stats, setup logs and source geometry.
6. **Analyse:** calculate relevant quadratic observation for each switching state; populate matrix `A`; evaluate singular values, rank and condition number with documented normalisation. Keep gain metrics distinct.
7. **Independent numerical validation:** repeat with adapted mesh/boundary convergence criteria. Compare at identical physical observation locations and units; record exact gates, not just PASS/FAIL.
8. **Physical transfer checks:** inspect finite-aperture and distance dependence, S3 sensitivity, and whether a calibration derived from periodic/independent mesh transfers.
9. **Release:** publish exact CSV/JSON/solver logs, script commit and source SHA-256, with labelled figure provenance. Add `.aedt` and `.aedtresults` only when available, permissible and safely compressed.

## Command examples for included offline material

```bash
python scripts/verify_archive.py
python -m unittest discover -s tests -v
python scripts/summarise_evidence.py
```

The scientific paper figure script expects additional Python packages; use a separate virtual environment and run it from `papers/manuscript-source` after checking its own dependencies and path assumptions. No new HFSS field data are fabricated by these offline commands.

## Re-run checklist

- All six states and both complex linear excitation bases present.
- Complex phase conventions and units documented.
- Matrix rank 4 and condition number evaluated at exact source frequency.
- Source hashes verified, and all paper plots link back to source data.
- Finite-array, mesh and S3 transfer tests reported with their actual numerical results.
