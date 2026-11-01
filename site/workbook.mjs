/**
 * Rydberg Academy: 1,000 original, deterministic, solved physics practice cases.
 * Twenty mathematical families x 50 distinct input cases. Educational only.
 * No experiment, HFSS result, manufactured component or atomic signal is asserted.
 *
 * Each case has exact inputs, formula, numeric result, interpretation, pitfalls
 * and a reference tag. Browser and Node can run this unmodified.
 */
const C=299792458, H=6.62607015e-34, E=1.602176634e-19;
const MU_B=9.2740100783e-24, A0=5.29177210903e-11;
const pi=Math.PI;
const format=(x,d=5)=>Number(x.toPrecision(d)).toString();
const cases=[
["rf-wavelength","RF wavelength","RF / antenna",i=>{
 const f=0.8+0.065*i; const lambda=C/(f*1e9);
 return {inputs:"f = "+format(f,5)+" GHz",formula:"λ = c/f",value:lambda,unit:"m",
 explanation:"Use the free-space wavelength to compare cell aperture and finite copper size, but do not infer local near-field strength from λ alone.",pitfall:"Confusing free-space and dielectric wavelength; treating finite-board resonance as a simple half-wave dipole."};
}],
["optical-photon-energy","Optical photon energy","Optics",i=>{
 const nm=460+7*i;return {inputs:"λ = "+nm+" nm",formula:"E = hc/λ",value:H*C/(nm*1e-9)/E,unit:"eV",explanation:"Photon energy is set by frequency. This does not guarantee a specific allowed Rb-87 ladder without atomic state selection.",pitfall:"Conflating an approximate 480 nm setpoint with a confirmed Rydberg transition."};
}],
["rf-rabi","RF Rabi frequency","Atomic",i=>{
 const d=400+13*i,field=0.05+0.01*i;return {inputs:"μ = "+d+" ea₀; |E| = "+format(field)+" V/m",formula:"Ω/(2π) = μ|E|/h",value:d*E*A0*field/H/1e6,unit:"MHz",explanation:"Illustrates peak dipole coupling for a fixed orientation and resonant transition; not an experimentally derived field.",pitfall:"Forgetting the selection-rule projection, field phasor convention or h versus ℏ."};
}],
["zeeman","Linear fine-structure Zeeman shift","Atomic",i=>{
 const B=0.01+0.003*i,g=4/3,m=0.5;return {inputs:"B = "+format(B)+" mT; gJ=4/3; mj=1/2",formula:"Δf = μB gJ mj B/h",value:MU_B*g*m*B*1e-3/H/1e6,unit:"MHz",explanation:"A simplified linear fine-structure estimate; not an Rb hyperfine Breit–Rabi calculation.",pitfall:"Treating a toy gJ value as valid for the selected experimental hyperfine manifold."};
}],
["power-decibel","Power contrast","RF",i=>{
 const ratio=1.5+0.8*i;return {inputs:"Ppass/Preject = "+format(ratio),formula:"ΔdB = 10 log₁₀(Ppass/Preject)",value:10*Math.log10(ratio),unit:"dB",explanation:"This is a positive calibrated power ratio. A 14 dB result on one antenna/rod grid does not calibrate a different setup.",pitfall:"Using 20 log for a direct power ratio."};
}],
["voltage-decibel","Voltage amplitude contrast","RF",i=>{
 const ratio=1.05+0.14*i;return {inputs:"Vpass/Vreject = "+format(ratio),formula:"ΔdB = 20 log₁₀(Vpass/Vreject)",value:20*Math.log10(ratio),unit:"dB",explanation:"The voltage form assumes a common impedance and detector calibration.",pitfall:"Using 10 log for a voltage ratio without squaring amplitude."};
}],
["lc-resonance","LC resonance","Metasurface",i=>{
 const L=9+0.4*i,Cp=0.3+0.012*i;return {inputs:"L = "+format(L)+" nH; C = "+format(Cp)+" pF",formula:"f₀ = 1/(2π√(LC))",value:1/(2*pi*Math.sqrt(L*1e-9*Cp*1e-12))/1e9,unit:"GHz",explanation:"A lumped LC guide only; HFSS distributed copper, substrate and fields can shift the resonant mode.",pitfall:"Claiming a fabricated resonance from an ideal lumped fit."};
}],
["field-decay","Coherence decay envelope","Quantum",i=>{
 const tau=2+0.25*i,t=0.5+0.13*i;return {inputs:"τ = "+format(tau)+" μs; t = "+format(t)+" μs",formula:"|ρge(t)| / |ρge(0)| = exp(−t/τ)",value:Math.exp(-t/tau),unit:"fraction",explanation:"An illustrative exponential; real decoherence can contain Doppler averaging and non-exponential components.",pitfall:"Equating this toy τ to a measured Rydberg lifetime."};
}],
["doppler-optical","Single-photon Doppler shift","Optics",i=>{
 const v=50+4*i,lambda=730+2*i;return {inputs:"v_parallel = "+v+" m/s; λ = "+lambda+" nm",formula:"|Δf| = |v_parallel|/λ",value:v/(lambda*1e-9)/1e6,unit:"MHz",explanation:"A single velocity class, not the width of the thermal Maxwellian distribution.",pitfall:"Forgetting the sign of counter-propagation in two-photon detuning."};
}],
["rabi-period","Ideal resonant Rabi period","Quantum",i=>{
 const f=0.1+0.05*i;return {inputs:"Ω/(2π) = "+format(f)+" MHz",formula:"T = 1 / (Ω/2π)",value:1/f,unit:"μs",explanation:"Ideal coherent on-resonance two-level population cycle; transit and damping modify observed oscillations.",pitfall:"Using 2π/Ω with Ω already in cycles/s."};
}],
["photocurrent","Photodiode photocurrent","Optics",i=>{
 const R=0.3+0.004*i,P=1+0.8*i;return {inputs:"Responsivity = "+format(R)+" A/W; P = "+format(P)+" μW",formula:"I = RP",value:R*P,unit:"μA",explanation:"The detection chain also needs offset, transimpedance, noise and saturation checks.",pitfall:"Equating sensor current with RF input current at the vapour cell."};
}],
["optical-depth","Beer–Lambert optical depth","Optics",i=>{
 const OD=0.05+0.04*i;return {inputs:"Natural-log optical depth = "+format(OD),formula:"T = exp(−OD)",value:Math.exp(-OD),unit:"fraction",explanation:"OD here uses the natural-log convention αL, not the decimal spectrophotometer OD=-log10(T).",pitfall:"Interchanging natural and base-10 optical-depth definitions."};
}],
["gaussian-beam","Gaussian beam diffraction","Optics",i=>{
 const w0=0.25+0.015*i,lambda=780,z=0.05+0.01*i;const zR=pi*(w0*1e-3)**2/(lambda*1e-9);
 return {inputs:"w₀="+format(w0)+" mm; λ=780 nm; z="+format(z)+" m",formula:"w(z)=w₀√(1+(z/zR)²), zR=πw₀²/λ",value:w0*Math.sqrt(1+(z/zR)**2),unit:"mm",explanation:"A paraxial Gaussian beam in free space, not the measured cell spot size.",pitfall:"Confusing 1/e² intensity radius with full width at half maximum."};
}],
["condition-number","Diagonal matrix condition number","Inversion",i=>{
 const small=0.02+0.007*i;return {inputs:"A = diag(1,0.8,0.45,"+format(small)+")",formula:"κ₂=σmax/σmin",value:1/Math.min(small,0.45),unit:"dimensionless",explanation:"One tiny singular mode amplifies noise; the project uses a 6x4 source matrix, not this toy diagonal example.",pitfall:"Assuming rank four guarantees acceptable estimation error."};
}],
["stokes-azimuth","Linear Stokes projection S₁","Polarimetry",i=>{
 const theta=-80+3.1*i;return {inputs:"ψ = "+format(theta)+"°; χ = 0°; S₀=1",formula:"S₁ = cos(2ψ) for linear input",value:Math.cos(2*theta*pi/180),unit:"normalised",explanation:"Pure linear polarisation on the Poincaré equator, with a declared azimuth reference.",pitfall:"Using ψ rather than 2ψ, or assuming linear measurements reveal S3."};
}],
["stokes-ellipticity","Stokes S₃ from ellipticity","Polarimetry",i=>{
 const chi=-44+1.75*i;return {inputs:"χ = "+format(chi)+"°; S₀=1",formula:"S₃ = sin(2χ) in this convention",value:Math.sin(2*chi*pi/180),unit:"normalised",explanation:"Handedness sign is convention-dependent; the actual source matrix must carry its convention.",pitfall:"Using an unlabeled right/left circular definition across optical and RF software."};
}],
["degree-polarisation","Degree of polarisation","Polarimetry",i=>{
 const p=0.1+0.015*i;return {inputs:"S₀=1; (S₁,S₂,S₃)=("+format(p)+",0,0)",formula:"DoP=√(S₁²+S₂²+S₃²)/S₀",value:p,unit:"fraction",explanation:"Partially polarised states lie inside the sphere. The input is a valid Stokes state for 0≤p≤1.",pitfall:"Plotting a mixed state exactly on the sphere surface."};
}],
["shot-noise","Integration-time scaling","Metrology",i=>{
 const T=1+0.35*i;return {inputs:"Time ratio T/T₀ = "+format(T),formula:"σ/σ₀ = 1/√(T/T₀)",value:1/Math.sqrt(T),unit:"relative uncertainty",explanation:"A shot-noise-like scaling assumption; correlated drift can spoil this trend.",pitfall:"Reporting theoretical precision improvement as measured experimental performance."};
}],
["rydberg-spacing","Hydrogenic adjacent-spacing scaling","Rydberg",i=>{
 const n=45+i;return {inputs:"Effective n*= "+n+", reference n*=70",formula:"ΔE(n)/ΔE(70) ≈ (70/n)³",value:(70/n)**3,unit:"dimensionless",explanation:"Approximate high-n scaling only, not a specific rubidium transition frequency.",pitfall:"Forgetting state-specific quantum defects and level mixing."};
}],
["photons-per-second","Optical photon flux","Optics",i=>{
 const P=0.2+0.08*i,lambda=780;return {inputs:"Power = "+format(P)+" μW; λ=780 nm",formula:"Ndot=Pλ/(hc)",value:P*1e-6*lambda*1e-9/(H*C),unit:"photons/s",explanation:"Mean photon flux of a monochromatic ideal beam; detector quantum efficiency is additional.",pitfall:"Assuming all incident photons are absorbed or detected."};
}]
];
const sources={
"rf-wavelength":"Balanis, Antenna Theory (4th ed.); project finite-array HFSS notes",
"optical-photon-energy":"NIST CODATA h,c,e (SI exact definitions)",
"rf-rabi":"Gallagher, Rydberg Atoms; ARC dipole matrix element convention",
"zeeman":"Steck Rb87 D line data; ARC Zeeman API",
"power-decibel":"Pozar, Microwave Engineering; common reference impedance",
"voltage-decibel":"Pozar, Microwave Engineering; common reference impedance",
"lc-resonance":"Pozar, Microwave Engineering; distributed electromagnetic simulation",
"field-decay":"Scully & Zubairy, Quantum Optics",
"doppler-optical":"Foot, Atomic Physics; thermal Doppler model",
"rabi-period":"Foot, Atomic Physics; ideal two-level Rabi solution",
"photocurrent":"Saleh & Teich, Fundamentals of Photonics",
"optical-depth":"Steck, Quantum and Atom Optics",
"gaussian-beam":"Saleh & Teich, Fundamentals of Photonics",
"condition-number":"Golub & Van Loan, Matrix Computations",
"stokes-azimuth":"Collett, Field Guide to Polarization; source lab sign convention",
"stokes-ellipticity":"Collett, Field Guide to Polarization; source lab sign convention",
"degree-polarisation":"Collett, Field Guide to Polarization",
"shot-noise":"Kay, Fundamentals of Statistical Signal Processing",
"rydberg-spacing":"Gallagher, Rydberg Atoms",
"photons-per-second":"NIST CODATA exact SI constants"
};
export function generateWorkbook(){
 const out=[];
 for(let k=0;k<cases.length;k++){
   const [id,label,part,compute]=cases[k];
   for(let i=0;i<50;i++){
     const e=compute(i),number=k*50+i+1;
     if(!Number.isFinite(e.value))throw new Error("Non-finite generated answer #"+number);
     out.push({id:String(number).padStart(4,"0"),family:id,title:label,part,
       question:"Calculate "+label.toLowerCase()+" for "+e.inputs+". Explain the applicable physical assumptions.",
       inputs:e.inputs,formula:e.formula,value:e.value,unit:e.unit,
       formattedAnswer:format(e.value,6)+" "+e.unit,
       derivation:"Apply "+e.formula+" to "+e.inputs+". The result is "+format(e.value,6)+" "+e.unit+".",
       explanation:e.explanation,diagnostic:e.pitfall,reference:sources[id]});
   }
 }
 return out;
}
export function getBookMetrics(){
 const e=generateWorkbook();return {families:cases.length,exercises:e.length,uniqueIds:new Set(e.map(x=>x.id)).size};
}
export {C,H,E,MU_B,A0};
