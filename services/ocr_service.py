import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import os

# Configure tesseract path (Windows default installation path)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\SYED\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


def extract_text_from_image(image_path):
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)

def extract_text_from_pdf(pdf_path):
    pdf = fitz.open(pdf_path)
    text = ""

    for page_num in range(len(pdf)):
        page = pdf[page_num]
        text += page.get_text()

    return text.strip()

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext in [".jpg", ".jpeg", ".png"]:
        return extract_text_from_image(file_path)

    elif ext == ".pdf":
        return extract_text_from_pdf(file_path)

    else:
        return "Unsupported file format"
