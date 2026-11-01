# Magnetic structure, field tuning and precision diagnosis

**General advanced atomic science reference.** No particular laboratory result is asserted. Primary numerical APIs are linked in the [bibliography](../REFERENCES.md).

## Learning objectives

Build physically allowed state models, select the correct coupling and rate units, compute a limiting-case prediction and troubleshoot model/measurement disagreement.

## 1. Magnetic quantum numbers and weak-field shifts

The magnetic interaction involves electronic orbital/spin and nuclear contributions. In a weak-field fine-structure manifold, a common estimate is ΔE≈μB gJ mJ B. For hyperfine-resolved states, ΔE≈μB gF mF B may be more appropriate in the low-field regime. The quantisation axis is defined by B when it dominates competing interactions; reversing B may reverse labels or change optical pumping. The scalar size of B alone does not specify a full vector field.

## 2. Breit–Rabi and crossover regimes

When electron and nuclear angular momenta stop coupling strongly to good F states, the simple linear gF formula fails. The Breit–Rabi expression predicts magnetic dependence for certain alkali ground hyperfine manifolds, but excited and Rydberg states can require different Hamiltonians. A field scan should include state mixing, selection rules and uncertainties in measured coil field. A numerically smooth line is not proof of a correct basis or isotope.

## 3. Magnetic fields in optical spectroscopy

Bias fields resolve magnetic sublevels but can also alter optical pumping and selection-rule strengths. Multiple m-state EIT pathways can produce several peaks or cancellation even when a simple three-level model predicts one. For σ and π optical polarisation, alignment with the quantisation axis must be measured at the atoms. Laser lock drift and coil heating are practical confounders; use RF-off optical references and compare coil reversal at fixed optical conditions.

## 4. Field coils and calibration

A Helmholtz pair can provide approximately uniform field near its centre, but real winding geometry, nearby magnetic materials, power supply current noise and temperature change the field. The nominal current-to-field formula should be checked against a sensor or known atomic spectroscopic shift. Map field gradients and off-axis components over the active atom volume, not only one point. A magnetometer calibration itself has bandwidth and uncertainty.

## 5. Interpreting failures properly

A spectrum peak moving with coil current is suggestive but not diagnostic on its own. Change the laser reference, measure the coil waveform and verify the feature disappears in appropriate coupling-off conditions. Detect spurs at RF sources and photodiode electronics. If a simplified Zeeman model fails, first inspect state basis and competing broadening mechanisms before invoking new physical states.

## 6. Alternative polarisation strategies

Multiple magnetic sublevels can encode vector-field information, but achieving a unique inversion requires a calibrated set of independent optical observations. Other architectures use local oscillators, physical polarisation analyzers or simultaneous orthogonal transitions. The best architecture depends on field bandwidth, coherence and hardware complexity rather than a universal preference for magnetic bias.

## End-of-chapter questions with explained answers

### Question 1. When is mF a useful label?

<details><summary>Reveal scientific reasoning</summary>

In regimes where hyperfine coupling dominates and F remains a good approximate quantum number.

</details>

### Question 2. What can spoil a nominal Helmholtz field?

<details><summary>Reveal scientific reasoning</summary>

Magnetic materials, current calibration, coil geometry, position and environmental fields.

</details>

### Question 3. Does a peak shift under current prove Zeeman splitting?

<details><summary>Reveal scientific reasoning</summary>

No; check laser drift, coil heating, source mixing and proper atomic selection.

</details>

### Question 4. Why does the quantisation axis matter for RF polarisation?

<details><summary>Reveal scientific reasoning</summary>

It determines the spherical π and σ± field projections seen by specific transitions.

</details>

### Question 5. What model is needed beyond low-field hyperfine linear shifts?

<details><summary>Reveal scientific reasoning</summary>

Breit–Rabi or full coupled-state Zeeman Hamiltonian appropriate to the manifold.

</details>

### Question 6. How do magnetic gradients affect spectra?

<details><summary>Reveal scientific reasoning</summary>

Atoms sample different B shifts, causing inhomogeneous broadening or splitting.

</details>

## Reproducibility exercise

Run an independently testable calculation, record the package version and exact input state set, confirm units and selection rules, and compare to the cited API and a known physical limit. Write what a real experiment would need to validate the result. Avoid describing numerical output as an observed quantum sensor reading.

## References

ARC's [official documentation](https://arc-alkali-rydberg-calculator.readthedocs.io/en/latest/), RydIQule's [official documentation](https://rydiqule.readthedocs.io/en/stable/overview.html), Steck's spectroscopy tables, Gallagher and Foot; full [bibliography](../REFERENCES.md).
