import csv,json
import numpy as np
from pathlib import Path
R=Path(__file__).resolve().parents[1];d=R/'data';a=R/'analysis'
z=json.load(open(d/'V27_FINITE_EVIDENCE_AUDIT.json'))
A27=np.array(z['v420']['planes']['-5.0']['instrument_matrix'])
A24=np.array(z['v421']['planes']['-5.0']['instrument_matrix'])
assert A27.shape==(6,4) and A24.shape==(6,4)
assert np.linalg.matrix_rank(A27)==4 and np.linalg.matrix_rank(A24)==4
assert abs(np.linalg.cond(A27/A27[:,[0]])-24.724535285845082)<1e-9
assert abs(np.linalg.cond(A24/A24[:,[0]])-21.93417232190835)<1e-9
assert all(np.linalg.norm(a[1:]) <= a[0]+1e-8 for a in A27)
assert all(np.linalg.norm(a[1:]) <= a[0]+1e-8 for a in A24)
s=np.genfromtxt(a/'NEW_CROSS_MESH_RECONSTRUCTION.csv',delimiter=',',skip_header=1)
S=s[:,:4]; e1=s[:,4];e2=s[:,5]
np.testing.assert_allclose(np.linalg.pinv(A24)@(A24@S.T),S.T,atol=1e-11)
np.testing.assert_allclose(np.linalg.pinv(A27)@(A27@S.T),S.T,atol=1e-11)
for Acal,Aobs,stored in [(A24,A27,e1),(A27,A24,e2)]:
 calc=np.linalg.norm((np.linalg.pinv(Acal)@(Aobs@S.T)).T-S,axis=1)/np.linalg.norm(S,axis=1)*100
 np.testing.assert_allclose(calc,stored,rtol=1e-10)
# Check switch-mask source: each closed bridge name only when its bit is set
import zipfile
with zipfile.ZipFile(R/'source_evidence/V418_NATIVE_HFSS_RETURN_COMPACT.zip') as h:
 for mask in [3,6,8,10,12,13]:
  obj=json.loads(h.read(f'V416_CANDIDATES/C033/COPPER_M{mask:02d}.json'))
  for sh in obj['shapes']:
   if 'SWITCH' in sh['name']:
    bit=int(sh['name'].split('_')[2]);assert (mask>>bit)&1
report={'checks':'PASS','rank':[int(np.linalg.matrix_rank(A24)),int(np.linalg.matrix_rank(A27))],'cond_row_gain_normalised':[float(np.linalg.cond(A24/A24[:,[0]])),float(np.linalg.cond(A27/A27[:,[0]]))],'cond_raw':[float(np.linalg.cond(A24)),float(np.linalg.cond(A27))],'same_mesh_max_abs':[float(np.max(np.abs(np.linalg.pinv(A24)@(A24@S.T)-S.T))),float(np.max(np.abs(np.linalg.pinv(A27)@(A27@S.T)-S.T)))],'cross_mesh_p95':[float(np.percentile(e1,95)),float(np.percentile(e2,95))],'n_states':len(S),'gram_cone_check':'PASS','native_switch_masks':'PASS'}
(a/'EVIDENCE_CHECKS.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
