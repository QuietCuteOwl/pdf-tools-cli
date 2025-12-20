from pypdf import PdfReader, PdfWriter
import os
from typing import List

class Operations:
    def compress(input_pdf: str, output_pdf: str):

        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        # loop through every page in reader, compress it, and add in to writer
        for page in reader.pages:
            page.compress_content_streams()
            writer.add_page(page) 

        # add meta data to writer from reader
        writer.add_metadata(reader.metadata)

        # open output pdf in mode "wb" and write to it from writer
        with open(output_pdf, "wb") as f:
            writer.write(f)


    def merge(pdf_paths: List[str], output_path: str):

        writer = PdfWriter()

        for pdf in pdf_paths:
            writer.append(pdf)
        
        with open(output_path, "wb") as f:
            writer.write(f)


    def split(input_path: str, output_dir: str):

        reader = PdfReader(input_path)

        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)
            
            output_filename = os.path.join(output_dir, f"page_{i+1}.pdf")
            with open(output_filename, "wb") as f:
                writer.write(f)


    def extract_text(input_path: str) -> str:
        reader = PdfReader(input_path)

        text = ""

        for page in reader.pages:
            text += page.extract_text() + "\n"
            
        return text
    

    def add_page(source_pdf: str, page_num: int, target_pdf: str, output_path: str):
        # page_num is 1-based index for user friendliness

        reader_source = PdfReader(source_pdf)
        reader_target = PdfReader(target_pdf)

        writer = PdfWriter()

        for page in reader_target.pages:
            writer.add_page(page)

        if 0 < page_num <= len(reader_source.pages):
            writer.add_page(reader_source.pages[page_num - 1])
        else:
            raise ValueError(f"Page number {page_num} is out of range for source PDF")

        with open(output_path, "wb") as f:
            writer.write(f)


    def remove_page(input_path: str, page_num: int, output_path: str):
        # page_num is 1-based index

        reader = PdfReader(input_path)
        writer = PdfWriter()

        for i, page in enumerate(reader.pages):
            if i != (page_num - 1):
                writer.add_page(page)

        with open(output_path, "wb") as f:
            writer.write(f)


    def watermark(input_path: str, watermark_path: str, output_path: str):

        reader_input = PdfReader(input_path)
        reader_watermark = PdfReader(watermark_path)

        watermark_page = reader_watermark.pages[0]

        writer = PdfWriter()

        for page in reader_input.pages:
            page.merge_page(watermark_page)
            writer.add_page(page)
        
        with open(output_path, "wb") as f:
            writer.write(f)

def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return