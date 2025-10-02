# PDF Utilities (`backend.pdf_utils`)

Utilities for extracting text from PDFs and images.

## Environment
- `MISTRAL_API_KEY`: API key for OCR requests (set via environment variable in production; code currently uses a placeholder).

## Functions

### `extract_text_pdf(file_path: str) -> str`
Extract text from a digital (non-scanned) PDF using `pypdfium2`.

- **Parameters**: `file_path` – path to a local PDF file.
- **Returns**: Full text extracted from all pages.
- **Raises**: Exceptions from `pypdfium2` if PDF is invalid.

**Example**
```python
from backend.pdf_utils import extract_text_pdf

text = extract_text_pdf("/path/to/book.pdf")
print(text[:500])
```

---

### `extract_text_ocr(file_path: str) -> str`
Send a PDF/image to the Mistral OCR API and return extracted text.

- **Parameters**: `file_path` – path to a local PDF or image file.
- **Returns**: Extracted text.
- **Raises**: `requests.HTTPError` on non-2xx responses.

**Example**
```python
import os
from backend.pdf_utils import extract_text_ocr

os.environ["MISTRAL_API_KEY"] = "..."  # ensure key is available in production
text = extract_text_ocr("/path/to/scanned.pdf")
```

---

### `extract_text(file_path: str, threshold: int = 50) -> str`
Attempt digital extraction first; if the resulting text length is below `threshold`, fallback to OCR.

- **Parameters**:
  - `file_path` – path to the input document
  - `threshold` – minimal length before triggering OCR fallback
- **Returns**: Extracted text.

**Example**
```python
from backend.pdf_utils import extract_text

text = extract_text("/path/to/document.pdf", threshold=80)
```

---

### `save_extracted_text(file_path: str, file_id: str) -> str`
Extract text (with fallback) and write it to `data/processed/{file_id}_raw.txt`.

- **Parameters**:
  - `file_path` – input path
  - `file_id` – identifier used in output filename
- **Returns**: Output text file path.
- **Side effects**: Creates `data/processed` directory if needed.

**Example**
```python
from backend.pdf_utils import save_extracted_text

out_path = save_extracted_text("/path/to/document.pdf", file_id="book123")
print("Saved to:", out_path)
```

## Notes
- In production, replace the hardcoded `MISTRAL_API_KEY` with `os.environ["MISTRAL_API_KEY"]` or a secrets manager.
- Network calls to OCR service may incur latency; add retries/timeouts as needed.
