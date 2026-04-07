#!/usr/bin/env python3
import sys
import os
import shutil
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
        content = pptx.extract_text(input_path, args.output_path)
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
    
    # --- SISTEMA DE CUARENTENA (POST-PURGE INTELIGENTE) ---
    img_folder = base_docs_dir / args.output_path
    if img_folder.exists() and img_folder.is_dir():
        # Carpeta externa asilada fuera del ecosistema web para evitar peso innecesario
        quarantine_base = Path(os.path.expanduser('~/Documentos/Apuntes_Revision/Diapositivas_Descartadas'))
        quarantine_dir = quarantine_base / img_folder.name
        
        discarded_count = 0
        for img_file in img_folder.glob("*.png"):
            # Si el archivo exacto generado no figura en el cuerpo definitivo, IA lo rechazó
            if img_file.name not in md_content:
                if discarded_count == 0:
                    quarantine_dir.mkdir(parents=True, exist_ok=True)
                
                # Mover el archivo (Evacuación)
                shutil.move(str(img_file), str(quarantine_dir / img_file.name))
                discarded_count += 1
                
        if discarded_count > 0:
            print(f"🧹 Higiene del Proyecto: {discarded_count} diapositivas (sin gráficos clave) fueron descartadas del servidor web local.")
            print(f"   -> Han sido evacuadas exitosamente a cuarentena en: {quarantine_dir}")
    print("✅ Índice lateral de Starlight actualizado automáticamente vía Autogenerate.")

if __name__ == "__main__":
    main()
