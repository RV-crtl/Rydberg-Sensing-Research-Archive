# Validation report — Rydberg Workbench 0.4

Prepared 28 September 2026. **77 tests passed, 0 failed, 0 skipped** in the saved
Linux run (14.40 s). This is numerical and software verification, not laboratory
validation. All supplied experiment curves are synthetic. No B210 was attached.

## What changed

- Twelve executable graph examples: EIT, AT, weak/strong AM, FM, weak/strong
  atomic mixing, temperature, optical lock-in, electronic AM/FM and two-tone
  compression. Eighteen block types execute their configured behavior.
- Nonperturbative periodic four-state Lindblad solver with thermal averaging,
  harmonic/velocity refinement and sampled density physicality checks.
- Independent scopes opened by double-click, time/frequency tabs, movable
  cursors, linear-power spectral averaging, freeze, harmonic fits and CSV.
- Live independent acquisitions with optical-result caching, fresh noise and
  revision checks; parameter sweeps with cancellation between points and provenance.
- Separate two-level Rabi/Ramsey/echo bench with finite pulses and T1/Tφ.
- Optional one-channel UHD RX plus synthetic/replayed IQ, AM/FM demodulation,
  PSD/waterfall and NPZ / single-capture SigMF recordings. No transmitter.

## Checks and their meaning

| Area | Verified evidence | Scope of the claim |
|---|---|---|
| Atomic core | Analytical two-level limits, trace/Hermiticity/positivity, decay direction and independent RydIQule comparisons | Effective selected-sublevel core, not full Rb manifold |
| Periodic dynamics | Strong AM and FM compared with direct DOP853 time integration; all density elements differ by less than 2×10⁻⁸ in test cases | A separate numerical solution of the same physical equation |
| Weak-drive limit | Periodic fundamental agrees with linear harmonic response within 10⁻⁷ relative tolerance | One controlled reference configuration |
| Spectroscopy | Weak-probe single-velocity AT minima at ±ΩRF/2 within 0.005 MHz; thermal EIT exceeds coupling-off absorption | Analytical limiting behavior and a thermal example, not measured line fitting |
| Mixer sign | Rotating single RF link agrees with a static detuning transformation | Signed RF sideband convention checked |
| Thermal examples | All nine Rydberg catalogue graphs report velocity convergence; three strong-drive examples also report harmonic convergence | Numerical refinement indicators, not global parameter-space proof |
| Electronics | PSD/Parseval, loaded 0 dBm tone, filter phase, P1dB calibration, NF/noise, PD noise scaling, ADC/clipping; AM sidebands and intermodulation | Behavioral models and specified conventions |
| Analysis | Joint harmonic fit, phase-sensitive lock-in/DC reporting, stale export guard | Known isolated frequency; fitted harmonics may include noise |
| Pulse bench | Analytical resonant Rabi oscillations, density physicality for all sequences, static-detuning echo refocusing | Isolated two-level Lindblad model |
| Desktop | Actual Qt mouse double-click opens scope; worker result, live updates, freeze, parameter edits, quantum/SDR/sweep windows exercised | Qt offscreen on Linux |
| SDR | Fake UHD partial reads, coerced-rate metadata, stop commands, overflow/timeout/timestamp failures; IQ PSD calibration and replay round trips | Adapter/software contract, not physical hardware performance |
| Packaging | Wheel/source byte comparison and installed-wheel smoke run recorded separately | Source/wheel distribution; no Windows/macOS executable certification |

The test XML is `docs/evidence/v04/pytest-results.xml`. Captured environment and
full graph/config/metrics for every example are in the same directory. Reproduce:

```bash
QT_QPA_PLATFORM=offscreen OPENBLAS_NUM_THREADS=1 python -m pytest python/tests -q
python scripts/validate-desktop-release.py
```

## Representative synthetic outputs

The 1 m AM reference has −20 dBm generator power, 6 dBi antenna gain, 2 dB cable
loss, room-temperature Rb parameters and 30 dB amplifier gain. Its RF field is
about **38.822 mV/m peak** and RF Rabi frequency **1.602 MHz**. The 2% AM example
produces approximately **−94.64 dBm** fitted scope tone with the configured noise.
This does not identify the user's forgotten experimental power reading.

| Example | Mean optical transmission | Scope fitted fundamental | Diagnostic |
|---|---:|---:|---|
| Weak AM, noise on | 0.83011 | −94.64 dBm | 2% modulation; noise-limited harmonic estimates |
| Strong AM, noise off | 0.82794 | −65.16 dBm | 70% modulation; Fourier order 8; fitted THD ≈21.23% |
| Atomic FM, noise off | 0.81336 | −82.24 dBm | Order 8; 0.4 MHz peak deviation on a detuned line |
| Strong atomic mixer, noise off | 0.82805 | −67.76 dBm | Signal/LO field ratio 0.5; order 16 |
| Heated receiver, noise on | 0.13031 | −90.59 dBm | Gas and reservoir 323.15 K; fixed effective lifetimes/dephasing |

THD of weak/noisy traces is not an estimate of intrinsic device distortion. A
lock-in's meaningful output is signed DC voltage; it is no longer labelled as
a 10 kHz scope tone. The scope's total AC dBm excludes DC. Periodic atom/optics
and loaded periodic electronics retain their stated propagation assumptions.

## Limitations before V1

1. No independently held-out laboratory EIT/AT/modulation data have been fitted
   or tested; no uncertainty budget establishes absolute metrological accuracy.
2. No full hyperfine/Zeeman optical pumping, CP/Stokes manifold, interaction
   blockade, spatial overlap/depletion, dielectric RF field or circuit network.
3. No arbitrary-message atomic transients, atomic state carried continuously
   between live records, source phase-noise record synthesis or lossless
   high-rate recorder. Periodic solver convergence is not a calibration result.
4. The B210 requires separate UHD/USB setup and physical validation. It is an RF
   receiver, not a DC/baseband photodiode ADC. Hardware IQ does not feed arbitrary
   graph blocks yet. Calibration is an explicitly measured scalar offset only.
5. Windows/macOS install commands are supplied but not executed here. Undo,
   recovery, reusable subgraphs and a native packaged installer remain open.

The appropriate release label is **v0.4 research/development build**, not
commercially validated V1. Source, examples, tests, equations, references and
hardware instructions are supplied for review. Public GitHub publication remains
pending a stronger V1 and the user's existing release criterion.