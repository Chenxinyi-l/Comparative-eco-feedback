# Comparative Eco-Feedback

An interactive research companion for exploring how digital tools communicate environmental impacts through comparison. 

## Explore the site

- **Case Library** — Search cases and filter them by scenario, comparison method, or source type.
- **Design Patterns** — Explore the scenario-by-method heatmap at general or detailed levels. Select a cell to browse cases at that intersection.
- **Design Space** — Explore three dimensions of design and read the interpretive synthesis and observed practices for each group. Select factors for a design or click the framework figure to enlarge it.
- **Design Worksheet** — Describe the design context in eight fields, review the selected factors, and export the worksheet as a text file. The **View example** button opens a student housing laundry example.

## Repository guide

| Path | Purpose |
| --- | --- |
| `index.html` | Interface, styles, interaction logic, and offline data snapshot |
| `assets/cases/` | Case screenshots in WebP format |
| `assets/designspace.png` | Design Space framework figure |
| `data/cases.json` | Case records used by the hosted site |
| `data/cases.csv` | Spreadsheet copy of the case records |
| `data/images.json` | Image keys and their relative file paths |
| `data/taxonomy.json` | General and detailed scenario and comparison-method categories |
| `data/matrix.json` | Independently maintained heatmap counts |
| `data/designspace.json` | Design Space dimensions, groups, factors, synthesis, and observed practices |
| `scripts/validate_data.py` | Basic data and asset checks |
| `scripts/csv_to_json.py` | Legacy converter for the earlier CSV format |
| `.nojekyll` | Serves the static site without Jekyll processing |