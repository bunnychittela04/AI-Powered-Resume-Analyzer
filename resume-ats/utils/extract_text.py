import os
import io
import tempfile
from typing import Tuple
from PyPDF2 import PdfReader
import docx2txt

ALLOWED_EXTS = {".pdf", ".docx", ".txt"}

def allowed_file(filename: str) -> bool:
    return os.path.splitext(filename.lower())[1] in ALLOWED_EXTS

def extract_text_from_upload(file_storage, filename: str) -> Tuple[str, str]:
    """Return (text, error). If error is not empty, text may be empty."""
    ext = os.path.splitext(filename.lower())[1]
    try:
        if ext == ".pdf":
            return _extract_pdf_text(file_storage), ""
        elif ext == ".docx":
            return _extract_docx_text(file_storage), ""
        elif ext == ".txt":
            data = file_storage.read()
            try:
                return data.decode("utf-8", errors="ignore"), ""
            except Exception:
                return data.decode("latin-1", errors="ignore"), ""
        else:
            return "", f"Unsupported file type: {ext}"
    except Exception as e:
        return "", f"Failed to extract text: {e}"

def _extract_pdf_text(file_storage) -> str:
    # PdfReader accepts a file-like object
    reader = PdfReader(file_storage)
    texts = []
    for page in reader.pages:
        page_text = page.extract_text() or ""
        texts.append(page_text)
    return "\n".join(texts)

def _extract_docx_text(file_storage) -> str:
    # docx2txt needs a filesystem path, so write to a temp file
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=True) as tmp:
        tmp.write(file_storage.read())
        tmp.flush()
        text = docx2txt.process(tmp.name) or ""
    return text
