# Atomic angular momentum and transition selection rules

**General atomic and quantum physics textbook.** The treatment is not a project-specific apparatus description. Physics constants and state labels must be verified for each chosen species.

## Learning objectives

Derive the central equations, quantify assumptions, compute a simple limiting case, plan an independent experiment and diagnose numerical or laboratory errors.

## 1. Quantum numbers and coupling schemes

Electron orbital angular momentum L combines with spin S to form J, while nuclear spin I couples with J to form F. Magnetic projections are m_J and m_F in their respective bases. The allowed j values range from |l−s| to l+s; for alkalis s=1/2. A state label n,l,j is not sufficient to describe resolved hyperfine spectroscopy, and strong magnetic fields can invalidate the F-coupled basis by mixing manifolds. Always state the quantisation axis and the regime of field coupling.

## 2. Electric dipole selection rules

For electric-dipole E1 transitions, parity changes and Δl=±1 in a nonrelativistic one-electron description. Spherical components q=−1,0,+1 change magnetic projection by Δm=q when defined consistently. The triangle rule restricts angular momentum, and a J=0↔J′=0 E1 transition is forbidden. Hyperfine selection rules usually allow ΔF=0,±1 except F=0↔0, subject to the relevant approximations. Violating a selection rule can make a large radial integral irrelevant.

## 3. Clebsch–Gordan and Wigner coefficients

A dipole matrix element separates radial and angular parts using Wigner–Eckart theorem. The reduced matrix element captures much of the electronic structure, while 3j/6j coefficients describe projections and recoupling. Different phase conventions can flip the sign of an individual matrix element without altering absolute transition strengths, but relative phases are crucial in interference. Compare coefficient conventions before mixing ARC, spectroscopy tables and independent quantum simulators.

## 4. Zeeman and Breit–Rabi regimes

For weak field in a definite hyperfine manifold a linear approximation ΔE≈g_F μB m_F B may apply. At larger field the electron and nuclear angular momenta decouple gradually and a Breit–Rabi-like description is required for the relevant levels. Rydberg states can also have Stark mixing and core effects. A sharp magnetic spectral feature is not proof of a particular m-state until optical and RF reference conditions are controlled.

## 5. Angular components of an RF wave

Write a complex electric field in the coordinate system tied to quantisation axis. π drives q=0 components and σ± drive the corresponding circular spherical components under a declared time convention. Reversing propagation direction or changing e^{-iωt} to e^{+iωt} can invert handedness labels. A linear RF antenna generally excites a superposition of σ+ and σ− if its field is transverse to the magnetic axis.

## 6. Worked angular selection example

From j=1/2,m=+1/2 to j′=3/2,m′=+3/2 requires q=+1; to m′=−3/2 would require q=−2 and is forbidden for a single E1 photon. A radial matrix element could be large but the forbidden magnetic transition must be rejected. Enumerate allowed values before computing frequencies or assigning an observed optical peak.

## End-of-chapter review questions and worked answers

### Question 1. What changes if the quantisation axis rotates?

<details><summary>Show explained solution</summary>

The spherical decomposition of a fixed laboratory electric field and thus observed transition couplings.

</details>

### Question 2. Why is a dipole radial integral not a complete strength?

<details><summary>Show explained solution</summary>

Angular selection and Wigner coefficients may zero or weight the physical transition.

</details>

### Question 3. Which q couples Δm=−1?

<details><summary>Show explained solution</summary>

The spherical component conventionally labelled σ−, assuming the stated quantisation and phase conventions.

</details>

### Question 4. When is F a poor approximate quantum number?

<details><summary>Show explained solution</summary>

When magnetic-field mixing makes hyperfine coupling no longer dominant.

</details>

### Question 5. Does a right-circular optical label imply the same RF q in every frame?

<details><summary>Show explained solution</summary>

No; propagation and time-phase conventions must be aligned.

</details>

### Question 6. Why must a state be fully labelled?

<details><summary>Show explained solution</summary>

n,l,j alone may hide important m or hyperfine degeneracies and selection rules.

</details>

## Graduate practical problem

Develop a reproducible calculation for the principal equation in this chapter, record coordinate frame and units, compare against a separate source or an analytically solvable limit, and describe a controlled measurement that could falsify the model. Explicitly distinguish a derived teaching example from new experimental evidence.

## Scholarly sources

See [the textbook bibliography](../REFERENCES.md), Gallagher (*Rydberg Atoms*), Foot (*Atomic Physics*), Scully and Zubairy (*Quantum Optics*), and official atomic spectroscopy data when applying formulas to an actual species.
