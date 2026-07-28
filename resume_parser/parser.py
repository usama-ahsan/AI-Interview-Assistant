"""
resume_parser/parser.py

Extracts raw text from an uploaded resume PDF.
Pure function, no web/UI dependencies -- testable standalone.
"""

import io
from pypdf import PdfReader
from pypdf.errors import PdfReadError


def extract_text_from_pdf(file_path: str) -> str:
    """
    Read a PDF resume from disk and return its full text content.

    Args:
        file_path: path to a .pdf file on disk

    Returns:
        The extracted text as a single string (pages joined with newlines).
        Returns an empty string if the file has no extractable text
        (e.g. a scanned image-only PDF with no OCR layer).

    Raises:
        FileNotFoundError: if file_path does not exist
        ValueError: if the file is not a valid/readable PDF
    """
    try:
        reader = PdfReader(file_path)
    except FileNotFoundError:
        raise
    except (PdfReadError, Exception) as e:
        raise ValueError(f"Could not read PDF at {file_path}: {e}")

    return _extract_text_from_reader(reader)


def extract_text_from_bytes(file_bytes: bytes) -> str:
    """
    Read a PDF resume from in-memory bytes and return its full text.
    Used when the web layer receives an uploaded file and doesn't want
    to save it to disk first.

    Args:
        file_bytes: raw bytes of a PDF file

    Returns:
        The extracted text as a single string.

    Raises:
        ValueError: if the bytes do not form a valid/readable PDF
    """
    if not file_bytes:
        raise ValueError("Received empty file bytes")
    try:
        reader = PdfReader(io.BytesIO(file_bytes))
    except Exception as e:
        raise ValueError(f"Could not read PDF from bytes: {e}")

    return _extract_text_from_reader(reader)


def _extract_text_from_reader(reader: PdfReader) -> str:
    """Internal helper: pull text from every page of an already-open PdfReader."""
    if len(reader.pages) == 0:
        return ""

    pages_text = []
    for page in reader.pages:
        try:
            text = page.extract_text() or ""
        except Exception:
            # A single corrupt page shouldn't kill the whole extraction
            text = ""
        pages_text.append(text)

    return "\n".join(pages_text).strip()


if __name__ == "__main__":
    # Quick manual sanity check when run directly:
    #   python3 resume_parser/parser.py path/to/resume.pdf
    import sys
    if len(sys.argv) > 1:
        result = extract_text_from_pdf(sys.argv[1])
        print(result[:500])
    else:
        print("Usage: python3 parser.py <path_to_pdf>")
