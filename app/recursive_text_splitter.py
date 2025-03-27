from langchain.text_splitter import RecursiveCharacterTextSplitter
from pdf_text_extractor import PDFTextExtractor


class TextSplitter:
    def __init__(
        self, pdf_path: str, chunk_size: int, chunk_overlap: int
    ) -> None:
        self.pdf_path = pdf_path
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_pdf_text(self) -> str:
        pdf_extractor = PDFTextExtractor()
        text = pdf_extractor.extract_text_from_pdf(self.pdf_path)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " "],
            is_separator_regex=False,
        )

        texts = text_splitter.split_text(text)

        return texts
