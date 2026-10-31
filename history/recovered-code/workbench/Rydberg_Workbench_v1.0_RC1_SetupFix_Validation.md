# Rydberg Workbench 1.0.0-rc1 setup-fix handoff

This refreshed archive fixes the Windows setup failure reported in
`setup(2).log`.

## Diagnosis

The original `SETUP_WINDOWS.cmd` installed `python/requirements-tested.txt`
as one mandatory set. That set included the optional GNU Radio/ZeroMQ bridge,
so a Python index that could not resolve `pyzmq==27.2.0` aborted the entire
installation even though the native simulator does not use PyZMQ.

## Fix

- Core packages are now in `python/requirements-core.txt`.
- The bridge is isolated in `python/requirements-bridge.txt`.
- Windows, PowerShell, and shell installers complete the core install first.
- The bridge is attempted separately, with a PyZMQ 27.1.0 compatibility
  fallback; if both are unavailable, the simulator still starts and the
  warning is recorded.
- The Qt inspector now ignores delayed refresh callbacks during shutdown.

## Validation

- Source commit: `26cebd3` on `desktop/workspace-v1-rc1`
- Full pytest suite: **118 passed**
- Targeted Qt desktop tests: **12 passed**
- Installed repaired wheel smoke test: passed in isolated mode
- Wheel SHA-256: `a2ab439752282634f6556fe2c55d60914378144299bef684146939f92526e55f`
- Archive SHA-256: `fec1035f2f343d3610f1f2bf891e7e7234e015b27a3c8ef9e9921f19e3df9932`
- Archive size: 1,353,125 bytes; 120 files

The archive contains the native source, examples, tests, release evidence, and
the rebuilt wheel. No GitHub push has been made. Physical B210/Soapy reception
and the user's local Python index remain external validation gates.