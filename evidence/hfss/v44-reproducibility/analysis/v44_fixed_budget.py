"""Reproducible fixed-budget A-optimal allocation from existing HFSS C033 instrument.
No detector noise or new HFSS solves are used. Each observation is assumed to have
independent additive noise variance inversely proportional to dwell fraction.
"""
from pathlib import Path
from itertools import combinations
from scipy.optimize import minimize
import numpy as np, json, csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent.parent
A=np.loadtxt(ROOT/'analysis/V42_C033_INSTRUMENT_MATRIX.csv',delimiter=',',skiprows=1)
MASKS=np.array([3,6,8,10,12,13])
L=0.02 # require 2% of fixed total acquisition budget for each selected state
assert A.shape==(6,4)

def traceinv(X,w):
    I = X.T@(w[:,None]*X)
    return np.trace(np.linalg.inv(I))

def optimize(X,frac_min):
    K=len(X)
    w0=np.full(K,1/K)
    base=traceinv(X,w0)
    def fun(w): return traceinv(X,w)/base
    def grad(w):
        M=np.linalg.inv(X.T@(w[:,None]*X))
        return -np.einsum('ij,jk,ki->i',X,M@M,X.T)/base
    opt=minimize(fun,w0,jac=grad,method='SLSQP',bounds=[(frac_min,1.)]*K,
                 constraints=[{'type':'eq','fun':lambda x:np.sum(x)-1.,'jac':lambda x:np.ones_like(x)}],
                 options={'maxiter':1500,'ftol':1e-12})
    assert opt.success, (opt.message,opt.x)
    assert np.min(opt.x)>=frac_min-1e-8 and abs(sum(opt.x)-1)<1e-8
    return opt.x,traceinv(X,opt.x)

out=[]
for K in [4,5,6]:
  for inds in combinations(range(6),K):
    X=A[list(inds)]
    eq=traceinv(X,np.ones(K)/K)
    ww,j=optimize(X,L)
    out.append(dict(K=K,masks=[int(MASKS[i]) for i in inds],equal_trace=eq,
                    optimized_trace=j,weights=ww.tolist(),
                    improvement=eq/j,
                    condition_raw=float(np.linalg.cond(X)),
                    rownorm_condition=float(np.linalg.cond(X/X[:,0,None]))))
summary={}
for K in [4,5,6]:
    rows=[r for r in out if r['K']==K]
    be=min(rows,key=lambda r:r['equal_trace'])
    bo=min(rows,key=lambda r:r['optimized_trace'])
    summary[str(K)]={'best_equal':be,'best_opt':bo}

j6_eq=summary['6']['best_equal']['equal_trace']; j6_opt=summary['6']['best_opt']['optimized_trace']
for K in [4,5,6]:
  for variant in ['best_equal','best_opt']:
    r=summary[str(K)][variant]
    r['relative_to_six_equal']=r['equal_trace' if variant=='best_equal' else 'optimized_trace']/j6_eq
    r['relative_to_six_opt']=r['equal_trace' if variant=='best_equal' else 'optimized_trace']/j6_opt

# Independent finite-difference gradient check for nonlinear optimisation
rng=np.random.default_rng(7)
X=A
x=np.array([.23,.12,.13,.14,.18,.20]);
M=np.linalg.inv(X.T@(x[:,None]*X)); g=-np.einsum('ij,jk,ki->i',X,M@M,X.T)
fd=[]
for i in range(6):
    shift=np.zeros(6);shift[i]=1e-6
    fd.append((traceinv(X,x+shift)-traceinv(X,x-shift))/(2e-6))
assert np.allclose(g,fd,rtol=1e-6,atol=1e-4)

assert 1.0<=j6_eq/j6_opt<=3.0

(ROOT/'analysis/V44_FIXED_BUDGET_RESULTS.json').write_text(json.dumps({'assumptions':'HFSS periodic C033, 1.925 GHz, independent equal per-unit-time additive raw-output variance, fixed total integration budget; 2% minimum dwell for every selected mask','data_source':'analysis/V42_C033_INSTRUMENT_MATRIX.csv','mask_order':MASKS.tolist(),'dwell_minimum':L,'six_equal_trace':j6_eq,'six_opt_trace':j6_opt,'gradient_check':'PASS','summary':summary},indent=2))
with (ROOT/'analysis/V44_FIXED_BUDGET_ALL_SUBSETS.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['state_count','masks','equal_time_trace','optimised_trace','improvement_ratio','optimal_fractions'])
  for r in out:w.writerow([r['K'],'/'.join(str(m) for m in r['masks']),f"{r['equal_trace']:.7f}",f"{r['optimized_trace']:.7f}",f"{r['improvement']:.7f}",'/'.join(f'{x:.6f}' for x in r['weights'])])

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8,'pdf.fonttype':42,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(1,2,figsize=(6.98,2.55),gridspec_kw={'width_ratios':[1.04,1]})
colors=['#365B73','#087F8C','#B97A45']
Ks=np.array([4,5,6])
jeq=np.array([summary[str(k)]['best_equal']['equal_trace']/j6_eq for k in Ks])
jop=np.array([summary[str(k)]['best_opt']['optimized_trace']/j6_eq for k in Ks])
ax[0].plot(Ks,jeq,'o--',color=colors[0],lw=1.6,label='Best equal dwell')
ax[0].plot(Ks,jop,'s-',color=colors[1],lw=1.7,label='Optimised dwell')
for x,y in zip(Ks,jop):ax[0].annotate(f'{y:.2f}',(x,y),textcoords='offset points',xytext=(4,-12),fontsize=7,color=colors[1])
ax[0].set_xticks(Ks);ax[0].set_xlim(3.8,6.2);ax[0].set_ylim(.5,max(jeq)*1.18)
ax[0].set_xlabel('Number of selected masks');ax[0].set_ylabel('Relative inverse-trace bound')
ax[0].set_title('(a) Fixed total acquisition budget',fontsize=8.5)
ax[0].grid(axis='y',alpha=.18);ax[0].legend(fontsize=7,frameon=False)
best=summary['6']['best_opt'];ww=best['weights']
ax[1].bar(range(6),ww,color=[colors[1] if x>.05 else '#C0CCD1' for x in ww],width=.65)
ax[1].axhline(1/6,color=colors[2],linestyle='--',lw=1,label='Equal dwell (16.7%)')
ax[1].set_xticks(range(6),[f'{k:02d}' for k in MASKS]);ax[1].set_ylim(0,max(ww)*1.2)
ax[1].set_xlabel('HFSS switch mask');ax[1].set_ylabel('Fraction of total time')
ax[1].set_title('(b) Six-state A-optimal dwell schedule',fontsize=8.5)
ax[1].grid(axis='y',alpha=.16);ax[1].set_axisbelow(True);ax[1].legend(fontsize=7,frameon=False,loc='upper right')
fig.tight_layout(pad=.9,w_pad=2.0)
for ext in ['pdf','png']:
    fig.savefig(ROOT/f'figures/V44_FIXED_BUDGET.{ext}',dpi=300 if ext=='png' else None,bbox_inches='tight',pad_inches=.08)
plt.close(fig)
print('Best fixed-budget schedules:')
for k in Ks:
 r=summary[str(k)]['best_opt'];print(k,'/'.join(map(str,r['masks'])),'norm J',r['relative_to_six_equal'],'weights',np.round(r['weights'],3))
print('Six-state equal->opt improvement',round(j6_eq/j6_opt,4),'gradient PASS')
