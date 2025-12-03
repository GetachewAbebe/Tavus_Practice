import os
import pypdf

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.
    
    Args:
        file_path: Path to the PDF file
        
    Returns:
        Extracted text as a string
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF file not found: {file_path}")
        
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""
        
    return text.strip()

def find_pdf_in_dir(directory: str) -> str:
    """
    Find the first PDF file in a directory.
    
    Args:
        directory: Directory to search in
        
    Returns:
        Path to the first PDF found, or None
    """
    for file in os.listdir(directory):
        if file.lower().endswith('.pdf'):
            return os.path.join(directory, file)
    return None
