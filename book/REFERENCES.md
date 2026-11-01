# Rydberg Systems Engineering — references and source conventions

References are grouped by a general reader's learning path. The book contains **original explanatory text**, not copied textbook chapters. Publisher sites and software APIs evolve; verify the edition and source before treating a quoted constant or claim as authoritative. No licence to redistribute book chapters or figures is implied.

## Core monographs and theory

- **[F1]** C. J. Foot, *Atomic Physics*, Oxford University Press (2005). Angular momentum, laser spectroscopy, magnetic fields and Rabi dynamics.
- **[F2]** D. A. Steck, *Quantum and Atom Optics*, lecture notes, https://steck.us/teaching/. Atomic optical Bloch formalism and quantum-state basics.
- **[Q1]** M. O. Scully and M. S. Zubairy, *Quantum Optics*, Cambridge University Press (1997). Optical coherence, master equations and EIT.
- **[R1]** T. F. Gallagher, *Rydberg Atoms*, Cambridge University Press (1994; later reprints), https://doi.org/10.1017/CBO9780511524530. Quantum defects, scaling, Rydberg interactions and lifetimes.
- **[M1]** G. H. Golub and C. F. Van Loan, *Matrix Computations*, 4th ed., Johns Hopkins (2013). SVD, least squares, conditioning and numerical algebra.
- **[M2]** S. M. Kay, *Fundamentals of Statistical Signal Processing: Estimation Theory*, Prentice Hall (1993). Likelihood, Fisher information and experimental estimation.
- **[E1]** D. M. Pozar, *Microwave Engineering*, 4th ed., Wiley (2011). Microwave networks, S parameters, materials and resonant devices.
- **[E2]** C. A. Balanis, *Antenna Theory: Analysis and Design*, 4th ed., Wiley (2016). Antenna gain, near/far field and apertures.
- **[O1]** B. E. A. Saleh and M. C. Teich, *Fundamentals of Photonics*, 3rd ed., Wiley (2019). Optical beams, coherence, detection.
- **[O2]** M. Born and E. Wolf, *Principles of Optics*, 7th ed., Cambridge University Press (1999). Polarisation and electromagnetic propagation.
- **[P1]** E. Collett, *Field Guide to Polarization*, SPIE Press (2005). Jones/Stokes/Mueller with specific sign conventions.

## Primary atomic data, reproducible APIs and numerical tools

- **[S1]** D. A. Steck, *Rubidium 87 D Line Data*, https://steck.us/alkalidata/rubidium87numbers.pdf. Vacuum/air reference wavelengths, isotope hyperfine constants; use published revisions rather than a single generic '780 nm'.
- **[S2]** NIST Atomic Spectra Database, https://physics.nist.gov/asd/. Independently check lines, series and energy reference levels.
- **[ARC]** N. Šibalić et al., “ARC: An open-source library for calculating properties of alkali Rydberg atoms,” *Computer Physics Communications* **220**, 319–331 (2017), DOI https://doi.org/10.1016/j.cpc.2017.06.015; current documentation https://arc-alkali-rydberg-calculator.readthedocs.io/en/latest/. Source for state-dependent energies, E1 dipoles, Stark and pair interaction functions.
- **[RQ]** B. N. Miller et al., “RydIQule: A graph-based paradigm for modeling Rydberg and atomic sensors,” *Computer Physics Communications* **294**, 108952 (2024), https://doi.org/10.1016/j.cpc.2023.108952; official documentation https://rydiqule.readthedocs.io/en/stable/. Distinguish Sensor and physically parameterised Cell, rate and detuning conventions.
- **[EM]** Ansys HFSS/Electronics Desktop technical documentation, https://ansyshelp.ansys.com/. Boundary conditions, periodic/finite electromagnetic solvers and mesh convergence; installation version matters.
- **[SI]** NIST CODATA constants and SI definitions, https://physics.nist.gov/cuu/Constants/. Exact (c,h,e) under SI; measured (a_0,mu_B) have revision-dependent uncertainties.

## Experiment platforms and current scientific context

- **[RV]** NIST authors, “Rydberg states of alkali atoms as atomic vapor SI-traceable field probes and for communications,” *Nature Reviews Physics* (2024/2025), https://www.nist.gov/publications/rydberg-states-alkali-atoms-atomic-vapor-si-traceable-field-probes-and-communications-1. Validate final publisher edition/volume before formal use.
- **[ELECT]** P. K. Elgee et al., “Complete three-dimensional vector polarimetry with a Rydberg-atom RF electrometer,” *Physical Review Applied* **22**, 064012 (2024), https://doi.org/10.1103/PhysRevApplied.22.064012. Published prior experimental vector polarimetry.
- **[CHIL]** M. Chilcott et al., 2026 Rydberg RF polarimetry preprint, https://arxiv.org/abs/2605.14529. Preprint; publication and revised versions must be checked when citing.
- **[MOL]** C. H. Greene, A. S. Dickinson and H. R. Sadeghpour, “Creation of polar and nonpolar ultra-long-range Rydberg molecules,” *Physical Review Letters* **85**, 2458 (2000), https://doi.org/10.1103/PhysRevLett.85.2458.
- **[BLOCK]** M. Saffman, T. G. Walker and K. Mølmer, “Quantum information with Rydberg atoms,” *Reviews of Modern Physics* **82**, 2313 (2010), https://doi.org/10.1103/RevModPhys.82.2313.
- **[QSIM]** H. Bernien et al., “Probing many-body dynamics on a 51-atom quantum simulator,” *Nature* **551**, 579–584 (2017), https://doi.org/10.1038/nature24622.
- **[CAV]** S. Haroche and J.-M. Raimond, *Exploring the Quantum: Atoms, Cavities, and Photons*, Oxford University Press (2006). Cavity quantum electrodynamics and photon counting.

## Cross-disciplinary method and publishing

Use authoritative metrology and institute guidance for laser hazards, electrical high voltage, vacuum/pressure and RF safety. Modern defence-funded work additionally needs appropriate data/export/security review; a public strategic priority is not an authorization to share controlled information.

**Citation maintenance:** each revised chapter should connect particular equations, tables and constants to exact source entries rather than relying only on a final chapter bibliography. Every current scholarly claim needs its publication date, paper status and independent evidence review. The [Australian source monitor](../automation/README.md) is project-specific opportunity intelligence and is not a general physics primary source.

[Back to book](README.md) · [Editorial quality standard](EDITORIAL_STANDARD.md).
