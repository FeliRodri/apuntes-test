import sys
import os

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Falta la librería PyMuPDF. Por favor instala las dependencias:")
    print("pip install PyMuPDF")
    sys.exit(1)

def extract_text(filepath, output_path):
    """Extrae texto e imágenes completas (screenshots de páginas) de un PDF."""
    text_content = []
    
    base_docs_dir = os.path.join("src", "content", "docs")
    img_dir = os.path.join(base_docs_dir, output_path)
    folder_name = os.path.basename(output_path)
    
    try:
        doc = fitz.open(filepath)
        os.makedirs(img_dir, exist_ok=True)
        
        for i, page in enumerate(doc):
            page_text = page.get_text()
            extracted_images = ""
            
            # --- Renderizado de Captura (Screenshot de la diapositiva completa) ---
            # Utilizamos una matriz de zoom para obtener resolución nítida
            zoom = 2.0
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)
            
            image_filename = f"slide_p{i+1}.png"
            image_filepath = os.path.join(img_dir, image_filename)
            
            pix.save(image_filepath)
            
            # Formateamos el enlace exacto para pasarlo a Gemini
            extracted_images = f"\n\n![Captura de Diapositiva {i+1}](./{folder_name}/{image_filename})\n\n"
            
            if page_text and page_text.strip():
                text_content.append(f"## Página {i+1}\n\n{page_text}\n{extracted_images}")
                
    except Exception as e:
        print(f"Error leyendo PDF con PyMuPDF: {e}")
        sys.exit(1)
    
    return "\n\n".join(text_content)
