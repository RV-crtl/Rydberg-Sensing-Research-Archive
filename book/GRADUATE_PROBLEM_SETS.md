# Graduate problem sets — original multistep solutions

This companion source provides **12 worked, conceptually distinct research problems**, each with its own method and detailed physical interpretation. Unlike the separate 1,000-case formula-practice workbook, these problems require modelling choices, derivations, uncertainty interpretation and research judgement.

All numerical inputs are illustrative except exact defined SI constants. None of the answers represents a real laboratory result or a completed full-wave solve. Students should attempt the problem first, then reveal the solution.

## Problem 1. Quantum phase and complementary measurements

**Problem.** A qubit is prepared as (|g⟩+e^{iφ}|e⟩)/√2. Derive the probabilities in the z, x and y bases. Explain which measurement identifies φ and what ambiguities remain if only the z basis is available.

<details><summary>Show the worked reasoning and diagnostic significance</summary>

Use the Pauli matrices σx,σy,σz in basis {|g⟩,|e⟩}. Its density matrix has diagonal 1/2 and off-diagonal e^{-iφ}/2. Consequently ⟨σx⟩=cosφ, ⟨σy⟩=sinφ and ⟨σz⟩=0. The ± eigenstate probabilities in each Pauli basis are p±=(1±⟨σ⟩)/2. Thus z measurements are 50/50 for every φ. Combining x and y expectations determines φ modulo 2π using atan2(⟨σy⟩,⟨σx⟩). If only x is measured, cosφ cannot distinguish +φ and −φ. This is the atomic counterpart of adding a circular-sensitive analyser to linear polarimetry. An actual experiment must calibrate basis rotations and detector errors rather than reading φ directly from one raw count.

</details>

**Further investigation.** Which physical assumption is weakest? Design one independent calibration or numerical limiting-case test that would falsify this solution. Compare your analysis with [the relevant textbook chapter](chapters/01-mathematical-language.md).

## Problem 2. Rotating-wave approximation and when it breaks

**Problem.** For a two-level system driven by E(t)=E0cosωt, derive the fast and slow phase factors in the interaction picture. State a dimensionless measure indicating whether counter-rotating terms can be neglected.

<details><summary>Show the worked reasoning and diagnostic significance</summary>

The cosine is (e^{iωt}+e^{−iωt})/2. In the interaction picture the raising operator acquires exp(iω0t); therefore its two terms oscillate at frequencies ω0−ω and ω0+ω. Near resonance, |Δ|=|ω−ω0| is small but ω0+ω≈2ω0 is large. If coupling Ω and detuning |Δ| are much smaller than carrier frequency ω0, the rapid term averages over the slower population dynamics. At very strong driving it produces effects such as the Bloch–Siegert shift, and the RWA should be compared against a full time-dependent/Floquet calculation. The approximation must be checked with angular frequencies throughout; substituting cyclic MHz for angular rates is a separate 2π mistake.

</details>

**Further investigation.** Which physical assumption is weakest? Design one independent calibration or numerical limiting-case test that would falsify this solution. Compare your analysis with [the relevant textbook chapter](chapters/03-hamiltonians.md).

## Problem 3. Density matrix physicality under numerical error

**Problem.** A solver returns ρ=[[0.52,0.51],[0.51,0.48]]. Decide whether the output is a physical density matrix, and derive a meaningful error diagnosis.

<details><summary>Show the worked reasoning and diagnostic significance</summary>

The matrix is Hermitian and has trace 1. Its determinant is 0.52×0.48−0.51²=0.2496−0.2601=−0.0105, so one eigenvalue must be negative; equivalently its Bloch vector length exceeds one. Explicit eigenvalues are [1±√((0.52−0.48)²+4×0.51²)]/2≈1.0104 and −0.0104. This cannot represent probabilities for all projective measurements. Investigate whether the model violated complete positivity, the numerical solve failed, rates have incorrect signs or reconstruction ignored a physical constraint. Do not silently set the negative eigenvalue to zero and claim the original solver passed. If a small numerical negative was expected, report the roundoff tolerance and the effect of mesh/time-step refinement.

</details>

**Further investigation.** Which physical assumption is weakest? Design one independent calibration or numerical limiting-case test that would falsify this solution. Compare your analysis with [the relevant textbook chapter](chapters/04-density-matrices.md).

## Problem 4. Comparing Rydberg scaling across principal quantum number

**Problem.** For a model Rydberg series with effective n* changing from 60 to 90, estimate the ratio of adjacent-level spacings, orbital radii and a heuristic polarizability scale. State where this fails.

<details><summary>Show the worked reasoning and diagnostic significance</summary>

Adjacent spacing scales approximately as n*^{−3}, so ΔE90/ΔE60≈(60/90)^3≈0.2963. Radius scales as n*², giving r90/r60≈(90/60)^2=2.25. A polarizability heuristic n*^7 yields α90/α60≈(1.5)^7≈17.09. These ratios are *not* state-specific rubidium measurements: quantum defects are n,l,j dependent, and near avoided crossings or degenerate manifolds perturbation theory can fail. Lifetime and blackbody effects introduce additional temperature-dependent constraints. Validate actual transition frequencies and polarizability with ARC or precision spectroscopy before committing laser hardware.

</details>

**Further investigation.** Which physical assumption is weakest? Design one independent calibration or numerical limiting-case test that would falsify this solution. Compare your analysis with [the relevant textbook chapter](chapters/06-rydberg-scaling.md).

## Problem 5. Atomic selection and circular field conventions

**Problem.** A state j=1/2,m=+1/2 is to be coupled by a single E1 photon. Which target j′=3/2 magnetic states can be accessed by q=−1,0,+1? Explain why changing field axis changes apparent circular labels.

<details><summary>Show the worked reasoning and diagnostic significance</summary>

The magnetic rule is m′−m=q. Therefore from m=+1/2, q=−1 leads to m′=−1/2, q=0 to m′=+1/2, and q=+1 to m′=+3/2. All these target projections exist for j′=3/2; allowed reduced matrix and angular coefficients still determine strengths. The target m′=−3/2 would require q=−2 and is not a one-photon E1 pathway. In practice a transverse field decomposes into spherical components relative to the *chosen* quantisation axis. Rotating B rotates that basis, so labels such as RHCP/LHCP must also state propagation and exp(±iωt) convention.

</details>

**Further investigation.** Which physical assumption is weakest? Design one independent calibration or numerical limiting-case test that would falsify this solution. Compare your analysis with [the relevant textbook chapter](chapters/05-angular-momentum.md).

## Problem 6. The thermal two-photon Doppler residual

**Problem.** A 780 nm probe propagates along +z and a 480 nm coupling beam along −z. Write the two-photon Doppler term and estimate its magnitude for a single atom with vz=100 m/s. Explain why this is not the total EIT FWHM.

<details><summary>Show the worked reasoning and diagnostic significance</summary>

Take signed wavevectors kp=+2π/(780 nm) and kc=−2π/(480 nm). The angular detuning shift is −(kp+kc)vz. Dividing magnitude by 2π gives |vz|×|1/780 nm−1/480 nm|≈100×0.8013×10^6 Hz≈80.1 MHz. This refers to one velocity class, not the width of the thermal ensemble. The actual EIT spectral width results from integrating a velocity-dependent quantum susceptibility weighted by Maxwell–Boltzmann velocities, power/laser linewidths, decay and optical propagation. Counterpropagation reduces but cannot cancel residual Doppler when wavelengths are unequal.

</details>

**Further investigation.** Which physical assumption is weakest? Design one independent calibration or numerical limiting-case test that would falsify this solution. Compare your analysis with [the relevant textbook chapter](chapters/16-doppler-and-linewidth.md).

## Problem 7. RF wavelength and field versus antenna dimensions

**Problem.** A sensor operates at 1.925 GHz. Compute free-space wavelength and judge whether an aperture of 70×50 mm should be modelled as an infinite periodic surface.

<details><summary>Show the worked reasoning and diagnostic significance</summary>

Using c=299792458 m/s, λ=c/f≈0.1557 m or 155.7 mm. The proposed aperture dimensions are about 0.450λ and 0.321λ, i.e. not large compared with wavelength. An infinite periodic cell assumes transverse repetition and a specified Bloch phase, while a finite aperture has edge scattering and field variation. The atom volume may lie in a complicated near field rather than a far-field plane wave. A periodic S21 simulation can guide unit-cell optimisation but cannot automatically establish the local complex E field or calibrated finite-array Stokes response.

</details>

**Further investigation.** Which physical assumption is weakest? Design one independent calibration or numerical limiting-case test that would falsify this solution. Compare your analysis with [the relevant textbook chapter](chapters/18-hfss-metasurface.md).

## Problem 8. Why condition number is not a noise performance number

**Problem.** Compare response matrices A=I4 and B=0.001 I4, under equal independent output-voltage noise. Both have κ2=1. Which is the stronger estimator and why?

<details><summary>Show the worked reasoning and diagnostic significance</summary>

The matrices are equally conditioned under relative perturbations because all singular values have the same ratio one. But B's absolute sensitivity is 1000 times smaller. For equal Gaussian noise variance σ², the formal inverse-estimator covariance under A is σ²I, whereas under B it is 10^6σ²I. Thus rank/condition-number alone cannot compare physical metrological performance. Gain-aware Fisher information AᵀC⁻¹A retains that scale. When rows are normalized before computing κ, always report separate absolute signal/gain and expected noise before declaring one sensor better.

</details>

**Further investigation.** Which physical assumption is weakest? Design one independent calibration or numerical limiting-case test that would falsify this solution. Compare your analysis with [the relevant textbook chapter](chapters/19-information-matrix.md).

## Problem 9. Why a finite calibrated matrix can fail transfer

**Problem.** A periodic model gives response Aref and finite model gives Aactual=Aref+ΔA. Derive the first-order reconstruction bias when an inverse calibrated using Aref is applied to noiseless finite observations.

<details><summary>Show the worked reasoning and diagnostic significance</summary>

With y=Aactual S=(Aref+ΔA)S and the full-column-rank pseudoinverse Aref⁺, reconstruction is S_hat=Aref⁺y=S+Aref⁺ΔA S. Thus systematic bias is ΔS=Aref⁺ΔA S. Its norm can be bounded by ||Aref⁺|| ||ΔA|| ||S||, showing that a weak minimum singular value magnifies even a modest matrix discrepancy. Mesh agreement in source S parameters does not establish agreement in derived Stokes rows if phase-sensitive field terms are changing. A robust validation uses known holdout fields through an independently converged finite model and compares every coordinate and physicality residual.

</details>

**Further investigation.** Which physical assumption is weakest? Design one independent calibration or numerical limiting-case test that would falsify this solution. Compare your analysis with [the relevant textbook chapter](chapters/20-finite-calibration.md).

## Problem 10. Rydberg blockade-scale sensitivity to drive rate

**Problem.** Assume a pair interaction V=C6/R^6 and a blockade criterion |V(Rb)|=ℏΩ. Derive the blockade radius's dependence on Ω and C6. What happens when Ω doubles?

<details><summary>Show the worked reasoning and diagnostic significance</summary>

Rearranging gives Rb=(|C6|/(ℏΩ))^{1/6}. Its logarithmic sensitivities are dlnRb/dln|C6|=+1/6 and dlnRb/dlnΩ=−1/6. Doubling Ω reduces the nominal radius by 2^{−1/6}≈0.891; doubling |C6| increases radius by ≈1.122. The criterion defines only a characteristic scale: finite-linewidth, anisotropic pair interactions, Förster resonances and atom-position spread alter actual double-excitation error. At near resonant pair-state mixing, a single C6 law should be replaced by pair-state diagonalisation.

</details>

**Further investigation.** Which physical assumption is weakest? Design one independent calibration or numerical limiting-case test that would falsify this solution. Compare your analysis with [the relevant textbook chapter](chapters/25-rydberg-blockade.md).

## Problem 11. Choosing a realistic observation and noise model

**Problem.** A photodiode delivers an optical signal V that depends on field E and laser detuning Δ. How can one distinguish field sensitivity from drift-induced apparent sensitivity in a Fisher analysis?

<details><summary>Show the worked reasoning and diagnostic significance</summary>

Define V=f(E,Δ,...) and linearise around a calibrated operating point: δV=(∂f/∂E)δE+(∂f/∂Δ)δΔ+noise. If only one scalar observation is taken, field and detuning may be nonidentifiable when both slopes contribute. Introduce an independent laser-frequency reference, additional optical detuning points or RF on/off channels so the combined Jacobian has independent columns. Estimate covariance of the calibration and technical noise, not simply shot-noise variance. In a Fisher analysis, include Δ as a nuisance parameter and inspect marginalized variance for E. Verify predictions against held-out field steps at different lock conditions.

</details>

**Further investigation.** Which physical assumption is weakest? Design one independent calibration or numerical limiting-case test that would falsify this solution. Compare your analysis with [the relevant textbook chapter](chapters/35-inverse-modelling-and-bayesian-inference.md).

## Problem 12. Planning a new experiment instead of selecting a pretty plot

**Problem.** A new researcher wants to detect a 1 GHz field with Rydberg atoms. Describe the sequence of decisions, data sources and acceptance gates before buying optics or writing an 'AI optimiser'.

<details><summary>Show the worked reasoning and diagnostic significance</summary>

First define field amplitude/polarisation, bandwidth, spatial coverage and desired uncertainty. Screen candidate atomic species/transitions with state-specific ARC energies, optical access and E1 dipoles rather than asserting that any Rydberg n is suitable. Compare warm-vapour and cold-atom platforms against linewidth, cost, optical/readout constraints and rate of measurement. Develop a minimal density-matrix forward model and independently validate its limits. Specify optics/laser locks, calibrated RF source, antenna/cell field geometry, probe readout and safety protocols. Commission with optical coupling-off and RF-off controls, then field steps and repeatability, followed by independent holdout states. Record raw signals, source versions and uncertainty; do not use a perfect simulated inverse to certify the hardware.

</details>

**Further investigation.** Which physical assumption is weakest? Design one independent calibration or numerical limiting-case test that would falsify this solution. Compare your analysis with [the relevant textbook chapter](chapters/34-design-a-rydberg-system.md).


## General grading and research standard

A complete solution must define the state/coordinate basis, sign conventions, units, physical observable, model approximations, derivation and an independent verification strategy. An aesthetically convincing plot, rounded numerical answer or passing unit test alone does not establish scientific correctness. See the [source bibliography](REFERENCES.md) and [textbook editorial standard](EDITORIAL_STANDARD.md).
