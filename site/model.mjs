/** Source-backed offline Stokes model. NOT a HFSS solver or an atomic measurement. */
export const SOURCE_REPO = "https://github.com/RV-crtl/Rydberg-Sensing-Research-Archive";
export function stokesFromAngles(azimuthDeg, ellipticityDeg) {
  const p = Number(azimuthDeg) * Math.PI / 180;
  const c = Number(ellipticityDeg) * Math.PI / 180;
  if (!Number.isFinite(p) || !Number.isFinite(c) || Math.abs(c) > Math.PI/4+1e-9)
    throw new RangeError("Azimuth and ellipticity must be finite, |ellipticity| <= 45 degrees");
  return [1, Math.cos(2*c)*Math.cos(2*p), Math.cos(2*c)*Math.sin(2*p), Math.sin(2*c)];
}
export function matrixResponses(rows, vector) {
  if(!Array.isArray(rows) || rows.length !== 6 || !Array.isArray(vector) || vector.length !== 4)
    throw new TypeError("Expected a 6 x 4 analyser matrix and four-element Stokes vector");
  return rows.map(row=>{
    if(!Array.isArray(row) || row.length!==4 || row.some(x=>!Number.isFinite(x)))
      throw new TypeError("Invalid analyser row");
    return row.reduce((sum,v,j)=>sum+v*vector[j],0);
  });
}
export function rank(matrix, tol=1e-10) {
  const a=matrix.map(row=>row.map(Number));
  if(a.length===0)return 0;
  let r=0;
  for(let col=0;col<a[0].length && r<a.length;col++){
    let pivot=r;
    for(let j=r+1;j<a.length;j++)if(Math.abs(a[j][col])>Math.abs(a[pivot][col]))pivot=j;
    if(Math.abs(a[pivot][col]) <= tol)continue;
    [a[r],a[pivot]]=[a[pivot],a[r]];
    const v=a[r][col];for(let j=col;j<a[r].length;j++)a[r][j]/=v;
    for(let i=0;i<a.length;i++){if(i===r)continue;const f=a[i][col];for(let j=col;j<a[i].length;j++)a[i][j]-=f*a[r][j];}
    r++;
  }
  return r;
}
export function improvementPercent(equal,optimized) {
  if(!Number.isFinite(equal) || !Number.isFinite(optimized) || equal<=0||optimized<=0)
    throw new RangeError("Information criterion values must be positive");
  return 100*(equal-optimized)/equal;
}
export function filterFiles(files,term="",group="All") {
  const q=term.toLocaleLowerCase().trim();
  return files.filter(f=>(group==="All" || f.g===group)
    && (f.p+" "+f.g).toLocaleLowerCase().includes(q));
}
export function githubFileUrl(path) {
  if(typeof path!=="string" || path.startsWith("/") || path.split("/").some(x=>x===".."||x===""))
    throw new TypeError("Invalid repository path");
  return SOURCE_REPO+"/blob/main/"+path.split("/").map(encodeURIComponent).join("/");
}
export function validateAtlas(data) {
  if(!data || data.schema!==1 || !Array.isArray(data.files)|| !Array.isArray(data.timeline))
    throw new TypeError("Invalid research atlas schema");
  const m=data.matrix;
  if(!m || m.rows?.length!==6 || m.rows.some(row=>row.length!==4 || row.some(x=>!Number.isFinite(x))))
    throw new TypeError("Invalid source matrix shape");
  if(rank(m.rows)!==4)throw new Error("Source instrument rank is not four");
  if(m.maskOrder.length!==6 || new Set(m.maskOrder).size!==6)throw new Error("Incorrect mask order");
  const names=new Set(data.files.map(f=>f.p));
  if(!names.has(m.sourcePath) || !names.has(m.dwell.sourcePath))throw new Error("Source provenance path missing from index");
  if(data.files.some(f=>typeof f.p!=="string" || !f.g || !Number.isFinite(f.bytes)))throw new Error("Invalid file record");
  if(data.timeline.some(t=>!names.has(t.path)))throw new Error("Timeline references missing files");
  if(!m.dwell || m.dwell.optimizedWeights.length!==6 ||
     Math.abs(m.dwell.optimizedWeights.reduce((s,x)=>s+x,0)-1)>1e-8)
    throw new Error("Invalid dwell weights");
  return true;
}