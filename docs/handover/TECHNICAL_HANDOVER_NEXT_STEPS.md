# Engineering handover — reproducible next steps

## 1. Establish exact source baseline

The current article and V44 numeric tree form the **simulation-source baseline**, with six analyser states and a 6×4 matrix. Pin a reproducible commit, regenerate figures from existing data, inspect all normalisation conventions, and run the provided integrity tests. Never change reported scientific values from an undocumented summary.

## 2. Reproduce numerics on a clean workstation

Install matching Ansys HFSS/AEDT + PyAEDT versions, and record actual solver licence / project capabilities. Reopen the native project when available; otherwise use the preserved compact original return as read-only evidence. Independently check matrix rank/singular spectrum, circular leverage, gain/dwell objective, accepted frequency samples and finite-array calibration transfer. Record complex-field mesh convergence rather than trusting a generic solver-pass flag.

## 3. Plan physical switch implementation

For each of the four logical bridge locations, specify real PIN diode (or RF MEMS alternative) parasitics, DC drive current, package capacitance, orientation, bias trace, via return and measurement routing. Simulate the complete network under every analyser state and measured incidence angle. Confirm copper layers, board edge clearance and optical beam passage. Only after that generate manufacturer-approved artwork. A switch rendered on a plot is not a manufactured biased diode.

## 4. Atomic receiver integration

Use the 780/480 nm ladder EIT baseline, repeatable laser stabilisation and calibrated RF input. Produce a finite-board local-field calibration for the actual rubidium-cell position, use known Stokes reference states (linear, diagonal, LHCP/RHCP, elliptical) and record raw probe transmission. Fit a real instrument matrix and compare its conditioning with HFSS prediction using full errors, not only average similarity. Maintain independent holdout states, repeatability and reference-plane calibration.

## 5. Decisions and release

Keep the original current manuscript version, current reports, raw datasets, MATLAB/source projects, CAD and supplier evidence untouched; new work goes into versioned branches. Before public release, verify institute approval, unpublished-paper conditions, external copyright, raw laboratory confidentiality and client/defence restrictions. Publish the research narrative and cleared figures first; private annexes can retain restricted evidence.

## Practical success gates

- **Documentation:** claims and figures link to source files; original values, units, dates, revision and authorship checked.
- **HFSS:** every switch state and both linear basis excitations solved; independent complex-field mesh verified; finite and periodic cases separately quantified.
- **Stokes:** rank 4; condition and minimum singular response acceptable at useful absolute gain; S3 distinguishable; accurate held-out reconstructions within predeclared tolerances.
- **Hardware:** manufacturing package passed DFM, switch-state truth table, continuity and RF VNA/optical alignment tests.
- **Atomic:** real raw optical datasets show calibrated response to independent incident polarisation states and reproducible full-Stokes inversion.

A software demonstration, numeric full rank, or photograph is not a replacement for any of these source-specific checks.
