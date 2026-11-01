import sys
import unittest
from pathlib import Path
from datetime import date

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"automation"))
from opportunity_triage import classify,check_sources,generate

class VerifiedOpportunityStatusTests(unittest.TestCase):
 def test_expired_call_must_not_be_called_live(self):
  a=classify({"statedDeadline":"2026-10-23","deadlineTimezone":"Australia/Perth"},today=date(2026,11,1))
  self.assertEqual(a["status"],"PAST_RECORDED_DEADLINE")
 def test_future_deadline_is_unverified(self):
  a=classify({"statedDeadline":"2026-11-30","deadlineTimezone":"Australia/Sydney"},today=date(2026,11,1))
  self.assertEqual(a["status"],"FUTURE_ADVERTISED_DEADLINE_UNVERIFIED")
  self.assertEqual(a["days"],29)
 def test_no_deadline_never_claims_open(self):
  self.assertEqual(classify({"statedDeadline":None,"deadlineTimezone":None},date(2026,11,1))["status"],"REVIEW_CURRENT_SOURCE")
 def test_unique_sources_and_complete_eligibility(self):
  self.assertGreater(len(generate(today=date(2026,11,1))),5)
  with self.assertRaises(ValueError):
   check_sources([{"id":"x","url":"http://example.org","publisher":"Fake","eligibility":"Any"}])
