# RydIQule: open-system modelling and optical observables

**General advanced atomic science reference.** No particular laboratory result is asserted. Primary numerical APIs are linked in the [bibliography](../REFERENCES.md).

## Learning objectives

Build physically allowed state models, select the correct coupling and rate units, compute a limiting-case prediction and troubleshoot model/measurement disagreement.

## 1. The three layers of RydIQule

RydIQule represents an atomic level/coupling graph, solves density-matrix dynamics, then maps a selected coherence to an observable. A Sensor defines a mathematical graph with user-supplied couplings and rates, while a Cell introduces atomic species-dependent information and optical response properties. Confusing these classes produces common teaching errors: a bare three-level Sensor with arbitrary rates is not a calibrated Rb or Cs optical transmission model.

## 2. Constructing a minimal graph

Choose states 0,1,2 with probe coupling (0,1), upper coupling (1,2), and relaxation so that a physical stationary state exists. Name the Rabi rates, detunings and whether package inputs are cyclic-frequency or angular-frequency-like numerical units. Use a small scanned probe detuning array and a fixed optical coupling. Verify the coupling-off limit, and inspect the system's states/edges before solving. The library permits arbitrary graph topology, making unphysical loops possible if selection rules are ignored.

## 3. Steady-state solution and physicality

A steady-state solver solves the Liouvillian nullspace with trace one. Check whether its returned rho is an array of real independent components or a full complex density matrix; representation can be compacted and varies by API. Do not assume rho.shape corresponds directly to N×N. Compare optical coherence and populations with known two-level limits. Numerically stable solutions can still be wrong if rates, units or level ordering are incorrectly assigned.

## 4. Thermal velocity averaging

The thermal probe/coupling detunings depend on k·v, making beam geometry essential. A Doppler-averaged solver must know relevant wavevectors and the gas velocity distribution. Increase velocity-class span and resolution until the predicted observable converges, then vary temperature and beam angle as separate physical parameters. A simple Lorentzian broadening slider does not reproduce all Doppler phenomena.

## 5. Susceptibility and propagation

The probe optical coherence becomes susceptibility only after dipole density and probe-frequency constants have been supplied. A Cell can encode physical vapor parameters, while bare Sensor examples need separate experiment values. An idealised optical susceptibility still requires propagation and detector conversion for a directly comparable intensity/voltage curve. Label axes by physical meaning, not generic 'EIT response' when the plotted variable is actually an internal coherence.

## 6. Time-domain and modulated signals

Time solvers can follow changing RF/optical phases, but integrating a stiff Liouvillian requires time steps that resolve fast and slow rates. Steady-state approximations fail if the modulation period is comparable to relaxation. Validate the t→long-time limit against an independently converged steady-state solve, and inspect Fourier sidebands with windowing and sample-rate controls.

## 7. Companion reproducible example

The book/examples/rydiqule_three_level.py script uses the documented Sensor/add_coupling/add_transit_broadening/solve_steady_state APIs when RydIQule is installed. It reports shape, parameters and limitations as JSON rather than inventing an experimental line. Extend it to a real Cell only after specifying full atomic state data and observable calibration.

## End-of-chapter questions with explained answers

### Question 1. Why is a Sensor plot not automatically measured Rb-87 transmission?

<details><summary>Reveal scientific reasoning</summary>

A Sensor need not include physical species, optical density, propagation or detector calibration.

</details>

### Question 2. What does a stationary solver solve?

<details><summary>Reveal scientific reasoning</summary>

The open-system Liouvillian fixed-point equations with trace conservation.

</details>

### Question 3. Why can rho have N²−1 real components rather than an N×N array?

<details><summary>Reveal scientific reasoning</summary>

A Hermitian trace-one matrix has N²−1 independent real degrees of freedom, which a numerical solver may compact.

</details>

### Question 4. When is Doppler averaging necessary?

<details><summary>Reveal scientific reasoning</summary>

When thermal motion changes relevant laser detunings sufficiently to alter the ensemble optical response.

</details>

### Question 5. How do you validate a time solver?

<details><summary>Reveal scientific reasoning</summary>

Check time-step convergence and long-time behavior against the steady-state solution where one exists.

</details>

### Question 6. What must precede interpretation of a probe coherence as volts?

<details><summary>Reveal scientific reasoning</summary>

Atomic susceptibility, medium propagation, photodetector transfer and measurement calibration.

</details>

## Reproducibility exercise

Run an independently testable calculation, record the package version and exact input state set, confirm units and selection rules, and compare to the cited API and a known physical limit. Write what a real experiment would need to validate the result. Avoid describing numerical output as an observed quantum sensor reading.

## References

ARC's [official documentation](https://arc-alkali-rydberg-calculator.readthedocs.io/en/latest/), RydIQule's [official documentation](https://rydiqule.readthedocs.io/en/stable/overview.html), Steck's spectroscopy tables, Gallagher and Foot; full [bibliography](../REFERENCES.md).
