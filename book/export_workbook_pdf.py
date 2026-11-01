#!/usr/bin/env python3
"""Build an actual 1000+ page reference-and-exercise PDF with 1 problem/page."""
from pathlib import Path
from datetime import date
import json
import subprocess
import re
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parent.parent
DEST=ROOT/"book"/"dist"/"Rydberg_Systems_Engineering_1000_Worked_Problems.pdf"
W,H=A4
M=53
REG="Helvetica"
BOLD="Helvetica-Bold"

def configure():
 global REG,BOLD
 p=Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
 b=Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
 if p.exists() and b.exists():
  pdfmetrics.registerFont(TTFont("ResearchSans",str(p)))
  pdfmetrics.registerFont(TTFont("ResearchSansBold",str(b)))
  REG,BOLD="ResearchSans","ResearchSansBold"

def lines(text,size=10,bold=False):
 font=BOLD if bold else REG
 words=re.split(r"\s+",text.strip().replace("**","").replace(chr(96),""))
 out=[];row=""
 for word in words:
  try_width=pdfmetrics.stringWidth((row+" "+word).strip(),font,size)
  if row and try_width>W-2*M:
   out.append(row);row=word
  else:row=(row+" "+word).strip()
 if row:out.append(row)
 return out

def page_header(c,section):
 c.setFillColor(colors.HexColor("#0a2430"));c.rect(0,H-76,W,76,fill=1,stroke=0)
 c.setFillColor(colors.HexColor("#b6f173"));c.setFont(BOLD,11);c.drawString(M,H-38,"RYDBERG / SYSTEMS ENGINEERING")
 c.setFillColor(colors.white);c.setFont(REG,8);c.drawString(M,H-60,section[:110])
 c.setStrokeColor(colors.HexColor("#aacaba"));c.line(M,68,W-M,68)
 c.setFillColor(colors.HexColor("#49616a"));c.setFont(REG,8)
 c.drawString(M,47,"Instructional calculations; not measured or newly HFSS-computed evidence")
 c.drawRightString(W-M,47,str(c.getPageNumber()))

def draw(c,text,y,size=10,bold=False,leading=16):
 c.setFillColor(colors.HexColor("#16343e"))
 c.setFont(BOLD if bold else REG,size)
 for line in lines(text,size,bold):
  if y<89:
   c.showPage();page_header(c,"CONTINUED RESEARCH HANDBOOK");y=H-112
  c.drawString(M,y,line)
  y-=leading
 return y

def heading(c,text,y,size=17):
 y-=9
 for line in lines(text,size,True):
  if y<100:c.showPage();page_header(c,"CONTINUED CHAPTER");y=H-117
  c.setFillColor(colors.HexColor("#102c38"));c.setFont(BOLD,size);c.drawString(M,y,line)
  y-=size*1.27
 return y-12

def chapter(c,number,path):
 page_header(c,"CONCEPT CHAPTER "+str(number).zfill(2))
 y=H-109
 for raw in path.read_text(encoding="utf-8").splitlines():
  s=raw.strip()
  if not s:y-=4;continue
  if s.startswith("<") or s.startswith("---"):continue
  if s.startswith("# "):y=heading(c,s[2:],y,17)
  elif s.startswith("## "):y=heading(c,s[3:],y,12)
  else:y=draw(c,s,y,size=8.8,leading=14)
 c.showPage()

def exercise(c,x):
 page_header(c,"FULLY WORKED PROBLEM "+x["id"]+" / 1000")
 y=H-109
 y=heading(c,x["title"],y,20)
 y=draw(c,"CASE "+x["id"]+" · "+x["part"],y,11,True,18)
 y-=20
 y=heading(c,"Research question",y,12)
 y=draw(c,x["question"],y,10.5,False,18)
 y-=14
 y=heading(c,"Parameters and formula",y,12)
 y=draw(c,x["inputs"],y,10,False,17)
 y=draw(c,x["formula"],y,10,True,17)
 y-=17
 y=heading(c,"Step-by-step solution",y,12)
 y=draw(c,x["derivation"],y,10,False,17)
 y-=16
 y=heading(c,"Scientific interpretation",y,12)
 y=draw(c,x["explanation"],y,10,False,17)
 y-=18
 y=heading(c,"Red flag / diagnosis",y,12)
 y=draw(c,x["diagnostic"],y,10,False,17)
 y-=15
 y=heading(c,"Reference",y,11)
 y=draw(c,x["reference"],y,8.6,False,14)
 if y<68:raise RuntimeError("Overlong practice page "+x["id"])
 c.showPage()

def main():
 configure()
 cmd="import {generateWorkbook} from './book/workbook.mjs'; console.log(JSON.stringify(generateWorkbook()));"
 exercises=json.loads(subprocess.check_output(["node","--input-type=module","-e",cmd],cwd=ROOT,timeout=20))
 assert len(exercises)==1000 and len({x["id"] for x in exercises})==1000
 DEST.parent.mkdir(parents=True,exist_ok=True)
 c=canvas.Canvas(str(DEST),pagesize=A4,pageCompression=1)
 c.setTitle("Rydberg Systems Engineering — 1000 Worked Problems")
 c.setAuthor("Rydberg RF Sensing Research Archive")
 page_header(c,"PRINTED RESEARCH HANDBOOK")
 y=H-148
 y=heading(c,"Rydberg Systems Engineering",y,25)
 y=draw(c,"A referenced learning and numerical problem book for Rb-87 Rydberg electrometry, optical EIT, RF engineering, metasurfaces and full-Stokes inference.",y,12,False,22)
 y-=32
 y=heading(c,"24 concept chapters + 1000 solved exercises",y,16)
 y=draw(c,"Each worked example has unique parameters and a full explanation. These pages are not a 1000-page original monograph; they form an extended technical workbook and conceptual handbook.",y,11,False,20)
 y-=32
 y=draw(c,"Compiled "+date.today().isoformat()+". Source chapters, exact equations, original project evidence and references live in the companion GitHub repository.",y)
 c.showPage()
 chapters=sorted((ROOT/"book"/"chapters").glob("*.md"))
 for i,path in enumerate(chapters,1):chapter(c,i,path)
 for x in exercises:exercise(c,x)
 c.save()
 print("Generated",DEST,"chapters",len(chapters),"exercises",len(exercises))
if __name__=="__main__":main()
