---
title: "Portfolio Web — Arquitectura"
description: Estructura técnica y decisiones de diseño del proyecto portfolio.
---

## 📁 Estructura del Proyecto

```
portfolio/
├── public/
│   ├── favicon.svg
│   └── images/
├── src/
│   ├── components/
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── ProjectCard.astro
│   │   └── ThemeToggle.astro
│   ├── layouts/
│   │   └── MainLayout.astro
│   ├── pages/
│   │   ├── index.astro
│   │   ├── proyectos.astro
│   │   └── contacto.astro
│   └── styles/
│       └── global.css
├── astro.config.mjs
└── package.json
```

## Decisiones de Diseño

### ¿Por qué Astro?
- **Rendimiento**: Genera HTML estático, cero JavaScript por defecto
- **Flexibilidad**: Puede usar componentes de React, Vue, etc.
- **Simple**: Curva de aprendizaje baja
- **Optimizado**: Manejo automático de imágenes y assets

### Arquitectura de Componentes

```
┌──────────────────────────────────┐
│          MainLayout              │
├──────────────────────────────────┤
│  ┌────────────────────────────┐  │
│  │         Header             │  │
│  │  Logo | Nav | ThemeToggle  │  │
│  └────────────────────────────┘  │
│  ┌────────────────────────────┐  │
│  │         <slot />           │  │
│  │    (Contenido de página)   │  │
│  └────────────────────────────┘  │
│  ┌────────────────────────────┐  │
│  │         Footer             │  │
│  │   Links | Redes sociales   │  │
│  └────────────────────────────┘  │
└──────────────────────────────────┘
```

### Flujo de Datos

1. **Build time**: Astro procesa los archivos `.astro` y genera HTML estático
2. **Componentes**: Cada componente es independiente y recibe datos vía `props`
3. **Estilos**: CSS con scope por componente (no hay conflictos de estilos)
4. **Deploy**: El output es una carpeta `dist/` con archivos estáticos

## Patrones Utilizados

| Patrón | Descripción | Dónde |
|--------|-------------|-------|
| **Layout** | Template compartido entre páginas | `MainLayout.astro` |
| **Component** | UI reutilizable | `components/` |
| **Props** | Datos entre componentes | Todos los componentes |
| **Slots** | Contenido dinámico en layouts | `MainLayout.astro` |
