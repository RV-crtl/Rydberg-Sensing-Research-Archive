#!/usr/bin/env python3
"""Verify immutable source evidence, source links and readable original ZIPs."""
from pathlib import Path
from urllib.parse import unquote
import csv
import hashlib
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "docs/traceability/ASSET_REGISTER.csv"
TEXT_EOL = {".csv", ".json", ".md", ".py", ".tex", ".svg"}

def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()

def source_bytes_match(data, original_sha, original_size, ext):
    """Accept exact data or only a provably reversible CRLF-to-LF checkout."""
    if len(data) == original_size and sha256_bytes(data) == original_sha:
        return True, False
    if ext.lower() not in TEXT_EOL or b"\r" in data:
        return False, False
    restored = data.replace(b"\n", b"\r\n")
    valid = len(restored) == original_size and sha256_bytes(restored) == original_sha
    return valid, valid

def relative_links(path):
    source = path.read_text(encoding="utf-8")
    for link in re.findall(r"(?<!!)\[[^]]+\]\(([^)]+)\)", source):
        target = unquote(link.split("#", 1)[0].strip().split(" ", 1)[0])
        if target and not re.match(r"^(https?://|mailto:|data:)", target):
            yield target

def audit():
    errors = []
    with MANIFEST.open(encoding="utf-8", newline="") as f:
        records = list(csv.DictReader(f))
    names = []
    exact = restored = curated = 0
    for row in records:
        rel = row["path"]
        names.append(rel)
        path = ROOT / rel
        if (rel.startswith("/") or ".." in Path(rel).parts
                or not path.resolve().is_relative_to(ROOT.resolve())):
            errors.append("Unsafe registered path: " + rel)
            continue
        if not path.is_file():
            errors.append("Missing registered asset: " + rel)
            continue
        cls = row["source_class"]
        if cls == "curated-documentation-or-tool":
            curated += 1
            continue
        if cls != "imported-primary":
            errors.append("Unknown source class: " + rel)
            continue
        ok, changed_eol = source_bytes_match(
            path.read_bytes(), row["sha256"], int(row["bytes"]), path.suffix
        )
        if not ok:
            errors.append("Immutable evidence hash mismatch: " + rel)
        elif changed_eol:
            restored += 1
        else:
            exact += 1
        if path.suffix.lower() == ".zip":
            try:
                with zipfile.ZipFile(path) as archive:
                    bad = archive.testzip()
                    if bad:
                        errors.append("Bad ZIP member: " + rel + ": " + bad)
            except (OSError, zipfile.BadZipFile, zipfile.LargeZipFile) as err:
                errors.append("Unreadable ZIP: " + rel + ": " + str(err))
    if len(names) != len(set(names)):
        errors.append("Duplicate original asset paths")
    for md in ROOT.rglob("*.md"):
        if md.is_file():
            for link in relative_links(md):
                target = (md.parent / link).resolve()
                if not target.is_relative_to(ROOT.resolve()) or not target.exists():
                    errors.append("Broken Markdown link: " + str(md.relative_to(ROOT)) + " -> " + link)
    with (ROOT / "docs/traceability/CLAIM_EVIDENCE.csv").open(
        encoding="utf-8", newline=""
    ) as f:
        for row in csv.DictReader(f):
            target = (ROOT / row["repo_path"]).resolve()
            if not target.is_relative_to(ROOT.resolve()) or not target.exists():
                errors.append("Missing claim source: " + row["claim_id"] + ": " + row["repo_path"])
    print("Original manifest:", len(records), "| immutable exact:", exact,
          "| reversible CRLF:", restored, "| edited/Git-tracked docs:", curated)
    if errors:
        print("\n".join("ERROR: " + e for e in errors[:120]))
        return 1
    print("PASS: primary research evidence, registered claims and source links.")
    return 0

if __name__ == "__main__":
    sys.exit(audit())
