import pypdfium2 as pdfium
import os
import requests

MISTRAL_API_KEY = "YOUR_API_KEY"  # replace with env var in production
MISTRAL_OCR_URL = "https://api.mistral.ai/v1/ocr"


def extract_text_pdf(file_path: str) -> str:
    """Extract text from a digital PDF (non-scanned)."""
    pdf = pdfium.PdfDocument(file_path)
    texts = []
    for page_num in range(len(pdf)):
        page = pdf[page_num]
        textpage = page.get_textpage()
        texts.append(textpage.get_text_range())
    return "\n".join(texts).strip()


def extract_text_ocr(file_path: str) -> str:
    """Send PDF/image to Mistral OCR API and return extracted text."""
    with open(file_path, "rb") as f:
        response = requests.post(
            MISTRAL_OCR_URL,
            headers={"Authorization": f"Bearer {MISTRAL_API_KEY}"},
            files={"file": f},
        )
    response.raise_for_status()
    data = response.json()
    return data.get("text", "").strip()


def extract_text(file_path: str, threshold: int = 50) -> str:
    """Try digital extraction first, fallback to OCR if too little text."""
    text = extract_text_pdf(file_path)

    if len(text) < threshold:
        text = extract_text_ocr(file_path)

    return text


def save_extracted_text(file_path: str, file_id: str):
    text = extract_text(file_path)

    os.makedirs("data/processed", exist_ok=True)
    out_path = f"data/processed/{file_id}_raw.txt"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)

    return out_path
