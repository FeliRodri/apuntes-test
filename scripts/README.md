# 🛠️ Scripts de Conversión y Síntesis (PDF/PPTX a MDX)

Este directorio contiene el motor principal para automatizar la extracción, conversión y síntesis de material académico (diapositivas, apuntes en PDF o presentaciones PPTX) hacia páginas de documentación enriquecidas (`.mdx`) listas para usar en **Astro / Starlight**.

A través de **Gemini AI (Visión y Texto)**, el sistema no solo extrae el texto, sino que "ve" las diapositivas, rescata diagramas clave, ignora capturas de texto plano y maqueta la información utilizando componentes interactivos (Tarjetas, Callouts, Grillas).

---

## 📋 Requisitos Previos

### 1. Dependencias de Python

Debes tener instaladas las siguientes librerías:

```bash
pip install PyMuPDF google-genai
```

### 2. Dependencias del Sistema

Si planeas convertir archivos `.pptx`, el sistema utiliza LibreOffice en modo _headless_ (invisible) para asegurar que los vectores y SmartArts se rendericen correctamente:

```bash
# En Ubuntu/Debian:
sudo apt install libreoffice
```

### 3. Variables de Entorno

Para utilizar el motor de Inteligencia Artificial (síntesis estructural), necesitas exportar tu clave de Google Gemini:

```bash
export GEMINI_API_KEY="tu_clave_aqui"
```

---

## 🚀 Uso del Convertidor

El orquestador principal es `convert_doc.py`. Este script se encarga de determinar el tipo de archivo, extraer el contenido, enviarlo a la IA (si se requiere) y guardar el archivo en la ruta correspondiente dentro de `src/content/docs/`.

### Sintaxis Básica

```bash
python convert_doc.py <input_file> <output_path> "<title>" "<description>" [--ai] [-f]
```

### Argumentos

| Argumento       | Descripción                                                                                                          |
| :-------------- | :------------------------------------------------------------------------------------------------------------------- |
| `input_file`    | Ruta al archivo original (`.pdf` o `.pptx`).                                                                         |
| `output_path`   | Ruta de destino relativa a `src/content/docs/` (Ej: `clases/historia/unidad1`). **No incluyas la extensión `.mdx`**. |
| `title`         | Título del apunte (se inyecta en el frontmatter YAML).                                                               |
| `description`   | Descripción corta (se inyecta en el frontmatter YAML).                                                               |
| `--ai`          | **(Opcional)** Activa la síntesis con Gemini. Si no se incluye, extraerá el texto y las capturas en bruto.           |
| `-f`, `--force` | **(Opcional)** Sobrescribe el archivo de destino si ya existe, sin pedir confirmación.                               |

### Ejemplos de ejecución

**1. Conversión de PDF usando IA (Recomendado):**

```bash
python convert_doc.py ./material/clase1.pdf clases/bases-de-datos/introduccion "Intro a BD" "Conceptos iniciales" --ai
```

**2. Conversión de Presentación PPTX en bruto (Sin IA):**

```bash
python convert_doc.py ./material/expo.pptx proyectos/expo_final "Exposición Final" "Apuntes de la expo"
```

---

## ✨ Características Principales

### 🧩 Inyección Automática de Componentes MDX

El script calcula dinámicamente cuántas carpetas debe subir (`../`) desde el `output_path` hasta la raíz de componentes (`src/components/`). Así, tus apuntes siempre tienen acceso nativo a:

- `<ConceptCard>` y `<ConceptGrid>`
- `<Callout>` (info, tip, danger, caution)
- `<ErdDiagram>` (Mermaid)

### 👁️ Gemini Vision Integrado

Al usar la flag `--ai`, el script inyecta el PDF directamente a la API de Gemini. La inteligencia artificial está instruida para:

- Usar componentes visuales en lugar de Markdown aburrido.
- Identificar diapositivas que contienen diagramas/gráficos y embeberlos en el archivo final.
- Omitir las imágenes de diapositivas que solo contienen texto, evitando saturar tu documentación.

### 🧹 Sistema de Cuarentena (Higiene)

El parser genera imágenes en alta definición para _todas_ las páginas de tu documento. Sin embargo, tras la síntesis de la IA, **las diapositivas que la IA consideró irrelevantes (texto plano) son evacuadas del proyecto web** y enviadas a una cuarentena local (`~/Documentos/Apuntes_Revision/Diapositivas_Descartadas/`). Esto mantiene tu repositorio web extremadamente ligero y limpio.

---

## 📂 Estructura de Scripts

- `convert_doc.py`: Orquestador CLI principal.
- `parsers/pdf.py`: Motor de PyMuPDF para extracción rápida y screenshots vectoriales.
- `parsers/pptx.py`: Motor Puente que transforma presentaciones a PDF fantasma para reutilizar el parser.
- `ai/gemini.py`: Lógica de red, reintentos y _Prompts_ del asistente académico para procesar el contexto multimodal.
