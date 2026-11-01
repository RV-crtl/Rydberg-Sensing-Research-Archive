const $=id=>document.getElementById(id);
const C=299792458,H=6.62607015e-34,E=1.602176634e-19,A0=5.29177210903e-11;
const label=(id,val)=>$(id).textContent=val;
const complex=(re,im=0)=>({re,im});
const add=(a,b)=>complex(a.re+b.re,a.im+b.im);
const inv=a=>{const d=a.re*a.re+a.im*a.im;if(!(d>0))throw Error("Singular complex susceptibility");return complex(a.re/d,-a.im/d);};
const scale=(a,s)=>complex(a.re*s,a.im*s);
const div=(x,y)=>scale(inv(y),x);
function relativeAbsorption(delta,oc,orf,ge,gr){
 // Simplified weak-probe four-level nested model. All parameters are
 // equivalent frequency units in MHz; no thermally averaged observables.
 const gs=Math.max(0.2,gr*1.2);
 const Ds=complex(gs,-delta);
 const Dr=add(complex(gr,-delta),div(orf*orf/4,Ds));
 const De=add(complex(ge,-delta),div(oc*oc/4,Dr));
 const amp=ge*inv(De).re;
 return Math.max(0,amp);
}
function drawCurve(){
 const oc=+$("rabi-control").value,orf=+$("rf-control").value,ge=+$("linewidth-control").value,gr=+$("rwidth-control").value;
 label("rabi-value",oc.toFixed(1)+" MHz");label("rf-value",orf.toFixed(1)+" MHz");
 label("linewidth-value",ge.toFixed(2)+" MHz");label("rwidth-value",gr.toFixed(2)+" MHz");
 const N=320,pts=Array.from({length:N+1},(_,i)=>({x:-25+i*50/N,y:relativeAbsorption(-25+i*50/N,oc,orf,ge,gr)}));
 const s=$("eit-chart");s.replaceChildren();const ns="http://www.w3.org/2000/svg";
 const make=(tag,attrs)=>{const x=document.createElementNS(ns,tag);for(let [k,v] of Object.entries(attrs))x.setAttribute(k,String(v));return x;};
 const plot={left:65,right:715,top:40,bottom:340},max=Math.max(1,...pts.map(p=>p.y));
 for(let v=0;v<=5;v++){
  const y=plot.bottom-v*(plot.bottom-plot.top)/5;
  s.append(make("line",{x1:plot.left,y1:y,x2:plot.right,y2:y,stroke:"#335361","stroke-dasharray":"3 6"}));
  let t=make("text",{x:plot.left-12,y:y+4,fill:"#b0c8ca","font-size":12,"text-anchor":"end"});t.textContent=(v*max/5).toFixed(2);s.append(t);
 }
 for(const x of [-25,-15,-5,0,5,15,25]){
  const px=plot.left+(x+25)/50*(plot.right-plot.left);
  s.append(make("line",{x1:px,y1:plot.top,x2:px,y2:plot.bottom,stroke:"#294854"}));
  let t=make("text",{x:px,y:plot.bottom+22,fill:"#bbd0d3","font-size":12,"text-anchor":"middle"});t.textContent=x;s.append(t);
 }
 let path=pts.map((p,i)=>(i?"L":"M")+(plot.left+(p.x+25)/50*(plot.right-plot.left)).toFixed(2)+" "+(plot.bottom-p.y/max*(plot.bottom-plot.top)).toFixed(2)).join(" ");
 s.append(make("path",{d:path,fill:"none",stroke:"#b6f173","stroke-width":3,"stroke-linecap":"round","stroke-linejoin":"round"}));
 const ty=make("text",{x:plot.left, y:20,fill:"#aecad0","font-size":13});ty.textContent="Relative absorption (arbitrary normalisation)";s.append(ty);
 const tx=make("text",{x:(plot.left+plot.right)/2,y:385,fill:"#c7e2e1","font-size":14,"text-anchor":"middle"});tx.textContent="Probe detuning Δ (MHz)";s.append(tx);
 label("at-metric","ΩRF = "+orf.toFixed(1)+" MHz (model input)");
 label("min-metric","Min A = "+Math.min(...pts.map(p=>p.y)).toFixed(3)+" (dimensionless)");
}
function drawBench(){
 const f=+$("freq").value,e=+$("field").value,d=+$("dipole").value,lam=+$("laser").value;
 label("freq-val",f.toFixed(3)+" GHz");label("field-val",e.toFixed(2)+" V/m");
 label("dipole-val",d+" ea₀");label("laser-val",lam+" nm");
 const wavelength=C/(f*1e9);
 const rfMHz=d*E*A0*e/H/1e6;
 label("lambda-out",(wavelength*1e3).toFixed(1)+" mm");
 label("omega-out",rfMHz.toFixed(3)+" MHz");
 label("energy-out",(H*C/(lam*1e-9)/E).toFixed(3)+" eV");
 label("period-out",(1/rfMHz).toFixed(3)+" μs");
}
for(const id of ["rabi-control","rf-control","linewidth-control","rwidth-control"])$(id).addEventListener("input",drawCurve);
for(const id of ["freq","field","dipole","laser"])$(id).addEventListener("input",drawBench);
drawCurve();drawBench();
const examples={
 wave:"const c = 299792458;\nconst frequencyGHz = 1.925;\nconst lambda = c / (frequencyGHz * 1e9);\nconsole.log('Free-space wavelength:', (lambda*1e3).toFixed(2), 'mm');\nconsole.log('70 mm aperture / lambda:', (0.070/lambda).toFixed(3));",
 stokes:"const deg = Math.PI/180;\nconst psi = 30, chi = 18;\nconst S = [1, Math.cos(2*chi*deg)*Math.cos(2*psi*deg),\n  Math.cos(2*chi*deg)*Math.sin(2*psi*deg), Math.sin(2*chi*deg)];\nconsole.log('Stokes vector:', S.map(x=>x.toFixed(5)));\nconsole.log('Physicality:', Math.hypot(...S.slice(1)).toFixed(5));",
 rabi:"const h=6.62607015e-34, e=1.602176634e-19, a0=5.29177210903e-11;\nconst dipole=800, field=0.2;\nconst f= dipole*e*a0*field/h;\nconsole.log('Ideal resonant Rabi:',(f/1e6).toFixed(4),'MHz');\nconsole.log('Approximate cycle period:',(1e6/f).toFixed(4),'microseconds');",
 bistability:"const S=[1,0.65,-0.35,0.25];\nconst degree=Math.hypot(S[1],S[2],S[3])/S[0];\nconsole.log('Degree of polarisation:',degree.toFixed(5));\nconsole.log('Physical Stokes state?', S[0]>=0&&degree<=1+1e-12);\nconsole.log('Check your S3 sign against the chosen convention.');"
};
$("snippet").addEventListener("change",()=>{$("code-editor").value=examples[$("snippet").value];});
$("code-editor").value=examples.wave;
let frame=null,watch=null,nonce="";
function endFrame(){
 if(frame){frame.remove();frame=null;}if(watch){clearTimeout(watch);watch=null;}
 $("run-code").disabled=false;
}
window.addEventListener("message",event=>{
 if(!frame||event.source!==frame.contentWindow||!event.data||event.data.nonce!==nonce)return;
 const x=event.data;if(x.kind==="console")$("code-output").textContent+=x.value+"\n";
 else if(x.kind==="done")endFrame();
});
$("run-code").addEventListener("click",()=>{
 endFrame();$("run-code").disabled=true;$("code-output").textContent="Running in an isolated browser context…\n";
 nonce="q"+Math.random().toString(36).slice(2);
 const code=$("code-editor").value;
 // Encode as Base64 so literal user text cannot close the generated script tag.
 const bytes=new TextEncoder().encode(code),encoded=btoa(Array.from(bytes,x=>String.fromCharCode(x)).join(""));
 const bootstrap="(function(){const nonce="+JSON.stringify(nonce)+";const send=(kind,value)=>parent.postMessage({nonce,kind,value},'*');"+
 "const log={log:(...x)=>send('console',x.map(z=>typeof z==='object'?JSON.stringify(z):String(z)).join(' '))};"+
 "try{const raw=atob("+JSON.stringify(encoded)+");const bytes=Uint8Array.from(raw,c=>c.charCodeAt(0));"+
 "const code=new TextDecoder().decode(bytes);new Function('console',code)(log);}catch(e){send('console',String(e.name)+': '+String(e.message));}"+
 "send('done','');})();";
 frame=document.createElement("iframe");frame.setAttribute("sandbox","allow-scripts");frame.title="Isolated JS teaching code execution";frame.style.display="none";
 frame.srcdoc="<!doctype html><html><head><meta http-equiv='Content-Security-Policy' content=\"default-src 'none'; script-src 'unsafe-inline' 'unsafe-eval'; connect-src 'none'; img-src 'none'; frame-src 'none'; form-action 'none'\"></head><body><script>"+bootstrap+"<\/script></body></html>";
 document.body.append(frame);
 watch=setTimeout(()=>{if(frame){$("code-output").textContent+="Execution timed out after 2 seconds; isolated frame terminated.\n";endFrame();}},2000);
});
