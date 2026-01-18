import pdfplumber
from app.services.embeddings import embed
from app.services.rag_pipeline import collection

def ingest(pdf_path, source):
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                continue

            collection.add(
                documents=[text],
                embeddings=[embed(text)],
                metadatas=[{
                    "source": source,
                    "page": i + 1
                }],
                ids=[f"{source}_{i}"]
            )

if __name__ == "__main__":
    ingest("ncert_grade2.pdf", "NCERT Grade 2 Handbook")
