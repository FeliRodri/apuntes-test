# Apuntes Starlight — Bases de datos relacionales

## Estructura de archivos

```
src/
├── components/
│   ├── ConceptCard.astro   ← tarjeta de concepto (label + título + descripción)
│   ├── ConceptGrid.astro   ← grilla 2 columnas para ConceptCards
│   ├── Callout.astro       ← bloque destacado (info / tip / warn)
│   ├── TwoCol.astro        ← layout de dos columnas
│   ├── SectionBox.astro    ← caja con título para usar dentro de TwoCol
│   ├── Tag.astro           ← etiqueta pill
│   ├── TagRow.astro        ← fila de Tags con wrap
│   ├── MermaidDiagram.astro← base Mermaid (render + theme + errores)
│   ├── ErdDiagram.astro    ← wrapper para diagramas ER (erDiagram)
│   └── ClassDiagram.astro  ← wrapper para diagramas de clases (classDiagram)
└── content/
    └── docs/
        └── bases-de-datos.mdx
```

## Instalación

1. Copia los archivos de `components/` a `src/components/` de tu proyecto.
2. Copia `bases-de-datos.mdx` a `src/content/docs/` (o la ruta que uses para tus docs).
3. Ajusta los imports en el MDX si tus componentes están en otra carpeta:

```mdx
import ConceptCard from "../../components/ConceptCard.astro";
```

## Notas importantes

### Variables CSS de Starlight

Los componentes usan exclusivamente variables de Starlight:

- `--sl-color-bg-nav` — fondo de tarjetas
- `--sl-color-hairline` — bordes
- `--sl-color-white` — texto principal
- `--sl-color-gray-3` — texto secundario
- `--sl-color-text-accent` — color de acento (labels)
- `--sl-color-blue / green / orange` — colores de callouts

Funcionan automáticamente en modo claro y oscuro sin configuración adicional.

### Mermaid y Wrappers

`MermaidDiagram.astro` es el componente base que:

- carga mermaid.js desde `esm.sh` en cliente,
- aplica tema compatible con Starlight,
- maneja errores de render,
- acepta `type="erDiagram" | "classDiagram"` o detecta el tipo desde la primera línea del diagrama.

Sobre ese base existen wrappers especializados:

- `ErdDiagram.astro` para `erDiagram`
- `ClassDiagram.astro` para `classDiagram`

No requiere instalar ninguna dependencia adicional.

Starlight también tiene soporte nativo para mermaid via el plugin oficial:

```
npm install @astrojs/starlight-mermaid
```

Si ya lo usas, puedes reemplazar `<ErdDiagram>` y `<ClassDiagram>` con bloques de código ` ```mermaid ` directamente en el MDX.

### Modo oscuro

El componente base `MermaidDiagram` detecta el tema de Starlight leyendo
`document.documentElement.getAttribute("data-theme")`. Starlight establece
este atributo automáticamente al cambiar de tema, por lo que funciona sin
configuración adicional.

## Uso de los componentes

```mdx
import ConceptCard from "../components/ConceptCard.astro";
import ConceptGrid from "../components/ConceptGrid.astro";
import Callout from "../components/Callout.astro";
import TwoCol from "../components/TwoCol.astro";
import SectionBox from "../components/SectionBox.astro";
import Tag from "../components/Tag.astro";
import TagRow from "../components/TagRow.astro";
import ErdDiagram from "../components/ErdDiagram.astro";
import ClassDiagram from "../components/ClassDiagram.astro";

<!-- Grilla de tarjetas -->

<ConceptGrid>
  <ConceptCard label="Tipo" title="Nombre" desc="Descripción del concepto." />
</ConceptGrid>

<!-- Callout -->

<Callout type="info" title="Título opcional">
  Contenido del callout. Acepta **markdown** dentro.
</Callout>

<!-- Dos columnas -->

<TwoCol>
  <SectionBox title="Columna 1">- item a - item b</SectionBox>
  <SectionBox title="Columna 2">- item c</SectionBox>
</TwoCol>

<!-- Tags -->

<TagRow>
  <Tag>término 1</Tag>
  <Tag>término 2</Tag>
</TagRow>

<!-- Diagrama ERD -->

<ErdDiagram
  id="mi-erd"
  diagram={`erDiagram
  TABLA_A ||--o{ TABLA_B : relacion
`}
/>

<!-- Diagrama de clases -->

<ClassDiagram
  id="mi-class"
  diagram={`classDiagram
  class Piloto {
    dni PK
    nombre
  }
  class Escuderia {
    nombre PK
  }
  Piloto "*" --> "1" Escuderia : corre para
`}
/>
```
