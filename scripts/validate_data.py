#!/usr/bin/env python3
"""Basic data checks; does not validate scientific coding decisions."""
from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
read=lambda name: json.loads((B/'data'/name).read_text(encoding='utf8'))
cases=read('cases.json')['cases']; tax=read('taxonomy.json'); mat=read('matrix.json')['matrix']; ds=read('designspace.json')['spaces']; imgs=read('images.json')['images']
assert len(mat)==len(tax['scenarios'])
assert all(len(row)==len(tax['methods']) for row in mat)
assert all(isinstance(value,int) and value>=0 for row in mat for value in row)
assert len(set(c['id'] for c in cases))==len(cases)
for case in cases:
  assert case['scenario'] in tax['scenarios'], case['id']
  assert set(case['methods']).issubset(tax['methods']), case['id']
  assert case['image'] in imgs,case['id']
for name, path in imgs.items():
  assert (B/path).exists(), name
assert len(ds)==3
print(f'OK: {len(cases)} displayed cases; {sum(map(sum,mat))} full-corpus coded combinations; {len(ds)} design-space dimensions.')
print('Note: matrix totals are independent of cases.json; do not recompute from an illustrated sample.')
