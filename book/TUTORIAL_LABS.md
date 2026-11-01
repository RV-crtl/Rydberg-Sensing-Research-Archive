# General Rydberg Systems Engineering — laboratory and code manual

This is the **general, platform-independent** practical textbook companion: warm vapour, cold atoms, cavity-QED, tweezers, RF electrometry, optical spectroscopy and numerical experiments. Any one research project's actual apparatus or HFSS campaign belongs under its own research-source directories, not as the textbook's canonical example.

Each tutorial has a reproducible objective, execution plan, expected physical limit, and failure condition. These are *methodological teaching exercises*, not reports of measured or completed simulations. Follow institutional laser, electrical, high-voltage and vacuum safety rules.

## Lab 01. State-vector tomography without an atom

**Required background:** [Read the general chapter](chapters/01-mathematical-language.md).

**Procedure and verification:** Choose a normalized qubit |ψ⟩=cos(θ/2)|0⟩+e^{iφ}sin(θ/2)|1⟩. Predict probabilities in z, x and y measurement bases, and verify with small complex-array Python or JavaScript code. Record σ_y sign convention. As a limiting-case check, θ=0 must yield z=+1 independent of φ. Failure diagnosis: incorrect complex conjugation or interpreting a relative phase as a global phase.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 02. A two-level Hamiltonian from physical units

**Required background:** [Read the general chapter](chapters/03-hamiltonians.md).

**Procedure and verification:** Assemble a resonant two-level Rabi Hamiltonian using Ω/2π=1 MHz, then calculate the π-pulse time and complete cycle. Test finite detuning and compare the exact Rabi probability expression against a time-step integrator. Repeat with time step halved and verify norm conservation. Failure diagnosis: missing 2π, wrong off-diagonal conjugate or integrating a time-dependent Hamiltonian as a constant one.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 03. Open-system density matrix and positivity

**Required background:** [Read the general chapter](chapters/04-density-matrices.md).

**Procedure and verification:** Start with a physical ρ=diag(0.7,0.3), introduce a coherent phase and then a Lindblad dephasing operator. Verify trace one, Hermiticity, nonnegative eigenvalues and reduced coherence. Test zero-dephasing and long-time limits. Failure diagnosis: negative populations, unstable integration and confusion between population rate and optical coherence decay.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 04. E1 selection rules and state labels

**Required background:** [Read the general chapter](chapters/05-angular-momentum.md).

**Procedure and verification:** Enumerate n,l,j,m_j values for a hypothetical alkali Rydberg pair. Reject states that violate angular rules or parity. Use `python book/examples/arc_transition_atlas.py --list` before installing ARC. Validate the retained magnetic transitions by independent 3j/triangle rules. Failure diagnosis: q=m−m′ sign reversal or confusion between fine and hyperfine bases.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 05. Install and use actual ARC

**Required background:** [Read the general chapter](chapters/13-quantum-defect-and-arc.md).

**Procedure and verification:** Install dependencies using the versioned `book/examples/requirements-science.txt` (review platform-specific requirements). Run `python book/examples/arc_transition_atlas.py --run --species Rb87 --n 60 --output arc_results.csv`, checking that the scientific library is actually present. The CSV contains theoretical atom-model outputs, not measured data. Validate one transition against NIST/ARC documentation and test the energy-sign convention. Failure diagnosis: invalid states, unavailable package or accidental units conversion.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 06. Stark map and eigenstate identity

**Required background:** [Read the general chapter](chapters/27-multichannel-quantum-defect-theory.md).

**Procedure and verification:** Select a small finite atomic basis with a clear magnetic projection and field sweep. Use ARC Stark tools or an independent toy Hermitian Stark Hamiltonian to diagonalize at each E. Track eigenvector overlaps between adjacent field points instead of merely sorting eigenvalues. Increase basis size and field resolution until relevant levels converge. Failure diagnosis: swapped labels at avoided crossings or apparent energy discontinuity from basis mismatch.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 07. Three-state RydIQule steady state

**Required background:** [Read the general chapter](chapters/14-rydiqule-lab.md).

**Procedure and verification:** Install RydIQule into a reproducible virtual environment and run `python book/examples/rydiqule_three_level.py`. Check that `rq.solve_steady_state` returns finite real-basis density variables, which need not be an N×N matrix. Vary coupling strength and probe detuning, checking coupling-off and far-detuned limits. Then specify actual species-level data and Cell properties before claiming optical transmission. Failure diagnosis: missing decay/trace constraint, incorrect graph edges or invalid MHz convention.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 08. Thermal Doppler integration

**Required background:** [Read the general chapter](chapters/16-doppler-and-linewidth.md).

**Procedure and verification:** For an atomic thermal species at a declared temperature, generate a Maxwell–Boltzmann distribution of 1D velocities, calculate signed k·v detuning shifts for two beams, and integrate a complex weak-probe response. Double velocity range and integration resolution until the spectrum changes below a declared threshold. Failure diagnosis: incorrect co/counterpropagation sign or averaging intensity before susceptibility without justification.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 09. EIT, AT and unresolved splitting

**Required background:** [Read the general chapter](chapters/08-eit-and-autler-townes.md).

**Procedure and verification:** Construct a coherent ladder with ground, intermediate and upper states. Solve a steady-state density-matrix spectrum with finite decay and scan the probe detuning. Add a resonant RF-coupled fourth state and vary its Rabi rate. Observe how model peaks may overlap when splitting is smaller than linewidth. Test RF-off and coupling-off limits. Failure diagnosis: calling any pair of peaks an AT response or assuming splitting directly equals a calibrated external field without a state-specific dipole.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 10. Optical beam and detector calibration

**Required background:** [Read the general chapter](chapters/09-optics-lab.md).

**Procedure and verification:** For a Gaussian 780-nm test beam of known power and waist, calculate on-axis intensity, Rayleigh range and an estimated photodiode current at a declared responsivity. Compare with photodiode data under a safe approved setup, using a reference power meter and checking saturation/bandwidth. Failure diagnosis: using power measured before optical losses, or confusing the photodetector's electronic output with the optical carrier frequency.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 11. Radio-frequency antenna and measurement plane

**Required background:** [Read the general chapter](chapters/10-microwave-fundamentals.md).

**Procedure and verification:** Choose two microwave frequencies, calculate wavelength and expected far-field criteria, and decide whether the sensor lies in the radiative or near-field region for a specified antenna size. Calibrate a VNA at the desired reference plane and record complex S parameters with geometry. Failure diagnosis: interpreting S21 as the same thing as the local vector E field at the atom position.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 12. Full Stokes vector and circular sign

**Required background:** [Read the general chapter](chapters/11-stokes-jones.md).

**Procedure and verification:** Calculate Stokes coordinates for known Jones vectors H, V, diagonal and two circular phase signs. Verify S1²+S2²+S3²=S0² for ideal pure states and declare the phasor sign convention. Build a measured/analyser matrix with enough independent states and test S3 sensitivity, singular values and physicality. Failure diagnosis: a single linear polariser is unable to distinguish ±circular input states.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 13. Finite-array complex-field convergence

**Required background:** [Read the general chapter](chapters/18-hfss-metasurface.md).

**Procedure and verification:** Create a simple anisotropic electromagnetic structure in a documented full-wave solver. Use complex two-basis excitations, then compare a periodic cell with a finite panel. Export field values on a common physical sampling grid under independently adapted meshes and compare phase, gain, and derived observables. Failure diagnosis: claiming finite calibration from periodic S21 or accepting solver energy convergence without local-field agreement.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 14. Fisher information and experiment design

**Required background:** [Read the general chapter](chapters/19-information-matrix.md).

**Procedure and verification:** Build a known matrix with one weak singular direction and a calibrated Gaussian detector noise covariance. Compute F=AᵀC⁻¹A, compare candidate measurement states and optimize acquisition time under a fixed budget. Re-evaluate under correlated/heteroscedastic noise and held-out inputs. Failure diagnosis: declaring an algorithmically improved trace objective to be a measured improvement in hardware sensitivity.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 15. Two-atom Rydberg blockade

**Required background:** [Read the general chapter](chapters/25-rydberg-blockade.md).

**Procedure and verification:** For a two-atom toy interaction H with V=C6/R^6, compute dressed eigenenergies and double-excitation probability versus separation. Compare limiting cases V→0 and |V|≫ℏΩ. Add state-dependent interaction anisotropy as an extension. Failure diagnosis: treating a blockade radius as a discontinuous wall, or inferring entanglement from excitation suppression alone.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Lab 16. Plan a new Rydberg apparatus from an empty lab

**Required background:** [Read the general chapter](chapters/34-design-a-rydberg-system.md).

**Procedure and verification:** Choose the measurand and target uncertainty before choosing atomic species or lasers. Prepare species/transition, laser-lock, polarization, optical geometry, atomic motion, RF/cavity/tweezer platform, detector, source references, safety, commissioning stages and data/provenance budgets. Assign independent controls and explicit failure gates. Failure diagnosis: jumping directly to an impressive setup picture without a validated level ladder, measurement observable and readout chain.

**Notebook record:** source package/environment version; basis and all units; exact input/scan parameters; expected and observed model/measurement response; numerical convergence; uncertainty assumptions; failed controls; saved output path.

**Challenge question:** What independent measurement or numerical limit would most strongly falsify this interpretation? Answer in terms of a real observable rather than an unlabeled plot.


## Tutor assessment standards

A submission passes the conceptual rubric only if every calculation uses correct units, explains its assumptions and compares to an independent limiting case. A physical lab requires approved safety procedures, actual source data, calibrated references and reproducible collection. A browser-made illustration does not meet the experimental evidence gate.

[Actual ARC/RydIQule example sources](examples/README.md) · [Graduate multistep solutions](GRADUATE_PROBLEM_SETS.md) · [Annotated references](REFERENCES.md) · [Book home](README.md).
