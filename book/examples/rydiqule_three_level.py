#!/usr/bin/env python3
"""RydIQule three-state scientific example with explicit model limitations.

Use: pip install rydiqule numpy
     python book/examples/rydiqule_three_level.py

This bare Sensor demonstration is not a physical rubidium Cell model. It does
not convert optical coherences directly to calibrated transmission or voltage.
"""
from pathlib import Path
import argparse
import json
import sys

def construct(sensor_cls,probe_detunings,probe_rabi,coupling_rabi,transit):
 if probe_rabi<=0 or coupling_rabi<0 or transit<=0:
  raise ValueError("Rabi strengths and transit broadening must be physical")
 s=sensor_cls(3)
 s.add_coupling((0,1),detuning=probe_detunings,rabi_frequency=probe_rabi)
 s.add_coupling((1,2),detuning=0.0,rabi_frequency=coupling_rabi)
 s.add_transit_broadening(transit)
 return s

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--probe-rabi",type=float,default=0.3)
 p.add_argument("--coupling-rabi",type=float,default=4.0)
 p.add_argument("--transit",type=float,default=0.1)
 p.add_argument("--output",type=Path,default=Path("rydiqule_three_level_solver_report.json"))
 x=p.parse_args()
 try:
  import numpy as np
  import rydiqule as rq
 except ImportError as exc:
  raise SystemExit("Install the documented RydIQule and NumPy versions before running a real solver") from exc
 det=np.linspace(-12,12,121)
 s=construct(rq.Sensor,det,x.probe_rabi,x.coupling_rabi,x.transit)
 sol=rq.solve_steady_state(s)
 if not hasattr(sol,"rho"):
  raise RuntimeError("Unexpected RydIQule solution API; check installed version")
 rho=np.asarray(sol.rho)
 if not np.isfinite(rho).all():raise RuntimeError("Non-finite density-matrix solution")
 report={
  "schema":1,
  "mode":"physical equations solved by installed RydIQule; toy 3-state Sensor only",
  "source":"https://rydiqule.readthedocs.io/en/stable/overview.html",
  "rydiqule_version":getattr(rq,"__version__","not exposed"),
  "parameters":{"probe_rabi":x.probe_rabi,"coupling_rabi":x.coupling_rabi,
                "transit_broadening":x.transit,"scan_min":float(det.min()),"scan_max":float(det.max())},
  "units":"RydIQule's declared coupling/laser detuning convention (review installed documentation)",
  "solution_shape":list(rho.shape),
  "verified_properties":["finite solver output"],
  "limitations":["no atomic species chosen","no hyperfine/mJ structure","no Doppler averaging",
     "no optical depth, propagation, detector or measured data",
     "not sufficient for vector-polarisation recovery"]
 }
 x.output.parent.mkdir(parents=True,exist_ok=True)
 x.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
 print("RydIQule solved three-state teaching system:",report["solution_shape"])
 print("Next: build a real Cell, validate state graph and physical probe susceptibility.")
 return 0

if __name__=="__main__":
 sys.exit(main())
