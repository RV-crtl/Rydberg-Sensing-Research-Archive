import {resolveBookLink,resolveBookAsset} from "./academy-links.mjs";
import {generateWorkbook,getBookMetrics} from "./workbook.mjs";
const $=id=>document.getElementById(id),repo="https://github.com/RV-crtl/Rydberg-Sensing-Research-Archive";
let chapters=[],questions=generateWorkbook(),mode="chapters",index=0;
const mk=(tag,value,cls)=>{const z=document.createElement(tag);if(value!==undefined)z.textContent=value;if(cls)z.className=cls;return z;};
function inline(parent,line){
 const rx=/(\*\*[^*]+\*\*|\x60[^\x60]+\x60|\[[^\]]+\]\([^)]+\))/g;let c=0,m;
 while((m=rx.exec(line))){
  if(m.index>c)parent.append(document.createTextNode(line.slice(c,m.index)));
  const part=m[0];
  if(part.startsWith("**"))parent.append(mk("strong",part.slice(2,-2)));
  else if(part.charCodeAt(0)===96)parent.append(mk("code",part.slice(1,-1)));
  else {const r=part.match(/^\[([^\]]+)\]\(([^)]+)\)$/),a=mk("a",r[1]);const url=r[2];
   try{a.href=resolveBookLink(url);a.target="_blank";a.rel="noopener noreferrer";parent.append(a);}
   catch(e){parent.append(document.createTextNode(r[1]+" (source link rejected)"));}
  }c=rx.lastIndex;
 }if(c<line.length)parent.append(document.createTextNode(line.slice(c)));
}
function renderMarkdown(body,raw){
 const lines=raw.split(/\r?\n/);let inCode=false,code=[],list=null,details=null;
 const append=el=>(details||body).append(el);
 const flush=()=>{if(code.length){const p=mk("pre");p.append(mk("code",code.join("\n")));append(p);code=[];}};
 for(const original of lines){const s=original.trim();
  if(s.startsWith(String.fromCharCode(96).repeat(3))){if(inCode)flush();inCode=!inCode;continue;}
  if(inCode){code.push(original);continue;}
  if(!s){list=null;continue;}
  if(s==="<details>"){details=mk("details");body.append(details);continue;}
  if(s==="</details>"){details=null;continue;}
  if(s.startsWith("<summary>")){append(mk("summary",s.replace(/<\/?summary>/g,"")));continue;}
  if(s.startsWith("![")){
   const match=s.match(/^!\[([^\]]+)\]\(([^)]+)\)$/);
   if(match){try{
     const figure=mk("figure",undefined,"book-science-figure"),img=mk("img");
     img.src=resolveBookAsset(match[2]);img.alt=match[1];img.loading="lazy";img.decoding="async";
     figure.append(img,mk("figcaption",match[1]));append(figure);continue;
   }catch(e){append(mk("p","Unavailable figure: "+match[1]));continue;}}
  }

  const h=s.match(/^(#{1,5})\s+(.+)$/);if(h){list=null;let el=mk("h"+Math.min(3,h[1].length));inline(el,h[2]);append(el);continue;}
  if(s.startsWith("- ")){if(!list){list=mk("ul");append(list);}const li=mk("li");inline(li,s.slice(2));list.append(li);continue;}
  if(s==="---"){append(mk("hr"));continue;}
  const p=mk("p",undefined,s.startsWith(">")?"study-note":"");inline(p,s.startsWith(">")?s.slice(1).trim():s);append(p);
 }flush();
}
function makeChapter(data,i){
 const root=$("reading-panel");root.replaceChildren(mk("span",data.section.toUpperCase(),"chapter-flag"));
 renderMarkdown(root,data.markdown);
 $("reading-path").textContent="BOOK / CHAPTER "+String(i+1).padStart(2,"0");
 $("reading-status").textContent="Source-linked educational text • not a laboratory record";
 $("page-state").textContent=(i+1)+" / "+chapters.length+" chapters";
 $("prev-page").disabled=i===0;$("next-page").disabled=i===chapters.length-1;document.title=data.title+" · Rydberg Academy";
}
function makeQuestion(q,i){
 const root=$("reading-panel");root.replaceChildren(mk("span","WORKED PROBLEM / "+q.part.toUpperCase(),"chapter-flag"),mk("h1",q.title),mk("p",q.question));
 const st=mk("div",undefined,"problem-stat");st.append(mk("span","Exercise "+q.id+" / 1000"),mk("span",q.family.replaceAll("-"," ")));
 root.append(st,mk("div",q.formula,"problem-equation"),mk("h2","Solve before revealing"),mk("p","Given: "+q.inputs));
 const d=mk("details");d.append(mk("summary","Reveal complete solution and interpretation"),mk("p",q.derivation,"problem-answer"),mk("p",q.explanation));
 root.append(d,mk("h2","Engineering diagnosis"),mk("p",q.diagnostic),mk("div","Reference: "+q.reference,"study-note"));
 $("reading-path").textContent="PRACTICE / "+q.family.toUpperCase();
 $("reading-status").textContent="Deterministic numerical teaching example";
 $("page-state").textContent=(i+1)+" / 1,000 worked exercises";
 $("prev-page").disabled=i===0;$("next-page").disabled=i===questions.length-1;document.title=q.title+" · "+q.id+" · Rydberg Academy";
}
function route(){
 const v=decodeURIComponent(location.hash.slice(1));
 if(v.startsWith("practice/")){const id=v.split("/")[1];const j=questions.findIndex(x=>x.id===id);mode="practice";index=j>=0?j:0;}
 else{const id=v.startsWith("chapter/")?v.split("/")[1]:chapters[0].slug;const j=chapters.findIndex(c=>c.slug===id);mode="chapters";index=j>=0?j:0;}
 document.querySelectorAll("[data-mode]").forEach(b=>{let active=b.dataset.mode===mode;b.classList.toggle("active",active);b.setAttribute("aria-pressed",String(active));});
 renderMenu();if(mode==="practice")makeQuestion(questions[index],index);else makeChapter(chapters[index],index);
}
function go(offset){const a=mode==="chapters"?chapters:questions,j=Math.max(0,Math.min(a.length-1,index+offset));location.hash=mode==="chapters"?"chapter/"+a[j].slug:"practice/"+a[j].id;}
function renderMenu(){
 const root=$("chapter-list"),q=$("chapter-search").value.toLocaleLowerCase().trim();root.replaceChildren();const items=mode==="chapters"?chapters:questions;
 let group=null,n=0;
 for(let i=0;i<items.length;i++){if(n>=100)break;let obj=items[i],label=mode==="chapters"?obj.title:obj.title+" · "+obj.id;
  if(q&&!((label+" "+(obj.section||obj.part)+" "+(obj.markdown||"").slice(0,800)).toLocaleLowerCase().includes(q)))continue;
  let g=mode==="chapters"?obj.section:obj.part;if(g!==group){root.append(mk("div",g,"book-part"));group=g;}
  let link=mk("a",(mode==="chapters"?String(i+1).padStart(2,"0")+" / ":"")+label);link.href="#"+(mode==="chapters"?"chapter/"+obj.slug:"practice/"+obj.id);link.classList.toggle("active",i===index);root.append(link);n++;
 }
 if(!n)root.append(mk("p","No matches. Try EIT, Rydberg, photon, polarisation or RF."));
 if(mode==="practice")root.append(mk("p","Showing at most 100 matches. Use search to locate more.", "study-note"));
}
async function start(){
 const metaResponse=await fetch("./data/book-catalog.json");if(!metaResponse.ok)throw Error("Cannot load source-verified curriculum");const meta=await metaResponse.json();
 if(meta.schema!==2||!Array.isArray(meta.parts)||!meta.parts.length)throw Error("Invalid Academy catalog");
 const rs=await Promise.all(meta.parts.map(async name=>{const r=await fetch("./data/"+name);if(!r.ok)throw Error("Unable to load "+name+" ("+r.status+")");return r.json();}));
 chapters=rs.flat();if(chapters.length!==meta.chapterCount||chapters.length<24)throw Error("Textbook chapter inventory out of sync");
 const count=document.getElementById("chapter-total");if(count)count.textContent=chapters.length+" reference chapters";
 let m=getBookMetrics();if(m.exercises!==1000||m.uniqueIds!==1000)throw Error("Workbook check failed");
 document.querySelectorAll("[data-mode]").forEach(b=>b.addEventListener("click",()=>{$("chapter-search").value="";location.hash=b.dataset.mode==="chapters"?"chapter/"+chapters[0].slug:"practice/0001";}));
 $("chapter-search").addEventListener("input",renderMenu);
 $("prev-page").addEventListener("click",()=>go(-1));
 $("next-page").addEventListener("click",()=>go(1));
 window.addEventListener("hashchange",route);route();
}
start().catch(err=>{$("reading-panel").replaceChildren(mk("h2","Could not load this handbook"),mk("p",err.message+". Serve the site via a local HTTP server or read Markdown on GitHub."));console.error(err);});
