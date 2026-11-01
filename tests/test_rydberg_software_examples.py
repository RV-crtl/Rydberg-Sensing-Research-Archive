import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"book/examples"))
from arc_transition_atlas import State,allowed_e1,candidate_states
from rydiqule_three_level import construct

class ARCAndRydIQuleCurriculumTests(unittest.TestCase):
 def test_e1_selection_physics(self):
  a=State(60,0,.5,.5)
  self.assertTrue(allowed_e1(a,State(61,1,1.5,1.5),+1))
  self.assertTrue(allowed_e1(a,State(60,1,.5,-.5),-1))
  self.assertFalse(allowed_e1(a,State(60,2,2.5,2.5),+1))
  self.assertFalse(allowed_e1(a,State(61,1,1.5,-1.5),-1))
 def test_atom_candidates_nonempty_without_arc_import(self):
  c=candidate_states(70)
  self.assertGreaterEqual(len(c),2)
  self.assertTrue(all(allowed_e1(a,b,q) for a,b,q in c))
 def test_unphysical_numbers_fail(self):
  with self.assertRaises(ValueError):State(2,3,3.5,.5).validate()
 class SensorStub:
  def __init__(self,n):self.n=n;self.edges=[];self.transit=None
  def add_coupling(self,*args,**kwargs):self.edges.append((args,kwargs))
  def add_transit_broadening(self,x):self.transit=x
 def test_rydiqule_graph_and_rates(self):
  s=construct(self.SensorStub,[0.0,1.0],.1,3.0,.2)
  self.assertEqual(s.n,3)
  self.assertEqual(len(s.edges),2)
  self.assertEqual(s.transit,.2)
  with self.assertRaises(ValueError):construct(self.SensorStub,[0],.1,3,0)
