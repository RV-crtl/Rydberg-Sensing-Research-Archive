# Field ionisation, electron imaging and state-selective detection

**Independent textbook chapter / instrumentation**. Original general treatment; no project-specific RF apparatus or HFSS case is presented as universal physics. Read [references](../REFERENCES.md).

## Learning objectives

Explain the core physical mechanism, derive a model with explicit approximations, design a falsifiable measurement, diagnose artefacts and choose validated calculation methods.

## 1. The field-ionisation principle

A Rydberg electron has weak binding energy and may be removed by a sufficiently strong applied electric field, either through barrier suppression or tunnelling depending on state and ramp rate. A rough ionisation-field scaling varies as n^{-4} in hydrogenic estimates, but angular momentum, Stark-state orientation, tunnelling and ramp trajectory alter the actual threshold. The measured signal can be an ion or electron arrival time at a detector—not directly the initial state's unperturbed energy.

## 2. Pulsed-field ramps and state selectivity

Slow or fast field ramps traverse different avoided crossings in a Stark manifold. Adiabatic and diabatic state following produce different ionisation onset times and hence distinct detector signals. Timing must be referenced to laser excitation and extraction pulses. A claimed state-selective threshold is meaningful only if pulse waveforms, electrode fields and competing ionisation channels are characterised.

## 3. Electron and ion optics

Microchannel plates, channel electron multipliers or imaging detectors register charged-particle impacts. Extraction electrodes and electrostatic lenses map source position and emission momentum into detector time and position. Space charge, finite detector gain, dead time and secondary electron statistics can distort images. Electrostatic simulations should be checked against measured transport calibration; a pretty trajectory plot is not enough to establish collection efficiency.

## 4. Blackbody and collision backgrounds

Spontaneous blackbody transfers can move Rydberg atoms to levels with different ionisation thresholds before the pulse arrives. Penning and associative ionisation may create background charge. Vary laser excitation, atom density, extraction delay and ambient field independently. Maintain dark detector measurements and a calibrated time-of-flight reference.

## 5. Alternative state detection

In neutral-atom arrays, state-selective fluorescence can map a ground-state population after a coherent de-excitation or shelving sequence. A missing atom can be confused with a Rydberg excitation unless loss probability is modelled. Field-ionisation can be more direct for high Rydberg excitation but may be destructive and require specialised high-voltage engineering and vacuum hardware.

## 6. Reproducibility and safety

Ionisation experiments can involve hazardous high-voltage pulses, vacuum feedthroughs and laser beams. Use institutional high-voltage interlocks and trained personnel; specify theoretical field ramps without providing unreviewed wiring instructions. Report detector calibration, state mixture, field uncertainty, pulse jitter, timing bins and ionisation efficiency.

## Review problems with full explanations

### 1. Why is a simple n^{-4} ionisation estimate insufficient for a state assignment?

<details><summary>View worked reasoning</summary>

Real thresholds depend on angular state, Stark mixing, ramp rate and tunnelling dynamics.

</details>

### 2. What does selective field ionisation actually measure?

<details><summary>View worked reasoning</summary>

Time/threshold-dependent charged-particle detection influenced by state distribution and the extraction apparatus.

</details>

### 3. Why does ramp speed matter?

<details><summary>View worked reasoning</summary>

State-following at avoided crossings can change between adiabatic and diabatic regimes.

</details>

### 4. Can atom loss alone confirm Rydberg excitation?

<details><summary>View worked reasoning</summary>

No; heating, collisions, imaging failure and background losses can mimic shelving or excitation.

</details>

### 5. Why is collection efficiency a calibration issue?

<details><summary>View worked reasoning</summary>

Charged-particle transport and finite detector gain can vary by trajectory, energy and timing.

</details>

### 6. Which high-voltage concern is non-negotiable?

<details><summary>View worked reasoning</summary>

Approved interlocks, isolation, discharge procedures and competent institutional supervision.

</details>

## Design and verification assignment

Construct a research protocol for an appropriate species or platform. State what the detector measures, its model assumptions, the control experiment needed, expected scale, uncertainty sources and stopping criteria. Perform an independent computation or published-data comparison before claiming a new observation. Consult the bibliography for exact state constants and validated methods.

## Suggested source pathway

Gallagher, *Rydberg Atoms*; relevant ARC documentation and atomic spectroscopy; the NIST review of atomic electrometry (2024/2025) and field-specific primary literature. See [bibliography](../REFERENCES.md).
