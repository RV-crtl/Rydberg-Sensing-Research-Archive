import test from "node:test";
import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {stokesFromAngles,matrixResponses,rank,improvementPercent,filterFiles,githubFileUrl,validateAtlas} from "../site/model.mjs";
const atlas=JSON.parse(readFileSync(new URL("../site/data/research-atlas.json",import.meta.url),"utf8"));
test("source atlas shape, provenance and rank validated",()=>assert.equal(validateAtlas(atlas),true));
test("pure horizontal, vertical and diagonal Stokes states",()=>{
 const h=stokesFromAngles(0,0),v=stokesFromAngles(90,0),d=stokesFromAngles(45,0);
 assert.ok(Math.abs(h[1]-1)<1e-12);assert.ok(Math.abs(v[1]+1)<1e-12);assert.ok(Math.abs(d[2]-1)<1e-12);
});
test("circular coordinate endpoints and physicality",()=>{
 for(const x of [-45,45]){const s=stokesFromAngles(0,x);assert.ok(Math.abs(s[3]-Math.sign(x))<1e-12);assert.ok(Math.abs(Math.hypot(s[1],s[2],s[3])-1)<1e-12);}
});
test("unmodified HFSS-derived 6x4 matrix maps Stokes to correct six responses",()=>{
 const a=atlas.matrix.rows,s=stokesFromAngles(0,0),r=matrixResponses(a,s);
 assert.equal(r.length,6);for(let i=0;i<6;i++)assert.ok(Math.abs(r[i]-(a[i][0]+a[i][1]))<1e-12);
 assert.equal(rank(a),4);
});
test("reported information criterion difference rounds to 40.8%",()=>{
 const d=atlas.matrix.dwell;
 assert.equal(improvementPercent(d.equalTrace,d.optimizedTrace).toFixed(1),"40.8");
});
test("search filter is useful and links reject traversal",()=>{
 const matches=filterFiles(atlas.files,"INSTRUMENT_MATRIX","Manuscripts");assert.ok(matches.length>=1);
 assert.ok(githubFileUrl(matches[0].p).startsWith("https://github.com/"));
 assert.throws(()=>githubFileUrl("../secrets.txt"));
});
test("invalid shapes and inputs rejected",()=>{
 assert.throws(()=>stokesFromAngles(0,50));
 assert.throws(()=>matrixResponses([[1,2,3,4]],[1,0,0,0]));
});
