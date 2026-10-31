import unittest, csv, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'scripts'))
from summarise_evidence import matrix_rank
class ResearchArchiveTests(unittest.TestCase):
    def test_ideal_stokes_basis_has_four_dimensions(self):
        # Pure algebraic reference fixture, not HFSS or physical measurements.
        ideal=[[1,1,0,0],[1,-1,0,0],[1,0,1,0],[1,0,-1,0],[1,0,0,1],[1,0,0,-1]]
        self.assertEqual(matrix_rank(ideal),4)
    def test_real_imported_matrix_is_six_by_four_and_rank_four(self):
        p=ROOT/'papers/manuscript-source/data/V42_C033_INSTRUMENT_MATRIX.csv'
        with p.open(encoding='utf-8') as f:
            a=[[float(v) for v in row.values()] for row in csv.DictReader(f)]
        self.assertEqual((len(a),len(a[0])),(6,4))
        self.assertEqual(matrix_rank(a),4)
    def test_claim_ids_unique_and_sources_exist(self):
        with (ROOT/'docs/traceability/CLAIM_EVIDENCE.csv').open(encoding='utf-8') as f:claims=list(csv.DictReader(f))
        self.assertEqual(len(set(x['claim_id'] for x in claims)),len(claims))
        for c in claims:self.assertTrue((ROOT/c['repo_path']).exists(),c['claim_id'])
    def test_publication_article_source_editable(self):
        tex=(ROOT/'papers/manuscript-source/main.tex').read_text(encoding='utf-8')
        self.assertIn('\\documentclass',tex)
        self.assertIn('\\begin{document}',tex)
        self.assertNotIn('\\includepdf',tex)
if __name__=='__main__':unittest.main()
