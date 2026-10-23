---
title: 'Estimating sᵤ from synthetic CPT data'
summary: 'Demonstrate the conventional net cone resistance estimate sᵤ = (qₜ − σᵥ₀)/Nₖₜ with explicit parameter choices.'
status: 'Executable example'
topic: Soil mechanics
featured: true
notebook_file: '/notebooks-src/02_cpt_su_demo.ipynb'
notebook_html: '/assets/notebooks/02_cpt_su_demo.html'
---
## Example outline

1. Construct a simple **synthetic** CPT depth, corrected cone resistance and total overburden stress dataset.
2. Calculate net resistance and a notional undrained strength estimate.
3. Compare the effect of different user-defined cone factors \(N_{kt}\).
4. Plot profiles and inspect units.

The assumed cone factors are not a universal calibration. Engineering interpretation needs local field/lab calibration, soil-type checks, pore-pressure conventions and measurement provenance.
