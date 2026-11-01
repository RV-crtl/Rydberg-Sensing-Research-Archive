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
