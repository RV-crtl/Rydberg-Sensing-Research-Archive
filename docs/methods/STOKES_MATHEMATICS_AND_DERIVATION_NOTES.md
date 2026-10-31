# Jones–Stokes instrument derivation and engineering interpretation

This is a self-contained *mathematical working note* supporting the paper's information-aware analyser discussion; it does not replace the exact manuscript's model and numerical conventions. For authoritative paper values consult [the current paper](../../papers/manuscript-source/main.tex), [6×4 matrix](../../papers/manuscript-source/data/V42_C033_INSTRUMENT_MATRIX.csv) and [reproducibility scripts](../../evidence/hfss/v44-reproducibility/analysis/).

## Four real coordinates from complex fields

Let the incident Jones vector be e=(Ex,Ey)^T, and define (one common convention)

S0 = |Ex|² + |Ey|²  
S1 = |Ex|² − |Ey|²  
S2 = 2 Re(Ex Ey*)  
S3 = 2 Im(Ex Ey*).

Some optical/radio conventions reverse the sign of S3. State the adopted convention before interpreting RHCP and LHCP; the sign of the fourth analyser coefficient must change consistently if the convention changes.

A state-selective scalar electric-field power detector can be described by y = e† H e with a 2×2 Hermitian positive-semidefinite matrix

H = [[a, c+id], [c-id, b]],

where real a,b,c,d encode the state-dependent complex response, local averaging and detection functional. Substituting the Stokes definitions gives

y = [(a+b)/2] S0 + [(a-b)/2] S1 + c S2 + d S3.

Hence the real instrument row is

A_k = [(a+b)/2, (a-b)/2, c, d].

The sign on the d term changes if S3 is defined with the opposite sign. For six switch states, stack six rows into A ∈ ℝ^(6×4). A **full column rank** implies injectivity on the real four-dimensional linear model, but says nothing alone about measurement strength, precision or model mismatch.

## Local electric-field observation

For a finite atomic sensing volume V with weighting w(r), the quadratic response can be written schematically as

y_k = ∫_V w(r) |u(r)† R_k(r) e|² dr,

for a response operator R_k and projection u (depending on the actual EIT/atomic detection assumptions). This defines an effective Hermitian H_k = ∫_V w(r) R_k† u u† R_k dr. The exact measurement observable of a real atomic system requires experimental calibration; the integral is an engineering model, **not a derivation of all atomic optical physics**.

Under HFSS, complex X- and Y-excitation field maps with identical phase/coordinate reference permit constructing R_k. Two independent intensity-only magnitudes with missing relative phase cannot uniquely determine c,d.

## Invertibility and conditioning

For W positive semidefinite, weighted least squares formally gives

S_hat = (Aᵀ W A)⁻¹ Aᵀ W (y−b)

provided the weighted system has full column rank. Row-wise normalisation is useful for assessing *basis geometry* but changes absolute gain and uncertainty properties. Report:

- σ1 ≥ σ2 ≥ σ3 ≥ σ4 and the exact numerical rank tolerance;
- κ2 = σ1/σ4 after stating any row or column normalisation;
- original row gains and any statistical weights;
- stability to frequency, mesh, illumination angle, sensing distance and finite aperture;
- physical Stokes cone S0 ≥ sqrt(S1²+S2²+S3²).

The original project considered tetrahedral four-row ideal basis geometry; the actual optimised six-row HFSS response need not be an exact ideal tetrahedron.

## Information allocation under a fixed budget

If state k has independent precision weight proportional to measurement dwell t_k / ν_k, then the information matrix has the form F = Σ_k (t_k/ν_k) a_k a_kᵀ. Subject to t_k ≥ 0 and Σ_k t_k = T, candidate criteria include minimising tr(F⁻¹) or maximising det(F), where defined. This is a **model-dependent acquisition allocation**; do not report calculated improvement as a laboratory observation.

The paper's reported **40.8% reduction** is in a particular inverse-trace criterion under the assumptions of the archived analysis. Follow [V44 fixed-budget scripts](../../evidence/hfss/v44-reproducibility/analysis/v44_fixed_budget.py) and [results JSON](../../evidence/hfss/v44-reproducibility/analysis/V44_FIXED_BUDGET_RESULTS.json) rather than reconstructing numbers by hand.

## Numerical verification

Compare A and complex field maps on matched coordinates and frequency, not images. For every periodic and finite study, record original/independently adapted mesh, units, exact norms, thresholds and state ordering. Rank and condition should be recalculated for each finite geometry instead of copying the periodic result. Independent-Mesh percentage from one selected frequency is not a universal error bound.

## Provisional aperture laws

A conditional expression previously investigated was F_r² = Γ Q_L λ A / (2π), where Γ captures geometric/sampling factors and all variables must have a clear dimensional definition. Unless a fully specified derivation and independent HFSS regime test are present, classify it as a **design hypothesis or conditional scaling result**. No arbitrary universally valid relation can be inferred solely from a fitted finite-aperture dataset.

**Next step:** preserve the original mathematical proof/source scripts and test the law under multiple independent HFSS meshes and geometries if it is used in a future publication.
