# Advanced computational atomic-physics methods: ARC, RydIQule, Stark maps and EIT model verification

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
