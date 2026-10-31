#!/usr/bin/env python3
"""Generate corrected vector figures 9–12 using only archived C033 numerical CSVs.

No HFSS solve, synthetic measurements, or unrecorded numerical data are introduced.
"""
from pathlib import Path
from itertools import combinations
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import MaxNLocator

BASE=Path(__file__).resolve().parents[1]
DATA=BASE/'data'; OUT=BASE/'figures'; OUT.mkdir(exist_ok=True)
INK='#19374C'; BLUE='#186E8B'; ORANGE='#CF7736'; GREY='#718091'; GREEN='#16817C'
plt.rcParams.update({
 'font.family':'DejaVu Sans','font.size':8.3,'axes.titlesize':9.0,'axes.labelsize':8.1,
 'xtick.labelsize':7.5,'ytick.labelsize':7.5,'legend.fontsize':7.3,
 'axes.titleweight':'semibold','axes.labelcolor':INK,'text.color':INK,
 'axes.edgecolor':'#566676','xtick.color':'#526274','ytick.color':'#526274',
 'pdf.fonttype':42,'ps.fonttype':42,'savefig.facecolor':'white',
 'axes.grid':False,'figure.facecolor':'white',
})
def style(ax,grid=True):
 for sp in ('top','right'):ax.spines[sp].set_visible(False)
 if grid: ax.grid(axis='y',color='#DDE6EB',lw=.55,alpha=.9,zorder=0)
def save(fig,name):
 fig.savefig(OUT/(name+'.pdf'),bbox_inches='tight',pad_inches=.045)
 fig.savefig(OUT/(name+'.png'),dpi=400,bbox_inches='tight',pad_inches=.045)
 plt.close(fig)

# Original calibrated C033 matrix at 1.925 GHz
A=pd.read_csv(DATA/'V42_C033_INSTRUMENT_MATRIX.csv').to_numpy(dtype=float)
assert A.shape==(6,4)
masks=np.array([3,6,8,10,12,13]); P=A/A[:,[0]]
assert np.linalg.matrix_rank(A)==4
assert np.isclose(np.linalg.cond(P),9.528217428,atol=.02)

# --- Figure 9: rank-order subsets *actually* ascending ---
S=np.array([[1, 1, 0,0],[1,-1, 0,0],[1,0,1,0],[1,0,-1,0],[1,0,0,1],[1,0,0,-1]],float).T
R=P@S
subs=pd.read_csv(DATA/'FOUR_STATE_SUBSETS.csv')
subs=subs.sort_values('condition_row_normalised',ascending=True).reset_index(drop=True)
assert len(subs)==15
assert subs.loc[0,'masks']=='3/6/8/13'
assert np.isclose(subs.loc[0,'condition_row_normalised'],7.633721292)
fig,(ax,bx)=plt.subplots(1,2,figsize=(7.16,2.75),gridspec_kw={'width_ratios':[1.18,1.0]},constrained_layout=True)
im=ax.imshow(R,cmap='YlGnBu',vmin=0,vmax=2,aspect='auto',interpolation='none')
ax.set_xticks(range(6),['H','V','+45°','−45°','R','L'])
ax.set_yticks(range(6),[f'{m:02d}' for m in masks])
ax.set_xlabel('Incident polarisation state');ax.set_ylabel('Switch mask')
ax.set_title('(a) Six HFSS measurement projections',pad=7)
for i in range(6):
 for j in range(6):
  v=R[i,j]; ax.text(j,i,f'{v:.2f}',fontsize=6.7,ha='center',va='center',color='white' if v>1.28 else INK)
cb=fig.colorbar(im,ax=ax,fraction=.035,pad=.015);cb.ax.tick_params(labelsize=7)
cb.set_label(r'$m_k/A_{k0}$',fontsize=7.4)
x=np.arange(1,16); cond=subs['condition_row_normalised'].to_numpy(float)
bx.scatter(x,cond,s=23,facecolor=BLUE,edgecolor='white',lw=.4,zorder=3)
bx.scatter([1],[cond[0]],s=55,facecolor=ORANGE,edgecolor=INK,lw=.6,zorder=4)
bx.axhline(np.linalg.cond(P),ls=(0,(4,3)),c=GREY,lw=1,label=f'Six-state κ = {np.linalg.cond(P):.2f}')
bx.annotate('Best four: 03/06/08/13',xy=(1,cond[0]),xytext=(2.4,24),fontsize=7,
 arrowprops=dict(arrowstyle='->',color=GREY,lw=.7))
bx.set_yscale('log');bx.set_xticks([1,3,5,7,9,11,13,15]);bx.set_xlim(.4,15.7)
bx.set_xlabel('Four-state subset (ranked best → worst)')
bx.set_ylabel(r'$\kappa_2(\widetilde{A}_4)$');bx.set_title('(b) All 15 four-state subsets',pad=7)
bx.legend(frameon=False,loc='upper left');style(bx)
save(fig,'FIG09_verified_ranked')

# --- Figure 10: raw gains are existing masks, not removed masks ---
full_trace=lambda M: float(np.trace(np.linalg.inv(M.T@M)))
rpen=[];npen=[]
for i in range(6):
 rpen.append(full_trace(np.delete(A,i,0))/full_trace(A))
 npen.append(full_trace(np.delete(P,i,0))/full_trace(P))
rpen=np.array(rpen); npen=np.array(npen)
assert np.isclose(rpen[1],21.44,rtol=.002),rpen[1]
assert np.isclose(npen[1],86.41,rtol=.002),npen[1]
fig,(ax,bx)=plt.subplots(2,1,figsize=(3.55,4.82),constrained_layout=True)
xx=np.arange(6)
ax.plot(xx,A[:,0],'-o',c=BLUE,ms=4,lw=1.7)
ax.set_xticks(xx,[f'{m:02d}' for m in masks]);ax.set_ylim(0,.51)
ax.set_xlabel('Existing switch mask');ax.set_ylabel(r'Raw gain $A_{k0}$')
ax.set_title('(a) Receiving strength of the six states',pad=7)
ax.annotate('06: weakest gain',xy=(1,A[1,0]),xytext=(1.75,.16),fontsize=7.2,
 arrowprops=dict(arrowstyle='->',color=GREY,lw=.8))
style(ax)
bx.plot(xx,rpen,'-o',c=BLUE,lw=1.55,ms=4,label='Equal raw-output variance')
bx.plot(xx,npen,'--s',c=ORANGE,lw=1.4,ms=4,label='Equal normalised-output variance')
bx.set_yscale('log');bx.set_ylim(.85,135)
bx.set_xticks(xx,[f'{m:02d}' for m in masks]);bx.set_xlabel('Removed switch mask')
bx.set_ylabel('Inverse-trace penalty vs full set')
bx.set_title('(b) Cost of deleting each state',pad=7)
bx.annotate(f'{rpen[1]:.1f}×',xy=(1,rpen[1]),xytext=(1.36,9),fontsize=7.2,color=BLUE)
bx.annotate(f'{npen[1]:.1f}×',xy=(1,npen[1]),xytext=(1.36,105),fontsize=7.2,color=ORANGE)
bx.legend(frameon=False,loc='upper right',fontsize=6.8)
style(bx)
save(fig,'FIG10_verified_gain')

# --- Figure 11: independently select best equal-dwell and best optimised-dwell each n ---
budget=pd.read_csv(DATA/'V44_FIXED_BUDGET_ALL_SUBSETS.csv')
by=[]
for n in (4,5,6):
 d=budget[budget.state_count==n]
 eq=d.loc[d.equal_time_trace.idxmin()]
 opt=d.loc[d.optimised_trace.idxmin()]
 by.append((n,eq,opt))
assert by[1][1]['masks']=='3/6/8/10/13' and by[1][2]['masks']=='3/6/8/12/13'
base=float(budget.loc[budget.state_count==6,'equal_time_trace'].iloc[0])
xx=np.array([n for n,_,_ in by]); eq=np.array([float(e.equal_time_trace) for _,e,_ in by])/base
op=np.array([float(o.optimised_trace) for _,_,o in by])/base
fig,(ax,bx)=plt.subplots(1,2,figsize=(7.16,2.72),constrained_layout=True,
 gridspec_kw={'width_ratios':[1.16,1.0]})
ax.plot(xx,eq,'--o',color=BLUE,ms=4.6,lw=1.55,label='Best equal dwell')
ax.plot(xx,op,'-s',color=ORANGE,ms=4.3,lw=1.6,label='Best optimised dwell')
ax.axhline(1,lw=.85,color=GREY,ls=':')
ax.set_xticks([4,5,6]);ax.set_ylim(.47,1.1)
ax.set_ylabel(r'$J/J_{6,\mathrm{equal}}$');ax.set_xlabel('Number of selected states')
ax.set_title('(a) Fair fixed-budget comparison',pad=7)
ax.legend(frameon=False,loc='upper left',fontsize=7.0)
ax.annotate('Five-state sets differ',xy=(5,op[1]),xytext=(4.10,.67),fontsize=6.9,
 arrowprops=dict(arrowstyle='->',color=GREY,lw=.65))
style(ax)
# panel b: show true optimal six-state dwell fractions
row=budget[budget.state_count==6].iloc[0]
fr=np.array([float(s) for s in row.optimal_fractions.split('/')])
assert abs(fr.sum()-1)<1e-5
bx.vlines(np.arange(6),0,fr,lw=4,color=BLUE,zorder=3)
bx.scatter(np.arange(6),fr,s=20,c=BLUE,zorder=4)
bx.axhline(1/6,ls='--',color=ORANGE,lw=1,label='Equal dwell')
bx.set_xticks(np.arange(6),[f'{m:02d}' for m in masks])
bx.set_ylim(0,.54);bx.set_xlabel('Switch mask');bx.set_ylabel('Fraction of acquisition time')
bx.set_title('(b) Optimised six-state schedule',pad=7)
bx.legend(frameon=False,loc='upper right',fontsize=7.0);style(bx)
save(fig,'FIG11_verified_budget')

# --- Figure 12: markers represent actual recorded pass and fail statuses ---
mesh=pd.read_csv(DATA/'MESH_VERIFICATION_BY_FREQUENCY.csv')
assert set(mesh.candidate)=={'C033','C015'}
fig,axs=plt.subplots(1,2,figsize=(7.16,2.7),constrained_layout=True,sharey=True)
for i,(ax,candidate) in enumerate(zip(axs,['C033','C015'])):
 d=mesh[mesh.candidate==candidate].sort_values('GHz')
 x=d.GHz.to_numpy(float)
 v1=d.condition_M110.to_numpy(float);v2=d.condition_M125.to_numpy(float)
 passing=(d.status=='PASS_DUAL_MESH').to_numpy(bool)
 ax.plot(x,v1,'-',lw=1.5,color=BLUE,zorder=1)
 ax.plot(x,v2,'-',lw=1.5,color=ORANGE,zorder=1)
 for v,color in [(v1,BLUE),(v2,ORANGE)]:
  ax.scatter(x[passing],v[passing],facecolor=color,edgecolor=color,s=21,zorder=4,marker='o',lw=.5)
  ax.scatter(x[~passing],v[~passing],facecolor='white',edgecolor=color,s=25,zorder=4,marker='o',lw=1.15)
 ax.axhline(35,c=GREY,ls=(0,(3,2)),lw=1.0,zorder=0)
 ax.set_xlim(min(x)-.014,max(x)+.014)
 ax.set_ylim(6,51)
 ax.xaxis.set_major_locator(MaxNLocator(6))
 ax.set_xlabel('Frequency (GHz)')
 ax.set_title(f'({"a" if i==0 else "b"}) {candidate}: two independent meshes',pad=7)
 style(ax)
axs[0].set_ylabel(r'Row-normalised $\kappa_2$')
legend=[Line2D([0],[0],color=BLUE,lw=1.5,label='M110'),Line2D([0],[0],color=ORANGE,lw=1.5,label='M125'),
 Line2D([0],[0],marker='o',markerfacecolor=INK,markeredgecolor=INK,linestyle='none',markersize=4.6,label='Passed gate'),
 Line2D([0],[0],marker='o',markerfacecolor='white',markeredgecolor=INK,linestyle='none',markersize=4.6,label='Failed gate')]
fig.legend(handles=legend,loc='upper center',bbox_to_anchor=(.5,1.075),ncol=4,frameon=False,fontsize=7)
save(fig,'FIG12_verified_mesh')

pd.DataFrame({'n_states':xx,'best_equal_masks':[e['masks'] for _,e,_ in by],
 'best_equal_trace':[float(e.equal_time_trace) for _,e,_ in by],
 'best_optimised_masks':[o['masks'] for _,_,o in by],
 'best_optimised_trace':[float(o.optimised_trace) for _,_,o in by]}).to_csv(BASE/'data'/'CORRECTED_SUBSET_COMPARISON.csv',index=False)
print('PASS: four vector figures; state ordering, mask costs, dwell-optimum distinction, mesh status verified')
print('Best five-state equal vs optimal:',by[1][1]['masks'],by[1][2]['masks'])
