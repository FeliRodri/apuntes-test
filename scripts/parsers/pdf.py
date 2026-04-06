import sys

try:
    import PyPDF2
except ImportError:
    print("Falta la librería PyPDF2. Por favor instala las dependencias:")
    print("pip install PyPDF2")
    sys.exit(1)

def extract_text(filepath):
    """Extrae texto página por página de un PDF."""
    text_content = []
    try:
        with open(filepath, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text and page_text.strip():
                    text_content.append(f"## Página {i+1}\n\n{page_text}")
    except Exception as e:
        print(f"Error leyendo PDF: {e}")
        sys.exit(1)
    
    return "\n\n".join(text_content)
