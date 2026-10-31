# Rydberg modelling, scientific automation and Rydberg Workbench

## ARC / Rydiqule / MATLAB scientific computation

The initial project required more than a generic RF link model: reliable selection of accessible Rb-87 Rydberg transitions, optical 780+480 nm coupling, microwave dipole matrix elements and Zeeman shifts. Earlier ARC/Rydiqule work considered the Rb ladder, the 86P3/2 upper state, fine/hyperfine/Zeeman manifolds, RF transitions in the low-GHz band, laser tuning constraints and steady-state optical readout. For any simulation preserve exact versions, quantum-number basis, field quantisation axis, detunings, Rabi frequencies, decay/dephasing model, units and solver convergence.

Optical density-matrix simulations are **different physics and software** from HFSS; a simulated 1.8 GHz resonance or optical spectrum must not be relabelled a measured spectral line. Earlier Zeeman screening near 1.8 GHz and a suspected 2.4 GHz feature remained insufficiently verified to establish a positive magnetic-polarimetry result.

A relevant original source file is [ARC/Rydberg plotting and simulation script](../../research-code/arc/rydberg_tqe_advanced_poster_simulations.py). The [atomic modelling SOP](../methods/ATOMIC_MODELLING.md) sets up its research context.

## MATLAB and CST

MATLAB R2025a, RF PCB Toolbox and Antenna Toolbox were used in several polariser candidates for grid geometry, finite-aperture analysis, CP/chiral patterns, SVG-style artwork and optimisation. Design variants were not interchangeable: older 500 mm RO4350B analytical grids differed from later 200 mm FR-4 or RO4350B cells. Scripts with names such as “optimise” or “validated” may be surrogate calculations; use the underlying code/model class to determine what was actually solved.

CST educational studies were constrained by a limited mesh budget (historical ~100,000-cell educational cap). The workflow therefore emphasised periodic unit cells, smaller arrays and angle/frequency response before exporting expensive finite models to HFSS. Claims about a full 200 mm panel require a corresponding solved full-wave simulation, not a tiled screenshot alone.

## Rydberg Workbench desktop research environment

A separate open-source-oriented scientific workbench was investigated to provide a graphically configurable atomic/RF research workflow with flexible instrumentation and streaming data. Requested features included:

- graph-based creation and connection of atomic receivers, RF chains, oscilloscopes, SDRs, RF analysers, spectral displays and monitors;
- inserting scopes into **existing signal lines**, intuitive drag/connect/edit operations, and per-instrument double-click plots rather than a permanently cluttered multi-plot footer;
- live GNU Radio/SDR compatibility, possible Simulink-like signal flow and physical-model component interfaces;
- parameterised mathematical/atomic modules, data recording, diagnostics, reusable models and performance improvements;
- versioned desktop distribution, automated tests and installation validation.

Historical **Rydberg Workbench v1.0 RC1/RC2** archives exist in the source discovery library but are **not present in this GitHub archive** as an executable application. Earlier RC1 verification notes reported 118 passing tests and separated core dependencies from optional GNU Radio/ZeroMQ bridging. This is a *software validation record*, not an assertion that the programme is a commercial GNU Radio/Simulink replacement or that all SDR hardware was validated.

Import candidates and source history are listed in [historical catalogue](../catalog/README.md). A successor should: retrieve the final editable RC2 archive; inspect entrypoint/licences; run installer/self-test in a clean environment; record required Python/GNU Radio dependencies; add CI smoke tests; and then create a dedicated software subproject or git submodule rather than dumping unreviewed binaries into this scientific evidence directory.

## HFSS runner and data engineering requirements

Windows automation evolved to: one launch action; auto-continue through independent cases; stop only on genuine failure or necessary inspection; stream logs and progress; preserve original .aedt/.aedtresults when available; export complex X/Y electric fields and S-parameters, matrix/Jones/Stokes derivations, mesh/frequency/angle sweeps, figures and machine-readable verdict; collect a single return ZIP. Solver version/Ansys Student licence constraints and PyAEDT compatibility should be recorded per run, not hidden.

See [HFSS SOP](../methods/HFSS_SOP.md), [campaign lineage](../simulations/HFSS_CAMPAIGN_LINEAGE.md) and [V44 original analysis scripts](../../evidence/hfss/v44-reproducibility/analysis/).
