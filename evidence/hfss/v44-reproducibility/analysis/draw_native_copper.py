#!/usr/bin/env python3
"""Render EXACT polygons from archived HFSS COPPER_Mxx JSON (not illustrative trace drawings)."""
import zipfile,json,csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Rectangle,Circle
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parents[1];F=R/'figures'
Z=zipfile.ZipFile(R/'source_evidence/V418_NATIVE_HFSS_RETURN_COMPACT.zip')
NAVY='#11273d';ORANGE='#e28237';TEAL='#008899';GRAY='#627484'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titleweight':'bold','pdf.fonttype':42,'svg.fonttype':'none','axes.spines.top':False,'axes.spines.right':False})
def native(id,mask):return json.loads(Z.read(f'V416_CANDIDATES/{id}/COPPER_M{mask:02d}.json'))
def polys(ax,geom,dx=0,dy=0,alpha=1,mini=False):
 for sh in geom['shapes']:
  points=np.array(sh['polygon']) + [dx,dy]; c=ORANGE if sh['layer']=='TOP' else TEAL
  ax.add_patch(Polygon(points,closed=True,fc=c,ec='white',lw=.18 if mini else .33,alpha=alpha))
def setup(ax,title=None):
 ax.set_aspect('equal');ax.set_xlim(-12.1,12.1);ax.set_ylim(-12.1,12.1)
 ax.set_xticks([-12,-6,0,6,12]);ax.set_yticks([-12,-6,0,6,12]);ax.grid(alpha=.12)
 ax.tick_params(labelsize=7.6)
 if title:ax.set_title(title,color=NAVY,pad=10,fontsize=11)
 ax.set_xlabel('x (mm)',fontsize=9);ax.set_ylabel('y (mm)',fontsize=9)
def finish(fig,key):
 for ext in ['pdf','svg']:
  fig.savefig(F/(key+'.'+ext),bbox_inches='tight',facecolor='white',pad_inches=.10)
 fig.savefig(F/(key+'.png'),bbox_inches='tight',facecolor='white',dpi=230,pad_inches=.10)
 plt.close(fig)
# frozen exact polygon source (candidate, switch state=03) - 2 candidates + 11 normalized geometry params
fig=plt.figure(figsize=(14.2,4.65));gs=fig.add_gridspec(1,3,width_ratios=[1,1,1.58],wspace=.27)
for i,ident in enumerate(['C033','C015']):
 a=fig.add_subplot(gs[0,i]);setup(a,('A' if i==0 else 'B')+('  Bandwidth-optimised' if i==0 else '  High-band alternative'))
 a.add_patch(Rectangle((-12,-12),24,24,fc='#f7f9fa',ec=NAVY,lw=.8,zorder=-5))
 polys(a,native(ident,3))
 # Geometry shown in exact source coordinate frame; state specified in caption.

a=fig.add_subplot(gs[0,2]);a.set_title('C  Geometry parameters relative to baseline',loc='left',fontsize=11,pad=10,color=NAVY)
params=list(csv.DictReader(open(R/'data/V26_ARCHIVED_HFSS/THREE_DESIGNS_11_PARAMETERS.csv')))
keys=['top_x_scale','top_y_scale','rear_x_scale','rear_y_scale','front_width_mm','rear_width_mm','rear_angle_deg','rear_shrink','switch_gap_mm','gap_fraction_1','gap_fraction_2']
labels=['Front x-scale','Front y-scale','Rear x-scale','Rear y-scale','Front width','Rear width','Rear angle','Rear shrink','Switch gap','Gap position 1','Gap position 2']
vals=np.array([[float(p[k]) for k in keys] for p in params]);delta=(vals[1:]/vals[0]-1)*100
im=a.imshow(delta,cmap='PuOr',vmin=-25,vmax=25,aspect='auto');a.set_xticks(range(len(labels)),labels,fontsize=8,rotation=48,ha='right');a.set_yticks([0,1],['Optimised','Alternative'],fontsize=9)
for j in range(2):
 for k in range(11):a.text(k,j,f'{delta[j,k]:+.1f}',ha='center',va='center',color='white' if abs(delta[j,k])>15 else NAVY,fontsize=7.2)
cb=fig.colorbar(im,ax=a,shrink=.78,pad=.025);cb.set_label('Change (%)',fontsize=8.5)
fig.text(.03,.005,'Native HFSS geometry: COPPER_M03.json for both candidates. Orange: front Cu; teal: rear Cu. Identical 24-mm periodic cell.',color=GRAY,fontsize=9)
finish(fig,'FINAL_F03_DESIGN_EVOLUTION')
# Exact state 03 native polygons in panel; state code labels for all site positions
fig=plt.figure(figsize=(14.3,4.75));gs=fig.add_gridspec(1,3,width_ratios=[.99,.93,1.13],wspace=.27)
a=fig.add_subplot(gs[0,0]);a.set_aspect('equal');a.set_xlim(-43,43);a.set_ylim(-46,44)
a.set_title('A  Nine exact HFSS meta-atoms',loc='left',color=NAVY,pad=9)
a.add_patch(Rectangle((-41,-41),82,82,fc='#f6f8fa',ec=NAVY,lw=.9))
g=native('C033',3)
for ix in [-24,0,24]:
 for iy in [-24,0,24]:polys(a,g,ix,iy,mini=True)
a.set_xticks([-41,-24,0,24,41]);a.set_yticks([-41,-24,0,24,41]);a.tick_params(labelsize=8);a.set_xlabel('x (mm)');a.set_ylabel('y (mm)');a.grid(alpha=.08)
b=fig.add_subplot(gs[0,1]);setup(b,'B  Native copper and switch gaps')
polys(b,g)
# identify active switch sites using polygons from all available masks
positions={}
for mask in [3,6,8,10,12,13]:
 for sh in native('C033',mask)['shapes']:
  if 'SWITCH' in sh['name']:
   idx=int(sh['name'].split('_')[2]);positions[idx]=np.array(sh['polygon']).mean(axis=0)
for k,p in sorted(positions.items()):
 b.add_patch(Circle(p,radius=1.4,fill=True,fc='white',ec=NAVY,lw=.8))
 b.text(*p,f'D{k+1}',ha='center',va='center',fontsize=7.5,color=NAVY,weight='bold')
c=fig.add_subplot(gs[0,2]);c.set_xlim(0,1);c.set_ylim(0,1);c.axis('off')
c.set_title('C  Field sampling and material stack',loc='left',color=NAVY,pad=9)
for y,width,height,color,label in [(.82,.64,.035,ORANGE,'Front copper'),(.64,.64,.18,'#d4ddca','Dielectric · 1.6 mm'),(.605,.64,.035,TEAL,'Rear copper')]:
 c.add_patch(Rectangle((.065,y),width,height,fc=color,ec='none'))
 c.text(.74,y+height/2,label,va='center',fontsize=9.5,color=NAVY)
c.annotate('',xy=(.34,.31),xytext=(.34,.565),arrowprops=dict(arrowstyle='->',color='#cf992b',lw=2))
c.add_patch(Rectangle((.105,.18),.57,.115,fc='#e5f5f3',ec='#8cbab6',lw=1))
c.text(.39,.24,'70 × 50 mm sensing plane',ha='center',va='center',color=NAVY,fontsize=10)
c.text(.39,.075,'5, 10, 20 and 50 mm behind board',ha='center',color=GRAY,fontsize=9.2)
fig.text(.03,.01,'Geometry is reconstructed directly from frozen C033/M03 native HFSS copper-polygon export; no CAD paths were invented.',color=GRAY,fontsize=8.7)
finish(fig,'FINAL_F04_FINITE_PCB_METATOM_CIRCUIT')
print('Native copper figure update complete; D positions:',positions)
