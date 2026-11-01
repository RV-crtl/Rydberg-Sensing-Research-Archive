import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"automation"))
from editorial_audit import measure,assess,MIN_WORDS,MIN_IMAGES,MIN_QA

class EditorialAuditTests(unittest.TestCase):
 def test_measures_substantive_source_not_pdf_pages(self):
  data="# Chapter\n\n## Derivation\n\nThis has short physics text.\n\n<details><summary>Answer</summary>Physical explanation.</details>\n"
  s=measure(data)
  self.assertLess(s['words'],MIN_WORDS)
  self.assertEqual(s['answered_questions'],1)
  self.assertEqual(s['figures'],0)
 def test_short_course_is_not_marked_publisher_ready(self):
  with tempfile.TemporaryDirectory() as td:
   file=Path(td)/"draft.md"
   file.write_text("# Atomic theory\n\n## Source\n\nA short draft.")
   c=assess(file)
   self.assertEqual(c['editorial_status'],'draft')
   self.assertTrue(c['deficits'])
 def test_thresholds_are_actual_publication_targets(self):
  self.assertGreaterEqual(MIN_WORDS,5000)
  self.assertGreaterEqual(MIN_IMAGES,3)
  self.assertGreaterEqual(MIN_QA,12)
