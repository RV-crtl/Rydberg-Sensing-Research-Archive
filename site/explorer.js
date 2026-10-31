import {stokesFromAngles,matrixResponses,improvementPercent,filterFiles,githubFileUrl,validateAtlas,rank} from "./model.mjs";
const byId=id=>document.getElementById(id);
const svgNS="http://www.w3.org/2000/svg";
let model=null,sourceFiles=[],allTimeline=[],historicalRecords=[],sourceScope="tracked",activeGroup="All",activeTimeline="All",visible=16,yaw=-0.45,pitch=0.38,psi=0,chi=0;
const presets={H:[0,0],V:[90,0],D:[45,0],A:[-45,0],R:[0,45],L:[0,-45]};
function el(tag,cls,text){const e=document.createElement(tag);if(cls)e.className=cls;if(text!==undefined)e.textContent=text;return e;}
function svg(name,attrs){const e=document.createElementNS(svgNS,name);for(const [k,v] of Object.entries(attrs))e.setAttribute(k,String(v));return e;}
function project(x,y,z){const x2=x*Math.cos(yaw)-z*Math.sin(yaw),z2=x*Math.sin(yaw)+z*Math.cos(yaw);return [220+154*x2,220-154*(y*Math.cos(pitch)-z2*Math.sin(pitch))];}
function line(g,a,b,color,width=1,opacity=0.6){const p=project(...a),q=project(...b);g.append(svg("line",{x1:p[0],y1:p[1],x2:q[0],y2:q[1],stroke:color,"stroke-width":width,opacity}));}
function drawSphere(s){
 const root=byId("sphere");root.replaceChildren();
 root.append(svg("circle",{cx:220,cy:220,r:154,fill:"#0a2731",stroke:"#63878b","stroke-width":1.4}));
 const g=svg("g",{});
 for(const plane of ["xy","xz","yz"])for(let i=0;i<72;i++){
  const a=i*2*Math.PI/72,b=(i+1)*2*Math.PI/72;
  const f=t=>plane==="xy"?[Math.cos(t),Math.sin(t),0]:plane==="xz"?[Math.cos(t),0,Math.sin(t)]:[0,Math.cos(t),Math.sin(t)];
  line(g,f(a),f(b),plane==="xy"?"#5b8d99":"#46636e",0.85,0.47);
 }
 root.append(g);
 const axes=[[[1,0,0],"S1","#b6f173"],[[0,1,0],"S2","#75cde0"],[[0,0,1],"S3","#eeb98a"]];
 for(const [v,label,color] of axes){
  line(root,v.map(x=>-x),v,color,1.7,.85);
  const [px,py]=project(...v),text=svg("text",{x:px,y:py-9,fill:color,"font-size":16,"text-anchor":"middle","font-weight":700});
  text.textContent=label;root.append(text);
 }
 const p=project(s[1],s[2],s[3]);
 line(root,[0,0,0],[s[1],s[2],s[3]],"#edffb5",4,1);
 root.append(svg("circle",{cx:p[0],cy:p[1],r:9,fill:"#c2ff82",stroke:"#09212b","stroke-width":3}));
 byId("vector-label").textContent="S = ["+s.map(n=>n.toFixed(2)).join(", ")+"]";
}
function calculate(){
 const stokes=stokesFromAngles(psi,chi);
 byId("azimuth-value").textContent=psi+"°";byId("ellipticity-value").textContent=chi+"°";
 byId("stokes-values").replaceChildren(...stokes.map((v,i)=>{const d=el("div","sbox");d.append(el("b","",v.toFixed(3)),el("small","","S"+i));return d;}));
 drawSphere(stokes);
 const v=matrixResponses(model.rows,stokes),scale=Math.max(0.0001,...v.map(Math.abs));
 const track=byId("response-bars");track.replaceChildren();
 v.forEach((n,i)=>{const r=el("div","barline"),label=el("span","","M"+model.maskOrder[i]),bar=el("div","bar-track"),fill=el("div","bar-fill");
  fill.style.width=(Math.abs(n)/scale*100).toFixed(2)+"%";if(n<0)fill.style.background="linear-gradient(90deg,#bb6a6a,#dfa785)";bar.append(fill);
  r.append(label,bar,el("span","",n.toFixed(5)));track.append(r);
 });
 byId("rank-label").textContent=rank(model.rows);
 byId("dwell-criterion").textContent=improvementPercent(model.dwell.equalTrace,model.dwell.optimizedTrace).toFixed(1)+"%";
 document.querySelectorAll("[data-preset]").forEach(b=>b.classList.toggle("active",Math.abs(Number(b.dataset.az??999)-psi)<1e-6&&Math.abs(Number(b.dataset.ch??999)-chi)<1e-6));
}
function setAngles(p,c){psi=Number(p);chi=Number(c);byId("azimuth").value=psi;byId("ellipticity").value=chi;calculate();}
function exportCsv(){
 const s=stokesFromAngles(psi,chi),responses=matrixResponses(model.rows,s);
 const head="state,mask,S0,S1,S2,S3,model_linear_response,source_frequency_GHz,model_classification";
 const rows=responses.map((v,i)=>[i+1,model.maskOrder[i],...s.map(n=>n.toPrecision(12)),v.toPrecision(12),model.frequencyGHz,"HFSS-derived offline linear model"].join(","));
 const file=new Blob([[head,...rows].join("\r\n")+"\r\n"],{type:"text/csv;charset=utf-8"}),url=URL.createObjectURL(file);
 const a=el("a");a.href=url;a.download="rydberg_stokes_linear_model.csv";a.click();URL.revokeObjectURL(url);
}
function renderMatrix(){
 const root=byId("matrix-grid"),table=el("table","matrix-table"),head=el("thead"),hrow=el("tr");
 for(const label of ["Mask","S0","S1","S2","S3"])hrow.append(el("th","",label));
 head.append(hrow);table.append(head);const body=el("tbody");
 const limit=Math.max(...model.rows.flat().map(Math.abs));
 model.rows.forEach((row,i)=>{const tr=el("tr");tr.append(el("th","","M"+model.maskOrder[i]));
  row.forEach(v=>{const td=el("td","",v.toFixed(6));td.style.backgroundColor=v<0?"rgba(223,128,130,"+(0.08+0.50*Math.abs(v)/limit).toFixed(3)+")":"rgba(182,241,115,"+(0.04+0.38*Math.abs(v)/limit).toFixed(3)+")";tr.append(td);});body.append(tr);});
 table.append(body);root.replaceChildren(table);
}
function renderTimeline(){
 const list=byId("history-list");list.replaceChildren();
 allTimeline.filter(t=>activeTimeline==="All"||t.group===activeTimeline).forEach(t=>{
  const li=el("li"),time=el("time","",t.date);time.dateTime=t.date;
  const div=el("div");div.append(el("small","",t.group),el("h3","",t.title),el("p","",t.description));
  const a=el("a","","Read source ↗");a.href=githubFileUrl(t.path);a.rel="noopener noreferrer";div.append(a);
  li.append(time,div);list.append(li);
 });
 document.querySelectorAll("[data-timeline-filter]").forEach(b=>{const on=b.dataset.timelineFilter===activeTimeline;b.classList.toggle("chosen",on);b.setAttribute("aria-pressed",String(on));});
}
function renderFiles(){
 const q=byId("source-query").value.toLocaleLowerCase().trim(),historic=sourceScope==="historical";
 const matches=historic?historicalRecords.filter(f=>(f.n+" "+f.d+" "+f.batch).toLocaleLowerCase().includes(q)):filterFiles(sourceFiles,q,activeGroup);
 byId("result-count").textContent=matches.length+" matching "+(historic?"historical source records (discovery only)":"tracked GitHub files");
 const root=byId("file-results");root.replaceChildren();
 for(const f of matches.slice(0,visible)){
  const card=el("article","file-result");
  if(historic){
   card.append(el("span","group","Library discovery · batch "+f.batch));
   card.append(el("h3","name",f.n),el("div","meta","Library record date: "+f.d+" · not verified as a committed source"));
   const row=el("div","rowend");row.append(el("span","",new Intl.NumberFormat().format(f.b)+" bytes"));
   const a=el("a","","Open source catalogue ↗");a.href=githubFileUrl("docs/catalog/HISTORICAL_SOURCE_INDEX_BATCH_"+f.batch+".csv");a.rel="noopener noreferrer";row.append(a);card.append(row);
  }else{
   card.append(el("span","group",f.g),el("h3","name",f.p.split("/").at(-1)),el("div","meta",f.p));
   const row=el("div","rowend");row.append(el("span","",new Intl.NumberFormat().format(f.bytes)+" bytes"));
   const a=el("a","","Open in GitHub ↗");a.href=githubFileUrl(f.p);a.rel="noopener noreferrer";row.append(a);card.append(row);
  }
  root.append(card);
 }
 if(!matches.length)root.append(el("p","hint","No matches. Try another keyword or switch research source scope."));
 const more=byId("show-more");more.hidden=matches.length<=visible;more.textContent="Show more ("+(matches.length-visible)+" remaining)";
}
function init(){
 const cats=["All",...new Set(sourceFiles.map(f=>f.g))].sort((a,b)=>a==="All"?-1:b==="All"?1:a.localeCompare(b));
 const filterBar=byId("inventory-filters");
 document.querySelectorAll("[data-scope]").forEach(b=>b.addEventListener("click",()=>{sourceScope=b.dataset.scope;visible=16;document.querySelectorAll("[data-scope]").forEach(x=>{const on=x===b;x.classList.toggle("chosen",on);x.setAttribute("aria-pressed",String(on));});filterBar.hidden=sourceScope==="historical";byId("scope-description").textContent=sourceScope==="historical"?"Historical Library records are filenames and sizes only: not checked-in artefacts, measurements or proof of simulation completion. Open the associated catalogue in GitHub to locate an original.":"Showing files physically tracked in GitHub in the indexed repository snapshot.";renderFiles();}));
 cats.forEach(cat=>{const b=el("button",cat==="All"?"chosen":"",cat);b.type="button";b.setAttribute("aria-pressed",String(cat==="All"));b.addEventListener("click",()=>{activeGroup=cat;visible=16;filterBar.querySelectorAll("button").forEach(c=>{let on=c===b;c.classList.toggle("chosen",on);c.setAttribute("aria-pressed",String(on));});renderFiles();});filterBar.append(b);});
 byId("source-query").addEventListener("input",()=>{visible=16;renderFiles();});
 byId("clear-query").addEventListener("click",()=>{byId("source-query").value="";visible=16;renderFiles();byId("source-query").focus();});
 byId("show-more").addEventListener("click",()=>{visible+=20;renderFiles();});
 document.addEventListener("keydown",e=>{if(e.key==="/"&&!["INPUT","TEXTAREA"].includes(document.activeElement.tagName)){e.preventDefault();byId("source-query").focus();}});
 byId("azimuth").addEventListener("input",e=>setAngles(e.target.value,chi));
 byId("ellipticity").addEventListener("input",e=>setAngles(psi,e.target.value));
 document.querySelectorAll("[data-preset]").forEach(b=>{const [p,c]=presets[b.dataset.preset];b.dataset.az=p;b.dataset.ch=c;b.addEventListener("click",()=>setAngles(p,c));});
 byId("rotate-left").addEventListener("click",()=>{yaw-=Math.PI/12;calculate();});
 byId("rotate-right").addEventListener("click",()=>{yaw+=Math.PI/12;calculate();});
 byId("reset-state").addEventListener("click",()=>setAngles(0,0));
 byId("export-response").addEventListener("click",exportCsv);
 let lastX=null;const sphere=byId("sphere");
 sphere.addEventListener("pointerdown",e=>{lastX=e.clientX;sphere.setPointerCapture(e.pointerId);});
 sphere.addEventListener("pointermove",e=>{if(lastX===null)return;const d=e.clientX-lastX;lastX=e.clientX;yaw+=d/190;calculate();});
 for(const event of ["pointerup","pointercancel"])sphere.addEventListener(event,()=>{lastX=null;});
 document.querySelectorAll("[data-timeline-filter]").forEach(b=>b.addEventListener("click",()=>{activeTimeline=b.dataset.timelineFilter;renderTimeline();}));
 renderMatrix();calculate();renderTimeline();renderFiles();
}
try{
 const [response,historicalResponse]=await Promise.all([fetch("./data/research-atlas.json",{cache:"no-store"}),fetch("./data/historical-index.json",{cache:"no-store"})]);
 if(!response.ok || !historicalResponse.ok)throw new Error("HTTP source "+response.status+" / history "+historicalResponse.status);
 const data=await response.json(),history=await historicalResponse.json();validateAtlas(data);
 if(history.schema!==1 || history.status!=="discovery-only" || !Array.isArray(history.records))throw new Error("Invalid historical inventory");
 model=data.matrix;sourceFiles=data.files;allTimeline=data.timeline;historicalRecords=history.records;const counter=byId('tracked-file-total');if(counter)counter.textContent=sourceFiles.length;init();
}catch(error){
 for(const id of ["response-bars","file-results","history-list"]){const p=el("p","hint","Research source data could not be loaded: "+error.message+". Serve the site using an HTTP server or visit GitHub.");byId(id)?.replaceChildren(p);}
 console.error("Research explorer source load:",error);
}
