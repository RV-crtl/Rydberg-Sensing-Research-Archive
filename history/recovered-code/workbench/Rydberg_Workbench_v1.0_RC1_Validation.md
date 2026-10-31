# Rydberg Workbench 1.0.0-rc1 validation handoff

This is the local release-candidate handoff for the native desktop Rydberg
digital-twin workspace. No GitHub push has been made.

## Evidence

- Source commit: `bc6f348` on `desktop/workspace-v1-rc1`
- Full pytest suite: **118 passed**
- Offline workspace examples: **16 passed**
- Installed-wheel smoke test: passed outside the source tree
- Wheel SHA-256: `549e0660d00261e383e68590bff83abcd61e6f4b0e93a639861a46838d358623`
- Source archive SHA-256: `5810d6312c8ab632133be78bd400e938513501d41036008fa132d18194ceb1a7`
- Archive size: 1,351,301 bytes; 118 files

Machine-readable evidence is included in the archive under
`docs/evidence/rc1/`.

## First run

On Windows, run `SETUP_WINDOWS.cmd` once and then `RUN_WINDOWS.cmd`. On
Linux/macOS, install `python/requirements-tested.txt` into Python 3.12 and
run `python -m rydberg_workbench.desktop_app` with `PYTHONPATH=python`.

Load `examples/workspace/branches.rwb` to try branchable sampled streams, or
`examples/workspace/am_nonlinear.rwb` for the optical/Rydberg path. Double-click
an instrument to open its independent scope, IQ, RF, optical, or EIT/AT window.

## Release boundary

This is a release candidate, not a claim of perfect laboratory equivalence.
Physical B210/Soapy reception, USB drivers, platform launch, and held-out lab
trace calibration remain acceptance gates. The selected atomic model and
settled-periodic analog/atomic execution are documented in
`docs/RELEASE_RC1.md` and `docs/HARDWARE_RC1.md`.