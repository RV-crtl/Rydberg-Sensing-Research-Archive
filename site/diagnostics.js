const $=id=>document.getElementById(id),GH="https://github.com/RV-crtl/Rydberg-Sensing-Research-Archive/blob/main/";
let tasks=[],active=0,done={};
function elem(tag,text,cls){const x=document.createElement(tag);if(text!==undefined)x.textContent=text;if(cls)x.className=cls;return x;}
function srcLink(path){
 const a=elem("a","Open underlying source ↗");
 a.href=GH+path.replace(/^(\.\.\/)+/,"");a.target="_blank";a.rel="noopener noreferrer";return a;
}
function redrawMenu(){
 const q=$("diagnose-search").value.toLowerCase(),root=$("diagnose-menu");root.replaceChildren();
 tasks.forEach((t,i)=>{if(!((t.title+" "+t.group+" "+t.symptom).toLowerCase().includes(q)))return;
 const b=elem("button",t.id+" · "+t.title,i===active?"active":"");b.type="button";
 b.addEventListener("click",()=>{active=i;redrawMenu();redrawPanel();});root.append(b);
 });if(!root.children.length)root.append(elem("p","No matching symptom. Try a broader keyword."));
}
function exportRecord(){
 const t=tasks[active],checked=(done[t.id]||{}),row={
  schema:1,record:"Rydberg scientific troubleshooting worksheet",
  generated_utc:new Date().toISOString(),source_date:"2026-11-01",issue:t.id,
  symptom:t.title,steps:t.checks.map((value,i)=>({step:i+1,check:value,performed:!!checked[i]})),
  status:"Educational checklist only — no evidence of a passing experimental measurement",
  source:t.source,acceptance:t.acceptance};
 const blob=new Blob([JSON.stringify(row,null,2)+"\n"],{type:"application/json"});
 const url=URL.createObjectURL(blob),link=elem("a");link.href=url;link.download="rydberg-diagnostic-"+t.id+".json";
 link.click();setTimeout(()=>URL.revokeObjectURL(url),500);
}
function redrawPanel(){
 const t=tasks[active],root=$("diagnose-panel");root.replaceChildren();
 const pre=elem("span",t.id+" / "+t.group.toUpperCase(),"eyebrow"),heading=elem("h2",t.title),symptom=elem("p",t.symptom);
 root.append(pre,heading,symptom,elem("h3","Evidence checks to complete"));
 const steps=elem("div",undefined,"diagnose-checks"),checks=done[t.id]||{};
 t.checks.forEach((txt,i)=>{
  const l=elem("label"),c=elem("input");c.type="checkbox";c.checked=!!checks[i];
  c.addEventListener("change",()=>{(done[t.id]??={})[i]=c.checked;update();});l.append(c,elem("span",(i+1)+". "+txt));steps.append(l);
 });
 root.append(steps);
 const progress=elem("div",undefined,"diagnose-progress"),fill=elem("div");fill.id="diagnose-fill";progress.append(fill);
 const label=elem("p");label.id="diagnose-counter";root.append(progress,label);
 const actions=elem("div",undefined,"diagnose-actions"),exportButton=elem("button","Export diagnostic worksheet");
 exportButton.addEventListener("click",exportRecord);
 const reset=elem("button","Reset checks","outline");reset.addEventListener("click",()=>{done[t.id]={};redrawPanel();});
 actions.append(exportButton,reset);root.append(actions);
 const final=elem("div",undefined,"report-ready");final.append(elem("strong","Acceptance gate"),elem("p",t.acceptance),srcLink(t.source));root.append(final);
 root.append(elem("p","Marked checks mean reviewed, not verified passed. Preserve instrument settings, raw data, run IDs and signatures independently.","hint"));
 function update(){
  const count=Object.values(done[t.id]||{}).filter(Boolean).length;
  fill.style.width=(100*count/t.checks.length)+"%";
  label.textContent=count+" / "+t.checks.length+" diagnostic checks marked as reviewed";
 }
 update();
}
async function boot(){
 const r=await fetch("./data/diagnostic-playbooks.json");if(!r.ok)throw Error("Diagnostic knowledge base HTTP "+r.status);
 const data=await r.json();
 if(data.schema!==1||data.playbooks.length<10||data.playbooks.some(x=>x.checks.length<4))throw Error("Invalid diagnostic playbook data");
 tasks=data.playbooks;$("diagnose-search").addEventListener("input",redrawMenu);redrawMenu();redrawPanel();
}
boot().catch(e=>{$("diagnose-panel").replaceChildren(elem("h2","Error loading evidence checks"),elem("p",e.message));});
