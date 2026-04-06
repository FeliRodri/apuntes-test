import os
import sys

def synthesize(raw_text, filepath=None):
    """Usa la IA de Gemini para sintetizar los apuntes y 'ver' PDFs."""
    try:
        from google import genai
    except ImportError:
        print("Para usar la síntesis estructurada con IA, instala el SDK de Gemini:")
        print("pip install google-genai")
        sys.exit(1)
        
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: No se encontró la variable GEMINI_API_KEY.")
        print("Antes de ejecutar el script, exporta tu clave en la terminal:")
        print("export GEMINI_API_KEY='tu_clave_aqui'")
        sys.exit(1)
        
    print("🤖 Procesando apuntes con IA para estructurarlos (puede tomar unos segundos)...")
    client = genai.Client()
    
    prompt = f"""Eres un asistente académico experto. Tu objetivo es procesar el siguiente texto extraído de presentaciones y PDFs universitarios, eliminando el "ruido" y convirtiéndolo en apuntes de estudio de altísima calidad en formato Markdown.

REGLAS ESTRICTAS:
1. NUNCA uses un solo '#' y EVITA usar '####' o '#####'. Usa EXCLUSIVAMENTE '##' para las secciones principales y '###' para las subsecciones, ya que Starlight solo muestra estos niveles en su tabla de contenidos (sidebar derecho).
2. Usa listas para enumerar conceptos importantes.
3. Usa Callouts de Starlight (:::note, :::tip, :::danger, :::caution) para resaltes. ATENCIÓN: Si agregas un título al callout, DEBE ir entre corchetes pegado a los dos puntos. Ejemplo: :::note[Definición de X]. Luego cierras con ::: al final.
4. Elimina basura textual como "Página 1", "Unidad 1", pies de página o índices vacíos.
5. Formatea fragmentos de código con bloques (ej. ```sql).
6. CRÍTICO SOBRE CAPTURAS VISUALES: En el texto extraído que te proveeré, cada página está marcada con una ruta a su captura fotográfica (con formato exacto `![Captura de Diapositiva X](./carpeta/slide_pX.png)`). 
   - SI LA DIAPOSITIVA contiene un diagrama de flujo, tabla gráfica, mapa conceptual vectorial o elemento visual clave que sea valioso para el estudiante universitario, ESTÁS OBLIGADO a copiar y pegar esa ruta exacta (ej: `./mitema/slide_p4.png`) integrándola en la sección correspondiente.
   - SI LA DIAPOSITIVA es únicamente texto (bullets, definiciones teóricas, listados), DEBES OMITIR y ELIMINAR su enlace `![Captura...]` de tus apuntes finales para no saturar al estudiante con fotos de texto puro.
   - BAJO NINGUNA CIRCUNSTANCIA inventes nombres de archivo (como "unnamed-chunk"). Usa SOLAMENTE los tags proporcionados. NO uses mermaid.
7. Tu respuesta debe ser EXCLUSIVAMENTE el texto Markdown sintetizado. SIN saludos, SIN bloques "```markdown" englobando todo tu output.
"""

    contents_to_generate = [prompt]
    uploaded_file = None
    
    # Integración con Gemini Vision: Si es PDF, subirlo a la API para activar el análisis visual
    if filepath and str(filepath).lower().endswith('.pdf'):
        print("👁️  Inyectando PDF a Gemini Vision para análisis visual de diagramas y gráficos...")
        try:
            uploaded_file = client.files.upload(file=str(filepath))
            contents_to_generate.append(uploaded_file)
            print("👁️  Visión artificial activada. Leyendo texto y procesando imágenes...")
        except Exception as e:
            print(f"⚠️  Aviso: No se pudo inyectar para análisis visual ({e}). Cayendo a análisis de solo-texto.")
            contents_to_generate.append(f"Texto extraído a sintetizar:\n{raw_text}")
    else:
        contents_to_generate.append(f"Texto extraído a sintetizar:\n{raw_text}")

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=contents_to_generate,
        )
        content = response.text.strip()
        # Limpiar si el LLM envuelve todo en un bloque markdown
        if content.startswith("```markdown"):
            content = content[11:].strip()
            if content.endswith("```"):
                content = content[:-3].strip()
        
        # Limpieza de recursos en servidor
        if uploaded_file:
            try:
                client.files.delete(name=uploaded_file.name)
            except Exception:
                pass
                
        return content
    except Exception as e:
        print(f"Error procesando con IA: {e}")
        print("Se guardará el texto original en bruto.")
        return raw_text
