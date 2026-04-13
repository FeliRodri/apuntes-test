# Sonic Chromosphere

[![Built with Starlight](https://astro.badg.es/v2/built-with-starlight/tiny.svg)](https://starlight.astro.build)

Plataforma de apuntes academicos sobre Astro + Starlight, con contenido en MD/MDX, componentes reutilizables y soporte para diagramas Mermaid y formulas matematicas con KaTeX.

## Indice

- [Sonic Chromosphere](#sonic-chromosphere)
  - [Indice](#indice)
  - [Descripcion General](#descripcion-general)
  - [Inicio Rapido](#inicio-rapido)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Componentes Astro](#componentes-astro)
  - [Sistema de Scripts](#sistema-de-scripts)
  - [Configuracion y Stack](#configuracion-y-stack)
  - [Convenciones de Contenido](#convenciones-de-contenido)
  - [Comandos](#comandos)
  - [Referencias](#referencias)

## Descripcion General

Este repositorio esta orientado a:

- Gestionar material de clases en [src/content/docs](src/content/docs)
- Publicar documentacion navegable usando Starlight
- Reutilizar componentes visuales para mejorar legibilidad
- Convertir documentos PDF/PPTX a MDX usando scripts en Python y Gemini AI

## Inicio Rapido

Desde la raiz del proyecto:

```bash
npm install
npm run dev
```

Sitio local: `http://localhost:4321`

## Estructura del Proyecto

```text
.
├── .github/
│   └── agents/
│       └── apuntes.agent.md
├── public/
├── scripts/
│   ├── convert_doc.py
│   ├── ai/
│   ├── parsers/
│   └── README.md
├── src/
│   ├── assets/
│   ├── components/
│   │   ├── MermaidDiagram.astro
│   │   ├── ErdDiagram.astro
│   │   ├── ClassDiagram.astro
│   │   └── README.md
│   ├── content/
│   │   └── docs/
│   │       ├── clases/
│   │       └── proyectos/
│   ├── styles/
│   │   └── custom.css
│   └── content.config.ts
├── astro.config.mjs
├── package.json
└── tsconfig.json
```

## Componentes Astro

Componentes disponibles en [src/components](src/components):

| Componente       | Proposito                                            |
| :--------------- | :--------------------------------------------------- |
| `ConceptCard`    | Tarjeta de concepto (label/titulo/descripcion)       |
| `ConceptGrid`    | Grilla responsiva para multiples `ConceptCard`       |
| `Callout`        | Bloques destacados tipo info/tip/warn                |
| `TwoCol`         | Layout de dos columnas                               |
| `SectionBox`     | Caja con titulo para agrupar contenido               |
| `Tag`            | Etiqueta individual tipo pill                        |
| `TagRow`         | Fila de etiquetas con wrap                           |
| `MermaidDiagram` | Componente base para render Mermaid (tema + errores) |
| `ErdDiagram`     | Wrapper Mermaid para `erDiagram`                     |
| `ClassDiagram`   | Wrapper Mermaid para `classDiagram`                  |

Documentacion detallada y ejemplos: [src/components/README.md](src/components/README.md)

## Sistema de Scripts

La carpeta [scripts](scripts) contiene el pipeline para convertir material fuente a apuntes web:

- `convert_doc.py`: orquestador CLI
- `parsers/pdf.py`: extraccion de texto/imagenes PDF
- `parsers/pptx.py`: procesamiento de presentaciones
- `ai/gemini.py`: sintesis con Gemini

Documentacion completa de requisitos, flags y ejemplos: [scripts/README.md](scripts/README.md)

## Configuracion y Stack

Configuracion principal en [astro.config.mjs](astro.config.mjs):

- Starlight con sidebar para `clases` y `proyectos`
- Soporte matematico con `remark-math` + `rehype-katex`
- Tema personalizado con [src/styles/custom.css](src/styles/custom.css)
- Locale principal en espanol

Dependencias principales en [package.json](package.json):

- `astro`
- `@astrojs/starlight`
- `astro-mermaid`
- `remark-math`
- `rehype-katex`
- `sharp`

## Convenciones de Contenido

Este proyecto usa reglas editoriales para mantener calidad y consistencia:

- Principios SOLID aplicados a contenido y componentes
- Bajo acoplamiento y alta cohesion
- Evitar duplicados (DRY)
- Uso de enlaces relativos entre apuntes
- Estructura consistente en frontmatter y rutas

Referencia de trabajo del agente de apuntes: [.github/agents/apuntes.agent.md](.github/agents/apuntes.agent.md)

## Comandos

Todos se ejecutan desde la raiz del proyecto:

| Comando                   | Accion                                   |
| :------------------------ | :--------------------------------------- |
| `npm install`             | Instala dependencias                     |
| `npm run dev`             | Levanta entorno local (`localhost:4321`) |
| `npm run start`           | Alias de `npm run dev`                   |
| `npm run build`           | Genera build en `dist/`                  |
| `npm run preview`         | Previsualiza el build                    |
| `npm run astro -- --help` | Ayuda del CLI de Astro                   |

## Referencias

- [Starlight Docs](https://starlight.astro.build/)
- [Astro Docs](https://docs.astro.build)
- [Mermaid](https://mermaid.js.org/)
- [KaTeX](https://katex.org/)
