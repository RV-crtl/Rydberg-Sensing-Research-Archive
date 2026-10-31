#!/usr/bin/env python3
"""Check sequential first-citation IEEE bibliography and all cited keys present."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
s=(root/'main.tex').read_text()
refs=(root/'ieee_references.tex').read_text()
actual=re.findall(r'\\bibitem\{([^}]+)\}',refs)
order=[]
for m in re.finditer(r'\\cite(?:\[[^]]*\])?\{([^}]*)\}',s):
 for k in m.group(1).split(','):
  k=k.strip()
  if k not in order:order.append(k)
assert actual==order,(actual,order)
print('PASS: citations and bibliography in first-appearance order (%d cited references)'%len(order))
