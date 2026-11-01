#!/usr/bin/env python3
"""State-resolved ARC transition screening without fictitious atomic data.

Usage:
  python book/examples/arc_transition_atlas.py --list
  python -m pip install ARC-Alkali-Rydberg-Calculator
  python book/examples/arc_transition_atlas.py --run --species Rb87 --n 60

Output is created only if ARC is installed and actual ARC calculations succeed.
Field/optical access and state preparation still need separate validation.
"""
from __future__ import annotations
import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from math import isfinite
import sys

@dataclass(frozen=True)
class State:
 n:int
 l:int
 j:float
 mj:float
 def validate(self):
  if self.n<1 or self.l<0 or self.l>=self.n or abs(self.mj)>self.j:
   raise ValueError("Invalid atomic quantum numbers")
  if abs(2*self.j-round(2*self.j))>1e-9 or abs(2*self.mj-round(2*self.mj))>1e-9:
   raise ValueError("j and mj must be half-integer or integer")
  return self

def allowed_e1(a:State,b:State,q:int)->bool:
 a.validate();b.validate()
 return (q in (-1,0,1) and abs(a.l-b.l)==1
  and abs(a.j-b.j)<=1 and (a.j+b.j)!=0
  and abs((b.mj-a.mj)-q)<1e-9)

def candidate_states(n):
 # A generic adjacent- and near-adjacent-Rydberg pair-screening
 # exercise; NOT a claim that all pairs have optical access.
 start=State(n,0,.5,.5)
 return [(start,State(n2,1,j,mj),q)
   for n2 in (n-1,n,n+1) if n2>1
   for j in (.5,1.5) for mj in (-j,j)
   for q in (-1,0,1)
   if allowed_e1(start,State(n2,1,j,mj),q)]

def build(species,n):
 if species=="Rb87":
  from arc import Rubidium87
  atom=Rubidium87()
 elif species=="Cs":
  from arc import Caesium
  atom=Caesium()
 else:raise ValueError("Unknown atomic species")
 rows=[]
 for src,dst,q in candidate_states(n):
  # Frequencies are signed and reported in Hz by ARC.
  hz=float(atom.getTransitionFrequency(src.n,src.l,src.j,dst.n,dst.l,dst.j))
  mu=float(atom.getDipoleMatrixElement(src.n,src.l,src.j,src.mj,
                                      dst.n,dst.l,dst.j,dst.mj,q))
  if not isfinite(hz) or not isfinite(mu):
   raise ValueError("Non-finite ARC output")
  rows.append({"species":species,"from_n":src.n,"from_l":src.l,"from_j":src.j,"from_mj":src.mj,
    "to_n":dst.n,"to_l":dst.l,"to_j":dst.j,"to_mj":dst.mj,"q":q,
    "transition_hz_signed":hz,"frequency_ghz_magnitude":abs(hz)/1e9,
    "dipole_ea0_signed":mu,
    "status":"ARC theoretical calculation; not measured and optical access unverified"})
 return rows

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--species",choices=["Rb87","Cs"],default="Rb87")
 p.add_argument("--n",type=int,default=60)
 p.add_argument("--list",action="store_true",help="Explain candidate basis; no ARC data calculated")
 p.add_argument("--run",action="store_true",help="Require ARC to compute real state energies and dipoles")
 p.add_argument("--output",type=Path,default=Path("arc_calculated_transition_atlas.csv"))
 x=p.parse_args()
 if not 12<=x.n<=150:p.error("n must be in 12...150; validate species datasets separately")
 candidates=candidate_states(x.n)
 print("Allowed E1 m-state candidates:",len(candidates))
 if x.list:
  for a,b,q in candidates:print(a,"->",b,"q=",q)
  return 0
 if not x.run:
  p.error("Provide --run for actual ARC model calculations, or --list for a code-only preview")
 try:
  rows=build(x.species,x.n)
 except ImportError as exc:
  print("Missing ARC: install ARC-Alkali-Rydberg-Calculator in this Python environment.",file=sys.stderr)
  raise SystemExit(2) from exc
 if not rows:raise RuntimeError("No allowed transitions for selected input")
 x.output.parent.mkdir(parents=True,exist_ok=True)
 with x.output.open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]))
  w.writeheader();w.writerows(rows)
 print("Wrote",len(rows),"genuine ARC outputs to",x.output)
 print("Verify ARC state data, quantum defect, optical access and dipole convention before designing hardware.")
 return 0

if __name__=="__main__":raise SystemExit(main())
