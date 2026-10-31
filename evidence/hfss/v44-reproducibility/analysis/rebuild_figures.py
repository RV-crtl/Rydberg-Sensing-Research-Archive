#!/usr/bin/env python3
"""Revision figures from original photo, dimension parameter tables and HFSS results.
Uses no synthesized HFSS results or detector noise. Local matrix-based reconstructions are
post-processing of archived independently meshed HFSS matrices, not new field solves.
"""
import csv,json,math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle,Arc, FancyArrowPatch, FancyBboxPatch, Polygon
from matplotlib.colors import Normalize
from PIL import Image
R=Path(__file__).resolve().parents[1]; F=R/'figures';D=R/'data';F.mkdir(exist_ok=True)
NAVY='#0d2036'; TEAL='#00899a'; BLUE='#2774a6'; ORANGE='#df7437'; RED='#d05154'; GRAY='#586879'; PALE='#eef4f7'; GOLD='#d99c29'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10.4,'axes.titlesize':12,'axes.labelsize':10,'axes.edgecolor':'#b6c7d3','axes.spines.top':False,'axes.spines.right':False,'axes.titleweight':'bold','savefig.pad_inches':0.12,'pdf.fonttype':42,'svg.fonttype':'none','lines.linewidth':2.1})
def finish(fig,name):
 fig.savefig(F/(name+'.pdf'),bbox_inches='tight',facecolor='white')
 fig.savefig(F/(name+'.png'),bbox_inches='tight',facecolor='white',dpi=210)
 fig.savefig(F/(name+'.svg'),bbox_inches='tight',facecolor='white')
 plt.close(fig)
def box(ax,xy,w,h,title,sub=None,fc='white',border='#b5ccd8',fsize=11):
 ax.add_patch(FancyBboxPatch(xy,w,h,boxstyle='round,pad=.01,rounding_size=.025',fc=fc,ec=border,lw=1.2))
 ax.text(xy[0]+w/2,xy[1]+h*.66,title,ha='center',va='center',color=NAVY,weight='bold',fontsize=fsize)
 if sub:ax.text(xy[0]+w/2,xy[1]+h*.25,sub,ha='center',va='center',color=GRAY,fontsize=9)
def arrow(ax,x1,y1,x2,y2,color=TEAL,style='-|>',lw=2):
 ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle=style,lw=lw,color=color,mutation_scale=14))
# FIG 1. Actual laboratory image + explicit future RF insertion (no fake overlay on photograph).
fig=plt.figure(figsize=(14.6,6.3));gs=fig.add_gridspec(1,2,width_ratios=[.94,1.16],wspace=.06)
a=fig.add_subplot(gs[0,0]);a.set_axis_off();im=np.array(Image.open(R/'source_assets/image1.jpeg'))
a.imshow(im);a.set_xlim(0,1200);a.set_ylim(1510,70)
a.add_patch(Rectangle((19,74),1162,1330,linewidth=3,edgecolor='#fff',facecolor='none'))
a.text(42,122,'A  |  RUBIDIUM LABORATORY',fontsize=14,weight='bold',color='white',bbox=dict(fc=NAVY,ec='none',pad=9))
a.text(42,1454,'Photograph: existing optical bench · no PCB overlaid',fontsize=9,color=NAVY,bbox=dict(fc='white',pad=6,alpha=.9))
b=fig.add_subplot(gs[0,1]);b.set_axis_off();b.set_xlim(0,1);b.set_ylim(0,1)
b.text(.03,.96,'B  |  POLARISATION ANALYSIS AT A FIXED OPTICAL RECEIVER',fontsize=13,weight='bold',color=NAVY)
b.text(.04,.894,'RF plane wave',color=GRAY,fontsize=10)
# RF plane incoming wave & traces
for i in range(3):
 xx=.065+i*.038
 b.plot([xx,xx+.015],[.55,.83],color=GOLD,lw=2,alpha=.7)
arrow(b,.14,.70,.27,.70,GOLD,lw=3)
b.add_patch(Rectangle((.275,.49),.071,.40,facecolor='#eef3f3',edgecolor=ORANGE,lw=2.2))
for yy in [.53,.58,.63,.68,.73,.78,.83]:b.plot([.295,.325],[yy,yy],color=ORANGE,lw=1.5)
b.text(.307,.445,'Switched two-face\nRF surface',ha='center',va='top',fontsize=10,weight='bold',color=NAVY)
arrow(b,.348,.70,.42,.70,GOLD,lw=2.3)
# Rb vapor cell
b.add_patch(FancyBboxPatch((.44,.575),.208,.245,boxstyle='round,pad=.015,rounding_size=.085',fc='#eff4ef',ec='#3d7867',lw=2.4))
b.text(.544,.715,'Rb vapour cell',ha='center',fontsize=12,weight='bold',color=NAVY)
b.text(.544,.663,'Atomic RF interaction',ha='center',fontsize=9,color=GRAY)
# Optical beams counterpropagate / center line
arrow(b,.425,.63,.657,.63,RED,lw=3)
arrow(b,.663,.763,.42,.763,BLUE,lw=3)
b.text(.54,.60,'780 nm probe  →',fontsize=9.2,color=RED,ha='center')
b.text(.54,.798,'←  480 nm coupling',fontsize=9.2,color=BLUE,ha='center')
box(b,(.77,.58),.20,.17,'Photodetector','Probe transmission',fc='#f2f5ff',border='#a9b5dd',fsize=10)
arrow(b,.656,.63,.77,.63,RED,lw=2)
b.text(.03,.30,'MEASUREMENT SEQUENCE',fontweight='bold',color=NAVY,fontsize=12)
box(b,(.04,.135),.26,.125,'6 conductor states',r'$k=1,\ldots,6$',fc='#f5f8fa',fsize=10)
box(b,(.367,.135),.26,.125,'Complex HFSS fields',r'$A\in\mathbb{R}^{6\times4}$',fc='#f5f8fa',fsize=10)
box(b,(.692,.135),.272,.125,'Stokes estimator',r'$\widehat{\mathbf{S}}=A^+\mathbf{m}$',fc='#f5f8fa',fsize=10)
arrow(b,.306,.198,.36,.198);arrow(b,.634,.198,.687,.198)
b.text(.04,.035,'The optical readout is the target measurement channel; the plotted A is constructed from RF fields.',fontsize=8.9,color=GRAY)
finish(fig,'FINAL_F01_LAB_AND_ARCHITECTURE')
# FIG 2 physical principle without fabricated spectra. Level diagram + signal equation.
fig=plt.figure(figsize=(13.9,4.65));gs=fig.add_gridspec(1,3,width_ratios=[.94,1.12,1.15],wspace=.26)
a=fig.add_subplot(gs[0,0]);a.set_xlim(0,1);a.set_ylim(0,1);a.set_axis_off();a.set_title('A  Rubidium four-level ladder',loc='left',color=NAVY,pad=16)
levels=[(.11,.17,'5S'),(.36,.38,'5P'),(.63,.67,'nD / nS'),(.85,.88,'n\'P / n\'S')]
for yy,x,txt in levels:a.plot([.16,.75],[yy,yy],lw=3.1,color=NAVY);a.text(.80,yy,txt,va='center',fontsize=11,color=NAVY)
for low,hi,c,lab in [(.12,.36,RED,'780 nm'),(.39,.63,BLUE,'480 nm'),(.66,.85,GOLD,'RF')]:
 arrow(a,.42,low,.42,hi,c,lw=2.7);a.text(.44,(low+hi)/2,lab,ha='left',va='center',fontsize=10,color=c)
b=fig.add_subplot(gs[0,1]);b.set_axis_off();b.set_xlim(0,1);b.set_ylim(0,1);b.set_title('B  RF-to-optical transduction',loc='left',color=NAVY,pad=16)
box(b,(.04,.70),.91,.18,'Polarisation-dependent microwave drive',r'$\Omega_k(\mathbf{r})=|\mathbf{d}\!\cdot\!\mathbf{E}_k(\mathbf{r})|/\hbar$',fc='#f7f8fd')
box(b,(.04,.40),.91,.18,'Doppler-averaged optical coherence',r'$\chi(\Delta_p;\,\Omega_k,\Omega_c,\gamma, T)$',fc='#f4fafb')
box(b,(.04,.10),.91,.18,'Optical observable',r'$T_k(\Delta_p)=\exp[-k_p L\,\mathrm{Im}\,\bar\chi_k]$',fc='#f7f8fd')
arrow(b,.5,.69,.5,.58);arrow(b,.5,.39,.5,.28)
c=fig.add_subplot(gs[0,2]);c.set_axis_off();c.set_xlim(0,1);c.set_ylim(0,1);c.set_title('C  Observation models compared',loc='left',color=NAVY,pad=16)
box(c,(.04,.65),.92,.26,'HFSS receiving operator',r'$m_k=\int w|\mathbf{e}_d\cdot\mathbf{E}_k|^2dV$',fc='#f5f9fa')
box(c,(.04,.25),.92,.26,'Atomic spectrum (density-matrix model)',r'$T_k(\Delta_p)=\exp[-\alpha\int w\,\mathrm{Im}\chi_k\,dV]$',fc='#fff9f4')
c.text(.50,.137,'RF quadratic calibration requires a defined optical estimator',ha='center',fontsize=9,color=GRAY)
finish(fig,'FINAL_F02_EIT_PHYSICS')
# FIG 3 parameters true extracted values, no speculative CAD claim.
params=list(csv.DictReader(open(D/'V26_ARCHIVED_HFSS/THREE_DESIGNS_11_PARAMETERS.csv')))
keys=['top_x_scale','top_y_scale','rear_x_scale','rear_y_scale','front_width_mm','rear_width_mm','rear_angle_deg','rear_shrink','switch_gap_mm','gap_fraction_1','gap_fraction_2']
labels=['Front x','Front y','Rear x','Rear y','Front width','Rear width','Rear angle','Rear shrink','Switch gap','Gap position 1','Gap position 2']
fig=plt.figure(figsize=(13.8,4.6));gs=fig.add_gridspec(1,2,width_ratios=[.38,.62],wspace=.15)
a=fig.add_subplot(gs[0,0]);a.set_aspect('equal');a.set_xlim(0,24);a.set_ylim(0,24);a.axis('off');a.set_title('A  Shared two-face topology · 24 mm cell',loc='left',color=NAVY,pad=15)
a.add_patch(Rectangle((.1,.1),23.8,23.8,facecolor='#f4f7fa',edgecolor='#d3dce0',linewidth=2))
a.plot([4,4,20,20,4],[6,20,20,6,6],color=ORANGE,lw=5,solid_capstyle='round')
a.plot([6,19],[5,5],lw=4,color='white')
a.plot([6.4,6.4,17.6,17.6],[5,18.1,18.1,5],lw=3,color=TEAL,solid_capstyle='round')
a.plot([11,13],[18.1,18.1],lw=3,color='white')
a.text(12,22,'Front conductor',ha='center',color=ORANGE,fontsize=10,weight='bold');a.text(12,2,'Rear conductor (projected)',ha='center',color=TEAL,fontsize=9)
b=fig.add_subplot(gs[0,1]);b.set_title('B  Exact parameter differences from the frozen HFSS records',loc='left',color=NAVY,pad=15)
# meaningful variation plot normalized to baseline independent of physical units
vals=np.array([[float(p[k]) for k in keys] for p in params]);diff=(vals[1:]/vals[0]-1)*100
im=b.imshow(diff,cmap='PuOr',vmin=-25,vmax=25,aspect='auto');b.set_xticks(range(len(keys)),labels,rotation=43,ha='right',fontsize=8.1)
b.set_yticks([0,1],['Bandwidth-optimised','High-band alternative'])
for r in range(2):
 for j in range(len(keys)):b.text(j,r,f'{diff[r,j]:+.1f}',ha='center',va='center',fontsize=7.8,color=NAVY)
b.grid(False);cb=fig.colorbar(im,ax=b,fraction=.035,pad=.02);cb.set_label('Change from reference (%)',fontsize=9)
fig.text(.01,.008,'Source: native 11-parameter HFSS geometry records. Projection is a topology illustration, not fabrication Gerbers.',fontsize=9,color=GRAY)
finish(fig,'FINAL_F03_DESIGN_EVOLUTION')
# FIG 4 Combined 3x3 panel, face designs, switch sites, physical stack with not-to-scale.
fig=plt.figure(figsize=(14.2,4.9));gs=fig.add_gridspec(1,3,width_ratios=[.9,1,1.05],wspace=.20)
a=fig.add_subplot(gs[0,0]);a.set_aspect('equal');a.set_xlim(-5,87);a.set_ylim(-6,89);a.set_axis_off();a.set_title('A  Finite 3 × 3 array',loc='left',color=NAVY,pad=13)
a.add_patch(Rectangle((0,0),82,82,fc='#f0f5f8',ec=NAVY,lw=1.7))
for i in range(3):
 for j in range(3):
  x=5+i*24;y=5+j*24
  a.add_patch(Rectangle((x,y),24,24,fill=False,edgecolor='#c8d6de',lw=.9))
  a.plot([x+5,x+5,x+18,x+18],[y+5,y+18,y+18,y+5],lw=2.1,color=ORANGE)
  a.plot([x+8,x+17],[y+4,y+4],lw=2,color=TEAL)
a.annotate('',xy=(0,-3),xytext=(82,-3),arrowprops=dict(arrowstyle='<->',color=NAVY,lw=1.3))
a.text(41,-5.3,'82 mm',ha='center',va='top',fontsize=9)
a.text(41,86,'24 mm pitch  •  9 cells',ha='center',fontsize=9,color=GRAY)
b=fig.add_subplot(gs[0,1]);b.set_aspect('equal');b.set_xlim(0,26);b.set_ylim(0,28);b.axis('off');b.set_title('B  Four bridge locations',loc='left',color=NAVY,pad=13)
b.add_patch(Rectangle((.6,1),24,24,fc='#f6f8fb',ec=NAVY,lw=1))
b.plot([5,5,21,21],[5,21,21,5],color=ORANGE,lw=4)
b.plot([7,19],[6.7,6.7],color=TEAL,lw=3)
b.plot([9,9,17,17],[8,19,19,8],color=TEAL,lw=3,alpha=.8)
for i,(x,y) in enumerate([(5,14),(14,21),(21,13),(12,6.7)],1):
 b.add_patch(Circle((x,y),radius=1.25,ec=NAVY,fc='white',lw=1.3))
 b.text(x,y,str(i),ha='center',va='center',weight='bold',fontsize=9,color=NAVY)
b.text(12,1.2,'Illustrative trace connectivity; state masks in Fig. 5',ha='center',fontsize=7.7,color=GRAY)
c=fig.add_subplot(gs[0,2]);c.axis('off');c.set_xlim(0,1);c.set_ylim(0,1);c.set_title('C  Physical stack and sampling region',loc='left',color=NAVY,pad=13)
for y,clr,th,lab in [(.78,ORANGE,.033,'Top Cu'),(.64,'#9eb6a4',.14,'FR-4 substrate'),(.60,TEAL,.031,'Bottom Cu')]:
 c.add_patch(Rectangle((.10,y),.55,th,facecolor=clr,edgecolor='none'))
 c.text(.71,y+th/2,lab,va='center',fontsize=10,color=NAVY)
c.annotate('',xy=(.38,.13),xytext=(.38,.55),arrowprops=dict(arrowstyle='->',lw=2,color=GOLD))
c.add_patch(FancyBboxPatch((.16,.065),.52,.11,boxstyle='round,pad=.015',fc='#ebf5f3',ec='#82b1a8',lw=1.2))
c.text(.42,.12,'70 × 50 mm RF sampling region',ha='center',va='center',fontsize=9,color=NAVY)
c.text(.76,.31,'5 / 10 / 20 / 50 mm\nobservation planes',fontsize=9.3,color=GRAY,ha='center')
finish(fig,'FINAL_F04_FINITE_PCB_METATOM_CIRCUIT')
# FIG 5 explicit mask bit truth from source figure and masks
states=[3,6,8,10,12,13]
fig,ax=plt.subplots(figsize=(11.5,3.25));ax.set_axis_off();ax.set_xlim(-.4,5.9);ax.set_ylim(-.75,6.25)
ax.text(-.1,5.92,'Six nominal conductor configurations',fontsize=13,weight='bold',color=NAVY)
for i,lbl in enumerate(['Bridge D1','Bridge D2','Bridge D3','Bridge D4']):ax.text(1.65+i*.95,5.35,lbl,ha='center',fontsize=9.4,color=NAVY,weight='bold')
for i,mask in enumerate(states):
 y=4.65-i*.84
 ax.text(0,y,f'State {i+1}  ·  mask {mask:02d}',va='center',color=NAVY,fontsize=10,weight='bold')
 for k in range(4):
  x=1.24+k*.95;on=bool(mask&(1<<k))
  ax.add_patch(FancyBboxPatch((x,y-.27),.80,.52,boxstyle='round,pad=.005,rounding_size=.09',fc=TEAL if on else '#e9eef2',ec='none'))
  ax.text(x+.4,y,'CLOSED' if on else 'OPEN',ha='center',va='center',color='white' if on else GRAY,fontsize=8,weight='bold')
ax.text(0,-.56,'State identifiers map to four ideal HFSS conductive bridges; diode characteristics are not represented by these ideal states.',fontsize=9.3,color=GRAY)
finish(fig,'FINAL_F05_SWITCH_TRUTH')
# FIG 6 measured data only, no fabricated interpolation
fig,axes=plt.subplots(1,2,figsize=(12.8,4.2),gridspec_kw={'width_ratios':[1.05,.95]})
lab=['No polariser','Preferred','Nominal 45°','Rejected'];v=[-8.2,-13.9,-15.1,-23.6]
a=axes[0];x=np.arange(4)
a.bar(x,v,edgecolor='none',color=[GRAY,TEAL,BLUE,ORANGE],width=.62)
a.set_xticks(x,lab,fontsize=9);a.set_ylabel('Received power (dBm)');a.set_ylim(-28,1);a.set_title('A  Four archived received-power readings',loc='left',color=NAVY)
for xx,yy in zip(x,v):a.text(xx,yy+1,f'{yy:.1f}',ha='center',fontsize=10,weight='bold',color=NAVY)
a.annotate('9.7 dB orientation contrast',xy=(3,-22),xytext=(1.12,-26.6),color=NAVY,fontsize=10,weight='bold',arrowprops=dict(arrowstyle='->',color=ORANGE,lw=1.4))
a.grid(axis='y',alpha=.18)
b=axes[1];b.set_axis_off();b.set_xlim(0,1);b.set_ylim(0,1)
b.set_title('B  Interpretation without an invented fit',loc='left',color=NAVY)
box(b,(.03,.63),.94,.23,'Preferred / rejected power ratio',r'$10^{9.7/10}=9.33$',fc='#f4fafb')
box(b,(.03,.28),.94,.23,'Nominal 45° observation',r'$-15.1\ \mathrm{dBm}\;\;\mathrm{(archived)}$',fc='#f7f8fb')
b.text(.50,.12,'Separate earlier VNA campaign: ≈14–15 dB (different measurement chain)',ha='center',fontsize=9.2,color=GRAY)
finish(fig,'FINAL_F06_LINEAR_EXPERIMENT')
# FIG 9 finite HFSS cross-mesh reconstruction based on two matrices; 1231 deterministic physical Stokes points
z=json.load(open(D/'V27_FINITE_EVIDENCE_AUDIT.json'));P27=z['v420']['planes'];P24=z['v421_comparison']['planes']
# locate other matrices: v421 planes may not hold matrix raw; check
print('V421 plane keys',P24['-5.0'].keys())
# use archive v421 top for P24 matrices
print('v421 keys',z['v421'].keys())
# collect from archive explicit
P24mat=z['v421']['planes'] if 'planes' in z['v421'] else None
print('v421 matrix available',bool(P24mat))
if P24mat is None:
 # find in v421 raw record
 print(str(z['v421'])[:600])
# parse based on audit
A27=np.array(P27['-5.0']['instrument_matrix'],float)
if P24mat is not None and 'instrument_matrix' in P24mat['-5.0']:
 A24=np.array(P24mat['-5.0']['instrument_matrix'],float)
else:
 raise RuntimeError('P24 matrix not archived in V27 audit')
N=1231;i=np.arange(N);s3=1-2*(i+.5)/N;ang=math.pi*(3-math.sqrt(5))*i;rr=np.sqrt(1-s3*s3)
S=np.column_stack((np.ones(N),rr*np.cos(ang),rr*np.sin(ang),s3))
hat24=np.linalg.pinv(A24)@(A27@S.T);hat27=np.linalg.pinv(A27)@(A24@S.T)
err24=np.linalg.norm(hat24.T-S,axis=1)/np.linalg.norm(S,axis=1)*100
err27=np.linalg.norm(hat27.T-S,axis=1)/np.linalg.norm(S,axis=1)*100
# normalized angular differences when Stokes magnitude nonzero
summary={'stokes_sampling':'1231 deterministic Fibonacci points on pure-state Poincare sphere','observation':'HFSS native finite 3x3 matrices, 5 mm, 1.850 GHz','calibration':'P24 to P27 and P27 to P24','relative_norm_definition':'100*||S_est-S_true||_2/||S_true||_2','errors':{'P24_calibration_P27_observation':{'max_percent':float(err24.max()),'p95_percent':float(np.percentile(err24,95)),'median_percent':float(np.median(err24))},'P27_calibration_P24_observation':{'max_percent':float(err27.max()),'p95_percent':float(np.percentile(err27,95)),'median_percent':float(np.median(err27))}}}
(R/'analysis/NEW_CROSS_MESH_RECONSTRUCTION.json').write_text(json.dumps(summary,indent=2))
with open(R/'analysis/NEW_CROSS_MESH_RECONSTRUCTION.csv','w') as g:
 w=csv.writer(g);w.writerow(['S0','S1','S2','S3','error_P24_cal_P27_resp_percent','error_P27_cal_P24_resp_percent'])
 for row,u,v in zip(S,err24,err27):w.writerow(list(row)+[u,v])
fig=plt.figure(figsize=(13.5,4.8));gs=fig.add_gridspec(1,3,width_ratios=[1.2,1,1],wspace=.25)
a=fig.add_subplot(gs[0,0]);sc=a.scatter(S[:,1],S[:,2],c=err24,s=11,cmap='magma',rasterized=True);a.set_aspect('equal');a.set_xlim(-1.07,1.07);a.set_ylim(-1.07,1.07);a.set_xlabel('$S_1/S_0$');a.set_ylabel('$S_2/S_0$');a.set_title('A  Cross-mesh error mapped on Stokes disk',loc='left',color=NAVY)
a.grid(alpha=.16);cb=fig.colorbar(sc,ax=a,fraction=.045,pad=.02);cb.set_label('Full-vector error (%)',fontsize=9)
b=fig.add_subplot(gs[0,1]);b.hist(err24,bins=34,color=TEAL,alpha=.75,label='P24→P27');b.hist(err27,bins=34,color=ORANGE,alpha=.52,label='P27→P24');b.legend(fontsize=9,frameon=False);b.set_xlabel('Relative $\\|\\widehat{\\mathbf{S}}-\\mathbf{S}\\|_2$ (%)');b.set_ylabel('Input states');b.set_title('B  1,231 pure input states',loc='left',color=NAVY);b.grid(axis='y',alpha=.15)
c=fig.add_subplot(gs[0,2]);c.set_axis_off();c.set_xlim(0,1);c.set_ylim(0,1)
c.text(.03,.91,'C  Independent calibration transfer',fontsize=11.3,color=NAVY,weight='bold')
for j,(title,data,c0) in enumerate([('P24 calibration · P27 fields',err24,TEAL),('P27 calibration · P24 fields',err27,ORANGE)]):
 y=.65-.35*j
 c.add_patch(FancyBboxPatch((.025,y),.95,.24,boxstyle='round,pad=.015',fc='#f6f8fa',ec='#d6e1e6'))
 c.text(.06,y+.165,title,color=NAVY,fontsize=9.4,weight='bold')
 c.text(.06,y+.055,f'P95 {np.percentile(data,95):.1f}%    Maximum {np.max(data):.1f}%',color=c0,fontsize=12.5,weight='bold')
c.text(.04,.05,'HFSS matrix transfer; no additional full-wave solves',fontsize=9,color=GRAY)
finish(fig,'FINAL_F09_STOKES_AND_POINCARE')
# FIG10 finite dual mesh condition and gain & transfer vs distance
rows=list(csv.DictReader(open(D/'V27_FINITE_CONDITION_VS_DISTANCE.csv')))
x=np.array([float(q['distance_mm']) for q in rows]);c1=np.array([float(q['cond_P27']) for q in rows]);c2=np.array([float(q['cond_P24']) for q in rows]);d=np.array([float(q['matrix_drift_percent']) for q in rows]);t=np.array([float(q['worst_transfer_percent']) for q in rows])
fig,axes=plt.subplots(1,3,figsize=(14,4.15),gridspec_kw={'wspace':.27})
a=axes[0];a.plot(x,c1,'o-',color=TEAL,label='2.7 mm mesh');a.plot(x,c2,'s-',color=ORANGE,label='2.4 mm mesh');a.set_yscale('log');a.axhline(35,color=RED,ls='--',lw=1.2);a.set_ylabel('Condition number (log scale)');a.legend(frameon=False,fontsize=8);a.set_title('A  Full-rank does not ensure robustness',loc='left',color=NAVY)
b=axes[1];b.bar(x.astype(str),d,color=BLUE,width=.65);b.set_ylim(0,8);b.set_ylabel('Matrix drift (%)');b.set_title('B  Mesh-sensitive receiving matrix',loc='left',color=NAVY)
for ii,v in enumerate(d):b.text(ii,v+.15,f'{v:.2f}',ha='center',fontsize=8.5)
c=axes[2];c.plot(x,t,'o-',color=RED);c.set_ylabel('Worst archived transfer discrepancy (%)');c.set_title('C  Calibration error amplification',loc='left',color=NAVY)
for ax in [a,c]:ax.set_xticks(x)
for ax in axes:ax.set_xlabel('Distance behind surface (mm)');ax.grid(axis='y',alpha=.16)
fig.text(.02,-.02,'All results from completed 3×3 native complex total-field HFSS archives at 1.850 GHz. Both meshes retain rank four.',fontsize=9,color=GRAY)
finish(fig,'FINAL_F10_FINITE_DISTANCE')
print('Rebuilt 8 figures; new diagnostic',summary)
