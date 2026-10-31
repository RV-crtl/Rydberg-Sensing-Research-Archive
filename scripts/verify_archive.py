#!/usr/bin/env python3
"""Research-archive verifier: original SHA-256, reversible Git EOL, curated Git blobs."""
from pathlib import Path
from urllib.parse import unquote
import csv
import hashlib
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parent.parent
ORIGINAL = ROOT / "docs/traceability/ASSET_REGISTER.csv"
CURATED = ROOT / "docs/traceability/CURATED_DOCUMENT_BLOBS.csv"
TEXT_EOL_TYPES = {".csv", ".json", ".md", ".py", ".tex"}


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data):
    # Git blob object IDs include a length prefix and zero terminator.
    prefix = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(prefix + data).hexdigest()


def relative_links(path):
    source = path.read_text(encoding="utf-8")
    for link in re.findall(r"(?<!!)\[[^]]+\]\(([^)]+)\)", source):
        target = unquote(link.split("#", 1)[0].strip().split(" ", 1)[0])
        if not target or re.match(r"^(https?://|mailto:|data:)", target):
            continue
        yield target


def audit():
    errors = []
    original = list(csv.DictReader(ORIGINAL.open(encoding="utf-8", newline="")))
    changed = {r["path"]: r["git_blob_sha1"] for r in
               csv.DictReader(CURATED.open(encoding="utf-8", newline=""))}
    registered = [r["path"] for r in original]
    recovered_eol = 0
    curated_checked = 0
    exact = 0

    for row in original:
        rel = row["path"]
        path = ROOT / rel
        if not path.is_file():
            errors.append("Missing registered asset: " + rel)
            continue
        data = path.read_bytes()
        old_size = int(row["bytes"])
        actual_size = len(data)
        old_hash = row["sha256"]

        if sha256_bytes(data) == old_hash and actual_size == old_size:
            exact += 1
        elif rel in changed and changed[rel] != "PENDING":
            # Edited documentation/code receives a new Git-native content identity,
            # while the initial asset register remains a preserved baseline record.
            if git_blob_sha1(data) == changed[rel]:
                curated_checked += 1
            else:
                errors.append("Curated document Git blob mismatch: " + rel)
        elif path.suffix.lower() in TEXT_EOL_TYPES:
            # Git Desktop normalised CRLF text to LF on first upload.
            # Accept only when the *entire original file* is exactly reconstructible.
            original_bytes = data.replace(b"\n", b"\r\n") if b"\r" not in data else b""
            if (len(original_bytes) == old_size and
                    sha256_bytes(original_bytes) == old_hash):
                recovered_eol += 1
            else:
                errors.append("Non-reversible source-file mismatch: " + rel)
        else:
            errors.append("Checksum or size mismatch: " + rel)

        if path.suffix.lower() == ".zip":
            try:
                with zipfile.ZipFile(path) as zip_file:
                    if zip_file.testzip():
                        errors.append("Corrupt ZIP: " + rel)
            except Exception as exc:
                errors.append(f"Unreadable ZIP: {rel}: {exc}")

    for path in ROOT.rglob("*.md"):
        for target in relative_links(path):
            if not (path.parent / target).resolve().exists():
                errors.append(
                    f"Broken relative link: {path.relative_to(ROOT)} -> {target}"
                )
    claims = ROOT / "docs/traceability/CLAIM_EVIDENCE.csv"
    for row in csv.DictReader(claims.open(encoding="utf-8", newline="")):
        if not (ROOT / row["repo_path"]).exists():
            errors.append("Missing claim evidence: " + row["repo_path"])

    if len(set(registered)) != len(registered):
        errors.append("Duplicate paths in original asset manifest")
    print(
        f"Original asset rows: {len(original)}; exact bytes: {exact}; "
        f"reversible CRLF-normalised: {recovered_eol}; "
        f"versioned curated files: {curated_checked}"
    )
    if errors:
        print("\n".join("ERROR: " + err for err in errors[:100]))
        return 1
    print("PASS: original provenance recoverable or Git-versioned; links and claims verified.")
    return 0


if __name__ == "__main__":
    sys.exit(audit())
