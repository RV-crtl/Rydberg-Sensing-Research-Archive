#!/usr/bin/env python3
"""Conservative Rydberg paper monitor: source metadata, not fabricated summaries."""
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET
import json
import sys

OUT = Path(__file__).resolve().parent.parent / "research_updates"
KEYS = {"rydberg": 6, "microwave": 4, "polarimetry": 6, "polarization": 5,
        "polarisation": 5, "electrometry": 4, "metasurface": 5,
        "zeeman": 3, "fisher": 3, "autler": 3, "quantum sensing": 3}
UA = "RydbergResearchArchive/1.0 (bibliographic metadata for human review)"


def download(url):
    if not url.startswith(("https://api.crossref.org/works?", "https://export.arxiv.org/api/query?")):
        raise ValueError("Unapproved metadata endpoint")
    with urlopen(Request(url, headers={"User-Agent": UA}), timeout=25) as r:
        return r.read(2000000)


def crossref(since):
    q = urlencode({"query.title": "Rydberg microwave RF polarimetry", "filter": "from-pub-date:" + since,
                   "rows": 35, "sort": "published", "order": "desc"})
    payload = json.loads(download("https://api.crossref.org/works?" + q))
    out = []
    for v in payload.get("message", {}).get("items", []):
        title = " ".join(v.get("title", []))
        doi = v.get("DOI", "").strip()
        if not doi or not title:
            continue
        parts = v.get("published", {}).get("date-parts", [[None]])[0]
        date = "-".join(str(x).zfill(2) if i else str(x) for i, x in enumerate(parts)) if parts else "unknown"
        out.append({"title": title, "doi": doi.lower(), "url": "https://doi.org/" + doi,
                    "date": date, "source": "Crossref DOI metadata",
                    "venue": " ".join(v.get("container-title", [])) or "Unspecified"})
    return out


def arxiv():
    q = "search_query=all:rydberg+AND+(all:polarization+OR+all:microwave+OR+all:electrometry)"
    raw = download("https://export.arxiv.org/api/query?" + q + "&sortBy=submittedDate&sortOrder=descending&max_results=50")
    root = ET.fromstring(raw)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    for e in root.findall("a:entry", ns):
        title = " ".join(e.findtext("a:title", "", ns).split())
        url = e.findtext("a:id", "", ns).replace("http:", "https:")
        if not url.startswith("https://arxiv.org/abs/"):
            continue
        out.append({"title": title, "url": url, "doi": "", "date": e.findtext("a:published", "", ns)[:10],
                    "venue": "arXiv preprint", "source": "arXiv Atom metadata"})
    return out


def score(item):
    title = item["title"].casefold()
    return sum(w for k, w in KEYS.items() if k in title)


def shortlist(items, limit=8):
    out, seen = [], set()
    for item in sorted(items, key=lambda x: (score(x), x.get("date", "")), reverse=True):
        key = item.get("doi") or item["url"].split("v")[0]
        if key in seen or score(item) < 6:
            continue
        seen.add(key)
        out.append(item)
        if len(out) >= limit:
            break
    return out


def render(items, errors, today):
    lines = ["# Rydberg research review candidates — " + today, "",
             "**Automatically collected metadata; NOT an independent review, experimental validation or new physics result.**",
             ""]
    if errors:
        lines += ["## Data-source limitations", ""] + ["- " + e for e in errors] + [""]
    if not items:
        lines += ["No candidates verified. This may mean API failure, not an absence of research.", ""]
    for i, item in enumerate(items, 1):
        lines += ["## " + str(i) + ". " + item["title"], "",
                  "- **Source URL:** " + item["url"],
                  "- **Date / venue:** " + item["date"] + " — " + item["venue"],
                  "- **Metadata provenance:** " + item["source"],
                  "- **Relevance score:** " + str(score(item)) + " (title keywords only)",
                  "- **Method and dataset:** not verified from full text.",
                  "- **Findings:** not extracted; do not quote as established results.",
                  "- **Research gap / limitations:** requires full-text review of methods, claims and comparison with prior art.",
                  "- **Read priority:** " + ("High — inspect full paper" if score(item) >= 14 else "Consider — verify relevance"),
                  ""]
    lines += ["## Required human scientific review", "",
              "Validate DOI/preprint status and figure source, classify measured versus simulated results, and update the dated novelty/claim ledger only after reading the paper.", ""]
    return "\n".join(lines)


def main():
    now = datetime.now(timezone.utc)
    since = (now - timedelta(days=45)).date().isoformat()
    found, errors = [], []
    for name, fn in [("Crossref", lambda: crossref(since)), ("arXiv", arxiv)]:
        try:
            found.extend(fn())
        except Exception as exc:
            errors.append(name + " unavailable: " + type(exc).__name__ + ": " + str(exc)[:120])
    items = shortlist(found)
    OUT.mkdir(exist_ok=True)
    p = OUT / ("weekly_" + now.date().isoformat() + ".md")
    p.write_text(render(items, errors, now.date().isoformat()), encoding="utf-8")
    print(str(p))
    print("Candidates:", len(items), "API errors:", len(errors))
    return 1 if len(errors) == 2 else 0


if __name__ == "__main__":
    sys.exit(main())
