# Computational electromagnetics and polarization-selective structures

**Independent general reference chapter.** Discusses universally applicable physics and engineering; no project-specific numerical HFSS result is asserted.

## Competencies

Model the system, specify a measurement chain and units, choose appropriate numerical tools, reproduce limiting cases and debug signal/solver failures.

## 1. Maxwell boundary-value problems

Finite-element electromagnetic simulation solves Maxwell equations under material, geometry, boundary and excitation assumptions. For frequency-domain harmonic fields, ∇×E=−iωB and ∇×H=J+iωD under an e^{+iωt} convention; signs reverse with e^{−iωt}. Metallic traces, dielectrics, losses and ports define the actual boundary-value problem. A solver returning a smooth plot is not proof that the model matches a fabricated structure.

## 2. Periodic cells versus finite devices

Floquet periodic boundaries describe an effectively infinite tiling under a specified phase progression and incidence. An actual finite array has edge diffraction, current redistribution, nonuniform illumination, feed/cell proximity and finite substrate effects. The periodic unit-cell S21 is therefore not interchangeable with the complex near-field map at an atomic vapour cell. If a proposed design fits inside a small cell window, finite aperture and observation volume are usually central.

## 3. Anisotropy, Jones matrices and handedness

For a linear deterministic two-port polarization response, represent transmitted complex field by J_out=T J_in, with T a complex 2×2 Jones transfer matrix in a fixed transverse basis. Circular discriminators require relative phase and amplitude response, not only larger transmission for one linear basis. A chiral or bianisotropic surface may need more complete tensor surface susceptibilities and incidence-angle characterization; naming a copper pattern 'chiral' does not establish handedness performance.

## 4. Switches, materials and losses

Frequency-dependent copper conductivity, dielectric permittivity/loss tangent, geometry tolerances and PIN diode parasitics influence currents and phase. An ideal conducting bridge may model one theoretical switching state but is not a diode with bias-dependent resistance, capacitance and package inductance. Calibrate physical components from appropriate S-parameter/device models and distinguish a first-stage concept screen from a hardware-predictive simulation. Manufacturing drawings should use the same copper layer and mask truth table as the solver.

## 5. Mesh and solver convergence

Adaptive energy convergence can succeed while a local complex E field remains mesh sensitive. Phase and small circular Stokes components can be particularly fragile. Evaluate solution changes across genuinely independently adapted meshes on the same physical field-sampling coordinates. Include frequency, input polarization, incidence angle, boundary type, observation depth and all switching states. A single excellent reference point cannot validate a broad frequency band or all finite geometries.

## 6. Field-to-polarimetry postprocessing

Export signed complex Ex,Ey and potentially Ez at relevant points, together with spatial coordinates and phasor convention. Compute Stokes or other physically justified observables after defining any spatial integration over a sensing volume. Build a calibration matrix and inspect rank, gain, singular values and cross-mesh held-out reconstruction. Reproduce figures from source CSV and project IDs; report failures, not only the best masks.

## 7. Verification workflow for independent research

Archive native solver projects and logs, exact material stackups, CAD geometry, field data, source scripts and mesh reports. Test a simple conductor/dielectric analytic limit before more complicated anisotropic cells. Then verify a single cell, finite array, incidence-angle response, substrate uncertainty and, eventually, a real measured prototype. Clarify what was computed versus actually fabricated and measured.

## End-of-chapter questions and answers

### Question 1. Why can periodic S21 fail to predict a local finite panel response?

<details><summary>Read the worked explanation</summary>

Edges, illumination, near-field sampling and boundary conditions differ between periodic and finite geometries.

</details>

### Question 2. What is missing from magnitude-only transmission for circular polarization?

<details><summary>Read the worked explanation</summary>

Relative phase and signed complex field components.

</details>

### Question 3. Why should PIN diodes not be modeled only as copper on/off in a hardware claim?

<details><summary>Read the worked explanation</summary>

Bias-state parasitics, package inductance, reverse capacitance and losses matter.

</details>

### Question 4. What must a local-field mesh study compare?

<details><summary>Read the worked explanation</summary>

Complex fields at the same physical points under independently adapted meshes and matched excitations.

</details>

### Question 5. Can rank four alone certify a polarization sensor?

<details><summary>Read the worked explanation</summary>

No; physical calibration, gain, noise, finite-field transfer and relevant detection observable must also pass.

</details>

### Question 6. What distinguishes simulation evidence from a measured metasurface result?

<details><summary>Read the worked explanation</summary>

A physical prototype with independently calibrated illumination/detection and real acquired data.

</details>

## Research problem

Build a falsifiable numerical or experimental analysis with correct units and explicitly stated physical observables. Write its independent source and calibration references, convergence thresholds, and diagnostic on/off controls. Test at least one failure case. Never report simulated or illustrative values as new physical measurements.

## Further reading

Foot, *Atomic Physics*; Pozar, *Microwave Engineering*; official Ansys and RydIQule references; [complete bibliography](../REFERENCES.md).
