from pathlib import Path
import shutil, zipfile, hashlib, json
R=Path('/mnt/data/RYDBERG_V44_ACCESS');out=Path('/mnt/data')
sub=R/'SUBMISSION_SOURCE';evi=R/'RESEARCH_EVIDENCE'
for p in (sub,evi):shutil.rmtree(p,ignore_errors=True);p.mkdir()
for name in ['main_access.tex','ieee_references.tex','ieeeaccess.cls','spotcolor.sty','main_access.pdf','README_FIRST.md','EDITORIAL_AND_RUBRIC_REVIEW.md','bullet.png','logo.png','notaglinelogo.png']:
    p=R/name
    if p.is_file():shutil.copy2(p,sub/name)
shutil.copytree(R/'figures',sub/'figures',ignore=shutil.ignore_patterns('*.svg'))
for name in ['README_FIRST.md','EDITORIAL_AND_RUBRIC_REVIEW.md']:
    shutil.copy2(R/name,evi/name)
shutil.copytree(R/'analysis',evi/'analysis',ignore=shutil.ignore_patterns('contact*','*.png','__pycache__','*.log'))
shutil.copytree(R/'data',evi/'data')
shutil.copytree(R/'source_evidence',evi/'source_evidence')
# no font binary assets are included: .tfm/.pfb/.otf/.ttf/.map
for dest,path in [('Rydberg_V44_IEEE_Access_Submission_Source.zip',sub),('Rydberg_V44_Research_Reproducibility_Evidence.zip',evi)]:
    zz=out/dest
    with zipfile.ZipFile(zz,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for f in sorted(path.rglob('*')):
            if f.is_file():
                assert f.suffix.lower() not in {'.ttf','.otf','.pfb','.tfm','.map'}
                z.write(f,f.relative_to(path.parent))
    with zipfile.ZipFile(zz) as z:
        assert z.testzip() is None
    print(dest,zz.stat().st_size/1e6,'MB')
shutil.copy2(R/'main_access.pdf',out/'Rydberg_V44_IEEE_Access_Manuscript.pdf')
shutil.copy2(R/'EDITORIAL_AND_RUBRIC_REVIEW.md',out/'Rydberg_V44_Submission_Review.md')
# manifest of relevant evidence files and hashes
manifest={}
for f in [R/'main_access.tex',R/'main_access.pdf',R/'analysis/V44_FIXED_BUDGET_RESULTS.json',R/'analysis/V42_C033_INSTRUMENT_MATRIX.csv',R/'source_evidence/V418_NATIVE_HFSS_RETURN_COMPACT.zip']:
    manifest[f.relative_to(R).as_posix()]=hashlib.sha256(f.read_bytes()).hexdigest()
(out/'Rydberg_V44_SHA256_Manifest.json').write_text(json.dumps(manifest,indent=2))
print('paper',round((out/'Rydberg_V44_IEEE_Access_Manuscript.pdf').stat().st_size/1e6,2),'MB')
