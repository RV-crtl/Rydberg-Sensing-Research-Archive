# Linear polarisation measurements and Stokes interpretation

## Datasets must be kept separate

The history includes more than one RF polariser configuration and measurement chain. A **14–15 dB** rejection/passband contrast reported for the earlier steel-rod reference is not identical to the approximately **9.7 dB** laboratory RF-chain H/V contrast near **2 GHz** presented in subsequent poster/slides. Differences can come from the polariser geometry, antennas, reference plane and acquisition conditions. Never merge or relabel them without original data and calibration records.

An earlier rotation working sheet/slide recorded illustrative acquired powers **H(0°) ≈ 0.811**, **D(45°) ≈ 0.590**, **V(90°) ≈ 0.029**, with **A(135°) not recorded** for that subset. These entries are *historical conversation/slide records*, not a complete machine-verifiable dataset in this repository. They should not be substituted for original instrument exports in scientific fitting.

A later lab presentation reports a normalised linear estimate around **s1 ≈ 0.81**, **s2 ≈ 0.37**, **degree of linear polarisation ≈ 0.89** and **angle of linear polarisation ≈ 12.3°** under its stated convention. These estimates refer to a **conventional RF reference-chain analysis**, not a measured atomic full-Stokes estimator. Check the source slide before applying the numbers to a different dataset.

## What a linear analyser measures

With calibrated analyser intensity responses, a general linear polariser at angle θ has

I(θ) = (1/2)[S0 + S1 cos(2θ) + S2 sin(2θ)]

under the conventional ideal-angle convention. Rotating the linear analyser identifies S0, S1 and S2 if enough independent angular conditions, baselines and gains exist. No term in this ideal relation responds to S3: **linear-only rotation cannot determine handedness**.

For ideal 0°, 90°, 45° and 135° analyser intensities:

- S0 ≈ I0 + I90 (also ≈ I45 + I135 for independently calibrated channels);
- S1 ≈ I0 − I90;
- S2 ≈ I45 − I135;
- S3 requires an independent left/right circular or elliptical sensitive analyser state.

When any required measurement is missing, do not silently substitute theory or a fit as if observed. Nonideal states instead require a measured/simulated instrument matrix with gain and baseline calibration.

## Acquisition and processing protocol

1. Record the actual source polarisation, generator frequency/power and RF antenna geometry; measure the reference signal without the analysed polariser.
2. Fix the receive antenna, polariser stand-off, receiver gain, detector range, normalisation and cable setup while rotating through at least 0–180° (360° provides a reproducibility check).
3. Acquire repeated sweeps (project notes include five repeated angles averaged in a later linear rotation analysis); keep all repeats rather than only the average.
4. Use explicit dB definitions: insertion loss and discrimination are power- or field-ratio dependent; avoid mixing 10log10 power with 20log10 voltage.
5. Fit I(θ) to the 0, cos2θ and sin2θ basis with statistical/measurement uncertainty; retain residual plots, confidence intervals and checks against known RF polarisation.
6. Evaluate physicality S0 ≥ sqrt(S1²+S2²+S3²), noting that absent S3 cannot be silently imputed as zero.
7. For a future full-Stokes receiver, add calibrated handedness-sensitive states and verify rank, condition number, robustness, local atom sampling and independent polarisation holdouts.

## Evidence status

| Claim | Status | Anchor |
|---|---|---|
| RF front-end distinguishes tested linear states | Experimental, protocol-dependent | [June experimental report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf) and [poster](../../presentations/rydberg-rf-polarimetry-poster.png) |
| Linear/Poincaré equator is accessible to the observed analyser geometry | Experiment-informed interpretation | [Poincaré poster figure](../../presentations/linear-polarisation-poincare-equator.png) |
| Current copper analyser has four-coordinate simulated observability | HFSS-derived, separate experiment | [V44 simulation data](../../evidence/hfss/v44-reproducibility/) |
| Complete atomically measured S3 and full sphere | Not established in imported laboratory records | [Research handover](../handover/HANDOVER.md) |

**Reading order:** experimental report → associated instrument files (when imported) → calibration/fit scripts → polarisation plot → final paper’s numerical Stokes instrument matrix.
