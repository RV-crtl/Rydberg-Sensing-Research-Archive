#!/usr/bin/env python3
"""Textbook quality sentinel: reports editorial incompleteness, never fabricates a pass.

Runs with stdlib. Analyses canonical manuscript source, not PDF page count.
Thresholds are editorial *targets*, not scientific certification.
"""
from datetime import datetime, timezone
from pathlib import Path
import json
import re
import sys

ROOT=Path(__file__).resolve().parent.parent
CHAPTERS=ROOT/"book"/"chapters"
OUT=ROOT/"research_updates"/"editorial"
MIN_WORDS=5000
MIN_QA=12
MIN_IMAGES=3

def measure(text):
 # Count words with a consistent token regex, not browser rendering.
 words=len(re.findall(r"\b[\w]+(?:[-'][\w]+)*\b",text))
 qa=text.count("<details>")
 figures=len(re.findall(r"!\[[^\]]+\]\(([^)]+)\)",text))
 headings=len(re.findall(r"^## ",text,flags=re.MULTILINE))
 links=len(re.findall(r"(?<!!)\[[^\]]+\]\(https?://[^)]+\)",text))
 return {"words":words,"answered_questions":qa,"figures":figures,
         "section_headings":headings,"direct_external_citation_links":links}

def assess(path):
 text=path.read_text(encoding="utf-8")
 if not text.startswith("# "):raise ValueError("Missing chapter H1: "+str(path))
 values=measure(text)
 deficits=[]
 if values["words"]<MIN_WORDS:deficits.append("Expand original derivations and prose: "+str(values["words"])+"/"+str(MIN_WORDS)+" words")
 if values["answered_questions"]<MIN_QA:deficits.append("Add distinct, non-repeated worked question/answer pairs: "+str(values["answered_questions"])+"/"+str(MIN_QA))
 if values["figures"]<MIN_IMAGES:deficits.append("Create original, physically reviewed figures: "+str(values["figures"])+"/"+str(MIN_IMAGES))
 if values["direct_external_citation_links"]<1:deficits.append("Add exact source citations next to nontrivial claims/equations")
 if values["section_headings"]<7:deficits.append("Increase conceptual/derivation structure: "+str(values["section_headings"])+"/7 sections")
 try: rel=str(path.relative_to(ROOT))
 except ValueError:rel=str(path)
 return {"path":rel,"title":text.splitlines()[0][2:],
         "metrics":values,"editorial_status":"draft" if deficits else "needs_human_peer_review",
         "deficits":deficits}

def run():
 chapters=sorted(CHAPTERS.glob("[0-9][0-9]-*.md"))
 if len(chapters)<36:raise RuntimeError("Incomplete canonical chapter series")
 checked=[assess(x) for x in chapters]
 summary={"schema":1,"created_utc":datetime.now(timezone.utc).isoformat(),
          "standards":{"min_words":MIN_WORDS,"min_distinct_worked_questions":MIN_QA,
                       "min_figures":MIN_IMAGES,"human_peer_review":True},
          "chapter_count":len(checked),"total_words":sum(c["metrics"]["words"] for c in checked),
          "total_questions":sum(c["metrics"]["answered_questions"] for c in checked),
          "draft_chapters":sum(c["editorial_status"]=="draft" for c in checked),
          "chapters":checked,
          "editorial_verdict":"This edition is NOT independently peer-reviewed or publication-certified. Automated quantitative checks cannot prove scientific correctness."}
 OUT.mkdir(parents=True,exist_ok=True)
 (OUT/"textbook_editorial_audit.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 lines=["# Rydberg textbook editorial audit","",
  "**This is a structured development backlog, not an automatic scientific approval.**",
  f"Chapters: **{len(checked)}** · Manuscript words: **{summary['total_words']:,}** · end-chapter answered questions: **{summary['total_questions']}** · chapters still below at least one target: **{summary['draft_chapters']}**.","",
  "Publication targets: ≥5,000 substantive original words, ≥12 distinct fully reasoned answers and ≥3 accurate original scientific figures per chapter, with source-linked claims and independent expert review.","",
  "| Chapter | Words | Q&A | Figures | Status |",
  "|---|---:|---:|---:|---|"]
 for c in checked:
  m=c["metrics"]
  lines.append("| "+c["path"].split("/")[-1]+" | "+str(m["words"])+" | "+str(m["answered_questions"])+" | "+str(m["figures"])+" | "+c["editorial_status"]+" |")
 lines+=["","## Highest-priority revisions",""]
 priority=sorted(checked,key=lambda x:(x["metrics"]["words"],x["metrics"]["figures"]))
 for c in priority[:15]:
  lines.append("### "+c["title"])
  lines += ["- "+x for x in c["deficits"]]
 lines+=["","## Scientific review protocol","",
  "1. Verify every numerical formula against independent physics derivations or an authoritative source.",
  "2. Confirm image/equation unit and sign conventions and figure provenance.",
  "3. Have a qualified atomic/optical/RF researcher review the appropriate sections.",
  "4. Confirm original writing, copyright, permissions and all journal/monograph metadata.",
  "5. Add meaningful advanced exercises and solutions, not repeated formula substitution.",
  "6. Re-run numerical dependencies and independent acceptance tests before release.",
  "7. Separate the general textbook from this repository's project-specific HFSS and optical results.",""]
 (OUT/"textbook_editorial_audit.md").write_text("\n".join(lines),encoding="utf-8")
 print("Editorial audit:",len(checked),"chapters",summary["total_words"],"words",summary["draft_chapters"],"drafts")
 return summary

if __name__=="__main__":
 r=run()
 # Incomplete editorial maturity is not a CI *integrity* failure. The backlog
 # stays visible for human authors; missing source files and syntax do fail.
 sys.exit(0)
