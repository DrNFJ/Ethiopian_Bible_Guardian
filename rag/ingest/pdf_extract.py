from pathlib import Path

from pypdf import PdfReader


def extract_pdf_pages(pdf_path: Path) -> list[dict]:
    """Extract page-level text with provenance from a PDF file."""
    reader = PdfReader(str(pdf_path))
    pages: list[dict] = []

    for i, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        pages.append(
            {
                "source_file": pdf_path.name,
                "page_number": i,
                "text": text,
            }
        )

    return pages
