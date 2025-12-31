import pikepdf
import os
from typing import List

class Operations:
    def compress(input_pdf: str, output_path: str):

        name, _ = os.path.splitext(os.path.basename(input_pdf))
        destination = make_output_pdf(f"{name}_compressed", output_path)

        try:
            with pikepdf.open(input_pdf) as pdf:
                pdf.save(
                    destination,
                    static_id=True,
                    compress_streams=True,
                    object_stream_mode=pikepdf.ObjectStreamMode.generate,
                )
        except Exception as e:
            raise(e)

        return

    def merge(pdf_list: List[str], output_path: str):
        
        destination = make_output_pdf(f"merged", output_path)
        pdf_merged = pikepdf.new()
        for pdf_file in pdf_list:
            with pikepdf.open(pdf_file) as src:
                pdf_merged.pages.extend(src.pages)
        
        try:
            pdf_merged.save(destination)
        except Exception as e:
            raise(e)

    def split(input_pdf: str, output_dir: str):
        
        with pikepdf.open(input_pdf) as src:
            for i, page in enumerate(src.pages):
                tmp_pdf = pikepdf.new()
                tmp_pdf.pages.append(page)
                destination = make_output_pdf(f"{i + 1}_split", output_dir)
                tmp_pdf.save(destination)


    def extract_text(input_pdf, output_dir):
        import fitz
        
        src = fitz.open(input_pdf)
        text = ""

        for page in src:
            text += page.get_text()

        return text

    def add_page(source_pdf: str, page_num: int, target_pdf: str, output_dir: str):
        tmp_pdf = pikepdf.new()
        
        with pikepdf.open(target_pdf) as target:
            with pikepdf.open(source_pdf) as src:
                tmp_pdf.pages.extend(target.pages)
                if not page_num > len(src.pages):
                    tmp_pdf.pages.append(src.pages[page_num - 1])
                    name, _ = os.path.splitext(os.path.basename(target_pdf))
                    tmp_pdf.save(make_output_pdf(f"{name}_add", output_dir))
                else:
                    raise IndexError('Page number not in pdf')

        
    def remove_page(input_pdf: str, page_num: int, output_dir: str):
        tmp_pdf = pikepdf.new()

        with pikepdf.open(input_pdf) as src:
            for i, page in enumerate(src.pages):
                if i != page_num - 1:
                    tmp_pdf.pages.append(page)
            name, _ = os.path.splitext(os.path.basename(input_pdf))
            tmp_pdf.save(make_output_pdf(f"{name}_removed", output_dir))

    def watermark(input_pdf: str, watermark_pdf: str, output_dir: str):
        from pypdf import PdfReader, PdfWriter, Transformation
        
        reader = PdfReader(input_pdf)
        wm_reader = PdfReader(watermark_pdf)
        writer = PdfWriter()

        wm_page = wm_reader.pages[0]

        wm_w = wm_page.mediabox.width
        wm_h = wm_page.mediabox.height

        for page in reader.pages:
            
            src_w = page.mediabox.width
            src_h = page.mediabox.height

            scale_x = src_w / wm_w
            scale_y = src_h / wm_h

            transformation = Transformation().scale(sx=scale_x, sy=scale_y)

            page.merge_transformed_page(wm_page, transformation, over=True)

            writer.add_page(page)

        name, _ = os.path.splitext(os.path.basename(input_pdf))
        with open(make_output_pdf(f"{name}_watermarked", output_dir), "wb") as f:
            writer.write(f)


def ensure_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    return


def make_output_pdf(name, output_path):
    # change the destination_path to ../filename(n).pdf
    n = 1
    destination = os.path.join(output_path, (name + '.pdf'))
    while os.path.exists(destination):
        # name = name(n) where n is the number of files with the same name - 1
        destination = os.path.join(output_path, ((name + '(' + str(n) + ')' ) + '.pdf'))
        n += 1

    return destination
