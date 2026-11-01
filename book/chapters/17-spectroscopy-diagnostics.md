# Spectroscopy troubleshooting and fault isolation

**Independent general reference chapter.** Discusses universally applicable physics and engineering; no project-specific numerical HFSS result is asserted.

## Competencies

Model the system, specify a measurement chain and units, choose appropriate numerical tools, reproduce limiting cases and debug signal/solver failures.

## 1. Start with the observation chain

An optical spectrum is a sequence of measurements from a source-frequency scan, an atomic response, optical propagation, photodetection, amplification and digitization. A vanished EIT feature could be caused by any of these stages. Construct a block diagram and independently verify each: measured laser frequency, beam power, reference absorption, photodiode gain and raw digitizer waveform. Do not begin debugging by rewriting an atomic Hamiltonian when an oscilloscope is clipping.

## 2. Reference spectra and experiment controls

Collect a four-condition grid with coherent coupling off/on crossed with RF source off/on. Coupling-off tests isolate optical and electronic features not requiring the Rydberg ladder; RF-off tests identify standing optical background and drift. Maintain the same detector gain, scan timing and laser powers when comparing traces. A signal persisting after disabling the coupling laser may indicate unintended pathways or a non-atomic artefact; a confident interpretation requires the exact apparatus context.

## 3. Line assignment and scan calibration

Compare measured peak frequencies with independent calibrated wavemeter/etalon or beat notes, not the piezo control voltage alone. State isotope, hyperfine state, polarisation and expected two-photon detuning. When field or current changes, repeat the full reference scan to test whether laser lock, cell temperature or detector gain moved. Assign transitions only after comparing to allowed state-specific lines, including potentially multiple magnetic sublevels and blackbody-transferred states.

## 4. RF spur and harmonic interference

A synthesizer and amplifier can emit harmonics and spurious tones that couple through the antenna or directly into measurement electronics. Cable mismatch, mixer products and digitizer aliasing can produce repeatable features at unexpected frequencies. Use a calibrated independent RF receiver/reference with attenuation, inspect source spectrum under RF on/off conditions, vary carrier and power, and verify whether the optical response follows the predicted atomic detuning rather than the electronics.

## 5. Numerical fit diagnostics

Inspect residuals as functions of detuning and acquisition time. A good least-squares fit can be wrong when the solver assigns the wrong m-state, uses an incorrect 2π convention, lacks Doppler averaging or overfits baseline drift with linewidth. Test multiple scan rates and laser powers on held-out spectra. When a fit returns a negative population or unphysical Rabi field, investigate the forward model instead of hiding the failure with clipping.

## 6. A reproducible repair record

A fault ticket should include symptom, apparatus state, source/scan frequencies, optical power, thermal conditions, field orientation, RF calibration, observed control outcomes, raw data pointers and changes made one at a time. State whether a proposed fix passed a predeclared acceptance gate; a visually stronger trace is not necessarily a better calibrated sensor. A researcher joining the laboratory should be able to reproduce the fault without relying on oral history.

## End-of-chapter questions and answers

### Question 1. Why do four on/off conditions help?

<details><summary>Read the worked explanation</summary>

They separate RF-dependent features from coherent-ladder-dependent and electronic/optical backgrounds.

</details>

### Question 2. Why is a peak at a predicted frequency not sufficient for a state assignment?

<details><summary>Read the worked explanation</summary>

Unexpected harmonics, mixing, drift, other transitions or background can overlap the prediction.

</details>

### Question 3. What first test should follow a saturated detector?

<details><summary>Read the worked explanation</summary>

Restore the linear operating range and record the same physical reference before interpreting spectroscopy.

</details>

### Question 4. Can a low residual prove the atomic level graph is right?

<details><summary>Read the worked explanation</summary>

No; overparameterized or biased models can fit the training trace despite wrong physics.

</details>

### Question 5. Why scan in both directions?

<details><summary>Read the worked explanation</summary>

It can reveal temporal drift, hysteresis, scan nonlinearity and slow servo effects.

</details>

### Question 6. What should a debugging log preserve?

<details><summary>Read the worked explanation</summary>

Exact settings, control results, raw data, source revisions, date and acceptance criteria.

</details>

## Research problem

Build a falsifiable numerical or experimental analysis with correct units and explicitly stated physical observables. Write its independent source and calibration references, convergence thresholds, and diagnostic on/off controls. Test at least one failure case. Never report simulated or illustrative values as new physical measurements.

## Further reading

Foot, *Atomic Physics*; Pozar, *Microwave Engineering*; official Ansys and RydIQule references; [complete bibliography](../REFERENCES.md).


---

## Detailed independent reference, extended case study and problem set

This general atlas applies to atomic vapour sensors, MOT/cloud spectroscopy, single-atom arrays and ionisation-based Rydberg studies. It is not a substitute for safety training; high-voltage, lasers, vacuum, RF radiation and cryogenics are supervised laboratory hazards. The purpose is to prevent a seductive symptom from becoming an unsupported physical explanation.

## The first six diagnostic questions

1. **What is the directly measured quantity?** Distinguish counts, optical volts, RF analyser power, CCD intensity, laser error voltage and calculated atomic populations.
2. **What was deliberately changed?** One independent control at a time: microwave field, optical coupling, bias field, scan time, atom preparation or lattice spacing.
3. **What reference remained unchanged?** Frequency calibrations, exposure time, detector gain, laser lock and pointing, atom number and field geometry.
4. **Is the feature reproducible?** Repeat at different times, randomise scan order and record raw unfiltered data.
5. **Does the simplest valid model predict the limit?** Zero drive, zero coupling, no atoms, reversed polarisation, sign reversal or large detuning.
6. **What independent measurement could falsify the current explanation?** A source spectrum, reference beam, atomic-state tag, independent mesh, controlled field probe or unrelated detector.

## Symptoms: optical and thermal alkali vapour systems

| Symptom | Primary suspect | First discriminating measurement | Model check |
|---|---|---|---|
| No Doppler-free feature | Wrong lock transition, beam alignment, power/temperature | Independent saturated-absorption reference | Known optical level spacings |
| EIT contrast disappears | Coupling detuning, optical overlap, two-photon Doppler, dephasing | Couple light off/on at fixed optical scan | Weak probe three-level limit |
| EIT peak shifts with power | AC Stark/power broadening or drift | Independently log power and laser reference | Power scan in density matrix model |
| Lines broaden asymmetrically | Drift, velocity distribution, optical pumping | Reverse scan, change propagation geometry | Doppler-averaged response |
| RF-dependent signal present with coupling blocked | Detector/electronics/optical artefact | RF/coupling four-control design | RF response must vanish without coherent ladder |
| Oscilloscope looks clean but spectrum is wrong | Bandwidth, aliasing, detector transfer | Calibrated detector/electronics sweep | Full acquisition chain |
| Rapid change under cell temperature | Density/optical depth or collisions | Log temperature and probe-only absorption | Propagation and broadening model |

An RF source's carrier and the optical EIT resonance are observables from different instruments. Agreement in their numerical frequency labels does not establish atomic transduction. Use a physically calibrated transfer function.

## Symptoms: laser cooling and tweezer arrays

| Symptom | Likely mechanism | Control / acceptance |
|---|---|---|
| MOT loads slowly | Cooling detuning, field gradient, vacuum lifetime | Measure independent loading curve and background-gas lifetime |
| Rydberg excitation inconsistent across sites | Local light shifts, beam uniformity, addressing | Site-resolved Rabi and detuning maps; track trap position |
| Gate output dominated by loss | Blackbody transitions, trap leakage, imperfect readout | Separate actual state loss from SPAM and leakage |
| Blockade radius differs from expectation | Interaction manifold, nearby Förster channel | Pair-state diagonalisation and spacing sweep |
| Array dephases between runs | Technical laser phase, magnetic drift, temperature | Ramsey/echo sequences and correlated calibration |
| Atom image is bright despite expected dark state | Scattering/selection-rule mismatch | Optical pumping efficiency and detection leakage |
| Excitation linewidth is unexpectedly narrow | Bin averaging, selection bias or unstable fit | Retain raw shots, uncertainty intervals and scan-order randomisation |

In neutral-atom gates, the correct performance metric often involves conditional fidelity and leakage, not the depth of a single optical transmission trace. A beautiful time trace cannot replace a quantum process test.

## Symptoms: spectral theory, numerical solvers and code

| Symptom | Numerical reason | Independent test |
|---|---|---|
| Negative density-matrix eigenvalues | Integration, nonphysical dissipator, incorrect basis | Hermiticity, trace, positivity and time-step refinement |
| Anomalous 2π disagreement | Angular-frequency versus cycle-frequency units | Compare one analytically solved two-level period |
| Abrupt state labels at a Stark crossing | Eigenvector relabelling/avoided crossings | Track eigenvector overlap and enlarge basis |
| Lifetime unexpectedly short at high n | Blackbody transitions or extra decay | Separate zero-T radiative and finite-T rates |
| Doubled Doppler shift | Incorrect propagation sign or 2-photon frame | Derive k-v term from each laser phase |
| Strong predicted EIT with no experimental contrast | Omitted linewidth/optical-depth/misalignment | Introduce independently calibrated physical processes |
| Unstable full-Stokes inversion | Small singular values, poorly scaled rows | Singular spectrum, absolute gain and holdout error |
| Machine-precision fit to synthetic model | Testing model against itself | Validate on independent raw data / solver |
| API example fails in a new version | Version drift or renamed functions | Lock environment and compare official release docs |

A numerical script returning without exception proves neither atom-state realism nor scientific validity. Automated quality checks should be designed around conserved quantities, known limits, cross-tool comparisons and source provenance.

## Symptoms: microwave and finite electromagnetic design

If a physical metasurface or RF matching network has impressive simulated isolation but poor measured response, compare the actual substrate stackup, copper thickness, finite aperture, connectors, bias wiring, diode equivalent circuits, observation volume and incident field distribution. Ideal PEC on/off patches cannot verify a packaged PIN-diode response.

A solver mesh adaptively converged at its port can still have unacceptable phase-sensitive local field error. Export complex vector fields at the atomic sampling position for independent mesh profiles, then compare derived observables (singular values, circular sensitivity and worst-case reconstruction) at fixed coordinates. A valid periodic unit cell does not automatically imply a valid finite device.

## Minimal evidence record for any incident

Use a report with: timestamp and timezone; apparatus serial/calibration IDs; operating state and frequency; atomic state ladder; laser optical parameters; RF waveform and reference plane; numerical solver/mesh version; raw-data paths and hashes; changes performed; acceptance criterion; rejected hypotheses; next independent experiment. Separate a planned remedy from a remedy that was actually tested. Store safety-sensitive information only in approved restricted records.

## Fifteen challenge questions (answers)

<details><summary>1. An RF peak persists with the coupling laser turned off. Can the peak be called Rydberg EIT?</summary>

No. The optical Rydberg ladder is disabled. Investigate electrical pickup, optical background and detector response while recording the original source spectrum.

</details>
<details><summary>2. A code fit gives RMS residual 10⁻¹² but its data were generated by the same code. What has been validated?</summary>

Internal algebraic consistency, not physical fidelity or independent experimental correctness.

</details>
<details><summary>3. Which independent physical variable can test a claimed Doppler broadening mechanism?</summary>

Change cell temperature or beam propagation geometry while separately measuring laser jitter and optical power. Compare the observed spectral change with the predicted velocity dependence.

</details>
<details><summary>4. Does a high-n Rydberg state necessarily have a long observed coherent lifetime?</summary>

No. Radiative lifetime may increase in some regimes, but blackbody redistribution, laser noise, motion and collisions can dominate observed coherence.

</details>
<details><summary>5. Why can a resonant pair Rabi frequency be different from μE/h?</summary>

Angular-momentum projection, spatial field orientation, drive amplitude conventions, level mixing and effective coupling renormalisation change the relevant matrix element.

</details>
<details><summary>6. How do you distinguish a false linewidth from scan-speed distortion?</summary>

Repeat with slower/faster scans in both directions, monitor laser frequency independently and account for detector/time-response filtering.

</details>
<details><summary>7. What is the appropriate control for a claimed spin-selective RF feature?</summary>

Change its quantisation axis or prepare a different magnetic sublevel while keeping optical/RF references monitored; compare the complete selection-rule model.

</details>
<details><summary>8. Why do individual atom fluorescence counts not directly equal state population?</summary>

Detection efficiency, bright/dark-state confusion, atom loss, optical pumping and finite exposure create a readout transfer that must be calibrated.

</details>
<details><summary>9. When is a two-level Rabi model acceptable?</summary>

When other levels are sufficiently detuned and decay/motion mechanisms can be neglected for the intended time and accuracy, with those assumptions tested.

</details>
<details><summary>10. How can two frequency sweeps be falsely compared?</summary>

Different laser lock, detector bandwidth, acquisition gain, RF reference plane or smoothing can change observed contrast without changing the atomic physics.

</details>
<details><summary>11. Why must the finite EM response be checked at an observation volume rather than an arbitrary port?</summary>

The atom interacts with its local vector electric field; port S-parameters need not capture finite-cell spatial amplitude/phase variation.

</details>
<details><summary>12. What is the main distinction between hardware SNR and quantum Fisher information?</summary>

Quantum Fisher information describes information in a parameter-dependent quantum state under specified assumptions, while measured SNR depends on physical readout and noise. Neither alone describes the entire apparatus.

</details>
<details><summary>13. A unitary evolution yields trace 1 but negative populations after a script's “projection”. What does that imply?</summary>

The reported state is nonphysical or is being incorrectly transformed; check basis, normalisation, numerical errors and whether a nonunitary transformation was inserted.

</details>
<details><summary>14. A machine-generated literature issue states a grant is open based on an old notice. Is that verified?</summary>

No. Check the current official application portal, relevant stream and deadline/timezone, and eligibility before any outreach or proposal.

</details>
<details><summary>15. What should be done after a research model fails its acceptance criterion?</summary>

Preserve the failure data, log the violated gate, isolate causes, propose an independently testable revision and rerun; never overwrite original results or redefine the threshold silently.

</details>

## References

Steck, *Quantum and Atom Optics*, https://steck.us/teaching/ ; Gallagher, *Rydberg Atoms*, DOI https://doi.org/10.1017/CBO9780511524530 ; ARC official documentation https://arc-alkali-rydberg-calculator.readthedocs.io/en/latest/ ; RydIQule solvers https://rydiqule.readthedocs.io/en/stable/overview.html ; National metrology guidance, including JCGM 100, https://www.bipm.org/en/committees/jc/jcgm/publications . See [book references](../REFERENCES.md).
