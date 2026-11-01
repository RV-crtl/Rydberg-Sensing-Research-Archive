# Annotated source bibliography

The chapters are **newly authored instructional text**, using the books and official documentation below as technical reference points. Titles and metadata are for scholarly citation, not copied figures or chapters. Publisher access/licensing may apply.

## Physics and mathematical foundations

1. Thomas F. Gallagher, *Rydberg Atoms*, Cambridge Monographs on Atomic, Molecular and Chemical Physics, Cambridge University Press, 1994; reprint 2009. DOI: https://doi.org/10.1017/CBO9780511524530. Core Rydberg scaling, quantum defects, field interactions and lifetime physics.
2. Christopher J. Foot, *Atomic Physics*, Oxford University Press, 2005. Atomic structure, laser spectroscopy, two-level dynamics and magnetic fields.
3. Marlan O. Scully and M. Suhail Zubairy, *Quantum Optics*, Cambridge University Press, 1997. Density matrices, coherent response, open-system dynamics and EIT.
4. Daniel A. Steck, *Quantum and Atom Optics*, lecture notes, https://steck.us/teaching/ (check current edition). Formalism, optical absorption, Doppler averaging and master equations.
5. Daniel A. Steck, *Rubidium 87 D Line Data*, https://steck.us/alkalidata/rubidium87numbers.pdf. Reference lines, hyperfine and Zeeman constants; validate state-specific frequency definitions.
6. Max Born and Emil Wolf, *Principles of Optics*, Cambridge University Press, 7th ed. Polarisation, coherence and field propagation.
7. Edward Collett, *Field Guide to Polarization*, SPIE Press, 2005. Jones/Stokes/Mueller formalism, with explicit conventions.
8. Constantine A. Balanis, *Antenna Theory*, Wiley, 4th ed. Radiation, near fields, aperture and antenna design.
9. David M. Pozar, *Microwave Engineering*, Wiley, 4th ed. Impedances, S parameters, loss, distributed resonance and calibration.
10. Bahaa E. A. Saleh and Malvin C. Teich, *Fundamentals of Photonics*, Wiley, 3rd ed. Beam propagation and photodetection.
11. Gene H. Golub and Charles F. Van Loan, *Matrix Computations*, Johns Hopkins University Press, 4th ed. SVD, numerical conditioning, pseudoinverse.
12. Steven M. Kay, *Fundamentals of Statistical Signal Processing: Estimation Theory*, Prentice Hall. Noise covariance and Fisher information.

## Software documentation and cited methods

13. N. Šibalić et al., *ARC: An open-source library for calculating properties of alkali Rydberg atoms*, *Computer Physics Communications* **220**, 319–331 (2017). https://doi.org/10.1016/j.cpc.2017.06.015 . Official API https://arc-alkali-rydberg-calculator.readthedocs.io/en/latest/ . Confirm current installed ARC version and units.
14. B. N. Miller, D. H. Meyer, T. Virtanen, C. M. O'Brien and K. C. Cox, *RydIQule: A graph-based paradigm for modeling Rydberg and atomic sensors*, *Computer Physics Communications* **294**, 108952 (2024). DOI https://doi.org/10.1016/j.cpc.2023.108952 . Official API https://rydiqule.readthedocs.io/en/stable/ .
15. RydIQule documentation, *Solve the System* and *Observable Validation* https://rydiqule.readthedocs.io/en/stable/overview.html . Its minimal Sensor and physical Cell models are different levels of modelling.
16. Ansys Electronics Desktop/HFSS documentation, https://ansyshelp.ansys.com/ . Verify frequency/phase, solver excitation and finite/periodic mesh settings against the installed version; results belong to native projects, not this handbook.

## Research and novelty comparisons

17. P. K. Elgee et al., *Complete three-dimensional vector polarimetry with a Rydberg-atom RF electrometer*, *Physical Review Applied* **22**, 064012 (2024). https://doi.org/10.1103/PhysRevApplied.22.064012 .
18. M. Chilcott et al., *Quantum-enabled complete RF-polarimetry with an optically-wired atomic sensor*, arXiv:2605.14529 (2026), https://arxiv.org/abs/2605.14529 . Preprint status should be reviewed on the date of reuse.
19. N. Schlossberger et al., *Resolving magnetic-sublevel structure in Rydberg Autler–Townes spectra with arbitrary RF polarization*, *Physical Review A* **114**, 033701 (2026), https://doi.org/10.1103/w5k9-1mlh .
20. C.-R. Liu et al., *Fisher-based sensitivity framework for Rydberg-atom microwave electrometry*, *Physical Review Applied* **25**, 034052 (2026), https://doi.org/10.1103/qsmd-yh44 .
21. The project’s own source-backed [V44 HFSS evidence](../evidence/hfss/v44-reproducibility/), [editable paper](../papers/manuscript-source/main.tex), [source diagnostic ledger](../docs/results/HFSS_V411_V422_ORIGINAL_DIAGNOSTIC_EVIDENCE.md) and [historical research files](../history/README.md). Cite native field datasets and versioned paper sources rather than treating the present book as independent primary experimental evidence.

## Responsible use and currency

The *weekly* automated literature monitor retrieves bibliographic metadata and produces **unreviewed candidate lists**. Metadata alone does not establish a paper's correctness, novelty or experimental validity. A human should inspect the complete paper before revising this bibliography. Preserve the source DOI, published/preprint status, date and method-specific limitations. Textbooks may contain different signs/units; our explicit convention always takes precedence for a calculation in this repository.
