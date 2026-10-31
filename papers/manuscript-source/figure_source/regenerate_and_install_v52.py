#!/usr/bin/env python3
"""Regenerate evidence-backed figures 9–12 and install under manuscript filenames.

Usage from the project root: python figure_source/regenerate_and_install_v52.py
Requires numpy, pandas, matplotlib. No HFSS solve or synthetic measurement.
"""
from pathlib import Path
import subprocess, sys, shutil
r=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(r/'figure_source'/'rebuild_verified_figures.py')],check=True)
names={
    'FIG09_verified_ranked.pdf':'V41_FIG_RESPONSE_AND_SUBSETS.pdf',
    'FIG10_verified_gain.pdf':'V51_FIG_GAIN_AWARE_INFORMATION.pdf',
    'FIG11_verified_budget.pdf':'V44_FIXED_BUDGET.pdf',
    'FIG12_verified_mesh.pdf':'V41_FIG_INDEPENDENT_HFSS_PASS.pdf',
}
for src,dst in names.items():
    shutil.copy2(r/'figures'/src,r/'figures'/dst)
    print(src,'->',dst)
