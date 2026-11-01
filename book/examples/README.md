# Executable atomic science examples — general Rydberg textbook

These Python examples execute **real atomic physics libraries** on a local machine or in the dedicated [scientific solver smoke workflow](../../.github/workflows/atomic-software-smoke.yml). The website's JavaScript toy curves are educational demonstrations and cannot replace these physics solvers.

## ARC transition atlas

Requirements: Python 3.11, `ARC-Alkali-Rydberg-Calculator`, and an internet connection only for initial package installation. Documentation: https://arc-alkali-rydberg-calculator.readthedocs.io/en/latest/.

    python -m pip install -r book/examples/requirements-science.txt
    python book/examples/arc_transition_atlas.py --list --n 60
    python book/examples/arc_transition_atlas.py --run --species Rb87 --n 60 --output arc_results.csv

The `--list` mode checks E1 magnetic-selection pathways without importing ARC. The `--run` mode queries the installed ARC library for actual calculated frequencies and signed dipole elements, writing *theoretical* CSV results. These are not measured fields; isotope, optical access and experimental viability require separate verification. Avoid publishing a generic formula result as state-specific atom spectroscopy without actually calling ARC.

## RydIQule steady-state three-level benchmark

Official API: https://rydiqule.readthedocs.io/en/stable/api/_autosummary/rydiqule.solvers.solve_steady_state.html.

    python book/examples/rydiqule_three_level.py --output rydiqule_result.json

This adds two couplings and positive transit broadening to a three-level `rq.Sensor`, scans probe detuning, solves the open-system steady state and records solver output shape and package version. RydIQule internally may store N²−1 independent *real* density-matrix variables rather than an N×N complex matrix. This code does **not** assert a physical vapour-cell transmission measurement. To compare with optical experiments, use `rq.Cell`, appropriate levels/decays, Doppler averaging, susceptibility, cell length, laser powers and calibrated detection.

## Real solver validation and scientific artifacts

The GitHub Actions [atomic science smoke test](../../.github/workflows/atomic-software-smoke.yml) installs both libraries into a new environment and attempts to run the actual models. It verifies nonempty, finite ARC outputs and a nonempty RydIQule result with appropriate shape. The generated CSV/JSON are uploaded as **theoretical calculations only**, never silently labelled native HFSS results or laboratory data. The workflow may fail if an upstream API changes; that failure is a signal to update the versioned methods, not to bypass validation.

The repository's regular `tests/test_rydberg_software_examples.py` does selection-rule and Sensor-graph regression tests offline, even when these optional science packages are not installed. Scientific correctness also requires independent reference-energy and experimental validation beyond a successful run.

## Suggested research modifications

- **Species exploration:** change Rb87 to Cs and verify the actual isotope data, transition access and levels.
- **Atomic-field polarimetry:** represent the appropriate m states and spherical q couplings; do not infer full vector fields from an unresolved 3-level ladder.
- **Laser spectroscopy:** add physically motivated decay, power, temperature and scan limits, using a Cell to calculate susceptibility rather than calling a generic model 'transmission'.
- **Reproducibility:** store Python and solver version, exact inputs, expected units, reference source and all original output files.

[Textbook](../README.md) · [ARC chapter](../chapters/13-quantum-defect-and-arc.md) · [RydIQule chapter](../chapters/14-rydiqule-lab.md).
