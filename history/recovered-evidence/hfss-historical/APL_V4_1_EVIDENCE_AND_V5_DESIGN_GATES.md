# V4.1 scientific audit and mandatory V5 design gates

**Source**: `RETURN_TO_CHATGPT_APL_OPTIMIZER_V4_20261018_174602.zip`. All numerical statements below originate in this archive or are explicitly marked as engineering proposals.

**Archive SHA-256**: `eb152d0c6ff83832fb04a04d6812378f1c6b4b728af82d87d37fed1b5129c1df`.

## 1. Verified HFSS execution verdict

- V4 verdict: `MAX_CANDIDATES`; `12` complete new designs. 12×8=96 independent X/Y state solves plus one V0001/T1/45-degree solve = 97. Four-state geometry smoke test passes.
- Campaign reached `max_new_candidates=12`, not the four-hour timeout. The V4 main log shows approximately 123 minutes remaining on reaching the final candidate.
- Best *composite objective*: `V0010`; worst-frequency EM condition `1026.758374`; minimum S3 L2 sensitivity `0.070961`.
- Neither the condition ≤12 nor S3 ≥0.20 screening gate passes. All electromagnetic results are coarse P35A, not independent mesh-validated final data.
- Independent 45-degree superposition test on V0001/T1 differs by 4.766%, 4.771%, 4.776% across the three narrowband frequencies; this is near a 5% screen and does not establish full convergence.

## 2. Why the architecture fails

The actual V0010 normalized instrument matrix at 1.675 GHz, `MATRIX_V0010_P35A_1.6750.csv`, gives the following analysed Stokes direction vectors:

| State | n1 | n2 | n3 | Py/Px inferred from n1 |
|---|---:|---:|---:|---:|
| T1 | +0.997816 | -0.062725 | -0.018362 | 0.00109324 |
| T2 | +0.996027 | -0.085725 | -0.018861 | 0.00199037 |
| T3 | +0.999825 | -0.017798 | +0.000706 | 8.75162e-05 |
| T4 | +0.975681 | -0.207807 | -0.066122 | 0.012309 |

- Maximum angular separation across states: 11.645 degrees (states T3 and T4), versus 109.47 degrees for the ideal four-state tetrahedron.
- All four normalized directions cluster near +S1. Individual analyser *purity* is not the limiting factor; *diversity* and orthogonal-input power balance are.
- Present copper arms are roughly 13–20 mm long; the 1.675 GHz free-space wavelength is about 179 mm. A loaded resonance and useful RF conversion are **not proven** by the narrow 1.670–1.680 GHz sweep.
- The objective strongly depends on uncalibrated atomic parameters; rewarding a small change in a still-degenerate instrument matrix is not a successful design criterion.

## 3. Covariance mechanism: measured evidence boundary

- The four-level weak-probe calculations show information improvement in 6/12 new designs versus the model-specific same-mean uniform counterfactual. The other 6 lose information.
- V0010: information ratio 1.003949 (only 0.395% relative improvement), assumed worst-direction Fisher eigenvalue 8.88195e-05.
- V0012: largest ratio 5.7293, but its assumed absolute Fisher eigenvalue is 2.6989e-08. Do not claim this as useful sensing performance.
- Rb transition, dipole, laser axis, magnetic quantisation axis, detector noise, optical depth and PIN parasitics are not calibrated. The covariance expansion is mathematical; an experimental physical improvement is not established.

## 4. Mandatory next-campaign design and implementation gates

| Gate | Test and required outcome | On failure |
|---|---|---|
| 0. Physics and coordinates | Freeze x/y/z axes, plane-wave direction, actual laser beam path, Rb transition(s), selection rules, Stokes S3 convention; record uncertainty where unknown. | No physical atomic performance claim; allow EM-only labelled exploration. |
| 1. Resonant RF mechanism | Sweep wider frequency range to locate x/y resonant modes and measure actual cross-coupling `h_y→E_sensitive` rather than assuming copper-arm resonances. Include bare-cell baseline. | Retune/rearchitect; do not run eight-case codebook search. |
| 2. True state diversity | One fixed physical PCB with selectable **complex** x/y coupling; tune amplitude balance, cross-polarisation response and relative phase. Require a state set that is not clustered near ±S1, with signs and directions spanning S2 and S3. | Change topology/phase network, not just geometric dimensions. |
| 3. Cheap HFSS go/no-go | For a new architecture run two independent X/Y excitations for a representative state, inspect local complex transfer ratio, and only then complete four-state eight-case screen. Rank-4 alone is insufficient. | Reject architecture immediately if orthogonal coupling or phase control missing. |
| 4. Objective and target | Optimise min singular value of a noise/throughput-normalised Stokes operator, plus nuisance-marginalised minimum Fisher eigenvalue and S3 sensitivity; preserve output powers and measurement time. Initial `κ≤12`, `η3≥0.20`; prefer `κ≤6` with both S3 signs. | Report failed feasibility, no publication-ready or fabrication flag. |
| 5. Nonlinear covariance | Compute full spatial and mean-field counterfactual Jacobians under identical RF power/noise/time. Report **absolute** information, ratio and approximation residual; compare EM-only against covariance-aware designs. | Reject claims based only on large relative ratios. |
| 6. Independent Maxwell numerical checks | Re-solve a promising state at independent P35D/P35E meshes and boundary domains; compare weak transfer components, phases, `η3` and instrument-matrix coefficients, not only total energy. Student volume-element limit must be respected. | No full-field quantitative claims. |
| 7. Independent excitations | Direct 45-degree, circular and elliptical HFSS excitations with conserved amplitude/phase conventions; compare against X/Y superposition. | Diagnose phase reference and mesh sensitivity. |
| 8. Switching and fabrication | Replace ideal copper bridges with practical diode ON/OFF RLC and routing; preserve one-board size/material constraints, 0.5 mm minimum features, edge clearances, and RF bias isolation. | Device is conceptual only. |
| 9. Return integrity | Atomic verification of every file/hash, checkpoint versioning, all-case provenance, correct count and a complete ZIP; launch a real short HFSS solve after geometry preflight. | Stop immediately with one actionable log. |

## 5. Topology decision

Keep V0010, V0007 and Q0010 as baselines. Introduce an explicitly coupled orthogonal-mode or bianisotropic/dual-layer-on-one-PCB architecture with a tunable relative-phase network. The V4 geometry is four largely separated, electrically small resonator elements; codebook permutations alone do not enforce distinct atom-weighted Jones transfer vectors.
A two-sided PCB with vias and/or genuine phase-selective reactive switching is a **design option**, not an automatically approved change: verify PCBWay/manufacturing conditions before substituting for the single-sided baseline.

## 6. Budget and stop conditions

- Stage A (offline, no HFSS): derive candidate-mode geometry and confirm physical switch topology and coordinates.
- Stage B (first ~30–60 min estimate, hardware-dependent): broad resonance/cross-coupling diagnostic on 2–3 architectures. Stop immediately if no physically meaningful Y→sensed-axis transfer.
- Stage C (remaining ~1–3 hours if warranted): eight-case screens only for architectures that pass the physics gate; stop at fixed time budget, not solely at a small candidate count.
- Stage D (separate validation budget): independent mesh/boundary and direct polarisation/diode tests only for accepted candidates.
- In all cases return best **verified** candidate and an explicit pass/fail decision; no absolute global-optimality guarantee.

## 7. Candidate ranking extracted from this return

| Candidate | Worst EM κ | Minimum S3 L2 | Assumed spatial / uniform information ratio |
|---|---:|---:|---:|
| V0001 | 6,005.4 | 0.0326 | 0.9853× |
| V0002 | 1,913.7 | 0.0398 | 0.7761× |
| V0003 | 1,839.0 | 0.0708 | 1.0109× |
| V0004 | 2,939.7 | 0.0424 | 0.9311× |
| V0005 | 23,991.0 | 0.0518 | 1.1054× |
| V0006 | 25,049.4 | 0.0435 | 0.7538× |
| V0007 | 2,837.8 | 0.0539 | 1.0397× |
| V0008 | 4,786.1 | 0.0343 | 0.8729× |
| V0009 | 2,231.0 | 0.0458 | 0.9330× |
| V0010 | 1,026.8 | 0.0710 | 1.0039× |
| V0011 | 30,604.0 | 0.0280 | 1.1174× |
| V0012 | 3,458.6 | 0.0311 | 5.7293× |

## 8. Manuscript claim boundary

May report 97 new successful solves, four-state geometry preflight, candidate comparisons, mathematical covariance theory, and conditional weak-probe information results. Cannot report calibrated Rb polarimetry, a novel law, independent patterned-mesh convergence, demonstrated PIN diode switching, strong broadband performance, global optimum or fabrication-ready design.