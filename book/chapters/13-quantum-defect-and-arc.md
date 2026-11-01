# Practical atomic calculations with ARC

**General advanced atomic science reference.** No particular laboratory result is asserted. Primary numerical APIs are linked in the [bibliography](../REFERENCES.md).

## Learning objectives

Build physically allowed state models, select the correct coupling and rate units, compute a limiting-case prediction and troubleshoot model/measurement disagreement.

## 1. What ARC computes and what it does not

The Alkali Rydberg Calculator (ARC) provides atomic energies, transition dipoles, Stark and Zeeman maps, lifetimes and pair-interaction methods for supported atomic species. These are numerical atomic-model results, not experimental measurements. A transition table must retain exact n,l,j,m labels, isotope, selected atomic model, electric/magnetic fields, output units and package version. A correctly installed library can compute an irrelevant transition if optical access or selection rules were not defined.

## 2. Build an auditable state table

Choose isotope and quantum-number basis before screening. For each initial/final pair, first test E1 parity and angular/magnetic selection rules, then query getTransitionFrequency; ARC returns signed frequency in Hz based on energy ordering. Query getTransitionWavelength in metres, and distinguish vacuum wavelength from laboratory wavelength-in-air conventions. Save dipole matrix elements in ea0 with their sign, not just absolute values, when interference between pathways is important.

## 3. Rabi frequency and electric-field orientation

For a resonant coupling, Ω=|μ·E|/ℏ in rad/s. ARC returns some Rabi-frequency APIs in angular-frequency units; documentation must be checked for each exact method. For a state-specific polarisation component q, supply m and m′ consistently: q=m′−m. A polarisation projection can be zero even if the reduced radial matrix element is large. Strength screening should account for laser/RF power and the actual field geometry, not only the number shown in a dipole table.

## 4. State lifetimes and environment

State radiative lifetimes, blackbody-induced transitions, level mixing and collisional loss affect usable coherence. A state near another manifold can have a long isolated radiative lifetime but poor stability in a thermal cell or near surfaces. ARC supplies transition rates and lifetime options, but experimental dephasing must be measured independently. Record temperature when evaluating blackbody-related rates.

## 5. Stark maps, avoided crossings and pair interactions

To generate a Stark map, define an atomic basis with n,l,j,m bounds, diagonalise over a field sweep and examine state admixtures and eigenvector overlap. Sorting eigenvalues by energy alone can relabel the physical state at avoided crossings. For interactions, choose pair basis, separation, angle and perturbative or nonperturbative regime; near Förster resonance, C6 approximations may fail. Convergence with basis truncation is part of the scientific result.

## 6. Run the companion code

Use book/examples/arc_transition_atlas.py with --list for a no-ARC preview of allowed E1 pathways, then --run to generate state-resolved numerical results using an installed version of ARC. The CSV records true computed values and theoretical model status; it does not fabricate measurements or assert optical access. Audit the output against a known reference line or an independent atom database before using it in hardware design.

## 7. Typical failure signatures

Negative transition frequency often means reverse level ordering rather than an invalid state. A missing level can reflect unsupported atom data or incorrect n/l/j values. Zero matrix element can be a real selection-rule result; an unexpectedly huge dipole may reflect an inadequate basis or unit conversion. If a Stark curve changes dramatically with basis-size increase, do not present the earlier graph as converged.

## End-of-chapter questions with explained answers

### Question 1. What is the unit of ARC getTransitionFrequency?

<details><summary>Reveal scientific reasoning</summary>

Hertz, signed by relative state-energy ordering.

</details>

### Question 2. Can a nonzero dipole matrix element imply an experimentally accessible ladder?

<details><summary>Reveal scientific reasoning</summary>

No; optical intermediate states, available wavelengths and linewidth constraints must also be checked.

</details>

### Question 3. Why may q=0 fail for a given pair?

<details><summary>Reveal scientific reasoning</summary>

The magnetic projection or other selection rules can forbid that E1 pathway.

</details>

### Question 4. Why examine eigenvectors on a Stark sweep?

<details><summary>Reveal scientific reasoning</summary>

Eigenvalue ordering alone may exchange state identity at an avoided crossing.

</details>

### Question 5. When should pair-state diagonalisation replace a C6 perturbative estimate?

<details><summary>Reveal scientific reasoning</summary>

Near resonant Förster channels or strong interaction mixing.

</details>

### Question 6. What distinguishes ARC output from a measured spectrum?

<details><summary>Reveal scientific reasoning</summary>

ARC computes atomic-model quantities; a real spectrum additionally requires populations, broadening, readout and experimental calibration.

</details>

## Reproducibility exercise

Run an independently testable calculation, record the package version and exact input state set, confirm units and selection rules, and compare to the cited API and a known physical limit. Write what a real experiment would need to validate the result. Avoid describing numerical output as an observed quantum sensor reading.

## References

ARC's [official documentation](https://arc-alkali-rydberg-calculator.readthedocs.io/en/latest/), RydIQule's [official documentation](https://rydiqule.readthedocs.io/en/stable/overview.html), Steck's spectroscopy tables, Gallagher and Foot; full [bibliography](../REFERENCES.md).


---

## Detailed independent reference, extended case study and problem set

A numerical atomic modelling workflow should answer a *scientific question*, not merely generate a plot. This guide distinguishes level data, optical transition strengths, state-resolved Hamiltonians, numerical density matrices and experimental transmission. It is valid across alkalis and atomic-receiver architectures; a project-specific laser range belongs in that project's laboratory folder.

## Stage A — specify physics before installing software

Write the isotope, intended ground/intermediate/Rydberg states, quantisation axis, optical polarisation and microwave polarisation. Specify whether you want an isolated-atom energy, a transition rate, a field-induced mixing calculation, coherent dynamics, Doppler-broadened susceptibility, absorption or an experimentally inferred electric field. Different APIs compute different outputs and do not become interchangeable because they return a number in MHz.

An atom database uses conventions: quantum numbers, quantum-defect approximation, fine/hyperfine treatments, selected isotope constants, blackbody temperature and field orientation. Document them in code and in the output table. When the requested experiment involves high angular momentum, Förster resonances or interacting pairs, a single-atom transition table is insufficient. When the requested result is a room-temperature EIT spectrum, a single transition frequency is insufficient.

## Stage B — obtain an auditable ARC environment

Use a dedicated Python virtual environment and pin the installed ARC version in the output manifest. Install with `python -m pip install ARC-Alkali-Rydberg-Calculator`; import `Rubidium87` from `arc` when working with that isotope. In a new environment, test one published reference line before using any generated transition list. Do not suppress warnings about numerical basis bounds or data sources.

A minimal exploratory cell is:

```python
from arc import Rubidium87
atom = Rubidium87()
frequency_hz = atom.getTransitionFrequency(60, 0, 0.5, 60, 1, 1.5)
print("Signed transition frequency in Hz:", frequency_hz)
print("Positive carrier in GHz:", abs(frequency_hz) / 1e9)
```

This example demonstrates the interface, **not** a verified experimentally accessible transition or a recommendation of states. Check the API version and sign convention and compare the result to an independent reference. For dipole coupling, check the documented dipole matrix element API, angular momentum projections and units. A value in elementary-charge Bohr radii `ea0` becomes C m only after multiplication by e and a0. A coupling Rabi angular rate is `Ω = |d·E|/ℏ`, whereas cycles-per-second `Ω/(2π)=|d·E|/h`. Those expressions are dimensionally equivalent but cannot be mixed in a solver's parameter convention.

## Stage C — design a defensible transition-search algorithm

A good search first filters by experimentally available optical channels, then by selection rules, next by microwave band and finally by strength/coherence constraints. If the optical ladder is not accessible, a very large RF dipole is scientifically irrelevant. Never sort thousands of pairs by absolute frequency difference alone and call the top five optimal. Use a Pareto set including oscillator strength, RF tuning margin, optical detuning, lifetime, blackbody population transfer, unwanted nearby lines, Zeeman susceptibility and practical power.

Keep each record's `species, isotope, n1,l1,j1,n2,l2,j2, F/m if modelled, frequency_Hz, dipole_SI, polarization_q, lifetime_s, method, library_version`. Avoid interpolated spectroscopic data that is not calculated or observed. For a field-sweep, record basis-state truncation and test level-map stability as basis size grows; eigenvalue crossing and near-degenerate mixing can make simplistic state labels unreliable.

A dipole transition strength and a spontaneous transition *rate* answer different questions. ARC's `getTransitionRate` explicitly takes upper/lower levels and temperature (with blackbody effects included according to its documentation); it does not return a laboratory coherent Rabi frequency. <https://arc-alkali-rydberg-calculator.readthedocs.io/en/latest/generated/arc.alkali_atom_functions.AlkaliAtom.getTransitionRate.html>

## Stage D — build from a two-level Hamiltonian to an optical-Bloch model

Before calling RydIQule, solve a simple resonant two-state Hamiltonian independently: ideal ground-to-excited population `Pe(t)=sin²(Ωt/2)`. Confirm `Pe(0)=0`, population never exceeds one and the oscillation period matches 2π/Ω. Then add one decay and compare the numerical steady state with the expected optical-pumping limit.

For a three-level EIT ladder, define which states share each optical coupling and which state relaxes into which lower state. A `Sensor` represents abstract states/couplings; a physical `Cell` brings atomic details and probe observable. RydIQule's steady-state solver solves the Lindblad master equation; time-dependent and Doppler treatments require distinct solver options. It may return a density matrix whose *interpretation* as optical transmission needs susceptibility, optical depth and the experimental optical reference. <https://rydiqule.readthedocs.io/en/stable/overview.html>

Never assume that an API's detuning uses Hz rather than angular-frequency units; inspect the **installed version**. This is a common source of false splitting and off-by-2π sensitivity. Define a single `MHz` convention at each model boundary and check a known small system before changing a large script.

## Stage E — Doppler and multilevel realism

For a moving atom, a laser phase `k·r−ωt` becomes a shifted drive as the atom traverses the beam: `Δ(v)=Δ(0)−k·v` under a declared sign convention. Counter-propagating probe and coupling fields can reduce or increase the two-photon Doppler term depending on ladder geometry. The weighted velocity average is *not* equivalent to fitting a single broadened Lorentzian; optical coherences and nonlinear propagation can break such shortcuts.

Add magnetic sublevels whenever elliptical polarisation or field direction matters. The spherical field components `E_{−1},E_0,E_{+1}` relative to B couple different `Δm`. A three-state scalar-RF model cannot identify arbitrary handedness or account for multi-mJ dressed spectra. Compare physical spectroscopy with independent magnetic-field and source-frequency references before assigning peaks.

For `solve_steady_state(sensor, doppler=True)`, consult the v2.x solver documentation for Doppler mesh methods and whether to sum weighted velocity classes; the returned arrays can otherwise be misunderstood. <https://rydiqule.readthedocs.io/en/stable/api/_autosummary/rydiqule.solvers.solve_steady_state.html>

## Stage F — numerical audits and acceptance criteria

Check that the density matrix is Hermitian to numerical tolerance; trace is one; real populations are nonnegative; purity does not exceed one. Verify convergence with respect to velocity mesh, state-basis truncation and detuning sampling. Repeat with zero RF, zero coupling and vanishing field to check expected limits. A simulated peak can move because the scan uses a changed reference sign—not because an atom changed its Zeeman state.

Distinguish broadening sources: spontaneous lifetime, blackbody redistribution, laser phase noise, transit dephasing, Doppler classes, atomic collisions and RF source linewidth. Do not bury all under one fitted `gamma` and then claim microscopic interpretation. Keep the original parameter table and avoid changing multiple mechanisms to match a single experimental spectrum.

Use an independent comparison whenever possible: a measured standard resonance, a published reference spectrum, a small analytically solvable Hamiltonian and a separate implementation of selected eigenenergies. Passing a package smoke test only confirms execution and basic numerical plausibility.

## Stage G — end-to-end output and collaboration readiness

Produce a machine-readable `run_manifest.json`, transition table, convergence table, source scripts, environment lock, plots with units and a human-readable limitations memo. A valid figure needs an exact path to its source data and no substituted illustrative values. If a native solver or a measurement is missing, status must say `NOT_RUN` or `NOT_AVAILABLE`, not `PASS`.

For a new research programme, maintain a bounded grid: atom species, levels, optical geometry, polarisation, RF field, temperature, B field, beam parameters and target observable. Use screening to discard impossible combinations before detailed simulation; log all rejected candidates and why. A new high-performance physical system is discovered by confronting models with independent data, not by recursively generating plots.

## Diagnostic cases with answers

<details><summary>1. ARC predicts a microwave transition in the right band but no EIT appears. Where should you start?</summary>

Check the entire optical ladder selection rules and tuning, not only the microwave difference. Verify optical locks, coupling/probe overlap, polarisation, cell condition, atomic density and detector before testing RF sensitivity.

</details>
<details><summary>2. What does a negative signed ARC transition frequency mean?</summary>

It reflects the requested level ordering and energy difference. A physical positive carrier may be its absolute value, but the state direction and quantum numbers must remain in the coupling matrix and transition table.

</details>
<details><summary>3. A reported dipole moment is 700 ea0 and field 0.1 V/m. What is the ideal cyclic Rabi rate?</summary>

Compute `fR=dE/h=700×(1.602176634×10⁻¹⁹)(5.29177210903×10⁻¹¹)(0.1)/(6.62607015×10⁻³⁴)`, roughly 0.894 MHz. This assumes aligned dipole and peak-field convention; a real state-specific Clebsch factor may reduce it.

</details>
<details><summary>4. The density matrix has trace 0.9999 and eigenvalue −0.02. Is it acceptable?</summary>

Not without investigation. Trace error is small, but a substantially negative eigenvalue violates positivity and often indicates numerical, model or interpretation problems.

</details>
<details><summary>5. Why are RydIQule absorption and photodiode voltage not directly identical?</summary>

The solver produces a quantum optical response. Optical propagation, beam geometry, atomic density, detector responsivity, gain and offsets are needed before predicting voltage. Fitting only a voltage baseline cannot validate the internal atomic Hamiltonian.

</details>
<details><summary>6. What does a successful minimal Sensor smoke test prove?</summary>

That one numerical configuration and package interface execute. It does not establish the isotope-specific multilevel physics, thermal averaging, field calibration, experimental agreement or research novelty.

</details>
<details><summary>7. How should a researcher select the Doppler velocity grid?</summary>

Converge the observable against increasing integration nodes and range, keeping temperature and beam geometry fixed. Compare alternative quadrature schemes and report the numerical residual.

</details>
<details><summary>8. Why might a simple AT doublet formula fail with elliptical RF polarisation?</summary>

Several magnetic sublevels can couple with different q components, mixing or overlapping dressed branches. Model the actual manifold and optical readout instead of attributing every pair of peaks to one two-level splitting.

</details>
<details><summary>9. Why can't all solver linewidths be reduced to zero to recover a “perfect” field estimate?</summary>

The resulting model is no longer representative of the apparatus; optical, thermal, atomic and source decoherence limit actual observability. Calibration and sensitivity must follow a physically justified noise/decay model.

</details>
<details><summary>10. How should a team decide whether a result can be used in a paper?</summary>

Require source inputs and exact environment, reproducible derived results, independent convergence or calibration, transparent limitations and an explicit claim-to-evidence chain. A graph or notebook finishing without exceptions is necessary but not sufficient.

</details>

## Authoritative references

Šibalić et al., *ARC*, Computer Physics Communications **220**, 319–331 (2017), DOI https://doi.org/10.1016/j.cpc.2017.06.015 . Miller et al., *RydIQule*, Computer Physics Communications **294**, 108952 (2024), DOI https://doi.org/10.1016/j.cpc.2023.108952 . Gallagher, *Rydberg Atoms*, Cambridge University Press. Official documentation linked above.


---

## Advanced ARC and RydIQule computational validation

## The atomic-data problem is a graph-search problem, not a table lookup

A working Rydberg receiver, tweezer experiment or coherent state-transfer experiment follows a path through atomic states. The nodes of that path carry energies, angular quantum numbers, hyperfine character and field-dependent mixing. The edges represent optical, microwave, Raman or collision-mediated coupling whose strengths depend on dipole matrix elements and the field's polarisation. Selecting only a single state-pair frequency ignores the fact that the chosen state must actually be populated and subsequently measured.

For an alkali atom, choose species and isotope first. State labels such as nS1/2 and nP3/2 describe principal, orbital and fine-structure angular momentum, but may be incomplete at low n, in strong magnetic fields or when hyperfine mixing matters. An ARC \`Rubidium87\` level calculation may screen energy differences; it does not by itself solve the full experimental level graph, atom density or laser transition power budget.

A general screening strategy enumerates only physically relevant states. Constrain the initial optical state, available laser frequencies and useful detunings. Generate allowed intermediate links, then test accessible Rydberg states. Rank RF-coupled neighbours only after this path exists. Each edge should record transition frequency, q polarisation, dipole strength, effective Rabi rate for a reference field, selected electric and magnetic field, lifetime and uncertainty in the model. Cross-check strongest predictions against published spectroscopy where possible.

## Quantum defects are state dependent

The hydrogenic high-n energy E≈−hcR*/n² is a useful scale but not sufficient for alkalis. Effective principal quantum number n*=n−δ_{ℓj}(n) accounts for penetration and core effects. Some quantum-defect parameterisations include an expansion δ(n)=δ0+δ2/(n−δ0)²+… whose domain of validity varies by species and state. Use the library's state-specific model rather than fitting one universal constant and applying it to all ℓ and j. Perturbed states, avoided crossings and electric field mixing can invalidate simple labels altogether.

For two neighbouring high-n levels in a hydrogenic limit, characteristic spacing scales roughly as n⁻³. That trend is useful when choosing a microwave band: larger n generally produces smaller neighbouring-state gaps, but the relevant RF selection rule and actual quantum defects determine the usable transition. A strong off-resonant dipole nearby can also produce AC Stark shifts or spectral interference that a naïve single-pair model misses.

## Calculate oscillator strengths with angular selection rules

An electric-dipole interaction H_int=−d·E is a tensor operator. Matrix elements of a spherical dipole component d_q involve reduced matrix elements times angular coefficients. The reduced matrix element relates to radial wavefunction overlap and state structure; the Clebsch–Gordan coefficient determines angular projection and may vanish. When calculating polarisation response, state which \`q∈{−1,0,+1}\` basis is used, and how it relates to the laboratory field components and magnetic-field direction.

If a numerical routine reports a reduced element or radial matrix element, do not automatically interpret it as the full m-resolved coupling strength. The lifetime and blackbody transitions also need state-specific evaluation. An allowed microwave transition may have a long ideal radiative lifetime yet short usable experimental coherence because of blackbody redistribution, collisions, transit or laser phase noise.

## Building Stark and Zeeman maps responsibly

An electric field mixes opposite-parity angular-momentum states and can induce nonlinear shifts. A numerical Stark map is constructed by diagonalising a Hamiltonian in a truncated basis. The basis extent in n,ℓ,j,m and the field range are therefore convergence parameters. For each field point, increase basis size until the eigenenergies and relevant transition strengths stabilise to the desired tolerance. An attractive avoided-crossing plot with no basis check is a numerical hypothesis.

Tracking states by sorting eigenenergies can swap their labels at avoided crossings. A more stable procedure tracks eigenvector overlap between adjacent field values and checks expectation values of diagnostic operators. Near true degeneracies, continuous tracking may not be unique and should be reported as a subspace; forcing a single label can create unphysical discontinuities in predicted dipole strengths.

For Zeeman response, determine which angular momentum is conserved in the field range. A low-field ground hyperfine manifold and a high-n fine-structure manifold do not necessarily obey the same simple linear g-factor formula. A Breit–Rabi model may be required for low-lying hyperfine states, while detailed numerical diagonalisation may be necessary where levels mix.

## A robust ARC Python pipeline architecture

A mature workflow separates configuration, atomic calculation, ranking, test fixtures and visualisation. The configuration must include the exact atom class, quantum-state limits, optical constraints, RF band, field ranges, dipole threshold conventions, units and environment version. A generated CSV should never lose the original state labels or separate the transition rate from the coherent Rabi rate.

A minimal source-checked starting point is:

\`\`\`python
from arc import Rubidium87
atom = Rubidium87()
f_hz = atom.getTransitionFrequency(60, 0, 0.5, 60, 1, 1.5)
assert isinstance(f_hz, (float, int))
print("Signed energy difference frequency [Hz]:", f_hz)
print("Positive carrier [GHz]:", abs(f_hz) / 1e9)
\`\`\`

The actual value is deliberately not fabricated here. Verify the installed API and physical level ordering, then compare with a published line before screening thousands of possibilities. The 60S↔60P example is an API demonstration, not a claim that those states are the optimum for any experiment. Keep the sign of f_hz in the scientific record.

An independent unit test should reproduce a known transition frequency to documented tolerance and ensure a deliberately swapped quantum number fails the expected physical selection. Another should check dipole conversion: 1 ea0≈8.4783536×10⁻³⁰ C m, using exact elementary charge and the adopted Bohr radius constant. Finally test that changing an input field orientation changes the projected coupling as expected. A test comparing output to an independently computed formula is stronger than comparing it to a number produced by the same function.

## RydIQule graphs and the Lindblad problem

A general RydIQule \`Sensor\` is a graph of energy states and coherent couplings with decay and dephasing. A physical atomic \`Cell\` can obtain certain atomic parameters from ARC and enable probe susceptibility and transmission-oriented calculations. The steady-state solver finds a density matrix satisfying the Lindblad dynamics under specified drives, not a detector voltage trace. The output observable must be linked to a chosen probe transition and optical propagation model.

A three-level ladder should be built incrementally: first test that the ground state is stationary with no drive; add probe and verify a conventional absorption response; add coupling and observe a coherent two-photon feature in the correct regime; then vary detuning to test dark-state and far-off-resonance limits. Introduce a fourth RF-coupled Rydberg state only after the optical response has been verified. Multilevel magnetic states must be included for handedness-sensitive effects.

An authoritative API demonstration is not equivalent to a validated apparatus simulation. RydIQule exposes \`solve_steady_state\` for its Sensor/Cell models, and also time-dependent and Doppler-specific capabilities. Its documentation explains that \`solve_steady_state(sensor, doppler=True)\` may require a suitable velocity-mesh method and aggregation options, depending on the installed version. Always read the current function signature and examples in the installed environment rather than copying arguments from an older notebook.

## Doppler averaging needs proper propagation geometry

For an atom moving at velocity v, an optical field's phase gives a frequency shift proportional to k·v. In a counter-propagating ladder, one two-photon Doppler combination can be substantially smaller than the other, but residual wavelength mismatch remains. Compute the actual vectors, not a memorised sign. The velocity distribution must be normalised and sufficiently sampled. Temperature determines characteristic velocities and atomic density, so it can alter both Doppler and absorption simultaneously.

Compare velocity-grid sizes and quadrature schemes until the predicted observable converges. Increasing grid resolution indefinitely without checking the physical line-shape model is wasteful; a model with the wrong beam geometry will converge beautifully to the wrong spectrum. Preserve the convergence study and the thermodynamic parameters with every plot.

## From density matrix to optical absorption

For a weak probe and a specified level convention, the probe coherence often enters the linear susceptibility. A propagation model then maps the susceptibility to transmitted probe amplitude and intensity. The physically calibrated cell length, density, beam waist and detection geometry may be needed. A raw \`Sensor\` density matrix does not define an absolute transmission without that optical context. Different experiments may instead use fluorescence, ionisation or microwave heterodyne observables; the inversion model must match the actual detector.

Optical depth, propagation saturation and spatially varying fields can cause departures from a simple optically thin formula. Always state when an approximation is made. A single arbitrary linewidth parameter cannot separately encode spontaneous decay, Doppler averaging, laser phase noise and transit in a way that supports unambiguous mechanistic inference.

## Verification against physical and mathematical limits

Before using numerical spectra in research reporting, check Hermiticity and trace of the returned density matrices, population positivity, convergence under state and Doppler truncation, and known drive-off limits. Verify that simulated optical features respond to physically meaningful parameter changes. If a calculated spectrum predicts a feature with no actual optical coupling, the level graph may contain an unintended edge or numerical misassignment.

For full-vector field inference, prepare multiple independent polarisation configurations. Field handedness may couple different m sublevels; a scalar three-state EIT fit cannot generally determine the sign of circular polarisation. When a model predicts splitting, compare it with multilevel dressed-state eigenvalues and realistic linewidth rather than assuming every doublet directly equals one microwave Rabi angular rate.

## End-of-chapter problems with answers

<details><summary>Q17. Why should transition ranking begin from laser access rather than RF dipole strength?</summary>

A transition that cannot be optically prepared or read out cannot be implemented as the intended experiment, regardless of its microwave strength. Filter the complete ladder before optimising RF response.

</details>

<details><summary>Q18. An ARC function reports frequency −1.9 GHz. Is the microwave carrier negative?</summary>

No. The signed energy difference reflects level order; the positive carrier magnitude is 1.9 GHz. Preserve the sign in the state transition record and do not silently reverse its associated polarisation conventions.

</details>

<details><summary>Q19. Convert 500 ea0 to SI dipole moment.</summary>

Using 1 ea0≈8.4783536×10⁻³⁰ C m, the dipole is approximately 4.239×10⁻²⁷ C m. The full transition coupling may include an angular coefficient not included in this reduced value.

</details>

<details><summary>Q20. Why is an ARC transition rate not a microwave Rabi frequency?</summary>

A transition rate describes spontaneous or thermally induced population transfer under a different physical model. Coherent Rabi frequency depends on applied field amplitude and the projected dipole matrix element.

</details>

<details><summary>Q21. What numerical experiment tests whether a Stark level is robust against basis truncation?</summary>

Recompute its energy, eigenvector composition and dipole strengths while systematically enlarging basis bounds, at fixed field and state-tracking criteria. Report convergence.

</details>

<details><summary>Q22. Why can an eigenvector label jump at an avoided crossing?</summary>

Sorting eigenvalues alone can exchange the physical character associated with adjacent eigenvectors. Track state overlaps and expectation values or report an ambiguous subspace.

</details>

<details><summary>Q23. What is the mathematical steady-state condition for RydIQule's density matrix?</summary>

The Liouvillian acting on ρ vanishes, Lρ=0, with trace-one and physicality constraints. This does not directly determine a measured photodetector voltage.

</details>

<details><summary>Q24. Why must a 3-state ladder test recover the no-coupling limit?</summary>

The simpler limit is an independent regression test of state ordering, detuning conventions and decay. A model that fails there cannot support a more complicated RF inference.

</details>

<details><summary>Q25. Can a perfectly converged Doppler grid rescue a wrong laser propagation sign?</summary>

No. It converges the mathematically wrong model. Derive the Doppler term from the actual optical phase and wavevector geometry first.

</details>

<details><summary>Q26. Why might a Doppler-broadened EIT line differ from a Lorentzian?</summary>

Different velocity classes and coherent pathways contribute nontrivially. Collisions, optical pumping and propagation can produce asymmetry or non-Lorentzian structure.

</details>

<details><summary>Q27. Does RydIQule's steady-state solution directly predict volts on a transimpedance amplifier?</summary>

No. The atomic response must be linked through optical susceptibility and propagation, detector responsivity, gain, offsets and bandwidth to the electrical readout.

</details>

<details><summary>Q28. What is a test of density-matrix physicality?</summary>

Check Hermiticity, trace ≈1, nonnegative populations and eigenvalues within numerical tolerance, plus purity bounds. Significant failures indicate a model or solver issue.

</details>

<details><summary>Q29. When is a single RF-coupled Rydberg pair model insufficient for polarimetry?</summary>

When the field couples multiple magnetic sublevels, has independent spherical components or mixes nearby states. Use a validated multilevel model and independent reference polarisations.

</details>

<details><summary>Q30. What scientific information should accompany an ARC transition-screening CSV?</summary>

Species/isotope, exact state quantum numbers, field/axis, optical/RF access criteria, signed frequency and units, dipole definition, lifetime model, ARC version and source references.

</details>

## Primary software references

- Šibalić et al., ARC, *Computer Physics Communications* **220**, 319–331 (2017), https://doi.org/10.1016/j.cpc.2017.06.015 .
- Miller et al., RydIQule, *Computer Physics Communications* **294**, 108952 (2024), https://doi.org/10.1016/j.cpc.2023.108952 .
- ARC documented atomic functions: https://arc-alkali-rydberg-calculator.readthedocs.io/en/latest/alkali_atom_functions.html .
- RydIQule steady-state and Doppler solver documentation: https://rydiqule.readthedocs.io/en/stable/api/_autosummary/rydiqule.solvers.solve_steady_state.html .
