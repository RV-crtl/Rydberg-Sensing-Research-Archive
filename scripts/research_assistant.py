#!/usr/bin/env python3
"""Rydberg research quality assistant: deterministic science + doc checks.

This is a repository auditor, not an AI scientist, HFSS solver, experimental
instrument or autonomous manuscript reviewer. It does not invent conclusions.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import re
import sys
import subprocess

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "book"
SITE = ROOT / "site"


def audit():
    findings = []
    def check(condition, code, message):
        findings.append({"status": "pass" if condition else "fail",
                         "code": code, "message": message})
    def warn(code, message):
        findings.append({"status": "notice", "code": code, "message": message})
    chapters = sorted((BOOK / "chapters").glob("*.md"))
    check(len(chapters) >= 24, "SYLLABUS", "24 or more original science chapters")
    raw_chapters = []
    for p in chapters:
        text = p.read_text(encoding="utf-8")
        raw_chapters.append(text)
        check(all(token in text.lower() for token in
                  ("##", "source", "question")), "CHAPTER_FORMAT",
              p.name + ": lesson, source and self-test present")
    pieces = []
    for name in ["book-part1.json", "book-part2.json"]:
        p = SITE / "data" / name
        if not p.exists():
            check(False, "SITE_BOOK", "Missing site source " + name)
            continue
        pieces.extend(json.loads(p.read_text(encoding="utf-8")))
    check(len(pieces) == len(chapters), "BOOK_COVERAGE",
          "Website chapter data count matches original Markdown chapters")
    for item in pieces:
        path = BOOK / "chapters" / (item["slug"] + ".md")
        check(path.is_file() and path.read_text(encoding="utf-8").strip()
              == item["markdown"].strip(), "BOOK_SOURCE",
              "Site chapter identical to manuscript: " + item["slug"])
    from hashlib import sha256
    source = (BOOK / "workbook.mjs").read_bytes()
    deployed = (SITE / "workbook.mjs").read_bytes()
    check(sha256(source).digest() == sha256(deployed).digest(), "WORKBOOK_SOURCE",
          "Browser workbook math is identical to original source")
    essential = ["CURRENT_STATE.md", "REFERENCES.md", "TUTORIAL_LABS.md"]
    for filename in essential:
        check((BOOK / filename).is_file(), "BOOK_REQUIRED", filename)
    for f in ["academy-ladder.svg", "academy-hfss-pipeline.svg", "academy-diagnostic-tree.svg"]:
        file = SITE / "assets" / f
        check(file.is_file() and "<svg" in file.read_text(encoding="utf-8"),
              "FIGURE_PROVENANCE", f + " editable native SVG present")
    index = json.loads((SITE/"data/research-atlas.json").read_text(encoding="utf-8"))
    check(index["matrix"]["sourcePath"] ==
          "papers/manuscript-source/data/V42_C033_INSTRUMENT_MATRIX.csv",
          "HFSS_SOURCE", "Site model still tied to specific imported HFSS source")
    report = BOOK / "CURRENT_STATE.md"
    status = report.read_text(encoding="utf-8")
    check(all(item in status for item in ["1.925 GHz", "9.53", "76.92%", "55.09%",
                                           "2024", "2026", "finite"]),
          "CURRENT_EVIDENCE", "Current reference and negative finite findings retained")
    watcher = ROOT / "scripts/research_watch.py"
    check(watcher.is_file(), "LITERATURE_MONITOR", "Citation-only watch installed")
    for file in ["academy.html", "lab.html"]:
        check((SITE / file).is_file(), "SITE_PAGES", file)
    warn("PUBLICATION", "GitHub repository has been reported public; site and source rights must be reviewed before adding private content.")
    warn("MATURITY", "Book has 24 authored concept chapters and 1000 parameterised exercises, not 1000 substantive textbook prose pages.")
    warn("NOT_SOLVER", "CI validates source-linked calculations; it does not run Ansys HFSS, ARC transition sweeps, RydIQule full spectra or atomic experiments.")
    failures = sum(x["status"] == "fail" for x in findings)
    result = {"schema": 1, "generated_utc": datetime.now(timezone.utc).isoformat(),
              "passed": sum(x["status"] == "pass" for x in findings),
              "failures": failures, "notices": sum(x["status"] == "notice" for x in findings),
              "findings": findings}
    print(json.dumps(result, indent=2))
    print("Research assistant:", "PASS" if failures == 0 else "FAIL",
          "failed:", failures, "notices:", result["notices"], file=sys.stderr)
    return int(bool(failures))


if __name__ == "__main__":
    sys.exit(audit())
