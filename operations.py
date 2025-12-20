from pypdf import PdfReader, PdfWriter
import os
from typing import List

def compress(input_pdf: str, output_pdf: str):

    if not os.path.exists(output_pdf):
        os.makedirs(output_pdf)

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
    # loop through every input path in the list of pdfs
    # append the pdf to the merger
    # open output pdf in mode "wb" and write to it from merger

def split(input_path: str, output_dir: str):
    # init pdf reader with path to input pdf
    # get the parent directory of input pdf for output reference
    # loop through every page in reader with its index
    # init writer for this single page
    # add the current page to the writer
    # construct output filename using the index
    # open output file in mode "wb" and write to it from writer

def extract_text(input_path: str) -> str:
    # init pdf reader with path to input pdf
    # init empty string variable to hold text
    # loop through every page in reader
    # extract text from the page and append it to the string variable
    # return the text string var

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
    