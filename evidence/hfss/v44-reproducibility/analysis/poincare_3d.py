#!/usr/bin/env python3
"""Native HFSS-matrix 1,231-state independent-mesh reconstruction; 3D Poincare display."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
R=Path(__file__).resolve().parents[1];F=R/'figures';D=R/'analysis'
x=np.genfromtxt(D/'NEW_CROSS_MESH_RECONSTRUCTION.csv',delimiter=',',skip_header=1)
S=x[:,:4];e1=x[:,4];e2=x[:,5]
NAVY='#0d2036';TEAL='#00899a';ORANGE='#df7437';GRAY='#586879'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10.1,'font.weight':'normal','pdf.fonttype':42,'svg.fonttype':'none','axes.titlesize':11.3,'axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(14.3,4.85));gs=fig.add_gridspec(1,3,width_ratios=[1.10,1.02,.92],wspace=.23)
a=fig.add_subplot(gs[0,0],projection='3d');a.set_title('A  1,231-state Poincaré reconstruction',pad=6,color=NAVY,loc='left',fontweight='bold')
phi=np.linspace(0,2*np.pi,48);theta=np.linspace(0,np.pi,20)
xx=np.outer(np.cos(phi),np.sin(theta));yy=np.outer(np.sin(phi),np.sin(theta));zz=np.outer(np.ones_like(phi),np.cos(theta))
a.plot_wireframe(xx,yy,zz,rstride=6,cstride=5,alpha=.10,lw=.55,color='#52667c')
sc=a.scatter(S[:,1],S[:,2],S[:,3],c=e1,cmap='magma',s=9,alpha=.9,edgecolors='none',rasterized=True)
a.set_xlabel('$S_1$',labelpad=1);a.set_ylabel('$S_2$',labelpad=1);a.set_zlabel('$S_3$',labelpad=1)
a.view_init(elev=19,azim=-52);a.set_box_aspect((1,1,1));a.set_xlim(-1.1,1.1);a.set_ylim(-1.1,1.1);a.set_zlim(-1.1,1.1)
a.set_xticks([-1,0,1]);a.set_yticks([-1,0,1]);a.set_zticks([-1,0,1]);a.tick_params(labelsize=8,pad=0);a.grid(False)
for ax in [a.xaxis,a.yaxis,a.zaxis]:ax.pane.fill=False;ax.line.set_color('#cbd4dc')
cb=fig.colorbar(sc,ax=a,location='right',shrink=.65,pad=.03);cb.set_label('Full-vector error (%)',size=8);cb.ax.tick_params(labelsize=7)
b=fig.add_subplot(gs[0,1]);b.hist(e1,bins=37,color=TEAL,alpha=.78,label='P24 calibration / P27 response');b.hist(e2,bins=37,color=ORANGE,alpha=.52,label='P27 calibration / P24 response');b.legend(frameon=False,fontsize=8.5,loc='upper right');b.set_xlabel('Full-Stokes relative error (%)');b.set_ylabel('Input states');b.set_title('B  Cross-mesh error distributions',loc='left',fontweight='bold',color=NAVY);b.grid(axis='y',alpha=.18)
c=fig.add_subplot(gs[0,2]);c.axis('off');c.set_xlim(0,1);c.set_ylim(0,1);c.set_title('C  Calibration transfer summary',loc='left',fontweight='bold',color=NAVY)
for j,(h,d,col) in enumerate([('P24 calibration → P27 response',e1,TEAL),('P27 calibration → P24 response',e2,ORANGE)]):
 top=.91-.37*j
 c.add_patch(FancyBboxPatch((.015,top-.27),.945,.27,boxstyle='round,pad=.006',fc='#f5f8fb',ec='#cbd7df',lw=1.0))
 c.text(.06,top-.075,h,color=NAVY,weight='bold',fontsize=9.2)
 c.text(.06,top-.155,f'P95 {np.percentile(d,95):.1f}%',color=col,weight='bold',fontsize=13.3)
 c.text(.06,top-.225,f'Maximum {np.max(d):.1f}%',color=col,weight='bold',fontsize=10.5)
c.text(.025,.05,'Native 6×4 HFSS matrices; 5 mm plane, 1.850 GHz.\nNo new full-wave runs or artificial detector noise.',fontsize=8.8,color=GRAY)
for ext in ['pdf','png','svg']:
 fig.savefig(F/('FINAL_F09_STOKES_AND_POINCARE.'+ext),bbox_inches='tight',facecolor='white',dpi=215)
plt.close(fig)
