# RydIQule: optical Bloch and Doppler modelling

**Part:** Atomic software · **Type:** educational background, not new experimental data.

## Core explanation

RydIQule uses Sensor/Cell graphs to represent states, coherent couplings and decay and then solves steady-state or time-dependent density matrices. It is NOT just a curve-fit library. Begin with a dimensionless three-state benchmark before introducing actual Rb-87 state structure, transit relaxation, optical depth, Doppler velocity classes and RF sublevels. Document whether a solver returns a dimensionless susceptibility, optical phase or transmission. In RydIQule's conventions, coupling detunings/Rabi frequencies are often in MHz-like units; consult the installed API documentation rather than automatically appending 2π.

## Worked learning / laboratory exercise

Run the upstream-documented minimal example: `import rydiqule as rq; s=rq.Sensor(3); s.add_coupling((0,1),detuning=1,rabi_frequency=1); s.add_coupling((1,2),detuning=2,rabi_frequency=2); s.add_transit_broadening(0.1); sol=rq.solve_steady_state(s)`. Check the number of independent density-matrix parameters (8 for three states) and solution convergence. For physical transmission use Cell with a valid probe observable and optical depth.

## Self-test

**Question:** Why is a three-state model inadequate for claiming arbitrary-RF polarimetry in a biased Rydberg gas?

<details><summary>Reveal answer and scientific reasoning</summary>

Polarisation can couple multiple magnetic sublevels coherently; a toy ladder may not distinguish handedness or additional avoided crossings. Use actual selected sublevels and RF spherical components with validated decays.

</details>

## Red flags and diagnosis

Blindly applying a two-level AT peak-to-field calibration to an unresolved multilevel spectrum.

## Validity and reflection

- Identify each approximation or model limitation before reusing the worked example.
- Identify which physical measurement or native HFSS field could falsify the argument.
- Document units, state basis, time convention, calibration reference, exact code and source versions.
- Check sensitivity to numerical errors and state a quantitative acceptance gate before declaring a result.

## Source

RydIQule documentation: https://rydiqule.readthedocs.io/en/stable/overview.html. [Book references](../REFERENCES.md) · [Syllabus](../README.md).
