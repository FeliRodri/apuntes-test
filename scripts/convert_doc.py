#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path

# Local imports
from parsers import pdf
from parsers import pptx
from ai.gemini import synthesize

def generate_frontmatter(title, description):
    """Genera el bloque YAML de frontmatter para Starlight."""
    return f"""---
title: {title}
description: {description}
---

"""

def main():
    parser = argparse.ArgumentParser(description="Convierte un archivo PDF o PPTX en una página Markdown para Starlight.")
    parser.add_argument("input_file", help="Ruta al archivo original (.pdf o .pptx)")
    parser.add_argument("output_path", help="Ruta relativa en src/content/docs (ej. 'clases/historia/unidad1')")
    parser.add_argument("title", help="Título de la página")
    parser.add_argument("description", help="Descripción de la página")
    parser.add_argument("--ai", action="store_true", help="Utiliza Gemini AI para estructurar y limpiar los apuntes automáticamente")
    parser.add_argument("-f", "--force", action="store_true", help="Sobrescribe el archivo de destino si ya existe, sin preguntar")
    
    args = parser.parse_args()
    
    # Determinar el archivo de salida inmediatamente para validarlo temprano
    base_docs_dir = Path("src/content/docs")
    output_file = base_docs_dir / f"{args.output_path}.md"
    
    # Seguro de protección contra sobreescritura accidental
    if output_file.exists() and not args.force:
        print(f"\n⚠️  ATENCIÓN: El archivo destino ya contiene apuntes valiosos:")
        print(f"   -> {output_file}")
        respuesta = input("¿Estás 100% seguro de que deseas destruirlo y SOBREESCRIBIRLO? (s/N): ")
        if respuesta.lower() not in ('s', 'si', 'sí', 'y', 'yes'):
            print("Operación cancelada por seguridad. (Tus apuntes están a salvo 🛡️)")
            print("Consejo: Cambia la ruta en tu comando, por ejemplo: 'clases/bases-de-datos/usm_v2'")
            sys.exit(0)
    
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: El archivo {input_path} no existe.")
        sys.exit(1)
        
    ext = input_path.suffix.lower()
    print(f"Procesando {input_path.name}...")
    
    # Delegar responsabilidad de parseo al módulo correspondiente (Alta cohesión)
    if ext == '.pdf':
        content = pdf.extract_text(input_path, args.output_path)
    elif ext == '.pptx':
        content = pptx.extract_text(input_path)
    else:
        print(f"Error: Formato {ext} no soportado. Usa .pdf o .pptx.")
        sys.exit(1)
        
    # Delegar responsabilidad de síntesis (Acoplamiento bajo)
    if args.ai:
        content = synthesize(content, filepath=input_path)
        
    # Construir el contenido final Markdown
    md_content = generate_frontmatter(args.title, args.description) + content
    
    # Escribir a disco
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print(f"✅ ¡Éxito! Archivo generado en: {output_file}")
    print("Recuerda agregar el nuevo slug al archivo astro.config.mjs para que aparezca en el sidebar.")

if __name__ == "__main__":
    main()
