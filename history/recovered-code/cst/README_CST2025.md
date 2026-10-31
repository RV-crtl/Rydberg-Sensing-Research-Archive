# Rydberg CP analyser — CST Studio Suite 2025 automation v1.2

This bundle automates the correct first full-wave design stage for the 1.8 GHz circular-polarisation analyser discussed in the thesis work. It constructs and solves one periodic bilayer unit cell, not the full 200 × 200 mm panel. The finite panel should only be tiled and checked after the unit cell has passed optimisation, mesh convergence and tolerance gates.

## What is automated

- parametric bilayer split-ring plus intentionally isolated cross geometry;
- nominal 1.60 mm FR-4 and 35 µm copper;
- no continuous ground plane;
- periodic x/y boundaries and open z boundaries;
- two orthogonal Floquet modes on each z face;
- frequency-domain solver, adaptive tetrahedral-mesh preferences and 1.8 GHz monitors;
- complex transmission and reflection Jones-matrix export;
- conversion of the linear Jones matrices into total RCP/LCP transmitted and reflected powers;
- a guarded, reproducible nominal optimiser centred on 1.8 GHz;
- audit CSV output for every attempted optimisation point.

## Files and order

0. `00_TEST_EXPORT_PATH_CST2025.bas` — optional, non-destructive path test
1. `01_BUILD_SOLVE_EXPORT_RYDBERG_CP_UNITCELL_CST2025.bas`
2. `02_RUN_GUARDED_RYDBERG_CP_OPTIMISER_CST2025.bas`
3. `03_EXPORT_CURRENT_BEST_CP_RESULTS_CST2025.bas`

## Exact CST 2025 workflow

1. Open CST Studio Suite 2025.
2. Create a **new Microwave & RF** 3D project. If the wizard offers a periodic-structure/FSS template, use it; otherwise an empty Microwave Studio project is acceptable because macro 01 supplies the boundaries, solver and Floquet ports.
3. Save the empty project as a new `.cst` file before running anything. This is still good project hygiene, but CSV export no longer depends on CST's project-path API.
4. On the ribbon, open **Home → Macros → Open VBA Macro**. In some installations it appears simply as **Macros → Open VBA Macro** or **Open VBA Macro Editor**.
5. Optionally open and run macro 00 first. It changes no CST model state and should create `%USERPROFILE%\Rydberg_CST_Exports\CST2025_PATH_TEST.txt`.
6. Open macro 01. Put the cursor anywhere inside `Sub Main` and press **F5**, or click the VBA editor's Run button.
7. Macro 01 builds the cell, starts the baseline solve and writes `RYDBERG_CP_BASELINE_JONES_AND_METRICS.csv` in `%USERPROFILE%\Rydberg_CST_Exports` (normally `C:\Users\<name>\Rydberg_CST_Exports`).
8. In the navigation tree, confirm that `1D Results → S-Parameters` contains the eight traces listed below. Also confirm that the two Floquet modes are orthogonal fundamental plane-wave modes and that the model contains no ground plane.
9. Open and run macro 02 in the same project. Accept the prompt only after step 8. It performs about 30 solves and leaves its best parameter point active. Its complete audit trail is `RYDBERG_CP_OPTIMISER_HISTORY.csv`.
10. Open and run macro 03. It writes the final parameter table and the full-frequency complex Jones/CP table.
11. Save the CST project under a new name such as `Rydberg_CP_1p8GHz_Optimised_v1.cst`.

Do not paste the code into the Components navigation tree. It belongs in the CST VBA macro editor.

### v1.2 correction

The CST 2025 macro environment encountered by the user rejects both `GetProjectPathName("Project")` and the selector-based `GetProjectPath("Root")` form. Version 1.2 removes both CST-specific path calls from all three macros. CSV files are now written using standard VBA environment functions to `%USERPROFILE%\Rydberg_CST_Exports`, falling back to `%TEMP%` and then the current working directory only if needed. The folder is created automatically.

## Expected result-tree names

The macros expect these CST names:

```text
1D Results\S-Parameters\SZmax(1),Zmin(1)   Txx
1D Results\S-Parameters\SZmax(2),Zmin(1)   Tyx
1D Results\S-Parameters\SZmax(1),Zmin(2)   Txy
1D Results\S-Parameters\SZmax(2),Zmin(2)   Tyy
1D Results\S-Parameters\SZmin(1),Zmin(1)   Rxx
1D Results\S-Parameters\SZmin(2),Zmin(1)   Ryx
1D Results\S-Parameters\SZmin(1),Zmin(2)   Rxy
1D Results\S-Parameters\SZmin(2),Zmin(2)   Ryy
```

Some CST templates label ports numerically rather than `Zmin`/`Zmax`. If macro 01 reports “Missing result tree item,” copy the exact eight trace names from CST into the `TREE_...` constants at the top of all three macros. Do not run macro 02 until this mapping is correct.

## What the optimiser actually optimises

The optimiser does not minimise one arbitrary `S21` curve. For each candidate it constructs the complex matrices

```text
T = [Txx Txy; Tyx Tyy]
R = [Rxx Rxy; Ryx Ryy]
```

and transforms them to a circular basis. It then calculates total transmitted power for each circular input, including any cross-hand conversion. The score uses the worst performance at 1.75, 1.80 and 1.85 GHz:

- pass-state insertion loss;
- blocked-state attenuation;
- circular extinction ratio;
- pass-state reflected power;
- numerical power excess as a validity penalty.

The geometry constraints enforce the 0.50 mm nominal minimum feature and copper-to-cell clearance, maintain `rOut > rIn`, and keep the internal cross disconnected from the ring.

## Important claim boundaries

- The starting cell is a material-aware dimensional seed based on Shah et al., *Scientific Reports* 11, 1774 (2021), DOI `10.1038/s41598-021-81435-w`. It is not a reproduction of that paper's result because the substrate and target frequency are different.
- The custom search is a reproducible local refinement. It cannot prove a global optimum or “perfect” performance.
- FR-4 is variable. A publishable release must test at least εr = 4.0, 4.3, 4.6 and 4.8, loss-tangent variation, 1.50–1.70 mm substrate thickness, copper/etch tolerance, and incidence angles such as 0°, 15° and 30°.
- Repeat the final model with successively finer meshes until the CP pass loss and extinction change negligibly. A plausible first gate is less than 0.1 dB change in pass loss and less than 0.5 dB change in extinction, but the thesis should state and justify its chosen gate.
- After optimisation, expand the solver range for validation. A resonant passive cell optimised around 1.8 GHz should not be claimed to discriminate CP from hundreds of MHz to 6 GHz unless full-wave results and measurements actually demonstrate that bandwidth.
- A 200 × 200 mm panel at the seed period contains 8 × 8 complete cells with generous edge margin. Panel tiling, finite-aperture plane-wave/horn modelling, fixtures and the Rydberg-cell environment are separate validation models.

## Complementary handedness

Macro 01 uses `BOTTOM_TWIST_SIGN = 1`. To build the complementary enantiomer, create another new CST project, change that constant to `-1`, and run macro 01 again. The R/L labels can swap with the phasor convention or illumination direction; the pass/block power and extinction calculations remain invariant to that label swap.

## If macro 01 stops

Record:

- the exact stage and error number shown in the message box;
- the CST edition/licence;
- the project template chosen;
- a screenshot of the navigation tree and the first 30 lines around the highlighted VBA line.

Do not repeatedly run macro 01 in the same partly built project. Start a fresh empty project for each corrected attempt.