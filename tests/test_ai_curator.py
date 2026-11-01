import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"automation"))
from curator_agent import allowed_filename,validate_output

class AICuratorGuardTests(unittest.TestCase):
 def test_allowlisted_file_path(self):
  self.assertEqual(allowed_filename("python_example","rabi_example"),"book/examples/agent_rabi_example.py")
  with self.assertRaises(ValueError):allowed_filename("python_example","../../scripts/verify_archive")
  with self.assertRaises(ValueError):allowed_filename("workflow","update_main")
 def test_reject_unparseable_python(self):
  with self.assertRaises(SyntaxError):validate_output({"mode":"python_example","name":"bad_example","content":"def b(: pass"})
 def test_editorial_citations_required(self):
  with self.assertRaises(ValueError):validate_output({"mode":"editorial_proposal","name":"bad_proposal","content":"All atomic sensors are perfect."})
 def test_source_constrained_editorial(self):
  p,_=validate_output({"mode":"editorial_proposal","name":"quantum_review","content":"Compare to the official literature at https://www.nist.gov and independently verify."})
  self.assertTrue(p.startswith("book/editorial-proposals/"))
