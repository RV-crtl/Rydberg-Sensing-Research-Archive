# Optical / atomic receiver — laboratory and engineering record

This page records the Rydberg sensing platform and measurement workflow without confusing **optical atomic measurements** with **conventional RF-chain measurements**. Begin with the original [June experimental report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf) and [existing experiment SOP](../methods/EXPERIMENTAL_SOP.md). Exact settings and calibration require the original run sheets.

## Signal and instrument chain

**Optical:** 780 nm probe interrogates the rubidium D-line; 480 nm coupling drives ladder EIT towards a Rydberg state. Counter-propagating beams intersect in an Rb-87 vapour cell. Transmitted probe intensity is read with a photodetector, gain electronics and oscilloscope/measurement acquisition. The RF field couples nearby Rydberg states and can modify optical transmission; optical evidence of an RF effect must be diagnosed against laser lock, temperature, power, and detector artifacts.

**RF:** Windfreak 12.5 MHz–6.4 GHz microwave source / laboratory RF generator → antennas and calibrated cables → polariser or metasurface / known RF state → vapour-cell region and/or conventional measurement receiver. Recorded laboratory hardware in previous reports includes LPDAs, RX10DF/RXM10DF RF front ends, LNAs/TIA, oscilloscope, photodetectors and an Ettus B210 SDR. These are identified equipment configurations, **not confirmed individual purchase transactions**.

**Magnetic field:** an early single-coil geometry placed its normal perpendicular to the laser propagation direction. Subsequent planning included Helmholtz-coil homogeneity improvements, magnetic calibration, Zeeman splitting and a possible software or hardware lock-in technique. The eventual thesis emphasis shifted toward planar RF analyser states and Stokes reconstruction. Do not write that successful full-vector Zeeman calibration was completed without the raw fitted spectra.

## Constraints and examined operating windows

| Parameter / constraint | Working record | Meaning |
|---|---|---|
| Probe laser | 780 nm (DL PRO platform) | Rb-87 lower ladder excitation |
| Coupling laser | 480 nm (DL PRO platform) | Rydberg ladder excitation; actual exact state requires measured wavelengths |
| Coupling coarse-tuning explorations | ~479.579, 479.456, 479.411 nm limits from different 480.000 nm reference windows | Exploratory scan/access envelopes, not verified Rydberg transition assignments |
| Low-frequency RF emphasis | ~1.8–2.0 GHz | Receiver and polarimetry design target |
| Photoreceiver bandwidth | research configurations with upper measurement/readout limits around 6 GHz or less | Distinguish photoreceiver bandwidth from RF source and atomic sensitivity |
| Rubidium-cell visible aperture | approximately 70 × 50 mm | Motivated finite metal-board aperture and sample-volume checks |
| Laser beam clearance | ≥5 mm margin in several proposed PCB designs | Practical routing/optics constraint, not evidence of manufactured board |

The exploratory transition target included the Rb-87 86P3/2 ladder. ARC and Rydiqule calculations should retain the exact n,l,j,m basis, detunings, laser polarisation, decay rates, couplings, RF dipole elements and solver versions. Inferences about AT splitting must be accompanied by raw optical traces and frequency calibration.

## Recommended raw-data manifest for each experiment

For a documented run, capture one machine-readable YAML/JSON record with experiment ID, date/time/timezone, operator, apparatus and optical topology, vapour-cell identification, temperature, laser settings (measured wavelengths, detunings, powers, waist/polarisation), RF generator and power at the antenna, source antenna position/orientation, polariser angle, magnetic coil current/geometry, oscilloscope acquisition/timebase, raw signal file, reference/background, calibration files, uncertainty assumptions and SHA-256 hashes. Preserve raw traces separately from later fitted values.

**Good sequence:** dark/reference → laser-only optical EIT baseline → no-RF control → RF source sweeps/known state → repeat after reference verification → calibrated comparison against instrument noise and ambient RF. Do not claim atomic polarimetric sensitivity from RF front-end voltage alone.

## Progress and evidence boundary

- The June report supports an assembled and investigated optical/RF receiver, RF polariser comparisons and magnetic-field calibration discussion.
- Laboratory linear-polarisation discrimination demonstrates part of the polarisation-conditioning chain, **not an S3-sensitive atomic measurement**.
- No source currently imported in the repository proves laboratory reconstruction over the complete Poincaré sphere, absolute atomic-field calibration for every analyzer state or hardware integration of the final simulated switchable PCB.
- Missing native oscilloscope traces / wavelength logs / coil calibration files belong in the [intake manifest](../handover/RESEARCH_COMPLETENESS_AND_IMPORTS.md).

## Key references in this repository

[Interim experimental report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf) · [Equipment/BOM](../engineering/HARDWARE_AND_BOM.md) · [Polarisation measurements](POLARISATION_MEASUREMENTS.md) · [Atomic-model SOP](../methods/ATOMIC_MODELLING.md)
