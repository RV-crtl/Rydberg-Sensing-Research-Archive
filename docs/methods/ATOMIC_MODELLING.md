# Atomic-level modelling and transition-screening pathway

The RF front-end model and the atomic optical system solve different parts of the sensing problem. A precise follow-up receiver model should connect these layers rather than treat the HFSS electric-field magnitude as a direct photodetector voltage.

## Scope of the modelling tools

| Tool | Appropriate role | Preserved material |
|---|---|---|
| ARC / Python | Rb atomic levels, energy gaps, dipole matrix elements, transitions and candidate RF resonance screening | [Historical source script](../../research-code/arc/rydberg_tqe_advanced_poster_simulations.py) |
| RydIQule or equivalent optical Bloch approach | Optical absorption, EIT and microwave-dressed response model with specified decoherence, optical powers and detunings | Methodical future integration; no complete validated project imported |
| MATLAB / RF PCB Toolbox / Antenna Toolbox | PCB/RF geometry and array experiments in earlier work | Historical workflow referenced; the latest MATLAB source packages were not imported |
| Ansys HFSS | Electromagnetic copper/air/substrate field solution and local receiving basis | [Actual numerical outputs and scripts](../results/EVIDENCE_INDEX.md) |

## Recommended atomic–RF co-simulation interface

1. From ARC and experimental spectroscopy, choose the actual Rb Rydberg state and transition coupled by the relevant GHz RF field.
2. From HFSS, export local complex RF field vectors at the physical vapour-cell positions for all analyser states, frequencies and reference polarisations.
3. Map field amplitudes and orientations onto atomic transition coupling elements with the correct optical axis, selection rules, field nonuniformity and linewidth model.
4. Compute optical readout observables and construct a receiver-specific response matrix.
5. Calibrate independent reference RF polarisation states and quantify error, rank, conditioning, S3 observability and temporal stability.

No artificial solver noise or unspecified measurement-error model should be presented as real laboratory data. Where a mathematical noise model is useful, disclose it as a modelling assumption and preserve native outputs separately.
