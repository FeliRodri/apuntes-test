import sys
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

# Re-utilizamos el engine robusto de PDF
from parsers import pdf

def extract_text(filepath, output_path):
    """
    Toma un archivo PPTX, lo renderiza silenciosamente a un PDF manteniendo 
    todos los vectores gráficos (SmartArt, Charts, Shapes), y luego lo 
    pasa por nuestro pipeline super-visual de pdf.py (PyMuPDF).
    """
    filepath = Path(filepath).resolve()
    print(f"🔄 Convirtiendo presentación a Formato Vectorial (PDF) mediante LibreOffice...")
    
    # Validamos que libreoffice exista en el sistema
    lo_bin = "libreoffice" if shutil.which("libreoffice") else "soffice"
    if shutil.which(lo_bin) is None:
        print("Error: Se necesita LibreOffice para renderizar presentaciones a PDF de forma nativa.")
        print("En Ubuntu/Debian instala con: sudo apt install libreoffice")
        sys.exit(1)
        
    # Crear un directorio temporal para el "PDF Fantasma"
    with tempfile.TemporaryDirectory() as temp_dir:
        # Comando para LibreOffice Headless
        cmd = [
            lo_bin,
            "--headless",
            "--convert-to", "pdf",
            str(filepath),
            "--outdir", temp_dir
        ]
        
        try:
            # Inhibimos el output estándar para no ensuciar la consola a menos que falle
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            print("Error: Falló la conversión de PPTX a PDF con LibreOffice.")
            sys.exit(1)
            
        # Encontramos el archivo generado (mismo nombre base, pero extensión .pdf)
        pdf_filename = filepath.stem + ".pdf"
        pdf_path = Path(temp_dir) / pdf_filename
        
        if not pdf_path.exists():
            print("Error: LibreOffice se ejecutó pero el PDF fantasma no apareció.")
            sys.exit(1)
            
        print(f"📖 Renderizado completado. Delegando al motor de capturas de alta definición...")
        
        # Le delegamos toda esta maravilla a nuestro parseador robusto.
        # pdf.py se encargará de hacer los png y generar el texto base.
        content = pdf.extract_text(pdf_path, output_path)
        
    return content
