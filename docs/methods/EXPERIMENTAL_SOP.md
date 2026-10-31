# Standard operating procedure: Rydberg RF experimental work

**Purpose:** document the method and required provenance of the atomic/optical and microwave experiment. This is a researcher handover checklist; it does not replace institution-approved laser, high-voltage, electrical or RF safety SOPs.

### 1. Pre-experiment and safety

Verify operator authorisation; instrument calibration; laser wavelength, interlocks and beam control; RF power limits; cell/optics positioning; photodetector ratings; VNA port-power limits; data storage, filename convention and clock synchronisation.

### 2. Optical receiver baseline

Record the 780 nm probe and 480 nm coupling wavelength, power, scan direction/rate, optical alignment, cell temperature, photodetector gain, scope or DAQ acquisition settings. Acquire a no-RF reference and record its raw data and calibration assumptions.

### 3. RF polarisation/reference acquisition

Record antenna identity, stand-off, orientation, source power/frequency, VNA calibration kit, reference plane, analyser angle, trial number, room and coil conditions. Capture co-polar/cross-polar references using identical instrumentation and document the exact pass/reject metric.

### 4. Rydberg response acquisition

Acquire and retain time/wavelength/detuning/power traces alongside RF configuration and optical settings. Explicitly tag whether the observation is spectroscopic EIT/AT, a reference RF measurement, a model prediction or a derived quantity.

### 5. Data reduction and review

Keep originals immutable. Generate cleaned data separately, with a script version and SHA-256 source hashes. Evaluate repeatability and uncertainty only from actual replicates and declared fitting models. Do not merge contrasts measured in different apparatus configurations.

### 6. Archive one experiment as

```text
experiments/YYYY-MM-DD_<experiment-id>/
  README.md       # aim, operator, apparatus, settings, summary
  raw/            # native instrument export (unchanged)
  metadata.json   # conditions, calibration, instrument versions
  derived/        # calculations and figures
  scripts/        # exact processing scripts
  verification.md # references, controls, checks
```

Use the [interim report](../../reports/2026-06-magnetically-biased-rydberg-receiver.pdf) for historical setup and analysis details, and follow current laboratory safety documentation before operating equipment.
