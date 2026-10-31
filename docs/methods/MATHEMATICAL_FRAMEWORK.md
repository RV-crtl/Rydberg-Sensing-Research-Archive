# Jones, Stokes and information-aware measurement framework

## 1. Incident polarisation

For a coherent harmonic field at a reference plane, the transverse Jones vector is

\[
\mathbf e = \begin{bmatrix}E_x & E_y\end{bmatrix}^{\mathsf T},
\qquad E_x,E_y\in\mathbb C.
\]

One convention defines

\[
\begin{aligned}
S_0 &= |E_x|^2+|E_y|^2,\\
S_1 &= |E_x|^2-|E_y|^2,\\
S_2 &=2\operatorname{Re}(E_x E_y^*),\\
S_3 &=2\operatorname{Im}(E_x E_y^*).
\end{aligned}
\]

Some publications reverse the sign of `S3` because of phasor convention or circular-handedness definition; record the adopted convention before comparing results across tools.

## 2. Polarimetric observation

A state-dependent RF analyser maps an incident field to the selected observation. If the observable is a quadratic intensity or other suitably calibrated scalar, the model can be written

\[
\mathbf y = \mathbf A\mathbf S+\boldsymbol\epsilon,
\quad \mathbf A\in\mathbb R^{6\times4},
\quad \mathbf S\in\mathbb R^4.
\]

An instrument matrix may depend on frequency, observation position, analyser state, actual RF transfer characteristics and the detector. The archived HFSS rows are **electromagnetic-model** coefficients: physical rubidium optical calibration is a separate measurement transfer function.

## 3. Inversion and numerical interpretation

For sufficiently independent rows, the Moore–Penrose inverse yields the ordinary least-squares estimate `S_hat = A^+ y` (with appropriate data weighting). Rank four is necessary for unique four-parameter reconstruction under the assumed model. The 2-norm condition number is `kappa_2(A) = sigma_max(A)/sigma_min(A)` using the nonzero singular values. The reported paper metric is *row normalised*; replicate that exact preprocessing before comparing conditioning numbers.

A conventional weighted information matrix takes the form `F = A^T W A` when the noise covariance and observation weights justify `W`; the information and time-allocation objective adopted in the manuscript should be read alongside its statistical assumptions. An improved inverse-trace **criterion** is not an experimental optical uncertainty guarantee.

## 4. Verification sequence

1. Validate Jones and Stokes convention with analytical H/V, ±45° and circular reference vectors.
2. Confirm each response row is derived from the matching complex HFSS fields, geometry state, frequency and observation region.
3. Compute matrix rank, singular values and conditioning using the stated normalisation.
4. Test reconstruction on held-out excitation states, separating same-mesh interpolation from independent-mesh transfer.
5. Compare finite aperture and observation geometry at the same physical coordinates.
6. Once a physical atomic receiver is available, identify an independently calibrated atomic response model and evaluate reconstruction against reference polarisation inputs.

## Original scientific sources

- [Current full derivations](../../papers/manuscript-source/main.tex).
- [Actual 6 × 4 coefficient table](../../papers/manuscript-source/data/V42_C033_INSTRUMENT_MATRIX.csv).
- [Related selection tables](../../papers/manuscript-source/data/V44_FIXED_BUDGET_ALL_SUBSETS.csv).
- [HFSS evidence and provenance](../results/EVIDENCE_INDEX.md).
