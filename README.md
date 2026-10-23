# Sergio Cacante — Geotechnical Research Website (prototype)

A functional website skeleton based on the **Jekyll / Academic Pages architectural pattern** of the GitHub project `wh1994.github.io`, adapted to the content of Sergio Cacante's public Google Sites and technical notebook workflows. New site code, content and visual identity have been authored as a separate project; original personal assets and scientific texts from the reference site have **not** been copied.

## Contents

- Modular static Jekyll website, collections (`_projects`, `_notebooks`, `_geoapps`, `_notes`, `_presentations`) and data-driven navigation.
- Responsive site design, working search/topic filter in the notebook catalogue.
- Three *synthetic educational* Python notebooks plus pre-rendered HTML reports.
- A functioning JavaScript/SVG strength-profile Geo App.
- GitHub Pages deployment workflow, authoring templates and migration plan.

**Important:** This is an initial prototype, not a deployed site or a validated engineering calculation package. The author's current Google Sites website is NOT modified.

## Local installation

Requirements: Ruby 3.3+ with Bundler. Install Bundler if needed (`gem install bundler`), then in this directory:

```bash
bundle install
bundle exec jekyll serve
```

Browse `http://localhost:4000`. For notebooks (Python 3.10+):

```bash
python -m pip install -r requirements-notebooks.txt
python scripts/render_notebooks.py
```

If you cannot install Jekyll yet, the **standalone working Geo App** at `apps/soil-profile/index.html` opens directly in a browser. The static notebook exports in `assets/notebooks/` also open without Jekyll.

## Publishing as GitHub Pages

1. Create a **new** repository `sergiocacante-ufrj/sergiocacante-ufrj.github.io` (or adapt `_config.yml` `url`, `baseurl`, `github_username`, `github_repo` if selecting another).
2. Upload this project's contents into that repo. Do **not** overwrite existing repos or notebooks without reviewing.
3. Commit to `main` and set GitHub Settings → Pages → Source to **GitHub Actions**.
4. The provided `.github/workflows/pages.yml` builds and deploys Jekyll.
5. After successful deployment and confirmation that public notebooks are reachable, change `show_colab_links` to `true` in `_config.yml` and commit again to activate Colab links.

**Actual HTML export is committed**, so no Python execution is needed during Pages build. Changes to `.ipynb` require regenerating HTML with `scripts/render_notebooks.py`.

## Safe notebook publication

- Keep source notebooks under `notebooks-src/` and mark inputs as synthetic or cite real public sources.
- Never commit client reports, licenses, private PLAXIS models or confidential laboratory data.
- Keep **executed reports** under `assets/notebooks/` as immutable documentation of a run.
- Use Colab for *public, compatible* Python analyses; the browser does not contain PLAXIS 3D or automatically execute Python notebooks on GitHub Pages.
- Advanced options: Binder with pinned environment for a hosted Jupyter server, or JupyterLite for limited browser-side Python / Pyodide packages. These are not enabled in this prototype.

## Editing content

- Main landing and indices: `_pages/`
- Menus: `_data/navigation.yml`
- Research areas: `_data/research.yml`
- Project cards/pages: `_projects/*.md`
- Notebook cards/pages: `_notebooks/*.md`
- Geo Apps: `_geoapps/*.md`, runnable client-side app: `apps/soil-profile/index.html`
- Theory notes: `_notes/*.md`
- Talks: `_presentations/*.md`
- Shared HTML: `_layouts/`, `_includes/`
- Styling: `assets/css/site.css`
- General config: `_config.yml`

See [ARQUITECTURA.md](ARQUITECTURA.md) and [ROADMAP.md](ROADMAP.md).
