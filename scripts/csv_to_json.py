#!/usr/bin/env python3
"""Convert Excel-exported cases.csv to cases.json; run from repository root.

Usage: python scripts/csv_to_json.py
CSV `methods` cell is pipe separated, e.g. "Numerical Comparison|Chart / Table".
"""
import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / 'data'
TAXONOMY = json.loads((DATA / 'taxonomy.json').read_text(encoding='utf-8'))
SCENARIOS = set(TAXONOMY['scenarios'])
METHODS = set(TAXONOMY['methods'])
REQUIRED = ['id','title','type','scenario','methods','image']

cases = []
ids = set()
with (DATA / 'cases.csv').open(encoding='utf-8-sig', newline='') as f:
    for line_no, row in enumerate(csv.DictReader(f), 2):
        if not any(row.values()):
            continue
        for field in REQUIRED:
            if not (row.get(field) or '').strip():
                raise ValueError(f'Row {line_no}: field {field!r} is missing')
        item = {k:(v or '').strip() for k,v in row.items()}
        item['methods'] = [m.strip() for m in item['methods'].split('|') if m.strip()]
        if item['id'] in ids:
            raise ValueError(f'Row {line_no}: duplicate ID {item["id"]}')
        if item['scenario'] not in SCENARIOS:
            raise ValueError(f'Row {line_no}: unknown scenario {item["scenario"]}')
        if item['type'] not in ('Academia','Industry'):
            raise ValueError(f'Row {line_no}: type must be Academia or Industry')
        for method in item['methods']:
            if method not in METHODS:
                raise ValueError(f'Row {line_no}: unknown comparison method {method}')
        if not (BASE / 'assets' / (item['image']+'.webp')).is_file():
            print(f'WARNING row {line_no}: assets/{item["image"]}.webp is missing')
        ids.add(item['id'])
        cases.append(item)

(DATA / 'cases.json').write_text(json.dumps({'cases':cases},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Keep image keys in sync automatically: add assets/my-case.webp then use image=my-case in CSV.
image_file = DATA / 'images.json'
image_map = json.loads(image_file.read_text(encoding='utf8'))
for item in cases:
    key = item['image']
    if (BASE / 'assets' / f'{key}.webp').exists():
        image_map['images'][key] = f'assets/{key}.webp'
image_file.write_text(json.dumps(image_map, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
print(f'Generated data/cases.json with {len(cases)} cases and updated image mapping')
