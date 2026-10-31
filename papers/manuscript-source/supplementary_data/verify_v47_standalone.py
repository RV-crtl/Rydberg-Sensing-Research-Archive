#!/usr/bin/env python3
"""Standalone verification of archived C033 Stokes rows and matrix identities.
Reads only included CSV. Does not run HFSS or assume a physical noise model.
"""
from pathlib import Path
import itertools, csv
import numpy as np
root=Path(__file__).resolve().parent
A=np.loadtxt(root/'V42_C033_INSTRUMENT_MATRIX.csv',delimiter=',',skiprows=1)
assert A.shape==(6,4)
assert np.linalg.matrix_rank(A)==4
assert (A[:,0]>0).all()
P=A/A[:,[0]]
assert abs(np.linalg.cond(P)-9.53)<.02, np.linalg.cond(P)
# Physical admissibility requires A0 >= sqrt(A1²+A2²+A3²)
assert (A[:,0]>=np.linalg.norm(A[:,1:],axis=1)-1e-10).all()
assert np.allclose(P.T@np.diag(A[:,0]**2)@P,A.T@A,rtol=1e-10)
mask=[3,6,8,10,12,13]
rows=[]
for inds in itertools.combinations(range(6),4):
 B=P[list(inds)]
 rows.append((tuple(mask[i] for i in inds),float(np.linalg.cond(B))))
best=min(rows,key=lambda x:x[1])
assert best[0]==(3,6,8,13)
assert abs(best[1]-7.633721292)<1e-6
assert len(rows)==15
# Sherman–Morrison leave-one-out exactness for full rank subsets
F=P.T@P
inv=np.linalg.inv(F)
for i in range(6):
 x=P[i]
 h=float(x@inv@x)
 assert h<1
 inverse_deleted=np.linalg.inv(np.delete(P,i,axis=0).T@np.delete(P,i,axis=0))
 predicted=inv+np.outer(inv@x,inv@x)/(1-h)
 assert np.allclose(inverse_deleted,predicted,rtol=2e-9,atol=2e-9)
# Independent circular response identity for + / - polarisation
Splus=np.array([1.,0.,0.,1.]);Sminus=np.array([1.,0.,0.,-1.])
assert np.allclose(A@Splus-A@Sminus,2*A[:,3],atol=1e-11)
print('PASS: C033 rank=4, 15 subsets, physical cone, gain scaling, state-deletion and circular identity')
print('row-normalised condition %.6f, best four %s condition %.6f'%(np.linalg.cond(P),best[0],best[1]))
