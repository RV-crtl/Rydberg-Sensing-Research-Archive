from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont
import json,zipfile,csv
import numpy as np
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle, FancyArrowPatch, Arc
R=Path(__file__).resolve().parents[1];F=R/'figures';F.mkdir(parents=True,exist_ok=True)
NAVY='#183247';BLUE='#22637b';ORANGE='#ba6931';TEAL='#007d82';GREY='#65727a'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8.3,'pdf.fonttype':42,'svg.fonttype':'none','axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})
def save(fig,name):
 for ext in ('pdf','svg','png'):
  fig.savefig(F/(name+'.'+ext),bbox_inches='tight',pad_inches=.08,dpi=270 if ext=='png' else 150)
 plt.close(fig)
# Lab photograph: use the interim report's actual recorded photographic evidence
lab=Image.open(R/'source_assets/EXPERIMENT_OPTICAL_TABLE_ORIGINAL.jpg').convert('RGB')
# It is a laboratory photograph, not a render; only crop and a discreet label; no fake components
fig,ax=plt.subplots(figsize=(5.1,3.35)); ax.imshow(lab);ax.axis('off');
ax.text(.018,.97,'RUBIDIUM EIT OPTICAL BENCH',transform=ax.transAxes,va='top',fontsize=9,weight='bold',color='white',bbox=dict(boxstyle='square,pad=.38',fc='#183247',ec='none',alpha=.91))
ax.text(.018,.038,'Original laboratory photograph  •  optical alignment and vapour-cell region',transform=ax.transAxes,va='bottom',fontsize=6.8,color='white',bbox=dict(boxstyle='square,pad=.26',fc='#183247',ec='none',alpha=.87))
save(fig,'F01_REAL_LAB_PHOTO')
# experimental photographs: original two polarizer setups from interim report
p1=Image.open(R/'source_assets/EXPERIMENT_LINEAR_POLARISER_VIEW_A.jpg').convert('RGB')
p2=Image.open(R/'source_assets/EXPERIMENT_LINEAR_POLARISER_VIEW_B.jpg').convert('RGB')
fig,ax=plt.subplots(1,2,figsize=(7.0,2.85),gridspec_kw={'wspace':.025})
for a,p,txt in zip(ax,[p1,p2],['(a) Linear-polariser reference','(b) Alternate experimental view']):
 a.imshow(p);a.axis('off');a.text(.02,.98,txt,va='top',transform=a.transAxes,fontsize=8,color='white',weight='bold',bbox=dict(fc=NAVY,ec='none',alpha=.90,pad=3))
save(fig,'F06_PHOTOGRAPHIC_POLARISER')
Z=zipfile.ZipFile(R/'source_evidence/V418_NATIVE_HFSS_RETURN_COMPACT.zip')
g=json.loads(Z.read('V416_CANDIDATES/C033/COPPER_M03.json'))
def native(ax,dx=0,dy=0,mini=False):
 for sh in g['shapes']:
  pts=np.array(sh['polygon'])+np.array([dx,dy]); col=ORANGE if sh['layer']=='TOP' else TEAL
  ax.add_patch(Polygon(pts,closed=True,facecolor=col,edgecolor='white',linewidth=.18 if mini else .3))
def geometry(ax,size=13):
 ax.set_aspect('equal');ax.set_xlim(-size,size);ax.set_ylim(-size,size);ax.set_xticks([-12,0,12]);ax.set_yticks([-12,0,12]);ax.tick_params(labelsize=7);ax.grid(alpha=.09)
# fig 3: one geometry panel + dimension-relevant geometry table rather than pointless alternate state
params=list(csv.DictReader(open(R/'data/V26_ARCHIVED_HFSS/THREE_DESIGNS_11_PARAMETERS.csv')))
a,b=params[0],params[1]
fig=plt.figure(figsize=(6.8,3.2));gs=fig.add_gridspec(1,2,width_ratios=[1,1.2],wspace=.35)
ax=fig.add_subplot(gs[0]);geometry(ax);native(ax);ax.set_title('(a) Optimised C033, state 03',loc='left',fontsize=9.5,weight='bold',color=NAVY);ax.set_xlabel('x (mm)');ax.set_ylabel('y (mm)')
ax=fig.add_subplot(gs[1]);ax.axis('off');ax.set_title('(b) Native parametric changes',loc='left',fontsize=9.5,weight='bold',color=NAVY)
selected=[('Front width (mm)','front_width_mm'),('Rear width (mm)','rear_width_mm'),('Rear rotation (°)','rear_angle_deg'),('Switch gap (mm)','switch_gap_mm'),('Rear scale','rear_shrink')]
vals=[[label,f"{float(a[k]):.2f}",f"{float(b[k]):.2f}"] for label,k in selected]
tab=ax.table(cellText=vals,colLabels=['Geometry parameter','Reference','C033'],loc='center',cellLoc='center',colWidths=[.56,.22,.22]);tab.auto_set_font_size(False);tab.set_fontsize(8);tab.scale(1,1.75)
for (i,j),cell in tab.get_celld().items():
 cell.set_edgecolor('#e0e7ea');cell.set_linewidth(.55)
 if i==0:cell.set_facecolor(NAVY);cell.get_text().set_color('white');cell.get_text().set_weight('bold')
 else:cell.set_facecolor('white' if i%2 else '#f5f8fa')
fig.text(.04,.01,'Solid polygons from the original HFSS copper export; orange = front Cu, teal = rear Cu.',fontsize=7.2,color=GREY)
save(fig,'F03_NATIVE_OPTIMISED_UNIT_CELL')
# Circuit schematic primitives, drawn as circuit not generic box schematic
fig=plt.figure(figsize=(12.6,4.0));gs=fig.add_gridspec(1,3,width_ratios=[1,1,1.52],wspace=.34)
a=fig.add_subplot(gs[0]);a.set_aspect('equal');a.set_xlim(-43,43);a.set_ylim(-43,43);a.add_patch(Rectangle((-41,-41),82,82,fc='#f7f8f9',ec=NAVY,lw=1))
for x in [-24,0,24]:
 for y in [-24,0,24]:native(a,x,y,True)
a.set_xticks([-41,0,41]);a.set_yticks([-41,0,41]);a.tick_params(labelsize=7);a.grid(alpha=.07);a.set_title('(a) HFSS finite 3×3 panel',fontsize=10,loc='left',weight='bold',color=NAVY);a.set_xlabel('x (mm)');a.set_ylabel('y (mm)')
b=fig.add_subplot(gs[1]);geometry(b);native(b);b.set_title('(b) Copper paths & switch sites',fontsize=10,loc='left',weight='bold',color=NAVY)
positions={}
for mask in (3,6,8,10,12,13):
 for sh in json.loads(Z.read(f'V416_CANDIDATES/C033/COPPER_M{mask:02d}.json'))['shapes']:
  if 'SWITCH' in sh['name']:
   idx=int(sh['name'].split('_')[2]);positions[idx]=np.array(sh['polygon']).mean(axis=0)
for k,p in sorted(positions.items()):
 b.add_patch(Circle(p,radius=1.45,fc='white',ec=NAVY,lw=.8));b.text(p[0],p[1],f'D{k+1}',ha='center',va='center',fontsize=7.1,weight='bold')
b.set_xlabel('x (mm)');b.set_ylabel('y (mm)')
c=fig.add_subplot(gs[2]);c.set_xlim(0,10);c.set_ylim(0,6.4);c.axis('off');c.set_title('(c) Coupled-resonator equivalent circuit',loc='left',fontsize=10,weight='bold',color=NAVY)
def wire(x1,y1,x2,y2,col=NAVY,lw=1.4):c.plot([x1,x2],[y1,y2],color=col,lw=lw,solid_capstyle='round')
def res(x,y,name):
 xs=np.linspace(x-.42,x+.42,9);ys=y+np.array([0,.14,-.14,.14,-.14,.14,-.14,.14,0]);c.plot(xs,ys,color=NAVY,lw=1.35);c.text(x,y+.31,name,ha='center',fontsize=8,color=NAVY)
def ind(x,y,name):
 # four semicircular turns continuing along x
 for off in [-.30,-.10,.10,.30]:c.add_patch(Arc((x+off,y),.2,.28,theta1=0,theta2=180,ec=NAVY,lw=1.4))
 c.text(x,y+.37,name,ha='center',fontsize=8,color=NAVY)
def cap(x,y,name):
 wire(x-.35,y,x-.09,y);wire(x-.07,y-.25,x-.07,y+.25);wire(x+.07,y-.25,x+.07,y+.25);wire(x+.09,y,x+.35,y);c.text(x,y+.36,name,ha='center',fontsize=7.8,color=NAVY)
# Front, rear each a closed resonant loop. gap capacitors in loops, with switch shunting the gap.
for y,mark,capname,ls,rname,col in [(4.65,'FRONT','C_g,f','L_f','R_f',ORANGE),(1.48,'REAR','C_g,r','L_r','R_r',TEAL)]:
 c.text(.18,y+.35,mark,fontsize=8.5,color=col,weight='bold')
 wire(1.05,y,1.57,y);res(1.91,y,rname);wire(2.33,y,2.73,y);ind(3.12,y,ls);wire(3.53,y,4.25,y);cap(4.61,y,capname);wire(4.96,y,7.9,y)
 wire(7.9,y,7.9,y-.72);wire(7.9,y-.72,1.05,y-.72);wire(1.05,y-.72,1.05,y)
 # switch parallel around capacitor (only one representative branch; four sites on two faces)
 wire(4.20,y,4.20,y+.79);wire(4.20,y+.79,4.57,y+.79)
 wire(4.66,y+.79,5.10,y+.79);wire(5.10,y+.79,5.10,y)
 c.add_patch(Circle((4.57,y+.79),radius=.065,fc='white',ec=NAVY,lw=1));c.add_patch(Circle((4.66,y+.79),radius=.065,fc='white',ec=NAVY,lw=1))
 c.text(5.22,y+.72,'D / bridge',fontsize=7,color=NAVY)
# capacitive interlayer coupling as shunt branch across front/rear loops
wire(8.58,4.65,8.58,3.43);wire(8.58,2.95,8.58,1.48)
c.plot([8.27,8.89],[3.40,3.40],color=NAVY,lw=1.6);c.plot([8.27,8.89],[2.98,2.98],color=NAVY,lw=1.6);c.text(8.83,3.60,r'$C_{fr}$',fontsize=9,color=NAVY)
wire(7.9,4.65,8.58,4.65);wire(7.9,1.48,8.58,1.48)
# mutual inductance magnetic interaction
c.annotate('',xy=(3.15,2.68),xytext=(3.15,3.75),arrowprops={'arrowstyle':'<->','lw':1.3,'linestyle':'dashed','color':GREY});c.text(3.33,3.1,r'$M_{fr}$',fontsize=9,color=NAVY)
c.text(1.25,.24,r'$Z_{g,k}^{-1}=j\omega C_{g,k}+Y_{D,k}(s)$   ·   $L/R$: trace loading',fontsize=8.1,color=GREY)
save(fig,'FINAL_F04_FINITE_PCB_METATOM_CIRCUIT')
# small switch-state truth table based on native bit mapping with meaningful rows
masks=[3,6,8,10,12,13]
fig,ax=plt.subplots(figsize=(4.7,2.65));ax.axis('off')
col=[f'D{k}' for k in range(1,5)]
data=[[f'{m:02d}']+[('CLOSED' if m&(1<<i) else 'OPEN') for i in range(4)] for m in masks]
tab=ax.table(cellText=data,colLabels=['Mask']+col,loc='center',cellLoc='center',colWidths=[.16,.21,.21,.21,.21]);tab.auto_set_font_size(False);tab.set_fontsize(7.3);tab.scale(1,1.35)
for (i,j),cell in tab.get_celld().items():
 cell.set_edgecolor('#e1e7eb');cell.set_linewidth(.55)
 if i==0:cell.set_facecolor(NAVY);cell.get_text().set_color('white');cell.get_text().set_weight('bold')
 elif j>0:cell.set_facecolor('#d5eeeb' if data[i-1][j]=='CLOSED' else '#f6f8f9');cell.get_text().set_color('#075c60' if data[i-1][j]=='CLOSED' else '#425462')
ax.set_title('Six HFSS analysis states · four conductor bridges',loc='left',weight='bold',color=NAVY,fontsize=9.5)
save(fig,'F05_SWITCHING_COMPACT')
# F06 experimental datapoints + photo split etc existing truthful bars from F06 retained
# extra fast-comprehensible numeric illustration derived from actual periodic condition 1.925 -> no invented HFSS numerical entry here
print('Figures created')
