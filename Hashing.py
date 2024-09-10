import fitz  # PyMuPDF
import hashlib

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

pdf_path = "C:/Users/PC/Desktop/Hash-A.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
print(pdf_text)



hashedval = hashlib.sha256(pdf_text.encode('utf-8')).hexdigest()
print(f"SHA-256 Hash: {hashedval}")