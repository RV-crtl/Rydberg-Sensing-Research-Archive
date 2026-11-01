#!/usr/bin/env python3
"""Official Australian research/Defence opportunities: review-only source monitor.

Only retrieves a fixed, reviewed list of HTTPS source URLs, never arbitrary
untrusted links. Does not submit applications, email people, award eligibility
or declare a program open from an old copy of a page. Outputs an inspectable
source report for human scientific and grant-administration review.
"""
from datetime import datetime, timezone, date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import hashlib
import json
import re
import sys

ROOT=Path(__file__).resolve().parent.parent
SEEDS=ROOT/"automation/official_sources.json"
OUT=ROOT/"research_updates/australia"
HOSTS={"www.arc.gov.au","www.minister.defence.gov.au","www.dst.defence.gov.au",
       "defencescienceinstitute.com","qdsa.au","business.gov.au"}
KEYWORDS=("quantum","rydberg","microwave","radio frequency","rf sensor","photonics",
          "grant","funding","collaboration","industry","defence","deadline",
          "applications","sensing","partnership","closes","open","research")

class Reader(HTMLParser):
 def __init__(self):
  super().__init__()
  self.skip=0
  self.buff=[]
  self.title=[]
  self.intitle=False
 def handle_starttag(self,tag,attrs):
  if tag in ("script","style","noscript"): self.skip+=1
  if tag=="title": self.intitle=True
  if tag in ("p","h1","h2","h3","li","div"):self.buff.append(" ")
 def handle_endtag(self,tag):
  if tag in ("script","style","noscript") and self.skip>0:self.skip-=1
  if tag=="title":self.intitle=False
  if tag in ("p","h1","h2","h3","li","div"):self.buff.append("\n")
 def handle_data(self,text):
  if self.skip:return
  self.buff.append(text)
  if self.intitle:self.title.append(text)

def normalize(text):
 return re.sub(r"\s+"," ",text).strip()

def parse_highlights(html):
 parser=Reader()
 parser.feed(html)
 title=normalize("".join(parser.title))
 paragraphs=[normalize(x) for x in "".join(parser.buff).split("\n")]
 unique=[]
 for p in paragraphs:
  low=p.casefold()
  if 45 <= len(p) <= 600 and any(k in low for k in KEYWORDS):
   if p not in unique:unique.append(p)
 return title,unique[:12]

def get_source(src):
 u=src["url"]
 parsed=urlparse(u)
 if parsed.scheme!="https" or parsed.hostname not in HOSTS or parsed.username or parsed.password:
  raise ValueError("Source not allowed: "+u)
 request=Request(u,headers={"User-Agent":"Rydberg-Research-Archive/1.0 official Australian R&D funding review",
                           "Accept":"text/html"})
 with urlopen(request,timeout=25) as response:
  redirected=urlparse(response.geturl())
  if redirected.scheme!="https" or redirected.hostname not in HOSTS:
   raise ValueError("Unexpected redirect destination: "+response.geturl())
  body=response.read(1100000)
  modified=response.headers.get("Last-Modified","")
 text=body.decode("utf-8",errors="replace")
 title,highlights=parse_highlights(text)
 return {"title":title or src["name"],"highlights":highlights,
         "last_modified_header":modified,"html_sha256":hashlib.sha256(body).hexdigest()}

def deadline_interpretation(src,today):
 if not src.get("statedDeadline"):
  return "No single deadline in seed; inspect the official source for current rounds."
 dt=date.fromisoformat(src["statedDeadline"])
 if dt<today:return "Historical advertised deadline passed; a new round must be independently verified."
 if dt==today:return "Advertised deadline today. Verify closure hour, timezone and eligibility immediately."
 return "Advertised deadline in "+str((dt-today).days)+" day(s); verify current official guidelines and any amendments."

def report(sources,fetch,today):
 lines=["# Australian Rydberg/quantum opportunities — "+today.isoformat(),"",
  "**Official-source review shortlist, not an eligibility determination or evidence that a grant is presently open.**",
  "Organisations, call dates and program terms can change; always read the latest official page.",
  "No applications or collaboration approaches are generated automatically.",""]
 for s in sources:
  result=fetch.get(s["id"],{})
  lines+=["## "+s["id"]+" — "+s["name"],"",
     "- **Publisher:** "+s["publisher"]+"; **type:** "+s["type"],
     "- **Official source:** "+s["url"],
     "- **Previously reviewed status:** "+s["sourceStatus"]+" (seed last reviewed 2026-11-01).",
     "- **Date rule:** "+deadline_interpretation(s,today),
     "- **Eligibility caveat:** "+s["eligibility"],
     "- **Collaborative relevance:** "+", ".join(s["tags"]),
     "- **Live retrieval:** "+result.get("state","not attempted")]
  if result.get("title"):lines.append("- **Current page title:** "+result["title"])
  if result.get("last_modified_header"):lines.append("- **Server Last-Modified:** "+result["last_modified_header"])
  if result.get("html_sha256"):lines.append("- **Retrieved response digest:** SHA-256 "+result["html_sha256"])
  if result.get("highlights"):
   lines+=["","### Verbatim on-page context (short excerpts; verify before using)",""]
   lines +=["> "+h[:200] for h in result["highlights"][:3]]
  if result.get("error"):lines.append("- **Retrieval issue:** "+result["error"])
  lines.append("")
 lines+=["## Researcher's next actions","",
         "1. Verify source publication/update time and whether the call is open in its own timezone.",
         "2. Check applicant career stage, institute, citizenship/security/IP requirements and partner organisations.",
         "3. Assess a concrete collaborative research work package, deliverables, evidence maturity and resources.",
         "4. Obtain supervisor/institutional approval before sending any proposal or Defence-relevant technical detail.",
         "5. Keep public and restricted lab material separated; do not paste sensitive design files into issues.",""]
 return "\n".join(lines)

def run(fetch_remote=True,today=None):
 today=today or datetime.now(timezone.utc).date()
 sources=json.loads(SEEDS.read_text(encoding="utf-8"))["sources"]
 result={}
 for s in sources:
  try:
   data=get_source(s) if fetch_remote else {"title":s["name"],"highlights":[]}
   result[s["id"]]={"state":"retrieved" if fetch_remote else "offline fixture",**data}
  except Exception as exc:
   result[s["id"]]={"state":"retrieval failed","error":type(exc).__name__+": "+str(exc)[:140]}
 OUT.mkdir(parents=True,exist_ok=True)
 p=OUT/("opportunities_"+today.isoformat()+".md")
 p.write_text(report(sources,result,today),encoding="utf-8")
 data=OUT/("opportunities_"+today.isoformat()+".json")
 data.write_text(json.dumps({"schema":1,"fetched_utc":datetime.now(timezone.utc).isoformat(),
                             "entries":result},indent=2)+"\n",encoding="utf-8")
 n=sum(item.get("state")=="retrieved" for item in result.values())
 print("Official-source retrievals:",n,"/",len(sources),"report:",p)
 return 0 if n>0 or not fetch_remote else 1

if __name__=="__main__":
 sys.exit(run(fetch_remote="--offline" not in sys.argv))
