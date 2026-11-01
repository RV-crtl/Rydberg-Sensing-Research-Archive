import test from "node:test";
import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {generateWorkbook,getBookMetrics,C,H,E,MU_B,A0} from "../book/workbook.mjs";
const questions=generateWorkbook();
test("1000 original numeric cases, 20 families, unique deterministic IDs",()=>{
 assert.deepEqual(getBookMetrics(),{families:20,exercises:1000,uniqueIds:1000});
 assert.equal(questions.length,1000);
 assert.equal(questions[0].id,"0001");assert.equal(questions.at(-1).id,"1000");
 assert.equal(new Set(questions.map(x=>x.family)).size,20);
 assert.ok(questions.every(x=>Number.isFinite(x.value)&&x.inputs&&x.derivation&&x.reference&&x.diagnostic));
 assert.deepEqual(generateWorkbook(),questions);
});
test("RF wavelength and optical photon energy recover SI values",()=>{
 assert.ok(Math.abs(C/(1.925e9)-0.155735)<0.0001);
 assert.ok(Math.abs(H*C/(780e-9)/E-1.5898)<0.01);
 assert.ok(Math.abs(A0-5.29177210903e-11)<1e-15);
});
test("specific solution families have correct dimensions and sample formulas",()=>{
 const q=questions[0];
 assert.ok(Math.abs(q.value-C/(0.8e9))<1e-12);
 const r=questions.find(x=>x.family==="rf-rabi");
 assert.ok(Math.abs(r.value-(400*E*A0*.05/H/1e6))<1e-12);
 const d=questions.find(x=>x.family==="power-decibel");
 assert.ok(Math.abs(d.value-10*Math.log10(1.5))<1e-12);
 const z=questions.find(x=>x.family==="zeeman");
 assert.ok(Math.abs(z.value-MU_B*(4/3)*.5*.01e-3/H/1e6)<1e-12);
});
test("no generated case is labeled as actual lab data",()=>{
 assert.ok(questions.every(x=>!/(confirmed experimentally|HFSS solver run completed|measured atomic full.Stokes)/i.test(x.explanation)));
});
test("browser and book exercise engines are byte identical",()=>{
 const source=readFileSync(new URL("../book/workbook.mjs",import.meta.url));
 const site=readFileSync(new URL("../site/workbook.mjs",import.meta.url));
 assert.deepEqual(source,site);
});
test("site-bound textbook chapters equal exact originals",()=>{
 const catalog=JSON.parse(readFileSync(new URL("../site/data/book-catalog.json",import.meta.url)));
 assert.equal(catalog.schema,2);
 const all=catalog.parts.flatMap(name=>JSON.parse(readFileSync(new URL("../site/data/"+name,import.meta.url))));
 assert.equal(all.length,catalog.chapterCount);assert.ok(all.length>=36);
 assert.equal(new Set(all.map(x=>x.slug)).size,all.length);
 assert.equal(catalog.totalWords,all.reduce((sum,x)=>sum+x.words,0));
 for(const x of all){
  const md=readFileSync(new URL("../book/chapters/"+x.slug+".md",import.meta.url),"utf8");
  assert.equal(x.markdown.trim(),md.trim());
 }
});
