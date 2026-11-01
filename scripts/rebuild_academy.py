#!/usr/bin/env python3
"""Build the standalone Academy search/reading datasets from canonical Markdown.

This is the only supported source of the website chapter JSON. Existing research
archive content remains separately under docs/, evidence/, history/ and papers/.
Runs offline with stdlib, deterministic order and a no-change validation mode.
"""
from pathlib import Path
import argparse
import json
import re
import sys

ROOT=Path(__file__).resolve().parent.parent
CHAPTERS=ROOT/"book/chapters"
DATA=ROOT/"site/data"
CATALOG=DATA/"book-catalog.json"
PART_SIZE=12

def classify(num):
 if num<=4:return "Quantum foundations"
 if num<=8:return "Atomic structure and coherent spectroscopy"
 if num<=12:return "Optics, RF and polarimetry"
 if num<=17:return "Numerical atomic science and diagnosis"
 if num<=24:return "Measurement engineering and research methods"
 if num<=28:return "Rydberg interactions and quantum platforms"
 if num<=32:return "Metrology, many-body and detection"
 return "Laser systems, research design and new frontiers"

def build():
 chapters=sorted(CHAPTERS.glob("[0-9][0-9]-*.md"),key=lambda p:p.name)
 results=[]
 for path in chapters:
  slug=path.stem
  num=int(slug[:2])
  body=path.read_text(encoding="utf-8")
  first=body.splitlines()[0].strip()
  if not first.startswith("# "):raise ValueError("No H1 title: "+str(path))
  answers=len(re.findall(r"<details>",body))
  words=len(re.findall(r"\b[\w]+(?:[-'][\w]+)*\b",body))
  results.append({"slug":slug,"title":first[2:],"section":classify(num),
                  "words":words,"answers":answers,"markdown":body})
 if not results or len(set(c["slug"] for c in results))!=len(results):
  raise ValueError("Duplicate/empty chapter collection")
 parts=[results[i:i+PART_SIZE] for i in range(0,len(results),PART_SIZE)]
 outputs={}
 for i,part in enumerate(parts,1):
  outputs[DATA/f"book-part{i}.json"]=json.dumps(part,ensure_ascii=False,indent=2)+"\n"
 catalog={"schema":2,"chapterCount":len(results),"sourceOfTruth":"book/chapters/",
          "parts":[f"book-part{i}.json" for i in range(1,len(parts)+1)],
          "totalWords":sum(x["words"] for x in results),
          "totalAnswers":sum(x["answers"] for x in results),
          "chapterSummaries":[{k:r[k] for k in ("slug","title","section","words","answers")} for r in results]}
 outputs[CATALOG]=json.dumps(catalog,ensure_ascii=False,indent=2)+"\n"
 return outputs,catalog

def main():
 a=argparse.ArgumentParser()
 a.add_argument("--check",action="store_true")
 opts=a.parse_args()
 outputs,cat=build()
 for path,content in outputs.items():
  if opts.check:
   if not path.exists() or path.read_text(encoding="utf-8")!=content:
    print("STALE BOOK SITE EXPORT:",path)
    return 1
  else:path.write_text(content,encoding="utf-8")
 print(("PASS" if opts.check else "BUILT"),
       cat["chapterCount"],"textbook chapters;",
       cat["totalWords"],"words;",
       cat["totalAnswers"],"question-answer reveal blocks")
 return 0

if __name__=="__main__":sys.exit(main())
