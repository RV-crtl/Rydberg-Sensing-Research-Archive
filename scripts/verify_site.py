#!/usr/bin/env python3
"""Verify a self-contained Pages artifact and exact scientific JSON provenance."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import csv
import json
import math
import sys

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
ALLOWED = {".html", ".css", ".js", ".mjs", ".json", ".png", ".jpg", ".jpeg",
           ".svg", ".webp", ".ico", ".txt", ".md"}

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.scripts = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        for field in ("src", "href"):
            if field in data:
                self.links.append((tag, field, data[field]))
        if tag == "script" and data.get("src"):
            self.scripts.append(data["src"])

def check():
    errors = []
    paths = [p for p in SITE.rglob("*") if p.is_file()]
    for p in paths:
        if p.suffix.lower() not in ALLOWED:
            errors.append("Unexpected file in publishable site: " + str(p.relative_to(SITE)))
        if p.name.startswith(".") or any(q in {".git", "evidence", "papers", "reports"} for q in p.relative_to(SITE).parts[:-1]):
            errors.append("Non-site raw/private path: " + str(p.relative_to(SITE)))
        if p.suffix.lower() == ".html":
            h = Links()
            h.feed(p.read_text(encoding="utf-8"))
            for tag, kind, link in h.links:
                if not link or link.startswith(("#", "mailto:", "tel:", "data:")):
                    continue
                parsed = urlsplit(link)
                if parsed.scheme in ("http", "https"):
                    if tag == "script" or (tag == "link" and kind == "href" and
                        not parsed.netloc.endswith("github.com")):
                        errors.append("Remote executable/resource in site: " + link)
                    continue
                if parsed.scheme:
                    errors.append("Unsupported site URL: " + link)
                    continue
                target = (p.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(SITE.resolve()):
                    errors.append("Site-only deploy cannot resolve parent link: " + str(p.relative_to(SITE)) + " -> " + link)
                elif not target.exists():
                    errors.append("Missing site resource: " + str(p.relative_to(SITE)) + " -> " + link)
    for p in [SITE/"explorer.js", SITE/"model.mjs", SITE/"explorer.css", SITE/"data/research-atlas.json"]:
        if not p.exists():
            errors.append("Missing scientific explorer asset: " + str(p))
    atlas = json.loads((SITE/"data/research-atlas.json").read_text(encoding="utf-8"))
    data = atlas["matrix"]
    source = ROOT / data["sourcePath"]
    with source.open(encoding="utf-8", newline="") as f:
        rows = [[float(x) for x in row.values()] for row in csv.DictReader(f)]
    if len(rows) != 6 or any(len(x) != 4 for x in rows):
        errors.append("Source six-state instrument matrix has wrong shape")
    elif any(not math.isclose(a, b, rel_tol=1e-13, abs_tol=1e-13)
             for row_a,row_b in zip(rows, data["rows"])
             for a,b in zip(row_a,row_b)):
        errors.append("Website matrix does not match original research CSV")
    original_budget=json.loads((ROOT/data["dwell"]["sourcePath"]).read_text(encoding="utf-8"))
    if data["maskOrder"] != original_budget["mask_order"]:
        errors.append("Mask order differs from source return")
    if not math.isclose(data["dwell"]["equalTrace"], original_budget["six_equal_trace"], rel_tol=1e-12):
        errors.append("Equal allocation criterion differs from HFSS-derived result")
    if not math.isclose(data["dwell"]["optimizedTrace"], original_budget["six_opt_trace"], rel_tol=1e-12):
        errors.append("Optimized allocation criterion differs from HFSS-derived result")
    historical=json.loads((SITE/"data/historical-index.json").read_text(encoding="utf-8"))
    if historical.get("schema") != 1 or historical.get("status") != "discovery-only":
        errors.append("Historical records are not labelled discovery-only")
    if len(historical.get("records", [])) != 1280:
        errors.append("Historical inventory count mismatch: expected 1,280 metadata rows")
    source_files={p["p"] for p in atlas["files"]}
    if len(source_files) != len(atlas["files"]):
        errors.append("Duplicate path in website source index")
    for f in atlas["files"]:
        if not (ROOT/f["p"]).is_file():
            errors.append("Website source index includes nonexistent path: " + f["p"])
    for t in atlas["timeline"]:
        if t["path"] not in source_files:
            errors.append("Chronology links to unindexed source: " + t["path"])
    print("Site assets:",len(paths),"tracked original sources:",len(source_files),"timeline milestones:",len(atlas["timeline"]))
    if errors:
        for error in errors[:60]:
            print("ERROR:", error)
        return 1
    print("PASS: standalone links, publishable asset scope and exact scientific source data.")
    return 0

if __name__=="__main__":
    sys.exit(check())
