"""Independent verification of information-geometry post-processing from archived HFSS rows.
No new EM solve and no measurement-noise assumption in checks.
"""
import json, zipfile, itertools
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
Z=zipfile.ZipFile(ROOT/'source_evidence/mix_results_20261025.zip')
original=json.loads(Z.read('V418_RESULTS/DATA/C033_EQUATION_VERDICT_1.9250.json'))
A=np.asarray(original['instrument'],float);P=A/A[:,[0]]
F=P.T@P;inv=np.linalg.inv(F)
summary=json.loads((ROOT/'analysis/V41/INFORMATION_GEOMETRY_RESULTS.json').read_text())
assert np.linalg.matrix_rank(A)==4
assert abs(np.linalg.cond(P)-summary['six_condition_row_normalised'])<1e-11
assert abs(np.trace(inv)-summary['trace_unit_variance_six'])<1e-11
assert abs(np.linalg.cond(P)-original['condition'])<1e-9
masks=summary['switch_masks']
subset=[]
for ids in itertools.combinations(range(6),4):
 B=P[list(ids)]
 sv=np.linalg.svd(B,compute_uv=False)
 subset.append((tuple(masks[i] for i in ids),sv[0]/sv[-1],np.trace(np.linalg.inv(B.T@B))))
best=min(subset,key=lambda t:t[1])
assert list(best[0])==list(summary['best_four_masks_by_condition'])
assert abs(best[1]-summary['best_four_condition'])<1e-11
for j in range(6):
 p=P[j];h=p@inv@p
 assert h<1
 deleted=np.delete(P,j,axis=0)
 via_direct=np.linalg.inv(deleted.T@deleted)
 via_SM=inv+np.outer(inv@p,inv@p)/(1-h)
 residual=np.max(abs(via_direct-via_SM))
 assert residual<1e-8,(j,residual)
 expected=np.trace(via_direct)/np.trace(inv)
 assert abs(expected-summary['leave_one_out_relative_variance'][str(masks[j])])<1e-10
# deterministic response identity and admissibility
for S in [np.array([1,1,0,0]),np.array([1,-1,0,0]),np.array([1,0,0,1]),np.array([1,0,0,-1])]:
 assert np.all(P@S>=-1e-11)
R=np.array([1,0,0,1]);L=np.array([1,0,0,-1]);assert np.max(abs((P@R-P@L)-2*P[:,3]))<1e-12
print('PASS: rank, source condition, all 15 subsets, Sherman-Morrison identity, leverage, and circular-contrast identity')
print('best four:',best[0], 'condition:',best[1])
print('six condition:',np.linalg.cond(P),'raw condition:',np.linalg.cond(A),'trace:',np.trace(inv))
