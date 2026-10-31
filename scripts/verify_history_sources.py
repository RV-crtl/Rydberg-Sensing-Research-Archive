#!/usr/bin/env python3
"""Check source-level historic research imports against committed Git object IDs.

This verification is intentionally separate from the baseline experiment/HFSS
SHA-256 manifest: the recovered files are TEXT EXTRACTS from old Library
documents, not byte-identical copies of their original upload formats.
"""
from pathlib import Path
import csv
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "history/RECOVERED_SOURCE_PROVENANCE.csv"
HISTORIC_PREFIXES = (
    "history/original-research-plans/",
    "history/recovered-code/",
    "history/recovered-evidence/",
    "history/recovered-reports/",
    "history/editorial-reviews/",
)


def committed_blobs():
    data = subprocess.check_output(
        ["git", "ls-tree", "-r", "-z", "HEAD"], cwd=ROOT
    )
    out = {}
    for blob in data.split(b"\x00"):
        if not blob:
            continue
        meta, path = blob.split(b"\t", 1)
        mode, kind, sha = meta.split()
        if kind == b"blob":
            out[path.decode("utf-8")] = sha.decode("ascii")
    return out


def main():
    errors = []
    paths = set()
    git = committed_blobs()
    with MANIFEST.open(encoding="utf-8", newline="") as f:
        records = list(csv.DictReader(f))
    for row in records:
        path = row["repository_path"]
        if path in paths:
            errors.append("Duplicate historic source: " + path)
        paths.add(path)
        if not path.startswith(HISTORIC_PREFIXES):
            errors.append("Manifest entry outside historic source trees: " + path)
        if not (ROOT / path).is_file():
            errors.append("Historic source missing: " + path)
        if git.get(path) != row["git_blob_sha1"]:
            errors.append("Original historic source modified without provenance revision: " + path)
        if row["source_representation"] != "original-Library-text-extraction":
            errors.append("Original byte provenance overstated: " + path)
    actual = {
        path for path in git if path.startswith(HISTORIC_PREFIXES)
    }
    for missing in sorted(actual - paths):
        errors.append("Historic source not registered: " + missing)
    for missing in sorted(paths - actual):
        errors.append("Provenance entry no longer tracked: " + missing)
    print(f"Recovered historic source records: {len(records)}")
    if errors:
        for e in errors[:100]:
            print("ERROR:", e)
        return 1
    print("PASS: all recovered historic text sources tracked and Git-object verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
