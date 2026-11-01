import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from research_watch import score, shortlist, render

class ResearchWatchTests(unittest.TestCase):
    def test_relevance_dedup(self):
        doc = {"title":"Rydberg microwave polarization sensor", "url":"https://doi.org/10.1/x",
               "doi":"10.1/x", "date":"2026-09-01", "source":"Crossref",
               "venue":"Test"}
        self.assertGreater(score(doc), 10)
        self.assertEqual(len(shortlist([doc, doc])), 1)
    def test_no_fake_results(self):
        d = {"title":"Rydberg microwave polarization sensor", "url":"https://doi.org/10.1/x",
             "doi":"10.1/x", "date":"2026-09-01", "source":"Crossref","venue":"Test"}
        s = render([d], [], "2026-11-01")
        self.assertIn("not extracted",s)
        self.assertIn("not verified from full text",s)
    def test_irrelevant_filtered(self):
        self.assertEqual(shortlist([{"title":"Agricultural policy", "url":"https://doi.org/a", "doi":"a"}]),[])
