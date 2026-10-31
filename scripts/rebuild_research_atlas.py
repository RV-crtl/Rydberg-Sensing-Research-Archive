#!/usr/bin/env python3
"""Refresh the static research website's source index from *tracked Git* files.

The manually published site cannot query the private repository's API without
credentials. This index is a dated, release-time public metadata snapshot, NOT
the contents of any untracked raw laboratory or confidential working files.

Usage:
    python scripts/rebuild_research_atlas.py
    python scripts/rebuild_research_atlas.py --check
"""
from pathlib import Path
import argparse
import json
import subprocess

ROOT = Path(__file__).resolve().parent.parent
ATLAS = ROOT / "site/data/research-atlas.json"


def file_category(path: str) -> str:
    categories = (
        ("history/original-research-plans/", "Original research plans"),
        ("history/recovered-code/matlab/", "Recovered MATLAB"),
        ("history/recovered-code/arc/", "Recovered ARC"),
        ("history/recovered-code/atomic/", "Recovered atomic modelling"),
        ("history/recovered-code/cst/", "Recovered CST"),
        ("history/recovered-code/workbench/", "Recovered Workbench"),
        ("history/recovered-code/figures/", "Figure generators"),
        ("history/recovered-evidence/", "Historical HFSS and numerical records"),
        ("history/recovered-reports/", "Original thesis and presentations"),
        ("history/editorial-reviews/", "Peer and academic reviews"),
        ("history/binary-imports/", "Source-intake manifests"),
        ("history/", "Research history"),
        ("evidence/", "Native simulation evidence"),
        ("papers/", "Manuscript sources"),
        ("presentations/", "Presentations"),
        ("docs/", "Research documentation"),
        ("research-code/", "Scientific code"),
        ("reports/", "Research reports"),
        ("governance/", "Governance"),
        ("literature/", "Literature"),
        ("designs/", "Hardware concepts"),
        ("site/", "Website"),
        ("tests/", "Verification"),
        ("scripts/", "Verification"),
    )
    return next((category for prefix, category in categories if path.startswith(prefix)), "Repository")


def git_index():
    try:
        result = subprocess.run(
            ["git", "ls-tree", "-r", "-z", "--long", "HEAD"],
            cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            check=True
        ).stdout
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        raise RuntimeError(
            "This generator requires a Git checkout containing the committed files. "
            "Open the local clone with GitHub Desktop, or run during GitHub Actions."
        ) from exc
    files = []
    for item in result.split(b"\x00"):
        if not item:
            continue
        # ls-tree -l: mode type object-id size<TAB>path; path may contain spaces.
        header, raw_path = item.split(b"\t", 1)
        fields = header.split()
        if fields[1] != b"blob":
            continue
        path = raw_path.decode("utf-8")
        files.append({
            "p": path,
            "g": file_category(path),
            "bytes": int(fields[3]) if fields[3] != b"-" else 0
        })
    return sorted(files, key=lambda f: f["p"])


def build():
    atlas = json.loads(ATLAS.read_text(encoding="utf-8"))
    # Preserve the HFSS-derived source matrix, numerical values, source
    # provenance and dated milestone timeline exactly. Update only index.
    atlas["files"] = git_index()
    atlas["sourceIndexNote"] = (
        "Git-tracked file metadata from the latest generator run; "
        "historical Library discovery records are a separate unimported list."
    )
    return atlas


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true",
                        help="Check source-index path/category/size against HEAD")
    args = parser.parse_args()
    current = json.loads(ATLAS.read_text(encoding="utf-8"))
    refreshed = build()
    if args.check:
        if refreshed["files"] != current["files"]:
            print("STALE: source index does not match tracked Git tree; run without --check")
            raise SystemExit(1)
        print(f"PASS: {len(refreshed['files'])} tracked files indexed in research atlas")
        return
    ATLAS.write_text(
        json.dumps(refreshed, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )
    print(f"Updated research atlas with {len(refreshed['files'])} tracked files")


if __name__ == "__main__":
    main()
