# Arquitectura propuesta — Sergio Cacante

## Objetivo

Transformar el Google Sites actual en una plataforma académica y computacional mantenible con GitHub, Jekyll y publicaciones reproducibles. El diseño conserva el modelo **Jekyll + `_layouts` + `_includes` + `_data` + colecciones** de Academic Pages / wh1994, pero usa contenido y estilos propios.

## Mapa del sitio

```text
Home
├── Research
│   ├── Offshore geotechnics / Torpedo anchors
│   ├── Numerical geotechnics / FEM
│   ├── Soil dynamics & seismic hazard
│   ├── Ground improvement
│   └── Geospatial analysis, AI & data
├── Projects
│   ├── Torpedo Anchor Project
│   ├── Seismic hazard / site effects
│   ├── FEM foundations and excavations
│   ├── Ground improvement
│   ├── MASW / geophysical characterization
│   └── Geostatistics
├── Notebooks
│   ├── Offshore: sᵤ depth profiles (demo)
│   ├── Soil mechanics: CPT → sᵤ (demo)
│   ├── Seismic: catalog QC (demo)
│   ├── Numerical: PLAXIS processing (pending)
│   └── Consolidation: analytical series (pending)
├── Geo Apps
│   ├── Clay sᵤ explorer (working browser app)
│   ├── 1D Consolidation (existing external)
│   ├── Shallow capacity (pending)
│   └── Deep capacity (pending)
├── Knowledge
│   ├── Constitutive models (MC, MCC, Matsuoka–Nakai)
│   ├── Soil dynamics
│   ├── Laboratory testing
│   └── Slope stability / earth pressure
├── Publications (registry pending verification)
├── Presentations
│   ├── Torpedo-anchor slides
│   ├── 2024 ground improvement talk
│   ├── 2026 soft-soil item (in preparation)
│   └── Geophysics / lab testing
├── Services / Geocerto
├── About / CV
├── Contact
└── Geophotography (secondary section)
```

## Separación de unidades de publicación

| Tipo | Pregunta | Recurso |
|---|---|---|
| Research | ¿Qué se investiga y por qué? | Objetivos, hipótesis, bibliografía |
| Projects | ¿Qué problema abordó el trabajo? | Caso, método, resultados verificables |
| Notebooks | ¿Cómo se reprodujo el cálculo? | `.ipynb`, HTML exportado, dependencias |
| Geo Apps | ¿Cómo interactúa un visitante con un método? | JS/SVG/browser o aplicación externa |
| Knowledge | ¿Cuál es el marco conceptual? | Notas, referencias, ecuaciones |
| Presentations | ¿Qué se comunicó y dónde? | Metadatos verificables, PDF autorizado |
| Services | ¿Qué ofrece Geocerto? | Servicios, proceso de contacto, alcance |

## Arquitectura de notebooks

```text
Dataset abierto/documentado
   ↓
Notebook fuente (.ipynb)
   ├── Datos y validaciones
   ├── Métodos, ecuaciones y supuestos
   ├── Gráficas y tablas
   ├── Verificación independiente
   └── Limitaciones / reproducibilidad
   ↓
render_notebooks.py (no edita fuentes)
   ├── HTML estático en GitHub Pages — lectura sin servidor
   └── .ipynb en el repo — reproducible localmente
                                      └── Colab — ejecución remota (tras publicar)
```

GitHub Pages solo sirve archivos estáticos. **No ejecuta notebooks Python ni PLAXIS en el servidor**. Para una app sencilla se usa JavaScript, y para notebooks Python se necesita Colab/Binder, o JupyterLite si las librerías son compatibles en navegador.

### Relación notebooks / repositorios

**Fase I** (implementada): notebooks de ejemplo dentro del repositorio del sitio para validar navegación, exportación y Colab futuro.

**Fase II**: proyectos de investigación con repositorios independientes, versiones, DOI y datasets asociados. El sitio muestra fichas que enlazan versiones estables y HTML de resultados, sin duplicar datos privados.

**Fase III**: pipeline CI opcional para probar y renderizar notebooks públicos de forma reproducible; separar notebooks ejecutables de dependencias/licencias propietarias.

## Decisiones de diseño

- Idioma inicial **inglés**, como en el sitio actual, ampliable a español y portugués.
- Menú superior reducido a los flujos centrales; Contact y Geophotography como páginas secundarias.
- Evidencia explícita: `Executable example`, `Research in progress`, `Outline`, `Planned`.
- Dominio objetivo orientativo: `sergiocacante-ufrj.github.io`; **no fue creado ni publicado**.
- Código fuente y documentos del proyecto original `wh1994` se conservan intactos en su ZIP original; este es un repositorio nuevo.
