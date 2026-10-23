---
title: 'Earthquake catalog: minimal quality-control workflow'
summary: 'Create synthetic seismic events, check duplicates and missing values, and generate a documented catalog plot.'
status: 'Executable example'
topic: Seismic
featured: true
notebook_file: '/notebooks-src/03_seismic_catalog_demo.ipynb'
notebook_html: '/assets/notebooks/03_seismic_catalog_demo.html'
---
## Workflow

- Read event identifiers, time, latitude, longitude, depth and magnitude.
- Check duplicates and missing values.
- Plot depth versus magnitude and summarize the screening.

All events are **artificial**. This is neither a complete seismic catalog nor a probabilistic seismic-hazard analysis.

Related topic: [Seismic hazard and site response]({{ '/projects/seismic-hazard/' | relative_url }}).
