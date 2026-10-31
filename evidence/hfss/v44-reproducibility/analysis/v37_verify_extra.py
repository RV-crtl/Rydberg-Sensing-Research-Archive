from pathlib import Path
import numpy as np,json
R=Path(__file__).resolve().parents[1];j=json.loads((R/'data/V27_FINITE_EVIDENCE_AUDIT.json').read_text());saved=json.loads((R/'analysis/V37_FINITE_SINGULAR_SPECTRA.json').read_text())
for row in saved:
 key='v421' if row['mesh']=='P24' else 'v420';A=np.asarray(j[key]['planes']['-5.0']['instrument_matrix']); B=A/A[:,[0]];s=np.linalg.svd(B,compute_uv=False)
 assert np.linalg.matrix_rank(A)==4
 assert np.isclose(row['smin'],s[-1]) and np.isclose(row['smax'],s[0])
 assert np.isclose(row['circular_max'],np.max(np.abs(B[:,3])))
 assert all(np.linalg.norm(a[1:])<=a[0]+1e-8 for a in A)
 assert np.linalg.matrix_rank(np.c_[np.ones(6),B[:,1:]])==4
print('PASS — finite singular spectra, Stokes admissibility and affine-span rank equivalence')
