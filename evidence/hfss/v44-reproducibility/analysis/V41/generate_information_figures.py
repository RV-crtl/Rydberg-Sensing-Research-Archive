# Recreate new information-geometry figures and machine-readable data from the embedded source archives.
from pathlib import Path
import zipfile,json,itertools,csv,io
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
root=Path(__file__).resolve().parents[2]
F=root/'figures'
Z=zipfile.ZipFile(root/'source_evidence/mix_results_20261025.zip')
audit=json.loads(Z.read('V418_RESULTS/DATA/C033_EQUATION_VERDICT_1.9250.json'))
A=np.asarray(audit['instrument'],float)
P=A/A[:,[0]]
masks=[3,6,8,10,12,13]
colors={'navy':'#1b344a','teal':'#097f85','gold':'#bb722f','muted':'#667788','red':'#af4a53'}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'pdf.fonttype':42,'axes.labelcolor':colors['navy'],'text.color':colors['navy'],'xtick.color':colors['navy'],'ytick.color':colors['navy'],'axes.spines.top':False,'axes.spines.right':False})
def save(fig,name):
    fig.savefig(F/(name+'.pdf'),bbox_inches='tight',pad_inches=.06)
    fig.savefig(F/(name+'.png'),dpi=260,bbox_inches='tight',pad_inches=.06)
    plt.close(fig)
# 1 Exact complex-response projection outcomes (not optical measurement)
inputs={
 'H':np.array([1,1,0,0]),
 'V':np.array([1,-1,0,0]),
 '+45°':np.array([1,0,1,0]),
 '−45°':np.array([1,0,-1,0]),
 'R':np.array([1,0,0,1]),
 'L':np.array([1,0,0,-1])}
resp=np.column_stack([P@v for v in inputs.values()])
assert resp.min()>=-1e-10,resp.min()
fig,axes=plt.subplots(1,2,figsize=(7.1,3.0),gridspec_kw={'width_ratios':[1.13,.87]})
ax=axes[0]
im=ax.imshow(resp,cmap='YlGnBu',vmin=0,vmax=2,aspect='auto')
ax.set_yticks(range(6),[f'{m:02d}' for m in masks]);ax.set_xticks(range(6),list(inputs));ax.set_ylabel('HFSS switch mask')
ax.set_title('(a) Normalised quadratic response',fontsize=9,loc='left',weight='bold')
for i in range(6):
 for j in range(6):
  ax.text(j,i,f'{resp[i,j]:.2f}',color='white' if resp[i,j]>1.35 else colors['navy'],ha='center',va='center',fontsize=7)
cb=fig.colorbar(im,ax=ax,shrink=.83,pad=.02);cb.set_label(r'$m_k/A_{k0}$',fontsize=8)
# subset comparison
conds=[]; tr=[]; sets=[]
for ids in itertools.combinations(range(6),4):
 B=P[list(ids)];s=np.linalg.svd(B,compute_uv=False)
 cond=s[0]/s[-1]; cov=np.trace(np.linalg.inv(B.T@B))
 conds.append(cond);tr.append(cov);sets.append(tuple(masks[i] for i in ids))
order=np.argsort(conds);best=sets[order[0]]; bcond=conds[order[0]]
axs=axes[1]; xs=np.arange(1,16);yy=np.asarray(conds)[order]
axs.vlines(xs,7,yy,color='#d0dae2',lw=1);axs.plot(xs,yy,'o',c=colors['teal'],ms=4)
axs.axhline(np.linalg.cond(P),c=colors['gold'],ls='--',lw=1.3,label='Six-state condition')
axs.set_yscale('log');axs.set_ylim(6,1900);axs.set_xticks([1,3,5,7,9,11,13,15]);axs.set_xlabel('Four-state subset (ranked)');axs.set_ylabel(r'$\kappa_2(\widetilde A)$')
axs.set_title('(b) Every four-state subset',fontsize=9,loc='left',weight='bold');axs.legend(frameon=False,fontsize=7,loc='upper left')
axs.text(1.2,75,f'Best masks: {best}',fontsize=7.3,color=colors['navy'])
axs.grid(axis='y',alpha=.17)
fig.subplots_adjust(wspace=.35)
save(fig,'V41_FIG_RESPONSE_AND_SUBSETS')
# 2 leverage and change of variance
Finfo=P.T@P;inv=np.linalg.inv(Finfo); base=np.trace(inv)
lever=np.array([float(p@inv@p) for p in P])
ratios=[]; leavecond=[]
for i in range(6):
 B=np.delete(P,i,axis=0)
 ratios.append(float(np.trace(np.linalg.inv(B.T@B))/base))
 leavecond.append(float(np.linalg.cond(B)))
ratios=np.array(ratios)
fig,axs=plt.subplots(1,2,figsize=(7.0,2.6))
a=axs[0]
a.vlines(range(6),0,lever,color='#a6d3d3',lw=3);a.plot(range(6),lever,'o',c=colors['teal'],ms=6)
a.set_xticks(range(6),[f'{m:02d}' for m in masks]);a.set_ylim(0,1.10);a.set_xlabel('Omitted mask');a.set_ylabel(r'Leverage $h_k$')
a.set_title('(a) Information leverage by state',fontsize=9,loc='left',weight='bold');a.grid(axis='y',alpha=.15)
a=axs[1];a.plot(range(6),ratios,'-o',c=colors['gold'],lw=1.5,ms=5)
a.set_yscale('log');a.set_ylim(.85,170);a.set_xticks(range(6),[f'{m:02d}' for m in masks]);a.set_xlabel('Omitted mask');a.set_ylabel('Relative covariance trace')
a.set_title('(b) Loss from removing one state',fontsize=9,loc='left',weight='bold');a.grid(axis='y',alpha=.15)
for i in [1,5]:
 a.text(i-.18, ratios[i]*1.08, f'{ratios[i]:.1f}×', fontsize=7, color=colors['navy'])
fig.tight_layout(w_pad=2)
save(fig,'V41_FIG_STATE_LEVERAGE')
# 3 dual-mesh status (don't claim continuous bandwidth)
dual=json.loads(Z.read('V417_RESULTS/V417_FULL_VERDICT.json'))['candidates']
fig,axs=plt.subplots(1,2,figsize=(7.1,2.75),sharey=True)
matched=[]
for ax,(candidate,info) in zip(axs,dual.items()):
 rows=[]
 for d in info['results']:
  if 'M110' in d and 'M125' in d and 'condition' in d['M110'] and 'condition' in d['M125']:
   rows.append((d['frequency_GHz'],float(d['M110']['condition']),float(d['M125']['condition']),d.get('status','')))
 x=np.array([r[0] for r in rows]);v=np.array([r[1] for r in rows]);w=np.array([r[2] for r in rows]);passed=np.array([r[3]=='PASS_DUAL_MESH' for r in rows]);
 ax.plot(x,v,c=colors['teal'],lw=1.3,label='M110');ax.plot(x,w,c=colors['gold'],lw=1.3,ls='--',label='M125')
 ax.scatter(x[passed],v[passed],c=colors['teal'],s=22,zorder=4,marker='o');ax.scatter(x[~passed],v[~passed],facecolor='white',edgecolor=colors['red'],s=25,zorder=4,marker='o')
 ax.axhline(35,ls=':',c=colors['muted'],lw=1)
 ax.set_xlim(1.71,2.01);ax.set_ylim(0,50);ax.tick_params(labelsize=7.5);ax.set_xlabel('Frequency (GHz)');ax.set_title(f'{candidate} · independent adaptive meshes',fontsize=8.5,loc='left',weight='bold');ax.grid(axis='y',alpha=.13)
 matched.extend([(candidate,*r) for r in rows])
axs[0].set_ylabel(r'Row-normalised $\kappa_2$');axs[0].legend(frameon=False,fontsize=7)
axs[1].text(.03,.92,'Filled = pass\nOpen = fail',transform=axs[1].transAxes,fontsize=7,va='top')
fig.tight_layout(w_pad=2.0);save(fig,'V41_FIG_INDEPENDENT_HFSS_PASS')
# 4 F03 redesigned native geometry and dimensionable parameter changes (no crammed table)
row=list(csv.DictReader(io.StringIO(Z.read('V418_RESULTS/DATA/THREE_DESIGNS_11_PARAMETERS.csv').decode())))
c0=next(r for r in row if r['candidate']=='C000');c33=next(r for r in row if r['candidate']=='C033')
geomz=zipfile.ZipFile(root/'source_evidence/V418_NATIVE_HFSS_RETURN_COMPACT.zip')
geom=json.loads(geomz.read('V416_CANDIDATES/C033/COPPER_M03.json'))
fig,axs=plt.subplots(1,2,figsize=(6.9,3.0),gridspec_kw={'width_ratios':[.95,1.25]})
a=axs[0]
for sh in geom['shapes']:
 pts=np.array(sh['polygon']); col=colors['gold'] if sh['layer']=='TOP' else colors['teal']
 a.add_patch(Polygon(pts,closed=True,facecolor=col,edgecolor='white',lw=.4))
a.set_xlim(-12,12);a.set_ylim(-12,12);a.set_aspect('equal');a.set_xticks([-10,0,10]);a.set_yticks([-10,0,10]);a.set_xlabel('x (mm)');a.set_ylabel('y (mm)')
a.set_title('(a) Native C033 copper geometry',fontsize=9,loc='left',weight='bold')
a.text(-10,-11,'Front copper',color=colors['gold'],fontsize=7,weight='bold');a.text(0,-11,'Rear copper',color=colors['teal'],fontsize=7,weight='bold')
b=axs[1];keys=['front_width_mm','rear_width_mm','rear_angle_deg','rear_shrink','switch_gap_mm'];labels=['Front width','Rear width','Rear rotation','Rear shrink','Switch gap']
changes=[100*(float(c33[k])/float(c0[k])-1) for k in keys]
ys=np.arange(len(keys));b.axvline(0,c='#9cabb4',lw=.8)
b.hlines(ys,0,changes,color='#a3cdcc',lw=2);b.scatter(changes,ys,color=colors['teal'],s=35,zorder=3)
for i,ch in enumerate(changes):b.text(ch+(1 if ch>=0 else -1),i,f'{ch:+.1f}%',ha='left' if ch>=0 else 'right',va='center',fontsize=7)
b.set_yticks(ys,labels);b.invert_yaxis();b.set_xlim(-5,25);b.set_xlabel('Change from reference C000 (%)');b.set_title('(b) Geometry change selected by search',fontsize=9,loc='left',weight='bold');b.grid(axis='x',alpha=.12)
fig.tight_layout(w_pad=2.2);save(fig,'F03_NATIVE_OPTIMISED_UNIT_CELL')
# record full numeric source
summary={
 'frequency_GHz':1.925,'source':'V418_RESULTS/DATA/C033_EQUATION_VERDICT_1.9250.json','source_kind':'native HFSS independently adapted periodic field amplitudes; offline algebra',
 'switch_masks':masks,'P_normalised':P.tolist(),'rank':int(np.linalg.matrix_rank(P)),'six_condition_row_normalised':float(np.linalg.cond(P)),'six_condition_raw':float(np.linalg.cond(A)),
 'trace_unit_variance_six':float(base),'best_four_masks_by_condition':best,'best_four_condition':float(bcond),'best_four_trace_unit_variance':float(tr[order[0]]),
 'four_subset_condition_min':float(min(conds)),'four_subset_condition_median':float(np.median(conds)),'four_subset_condition_max':float(max(conds)),
 'leave_one_out_leverage':dict(zip(map(str,masks),map(float,lever))),'leave_one_out_relative_variance':dict(zip(map(str,masks),map(float,ratios))),
 'leave_one_out_condition':dict(zip(map(str,masks),map(float,leavecond))),
 'numerical_identity_residual':float(audit['max_operator_identity_absolute']),
 'model_note':'Unit-variance noise metric is purely an equal-variance analytic diagnostic after row normalisation, NOT measured noise; the Jones outputs share their calibration source, so self inversion does not validate accuracy.'}
(root/'analysis'/'V41'/'INFORMATION_GEOMETRY_RESULTS.json').write_text(json.dumps(summary,indent=2))
with open(root/'analysis'/'V41'/'FOUR_STATE_SUBSETS.csv','w',newline='') as h:
 w=csv.writer(h);w.writerow(['masks','condition_row_normalised','smallest_singular','trace_Finverse'])
 for ids,c in zip(itertools.combinations(range(6),4),conds):
  B=P[list(ids)];w.writerow(['/'.join(str(masks[i]) for i in ids),f'{c:.10g}',f'{np.linalg.svd(B,compute_uv=False)[-1]:.10g}',f'{np.trace(np.linalg.inv(B.T@B)):.10g}'])
with open(root/'analysis'/'V41'/'MESH_VERIFICATION_BY_FREQUENCY.csv','w',newline='') as h:
 w=csv.writer(h);w.writerow(['candidate','GHz','condition_M110','condition_M125','status'])
 for r in matched:w.writerow(r)
