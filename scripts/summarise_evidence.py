#!/usr/bin/env python3
"""Offline summary of actual imported article matrix and archive evidence, not new HFSS solves."""
import csv, json, math, pathlib
P=pathlib.Path(__file__).resolve().parent.parent
src=P/'papers/manuscript-source/data/V42_C033_INSTRUMENT_MATRIX.csv'
A=[[float(x) for x in row.values()] for row in csv.DictReader(src.open(encoding='utf-8',newline=''))]

def matrix_rank(matrix,tol=1e-11):
    a=[r[:] for r in matrix];n=len(a);m=len(a[0]);rank=0
    for c in range(m):
        piv=max(range(rank,n),key=lambda i:abs(a[i][c]),default=rank)
        if abs(a[piv][c])<tol:continue
        a[piv],a[rank]=a[rank],a[piv]
        t=a[rank][c];a[rank]=[v/t for v in a[rank]]
        for i in range(n):
            if i!=rank:
                v=a[i][c];a[i]=[x-v*y for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==n:break
    return rank
def main():
    print('Article matrix path:',src.relative_to(P))
    print('Rows / columns:',len(A),len(A[0]))
    print('Matrix full-column-rank check:',matrix_rank(A),'of',len(A[0]))
    print('Row-0 values:', ', '.join(f'{v:.6g}' for v in A[0]))
    print('Note: these values are the archived V42/C033 sample, not the selected 1.925 GHz case.')
if __name__ == '__main__':
    main()
