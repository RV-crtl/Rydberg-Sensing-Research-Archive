# Rydberg Academy: numerical and content validation

The Academy's source is in book/. The site serves copies under site/ so that a site-only GitHub Pages deployment does not expose unpublished original datasets.

Checks: the 1000-case engine is deterministic, numerically finite and uses original SI unit equations; 36 source Markdown chapters match the website's exact content snapshots; the source and browser mathematics are byte identical; the HFSS model remains anchored to the original six-state CSV, and the latest-versus-historical evidence distinction is explicitly documented.

These checks are **not** physical RF calibration, density-matrix spectrum validation, finite-geometry HFSS reruns, hardware safety certification or peer review of a 1000-page book. Full ARC, RydIQule and PyAEDT exercises are runnable locally in their own documented scientific environments.

Generate a full-length print PDF with Node 22, Python 3.11 and ReportLab 4+:

    python -m pip install reportlab pypdf
    python book/export_workbook_pdf.py

The automated book-build GitHub Actions workflow verifies page count and makes a downloadable PDF artifact. Print volume: 36 authored learning chapters plus one *unique calculated case per printed page*. The page count is not a claim of 1000 pages of independent prose chapters.
