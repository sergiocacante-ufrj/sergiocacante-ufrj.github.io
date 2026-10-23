"""Rebuild static HTML from SOURCE notebooks without mutating .ipynb files.

Usage: python scripts/render_notebooks.py

By default each source notebook runs in an isolated temporary directory; only
public/demo notebooks should be committed to this site. This script performs
no access to licensed numerical solvers or proprietary input datasets.
"""
from __future__ import annotations
from pathlib import Path
import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / 'notebooks-src'
OUTPUT = ROOT / 'assets' / 'notebooks'
OUTPUT.mkdir(parents=True, exist_ok=True)

for source in sorted(SOURCES.glob('*.ipynb')):
    print(f'Rendering {source.name}')
    nb = nbformat.read(source, as_version=4)
    result = NotebookClient(nb, timeout=120, kernel_name='python3').execute()
    exporter = HTMLExporter(template_name='classic')
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True
    html, _ = exporter.from_notebook_node(result)
    (OUTPUT / f'{source.stem}.html').write_text(html, encoding='utf-8')
print('HTML reports generated successfully.')
