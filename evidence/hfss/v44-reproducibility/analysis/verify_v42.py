#!/usr/bin/env python3
from pathlib import Path
import numpy as np,json,zipfile
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'analysis/V42_GAIN_AWARE_RESULTS.json').read_text())
A=np.loadtxt(R/'analysis/V42_C033_INSTRUMENT_MATRIX.csv',delimiter=',',skiprows=1)
assert A.shape==(6,4) and np.linalg.matrix_rank(A)==4
G=A[:,0]
P=A/G[:,None]
assert np.all(G>0)
assert np.allclose(P.T@np.diag(G**2)@P,A.T@A,rtol=1e-11,atol=1e-11)
for key,B in [('raw_measurement_equal_variance',A),('row_normalized_equal_variance',P)]:
    F=B.T@B; inv=np.linalg.inv(F); tr=np.trace(inv)
    assert np.isclose(np.linalg.cond(B),d[key]['condition'],rtol=1e-9)
    for i,b in enumerate(B):
        h=b@inv@b
        ratio=np.trace(np.linalg.inv(np.delete(B,i,axis=0).T@np.delete(B,i,axis=0)))/tr
        law=1+(b@(inv@inv)@b)/((1-h)*tr)
        assert np.isclose(ratio,law,rtol=1e-9)
        assert np.isclose(ratio,d[key]['deletion_ratio'][i],rtol=1e-9)
with zipfile.ZipFile(R/'source_evidence/mix_results_20261025.zip') as z:
    assert z.testzip() is None
for f in ['main.tex','main.pdf','figures/V42_FIG_GAIN_AWARE_INFORMATION.pdf','ieee_references.tex']:
    assert (R/f).exists(),f
print('PASS: exact HFSS-derived raw and normalised information analyses; covariance scaling; rank-one deletion law; archive CRC; core artifact presence')
