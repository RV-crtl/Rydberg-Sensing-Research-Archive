# Experimental calibration and polarisation-recovery protocol

A reproducible Rydberg RF polarimetry experiment must maintain independent evidence for **(1) the incident RF reference state, (2) the RF analyser/meta-atom state, (3) the optical atomic response, and (4) the inversion computation**. The earlier exploratory receiver and linear-polariser findings establish starting points, not a fully calibrated four-coordinate atom experiment.

## 1. Apparatus baseline and safety

Before energising the vapour-cell apparatus, follow lab-specific laser, RF, high-voltage and chemical safety rules. Record laser eyewear and beam enclosure procedures, alignment controls and optical shutter conditions; note any hot-cell temperature, magnetic coil current, power supply limits and RF leakage controls. Identify source and readout serial numbers privately in the laboratory run record. A scientific GitHub issue should reference protected asset IDs rather than copy restricted records into an issue.

Record exact 780 nm probe laser and 480 nm coupling laser measured frequency/wavelength, power, detuning, polarisation, beam waist, mode overlap and path topology. Record cell species, dimensions, temperature, probe transmission reference and detector bandwidth/impedance. An 86P3/2 candidate from an ARC transition list must be verified against the actual optical ladder and the source frequency, not assumed from coarse wavelength set points.

## 2. Baseline controls for RF signals and magnetic bias

The historical RF search investigated incident frequencies near **1.5–1.56 GHz** while also observing isolated/variable features around **2.4 GHz**. A peak displaced from the nominal generator setting is not automatically an atomic Zeeman line or harmonic. For any such claim, acquire:

1. Synthesiser output spectrum into a calibrated 50 Ω measurement instrument (where available), power-vs-frequency, source spur catalogue.
2. Generator **off**, lasers **blocked** and cell-off / no-coupling controls, with identical gain and detector settings.
3. Coil current measured versus field at the cell, both field polarities, ascending and descending sweeps, thermal equilibrium and coil geometry.
4. Full **continuous** spectrum/oscilloscope trace at every current/laser condition instead of isolated hand-copied peak amplitudes.
5. Cables, attenuation, port calibration, antenna orientation and RF detector response checked independently of optical readout.
6. If using a lock-in, measured modulation frequency, reference phase, filter bandwidth and off-resonant response.

Classify an anomalous line as an **unassigned observation** until source spurs, intermodulation, background interference, artefacts and optical response have been ruled out by controls. An untested interpretation is not evidence of a measured RF transition.

## 3. Linear-analyser reference calibration

Calibrate physical polariser angle and antenna polarisation relative to a documented laboratory coordinate frame. Fix distance, gains, frequency, source power, receive reference plane and environment while collecting angle-dependent power over at least a 180° sweep. Record individual repeated traces—earlier work planned five repeats for later averaged sweeps. Never discard the full repetitions after calculating a mean.

For an ideal analyser, with consistent power normalisation and fixed sign convention,

\[
I(\theta) = \tfrac12 [S_0 + S_1\cos(2\theta) + S_2\sin(2\theta)].
\]

Fit measured intensity to constant, cosine and sine terms; show reference readings, calibration, model assumptions, fit uncertainties, residual structure, signal-to-noise and drift. When reporting pass/reject contrast, use **10 log10(P_pass/P_reject)** for calibrated power or **20 log10(V_pass/V_reject)** for coherent voltage under consistent impedance. Avoid combining the ~14–15 dB rod-grid reference and a later ~9.7 dB RF-chain measurement without matching geometries and reference planes.

The ideal linear response has no S3 term: such experiments constrain the Poincaré equator but do not measure circular handedness by themselves.

## 4. Circular and elliptical references

To experimentally identify S3, introduce known handedness-sensitive analyser states and verified RF input references. Record the RHCP/LHCP convention **looking along which propagation axis**, actual antenna axial ratio and complex Jones phase. Reversing an antenna observation axis can reverse an RHCP/LHCP label without changing physical fields; coordinate metadata must accompany results. Elliptical and oblique states are needed to test the full Stokes interior, not only six pole states.

## 5. Atomic transfer and calibrated instrument matrix

The full receiver requires repeated, gain-corrected atomic observations for each analyser switch setting. A conventional RF detector calibration cannot simply be relabelled a rubidium atomic calibration. For each state:

- Record bias/switch control status, copper geometry and any diode effects.
- Record RF generator frequency/incident polarisation and coherent local field context.
- Acquire raw probe transmission with laser-only and RF-off references.
- Calibrate baseline, dark/background, detector gain and lock drift.
- Derive **measured** instrument matrix (or a non-linear forward model if required) from well-conditioned reference states; reserve independent holdout states.
- Compare the calibrated physical matrix with the HFSS-derived matrix using matching local atom sensing volumes, physical PCB placements, absolute gains and uncertainties.

Numerical rank four is a *necessary* linear observability condition; an experiment should additionally show acceptable smallest singular value, stable signal, condition number, independent mesh/geometry transfer and held-out reconstruction.

## 6. Acquisition record schema

Each run needs: unique ID; UTC timestamp; optical references; RF power/frequency/calibration; antenna pose; board/cell distance; bias/current; physical/switch states; oscilloscope or SDR sampling rates and timebases; raw trace filenames; hashes; repetitions; reference/background; derived plot and analysis script; uncertainty ledger; and operator notes. A formal dataset manifest should distinguish measured values from simulation/analytical predictions.

## 7. End-to-end controls and scientific outcomes

Accept a future full-Stokes claim only when: known linear/circular/elliptical sources are verified independently; each physically distinct analyser state is repeatable; a full-rank actual measured matrix is obtained with stable conditioning; the holdout reconstructions satisfy the predeclared error metric and physical Stokes constraints; and the optical rubidium channel—not merely a separate RF probe—carries the information. Maintain distinct reports for atom-only, RF-only and full integrated controls.

**Source anchors:** [experimental interim report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf) · [measurement interpretation](../laboratory/POLARISATION_MEASUREMENTS.md) · [HFSS matrix study](../simulations/VERIFICATION_AND_INFORMATION_MATRIX.md) · [work-package register](../handover/MASTER_WORK_PACKAGE_REGISTER.md).
