---
title: Guía de Uso
description: Aprende cómo agregar y organizar contenido en tu sitio de documentación.
---

## ¿Cómo agregar contenido?

Todo el contenido vive dentro de la carpeta `src/content/docs/`. Solo necesitas crear archivos **Markdown** (`.md`) o **MDX** (`.mdx`).

### Crear una nueva página

1. Crea un archivo `.md` en la carpeta correspondiente:
   ```
   src/content/docs/clases/mi-materia/nuevo-tema.md
   ```

2. Agrega el **frontmatter** al inicio del archivo:
   ```markdown
   ---
   title: Nombre del Tema
   description: Una breve descripción del contenido.
   ---
   ```

3. Escribe tu contenido debajo usando Markdown normal.

4. Agrega la página al **sidebar** en `astro.config.mjs`.

### Sintaxis Markdown útil

```markdown
# Título principal
## Subtítulo
### Sub-subtítulo

**Texto en negrita** y *texto en cursiva*

- Lista con viñetas
- Otro punto

1. Lista numerada
2. Segundo paso

> Cita o nota importante

`código en línea`

| Columna 1 | Columna 2 |
|-----------|-----------|
| Dato 1    | Dato 2    |
```

### Bloques de código con resaltado

Puedes incluir código con syntax highlighting:

````markdown
```python
def hola():
    print("¡Hola mundo!")
```
````

### Alertas y notas

Starlight incluye componentes especiales para notas:

```mdx
import { Aside } from '@astrojs/starlight/components';

<Aside type="tip">Un consejo útil aquí.</Aside>
<Aside type="caution">¡Cuidado con esto!</Aside>
<Aside type="danger">Esto es importante.</Aside>
```

## Estructura de carpetas

```
src/content/docs/
├── index.mdx          ← Página principal
├── guia.md            ← Esta guía
├── clases/
│   ├── introduccion.md
│   ├── programacion/
│   │   ├── fundamentos.md
│   │   └── poo.md
│   └── bases-de-datos/
│       ├── introduccion.md
│       └── sql-basico.md
└── proyectos/
    ├── introduccion.md
    └── portfolio/
        ├── descripcion.md
        └── arquitectura.md
```

## Comandos útiles

| Comando | Descripción |
|---------|-------------|
| `npm run dev` | Inicia el servidor de desarrollo en `localhost:4321` |
| `npm run build` | Genera el sitio estático para producción |
| `npm run preview` | Vista previa del build de producción |
