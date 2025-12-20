from pypdf import PdfReader, PdfWriter
import os
from typing import List

class Operations:
    def compress(input_pdf: str, output_pdf: str):

        make_dir(output_pdf)

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

        make_dir(output_path)

        writer = PdfWriter()

        for pdf in pdf_paths:
            writer.append(pdf)
        
        with open(output_path, "wb") as f:
            writer.write(f)


    def split(input_path: str, output_dir: str):

        make_dir(output_dir)

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
        # init reader for the target pdf (the base document)
        # init reader for the source pdf (where the new page comes from)
        # init writer
        # loop through all pages in target reader and add them to writer
        # get the specific page from source reader using the page number
        # add the source page to the writer
        # add meta data to writer from target reader
        # open output pdf in mode "wb" and write to it from writer

    def remove_page(input_path: str, page_num: int, output_path: str):
        # init pdf reader with path to input pdf
        # init writer
        # loop through every page in reader with its index
        # check if current index is not equal to the page number to remove
        # if it is not the removed page, add it to the writer
        # add meta data to writer from reader
        # open output pdf in mode "wb" and write to it from writer

    def watermark_pdf(input_path: str, watermark_path: str, output_path: str):
        # init reader for input pdf
        # init reader for watermark pdf
        # get the first page of the watermark pdf to use as the stamp
        # init writer
        # loop through every page in input reader
        # merge the page with the watermark page contents
        # add the merged page to the writer
        # open output pdf in mode "wb" and write to it from writer

def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return