import sys
import unittest
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"automation"))
from australia_watch import parse_highlights,deadline_interpretation,get_source

class AustralianMonitorTests(unittest.TestCase):
 def test_parse_relevant_html_without_scripting(self):
  title,highlights=parse_highlights('<html><title>Australian Quantum Research</title><script>malicious funding = true</script><p>Applications for quantum sensing research close on 12 November; check official ARC eligibility requirements.</p></html>')
  self.assertEqual(title,'Australian Quantum Research')
  self.assertTrue(any('eligibility' in x for x in highlights))
  self.assertFalse(any('malicious' in x for x in highlights))
 def test_deadline_past_not_promoted(self):
  rec={'statedDeadline':'2026-07-20'}
  self.assertIn('passed',deadline_interpretation(rec,date(2026,11,1)))
 def test_future_date_does_not_certify_open(self):
  rec={'statedDeadline':'2026-11-25'}
  s=deadline_interpretation(rec,date(2026,11,1))
  self.assertIn('verify',s.lower())
 def test_untrusted_domains_rejected_before_request(self):
  with self.assertRaises(ValueError):
   get_source({'url':'https://example.com/private'})
