# Stokes instrument matrix and numerical verification

## Mathematical observation model

Use a four-coordinate real Stokes vector S = [S0,S1,S2,S3]^T. Each selectable analyser state k produces a scalar observation y_k after the stated normalisation. In a linear calibrated model,

y = A S + b + ε,

where A is an m × 4 calibrated instrument matrix (the main six-state design uses m=6), b is the baseline and ε represents uncertainty only when the particular evaluation explicitly includes a model for it.

A can be obtained by representing the complex Jones/field response of each state as an appropriate positive semidefinite Hermitian quadratic form and expanding it in the Pauli/Stokes basis with a fixed sign/handedness convention. **Keep electric-field amplitude, power, local averaging and gain normalisation separate**. A complex phase discrepancy can change the circular-sensitive coefficient even if total magnitude appears converged.

## Essential diagnostic checks

| Diagnostic | Meaning | Minimum reporting |
|---|---|---|
| rank(A) = 4 | All four components mathematically observable in the model | Matrix, singular values, numerical rank tolerance |
| Row-normalised κ2(A) | Scale-independent response geometry | Normalisation, σmax/σmin, exact frequency and state subset |
| Absolute gain / Fisher information | How measurement strength and time contribute | Raw row gains, weight/covariance model and time budget |
| S3 leverage | Sensitivity to handedness | Signed Stokes row coefficients, Jones phase reference |
| Physicality | Reconstructed state must satisfy Stokes cone constraints | S0 and degree of polarisation; convention |
| Independent mesh | Numerical error in complex fields and A | Mesh spec, matched sample coordinates, threshold, raw comparison |
| Finite-aperture transfer | Whether periodic calibration describes finite ROI | Separate finite fields/A, calibration residual, position |
| Frequency window | Contiguous *tested sample* set meeting gates | Grid spacing, acceptance rule, edge sample results |
| Input holdouts | Model inversion generalises beyond fitting cases | All source polarisation states and exact reconstruction metric |

Ideal tetrahedral four-state analysers have a characteristic favourable symmetric geometry, but **a proposed tetrahedron does not guarantee the physical HFSS states are tetrahedrally distributed**, nor does κ alone establish robustness at low gain. Do not present arbitrarily chosen synthetic noise trials as experimental repeatability.

## Paper-centred verified reference

The current evidence corpus reports an optimised six-state two-face split-loop analyser with six real measurements and a 6 × 4 matrix. The archived selected 1.925 GHz periodic response has rank 4 and row-normalised κ2 ≈ 9.53; the current manuscript states a sampled accepted interval of 250 MHz and a mesh discrepancy of 0.551%. The finite 3 × 3 result is qualified separately. These are **numerical, model-specific results**.

Start with [V42 six-state instrument matrix](../../papers/manuscript-source/data/V42_C033_INSTRUMENT_MATRIX.csv), [archived V44 data](../../evidence/hfss/v44-reproducibility/data/), [V44 scripts](../../evidence/hfss/v44-reproducibility/analysis/) and the [current paper](../../papers/manuscript-source/main.tex). If a value changes, update the narrative only after re-running the linked exact source.

## Derived-law and uncertainty work

The research also explored aperture/enhancement and measurement-information relationships. A conditional aperture/gain law involving resonant Q, wavelength and physical area was investigated, but its dimensional assumptions, field confinement and numerical data validity must be shown for the exact solved mode. It should be presented as a **conditional derived relationship**, not a universally proven calibration law. See [the existing mathematical framework](../methods/MATHEMATICAL_FRAMEWORK.md).

Measurement time allocation was optimised using an information matrix under a fixed total time / equal variance or gain-aware model; the paper reports a **40.8% reduction in an inverse-trace uncertainty criterion** compared with an equal-time allocation under that particular model. This is neither a measured uncertainty reduction nor a promise of improved receiver hardware SNR.

## Reproducibility checklist

- All X and Y complex drives for every state/frequency present with the same origin and phase convention.
- No Jones term silently reconstructed from intensity-only exports.
- Same sampling grid and local atom ROI for comparisons, with recorded physical coordinates.
- Boundary conditions and periodic/far-field vs near-field quantities explicitly labelled.
- Singular spectrum, gain, state ordering, matrix conventions and rank tolerance recorded.
- Finite-aperture results clearly distinguished from periodic unit-cell results.
- Raw solver files and machine verdict remain immutable after publication.
