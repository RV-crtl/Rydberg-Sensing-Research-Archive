#!/usr/bin/env python3
"""Independent local evaluation of time-based Australian opportunity metadata.

Never turns a stale web page into a claim of live eligibility. No network, no
secrets; suitable for routine CI and dated human-review artefacts.
"""
from datetime import date, datetime
from pathlib import Path
import json
import sys
from zoneinfo import ZoneInfo

ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/"automation/official_sources.json"
OUT=ROOT/"research_updates/opportunity_triage"
SUPPORTED={"Australia/Sydney","Australia/Brisbane","Australia/Perth","Australia/Adelaide","Australia/Canberra",None}

def classify(source,today=None):
    zone=source.get("deadlineTimezone")
    if zone not in SUPPORTED:
        raise ValueError("Unknown source deadline timezone: "+str(zone))
    if today is None:
        today=datetime.now(ZoneInfo(zone or "Australia/Sydney")).date()
    deadline=source.get("statedDeadline")
    if deadline is None:
        return {"status":"REVIEW_CURRENT_SOURCE","days":None,
                "reason":"No fixed deadline; verify current official guidelines and specific stream"}
    day=date.fromisoformat(deadline)
    remaining=(day-today).days
    if remaining<0:
        return {"status":"PAST_RECORDED_DEADLINE","days":remaining,
                "reason":"The recorded deadline has passed; a new round is not inferred"}
    if remaining==0:
        return {"status":"DEADLINE_TODAY_UNVERIFIED","days":0,
                "reason":"The advertised date is today; official time, timezone, eligibility and open status must be checked"}
    return {"status":"FUTURE_ADVERTISED_DEADLINE_UNVERIFIED","days":remaining,
            "reason":"Date is in the future, but live availability and eligibility are not guaranteed"}

def check_sources(records):
    seen=set()
    for obj in records:
        if obj["id"] in seen:raise ValueError("Duplicate official source ID: "+obj["id"])
        seen.add(obj["id"])
        if not obj.get("url","").startswith("https://"):raise ValueError("Only HTTPS official sources")
        if not obj.get("publisher") or not obj.get("eligibility"):
            raise ValueError("Source publisher and eligibility caveat required")

def generate(today=None):
    raw=json.loads(SRC.read_text(encoding="utf-8"))
    records=raw["sources"]
    check_sources(records)
    rows=[]
    for item in records:
        status=classify(item,today=today)
        rows.append({"id":item["id"],"name":item["name"],"publisher":item["publisher"],
                     "source":item["url"],"eligibility":item["eligibility"],"deadline":item["statedDeadline"],
                     "deadline_timezone":item.get("deadlineTimezone"),**status})
    return rows

def main():
    today=datetime.now(ZoneInfo("Australia/Sydney")).date()
    rows=generate(today=today)
    OUT.mkdir(parents=True,exist_ok=True)
    output=OUT/("triage_"+today.isoformat()+".json")
    output.write_text(json.dumps({"schema":1,"review_date":today.isoformat(),
        "status":"Source-metadata assessment; not verified live availability",
        "sources":rows},indent=2)+"\n",encoding="utf-8")
    for row in rows:
        print(row["status"],row["id"],row["deadline"],row["source"])
    print("Report",output)
    return 0

if __name__=="__main__":
    sys.exit(main())
