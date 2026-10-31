#!/usr/bin/env python3
"""Offline evidence integrity check. Uses only Python's standard library."""
from pathlib import Path
import csv, hashlib, re, sys, zipfile
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parent.parent
REGISTER=ROOT/'docs/traceability/ASSET_REGISTER.csv'

def sha256(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()

def audit():
    errors=[];records=list(csv.DictReader(REGISTER.open(encoding='utf-8',newline='')))
    paths={r['path'] for r in records}
    for r in records:
        p=ROOT/r['path']
        if not p.is_file():errors.append('Missing registered asset: '+r['path']);continue
        if sha256(p)!=r['sha256']:errors.append('Checksum mismatch: '+r['path'])
        if p.stat().st_size!=int(r['bytes']):errors.append('Size mismatch: '+r['path'])
        if p.suffix=='.zip':
            try:
                with zipfile.ZipFile(p) as z:
                    if z.testzip():errors.append('Corrupt ZIP: '+r['path'])
            except Exception as exc:errors.append(f'Unreadable ZIP: {r["path"]}: {exc}')
    for p in ROOT.rglob('*.md'):
        for link in re.findall(r'(?<!!)\[[^]]+\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            # Exclude URLs, dynamic templates, local fragments and mail links
            target=unquote(link.split('#',1)[0].strip().split(' ',1)[0])
            if not target or re.match(r'^(https?://|mailto:|data:)',target):continue
            resolved=(p.parent/target).resolve()
            if not resolved.exists():errors.append(f'Broken relative link: {p.relative_to(ROOT)} -> {link}')
    claims=ROOT/'docs/traceability/CLAIM_EVIDENCE.csv'
    for r in csv.DictReader(claims.open(encoding='utf-8',newline='')):
        if not (ROOT/r['repo_path']).exists():errors.append(f'Claim {r["claim_id"]} missing source {r["repo_path"]}')
    if len(paths)!=len(records):errors.append('Duplicate paths in asset manifest')
    print(f'Assets verified: {len(records)}; claim-source checks completed; relative Markdown links checked.')
    if errors:
        print('\n'.join('ERROR: '+x for x in errors[:100]));return 1
    print('PASS: registered files match SHA-256 and no missing local Markdown targets found.')
    return 0

if __name__=='__main__':sys.exit(audit())
