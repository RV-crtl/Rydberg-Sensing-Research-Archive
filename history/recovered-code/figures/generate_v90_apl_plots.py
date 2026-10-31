from pathlib import Path
import os, numpy as np
from PIL import Image
os.environ.setdefault('MPLCONFIGDIR','/tmp/mplconfig_v90')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.gridspec import GridSpec

BASE=Path(__file__).resolve().parent
A=BASE/'assets'; A.mkdir(exist_ok=True)

# AIP/APL-inspired graphics grammar:
# - sans-serif, consistent lettering/line weight
# - panel labels (a), (b)
# - experiment = symbols; simulations/models = continuous/dashed lines or fields
# - legends outside data whenever practical
# - line styles remain distinguishable in greyscale
plt.rcParams.update({
    'font.family':'DejaVu Sans',
    'font.size':12.4,
    'axes.titlesize':13.6,
    'axes.labelsize':12.5,
    'xtick.labelsize':10.8,
    'ytick.labelsize':10.8,
    'axes.linewidth':1.0,
    'lines.linewidth':2.0,
    'pdf.fonttype':42,
    'ps.fonttype':42,
    'legend.fontsize':10.3,
})

NAVY='#075078'; BLUE='#2B6CB0'; TEAL='#159DA5'; GOLD='#D99400'; MAG='#C83771'; GREY='#6A7883'; LIGHT='#D7E8F1'; INK='#17324D'

# Shared Poincare sphere mesh
u=np.linspace(0,2*np.pi,72); v=np.linspace(0,np.pi,40)
XS=np.outer(np.cos(u),np.sin(v)); YS=np.outer(np.sin(u),np.sin(v)); ZS=np.outer(np.ones_like(u),np.cos(v))

# Utility: panel label in axes coordinates
def panel_label(ax, label, x=-0.10, y=1.06):
    kw=dict(fontsize=14.5,fontweight='bold',va='top',ha='left',clip_on=False,color='black')
    if hasattr(ax, 'text2D'):
        ax.text2D(x,y,label,transform=ax.transAxes,**kw)
    else:
        ax.text(x,y,label,transform=ax.transAxes,**kw)

def clean_axes(ax):
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.tick_params(direction='out',length=4,width=1)

# ---------------------------------------------------------------------
# BLOCK 3: experiment + photograph
# Experimental data are explicit symbols. The smooth line is a guide to eye,
# not a simulated/model curve.
# ---------------------------------------------------------------------
angles=np.array([0.,45.,90.]); power=np.array([-5.9,-7.2,-15.6])
xx=np.linspace(0,90,400); coef=np.polyfit(angles,power,2); yy=np.polyval(coef,xx)
photo_path=Path('/mnt/data/shared image (12) (1).jpg')
img=Image.open(photo_path).convert('RGB')
# Crop with generous margin so the analyser is not cut at the poster boundary.
# Keeps the physical context while prioritising the rod grid and sensor PCB.
crop=img.crop((420,0,1510,1450))

fig=plt.figure(figsize=(11.7,5.15),dpi=350,constrained_layout=True)
gs=GridSpec(1,2,figure=fig,width_ratios=[1.63,1.0],wspace=.06)
ax=fig.add_subplot(gs[0,0])
# guide-to-eye line first
ax.plot(xx,yy,color=TEAL,lw=2.6,label='guide to eye',zorder=2)
# measured points on top
ax.plot(angles,power,linestyle='None',marker='o',markersize=8.2,
        markerfacecolor='white',markeredgecolor=NAVY,markeredgewidth=2.0,
        label='experiment',zorder=4)
ax.set_xlim(-3,93); ax.set_ylim(-16.7,-5.0)
ax.set_xticks([0,45,90])
ax.set_xlabel('Prepared linear polarization angle (deg)')
ax.set_ylabel('Power relative to open path (dB)')

clean_axes(ax)
# Legend above axes, never over data
handles=[
    Line2D([0],[0],marker='o',linestyle='None',markersize=7,markerfacecolor='white',markeredgecolor=NAVY,markeredgewidth=1.8,label='experiment'),
    Line2D([0],[0],color=TEAL,lw=2.4,label='guide to eye'),
]
ax.legend(handles=handles,loc='lower center',bbox_to_anchor=(0.5,1.015),ncol=2,frameon=False,borderaxespad=0.0)
panel_label(ax,'(a)',x=-0.08,y=1.035)

axp=fig.add_subplot(gs[0,1]); axp.imshow(crop); axp.axis('off')

panel_label(axp,'(b)',x=-0.02,y=1.035)
fig.savefig(A/'block3_apl_v90.pdf',bbox_inches='tight',pad_inches=.025)
fig.savefig(A/'block3_apl_v90.png',bbox_inches='tight',pad_inches=.025,facecolor='white')
plt.close(fig)

# ---------------------------------------------------------------------
# BLOCK 4: analytic geometry + exact analytic error map
# ---------------------------------------------------------------------
fig=plt.figure(figsize=(11.7,5.15),dpi=350,constrained_layout=True)
gs=GridSpec(1,2,figure=fig,width_ratios=[1,1],wspace=.05)
ax=fig.add_subplot(gs[0,0],projection='3d')
ax.plot_wireframe(XS,YS,ZS,rstride=6,cstride=6,color=LIGHT,lw=.55,alpha=.8)
t=np.linspace(0,2*np.pi,360)
ax.plot(np.cos(t),np.sin(t),0*t,color=TEAL,lw=3.0)
states=[((1,0,0),'H','#D84A4A'),((-1,0,0),'V','#D84A4A'),((0,1,0),'D',GOLD),((0,-1,0),'A',GOLD),((0,0,1),'RCP',MAG),((0,0,-1),'LCP',NAVY)]
# hand-tuned label offsets for no collisions
label_pos={'H':(1.15,.02,.05),'V':(-1.18,.02,.02),'D':(.02,1.18,.02),'A':(.02,-1.18,.02),'RCP':(.04,.02,1.18),'LCP':(.04,.02,-1.18)}
for p,lab,c in states:
    ax.scatter(*p,s=92,color=c,edgecolor='black',linewidth=.7,zorder=4)
    ax.text(*label_pos[lab],lab,fontsize=10.8,fontweight='bold',ha='center',va='center')
ax.plot([0,0],[0,0],[-1.08,1.08],ls='--',lw=1.7,color=GREY)

ax.set_xlim(-1.1,1.1);ax.set_ylim(-1.1,1.1);ax.set_zlim(-1.1,1.1);ax.set_box_aspect((1,1,1));ax.view_init(18,35);ax.set_axis_off()
panel_label(ax,'(a)',x=-0.04,y=1.025)

ax2=fig.add_subplot(gs[0,1])
psi=np.linspace(-90,90,241);chi=np.linspace(-45,45,181);P,C=np.meshgrid(psi,chi);err=2*np.abs(C)
im=ax2.imshow(err,origin='lower',extent=[-90,90,-45,45],aspect='auto',cmap='magma',vmin=0,vmax=90)
ax2.axhline(0,color='#00D8FF',lw=2.1,label=r'$S_3=0$ equator')
ax2.set_xlabel(r'Polarization azimuth, $\psi$ (deg)')
ax2.set_ylabel(r'Ellipticity, $\chi$ (deg)')

clean_axes(ax2)
ax2.legend(loc='lower center',bbox_to_anchor=(.5,1.015),frameon=False,borderaxespad=0.0)
cbar=fig.colorbar(im,ax=ax2,pad=.018);cbar.set_label('Angular error (deg)');cbar.ax.tick_params(labelsize=10)
panel_label(ax2,'(b)',x=-0.12,y=1.035)
fig.savefig(A/'block4_apl_v90.pdf',bbox_inches='tight',pad_inches=.025)
fig.savefig(A/'block4_apl_v90.png',bbox_inches='tight',pad_inches=.025,facecolor='white')
plt.close(fig)

# ---------------------------------------------------------------------
# BLOCK 5: tetrahedral geometry + deterministic Monte Carlo simulation
# ---------------------------------------------------------------------
rng=np.random.default_rng(20260921);N=50000
sv=rng.normal(size=(N,3));sv/=np.linalg.norm(sv,axis=1,keepdims=True);S=np.c_[np.ones(N),sv]
lin_an=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0]],float)
tet_an=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)/np.sqrt(3)
can_an=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],float)
def M(an):return .5*np.c_[np.ones(len(an)),an]
sigmas=np.array([0,.005,.01,.02,.04,.06,.08])
def sim(an):
    A_=M(an);pinv=np.linalg.pinv(A_);q=S@A_.T;med=[]
    for sig in sigmas:
        qn=q+rng.normal(scale=sig,size=q.shape);Sh=qn@pinv.T
        vv=Sh[:,1:]/Sh[:,[0]];n=np.linalg.norm(vv,axis=1);ok=n>1e-12;vv[ok]/=n[ok,None]
        dots=np.clip(np.sum(vv*sv,axis=1),-1,1);med.append(np.median(np.degrees(np.arccos(dots))))
    return np.array(med)
lin_err=sim(lin_an);tet_err=sim(tet_an);can_err=sim(can_an)

fig=plt.figure(figsize=(11.7,5.15),dpi=350,constrained_layout=True)
gs=GridSpec(1,2,figure=fig,width_ratios=[1,1],wspace=.06)
ax=fig.add_subplot(gs[0,0],projection='3d')
ax.plot_wireframe(XS,YS,ZS,rstride=6,cstride=6,color=LIGHT,lw=.55,alpha=.8)
pts=tet_an.copy();cols=['#D84A4A',TEAL,GOLD,'#6B5AA6'];labs=['00','01','10','11']
for i in range(4):
    for j in range(i+1,4):ax.plot(*zip(pts[i],pts[j]),color='#75B9D3',lw=1.4,alpha=.9)
for p,c,l in zip(pts,cols,labs):
    ax.scatter(*p,s=96,color=c,edgecolor='black',lw=.7,zorder=4);ax.text(*(p*1.14),l,fontsize=10.7,fontweight='bold')

ax.set_xlim(-1.1,1.1);ax.set_ylim(-1.1,1.1);ax.set_zlim(-1.1,1.1);ax.set_box_aspect((1,1,1));ax.view_init(20,38);ax.set_axis_off()
panel_label(ax,'(a)',x=-0.04,y=1.025)

ax2=fig.add_subplot(gs[0,1]);noise=sigmas*100
# simulation lines distinguished by colour, linestyle, and marker
ax2.plot(noise,lin_err,'s:',ms=5.2,lw=2.0,color=NAVY,label='linear H/V/D/A')
ax2.plot(noise,tet_err,'o-',ms=5.2,lw=2.2,color=GOLD,label='tetrahedral 4-state')
ax2.plot(noise,can_err,'^--',ms=5.2,lw=2.0,color=TEAL,label='canonical 6-state')
ax2.set_xlim(0,8.1);ax2.set_ylim(0,33)
ax2.set_xlabel(r'Gaussian readout noise, $\sigma_q/S_0$ (%)')
ax2.set_ylabel('Median Stokes angular error (deg)')

clean_axes(ax2)
# legend above axes, outside data region
ax2.legend(loc='lower center',bbox_to_anchor=(.5,1.015),ncol=3,frameon=False,borderaxespad=0.0,handlelength=2.4,columnspacing=.9)
panel_label(ax2,'(b)',x=-0.12,y=1.035)
fig.savefig(A/'block5_apl_v90.pdf',bbox_inches='tight',pad_inches=.025)
fig.savefig(A/'block5_apl_v90.png',bbox_inches='tight',pad_inches=.025,facecolor='white')
plt.close(fig)

(base_stats:=BASE/'simulation_stats_v90.txt').write_text(
    f'N={N}\nseed=20260921\n'
    f'tetra_rank={np.linalg.matrix_rank(M(tet_an))}\n'
    f'tetra_condition={np.linalg.cond(M(tet_an)):.8f}\n'
    f'tetra_median_error_1pct_deg={tet_err[2]:.6f}\n'
    f'canonical_median_error_1pct_deg={can_err[2]:.6f}\n'
    f'linear_median_error_0pct_deg={lin_err[0]:.6f}\n'
)

# ---------------------------------------------------------------------
# BLOCK 6: experimental bias points + reduced-order model heatmap
# ---------------------------------------------------------------------
B=np.array([0.00,0.22,0.44,0.66,0.88,1.10,1.32,1.54,1.76,1.98,2.20])
Y=np.array([-29.06,-28.20,-26.91,-26.08,-24.47,-25.63,-25.34,-26.29,-26.31,-23.83,-25.91])
fig=plt.figure(figsize=(11.7,5.15),dpi=350,constrained_layout=True)
gs=GridSpec(1,2,figure=fig,width_ratios=[1,1],wspace=.08)
ax=fig.add_subplot(gs[0,0])
# experimental symbols; thin line only as visual guide
ax.plot(B,Y,'o-',ms=6.0,lw=1.25,color=GREY,markerfacecolor='white',markeredgecolor=NAVY,markeredgewidth=1.6,label='experiment')
ax.axhline(-29.06,color='#7E8F9A',ls='--',lw=1.5,label='initial no-bias reference')
ax.axhline(-25.28,color=MAG,ls='-.',lw=1.5,label='final no-bias mean')
ax.set_xlim(-.06,2.28);ax.set_ylim(-29.8,-23.25)
ax.set_xlabel(r'Calibrated magnetic bias, $B_0$ (mT)')
ax.set_ylabel('Recorded level (dBm)')

clean_axes(ax)
ax.legend(loc='lower center',bbox_to_anchor=(.5,1.015),ncol=1,frameon=False,borderaxespad=0.0,handlelength=2.5)
panel_label(ax,'(a)',x=-0.10,y=1.035)

ax2=fig.add_subplot(gs[0,1])
b=np.linspace(0,1.05,380);d=np.linspace(-18,18,380);BB,DD=np.meshgrid(b,d);muB_h=13.996;width=.90
sig=lambda c:np.exp(-.5*((DD-c)/width)**2)
resp=1.15*sig(muB_h*BB)+.85*sig(0*BB)+1.15*sig(-muB_h*BB)
im=ax2.imshow(resp,origin='lower',extent=[0,1.05,-18,18],aspect='auto',cmap='magma')
# reserve a blank right strip for labels so text never covers the field map
ax2.set_xlim(0,1.19)
for y,lab in [(13.3,r'$\sigma^+$'),(0,r'$\pi$'),(-13.3,r'$\sigma^-$')]:
    ax2.text(1.09,y,lab,color=INK,fontsize=13,fontweight='bold',ha='center',va='center',clip_on=False)
ax2.set_xlabel(r'Magnetic bias, $B_0$ (mT)')
ax2.set_ylabel('Probe detuning (MHz)')

clean_axes(ax2)
cbar=fig.colorbar(im,ax=ax2,pad=.015);cbar.set_label('Relative spectral response');cbar.ax.tick_params(labelsize=10)
panel_label(ax2,'(b)',x=-0.10,y=1.035)
fig.savefig(A/'block6_apl_v90.pdf',bbox_inches='tight',pad_inches=.025)
fig.savefig(A/'block6_apl_v90.png',bbox_inches='tight',pad_inches=.025,facecolor='white')
plt.close(fig)

# ---------------------------------------------------------------------
# BLOCK 8: ideal analyser model + validation states
# ---------------------------------------------------------------------
canonical=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],float)
At=M(tet_an);Scan=np.c_[np.ones(6),canonical];Q=(Scan@At.T).T
fig=plt.figure(figsize=(10.9,5.0),dpi=350,constrained_layout=True)
gs=GridSpec(1,2,figure=fig,width_ratios=[1.15,.85],wspace=.05)
ax=fig.add_subplot(gs[0,0])
im=ax.imshow(Q,cmap='YlGnBu',vmin=0,vmax=1,aspect='auto')
ax.set_xticks(range(6));ax.set_xticklabels(['H','V','D','A','RCP','LCP'])
ax.set_yticks(range(4));ax.set_yticklabels(['00','01','10','11'])
ax.set_xlabel('Reference input polarization');ax.set_ylabel('Analyser state')

for i in range(4):
    for j in range(6):
        val=Q[i,j];ax.text(j,i,f'{val:.2f}',ha='center',va='center',fontsize=11.4,fontweight='bold',color='white' if val>.58 else INK)
clean_axes(ax);panel_label(ax,'(a)',x=-0.12,y=1.025)

ax2=fig.add_subplot(gs[0,1],projection='3d')
ax2.plot_wireframe(XS,YS,ZS,rstride=6,cstride=6,color=LIGHT,lw=.55,alpha=.8)
state_map={'H':(1,0,0),'V':(-1,0,0),'D':(0,1,0),'A':(0,-1,0),'RCP':(0,0,1),'LCP':(0,0,-1)}
col={'H':'#D84A4A','V':'#D84A4A','D':TEAL,'A':TEAL,'RCP':MAG,'LCP':NAVY}
for lab,p in state_map.items():
    ax2.scatter(*p,s=86,color=col[lab],edgecolor='black',lw=.7)
    ax2.text(*(np.array(p)*1.16),lab,fontsize=10.1,fontweight='bold')

ax2.set_xlim(-1.1,1.1);ax2.set_ylim(-1.1,1.1);ax2.set_zlim(-1.1,1.1);ax2.set_box_aspect((1,1,1));ax2.view_init(18,38);ax2.set_axis_off();panel_label(ax2,'(b)',x=-0.02,y=1.025)
fig.savefig(A/'block8_apl_v90.pdf',bbox_inches='tight',pad_inches=.025)
fig.savefig(A/'block8_apl_v90.png',bbox_inches='tight',pad_inches=.025,facecolor='white')
plt.close(fig)

print('Generated APL-style v90 figures')