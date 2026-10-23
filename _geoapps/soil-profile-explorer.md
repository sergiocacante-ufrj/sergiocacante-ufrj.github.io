---
title: 'Clay strength profile explorer'
summary: 'Interactive browser chart for an illustrative undrained strength gradient sᵤ = k·z, with adjustable k and depth.'
status: 'Working browser demo'
topic: Offshore
featured: true
parent: '/geo-apps/'
app_url: '/apps/soil-profile/'
---
## Live application

This tool uses HTML, CSS, SVG and JavaScript in the web browser. It does **not** run PLAXIS or calculate torpedo-anchor capacity.

<iframe class="geo-demo-frame" title="Undrained clay strength profile explorer" src="{{ '/apps/soil-profile/' | relative_url }}" loading="lazy"></iframe>

**Equation:** \(s_u(z)=kz\). Explore how a different gradient changes the assumed input profile. This is educational visualization only, not a site-calibrated interpretation.

[View the complementary Python notebook]({{ '/notebooks/torpedo-su-profiles/' | relative_url }}).
