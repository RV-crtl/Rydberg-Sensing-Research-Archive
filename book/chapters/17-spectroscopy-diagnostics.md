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
