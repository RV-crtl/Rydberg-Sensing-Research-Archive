import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from verify_archive import source_bytes_match, sha256_bytes

class ImmutableScientificSourceTests(unittest.TestCase):
    def test_exact_source_is_accepted(self):
        original = b"frequency,Ex,Ey\n1.8,0.3,0.4\n"
        self.assertEqual(
            source_bytes_match(original, sha256_bytes(original), len(original), ".csv"),
            (True, False)
        )
    def test_crlf_normalisation_is_exactly_reversible(self):
        original = b"frequency,Ex\r\n1.8,0.3\r\n"
        checkout = original.replace(b"\r\n", b"\n")
        self.assertEqual(
            source_bytes_match(checkout, sha256_bytes(original), len(original), ".csv"),
            (True, True)
        )
    def test_tampered_numeric_field_fails(self):
        original = b"frequency,Ex\r\n1.8,0.3\r\n"
        tampered = b"frequency,Ex\n1.8,0.4\n"
        self.assertEqual(
            source_bytes_match(tampered, sha256_bytes(original), len(original), ".csv"),
            (False, False)
        )
    def test_binary_change_cannot_be_exempted(self):
        original = b"%PDF-1.0\r\nx\r\n"
        checkout = original.replace(b"\r\n", b"\n")
        self.assertEqual(
            source_bytes_match(checkout, sha256_bytes(original), len(original), ".pdf"),
            (False, False)
        )
