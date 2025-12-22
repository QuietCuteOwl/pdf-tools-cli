import typer
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4, landscape
from PIL import Image
from pathlib import Path
from operations import ensure_dir
import os
import random
import string


app = typer.Typer()


def get_random_text(length=1000):
    return ''.join(random.choices(string.ascii_letters + string.digits + " ", k=length))


@app.command()
def text(filename: str = "text.pdf",
        pages: int = 1,
        heavy: bool = False,
        output_dir: Path = typer.Option(
        ...,
        "-o",
        "-output",
        dir_okay = True,
        file_okay = False,
        exists = True,
    )
):
    ensure_dir(output_dir)
    filepath = os.path.join(output_dir, filename)
    c = canvas.Canvas(filepath, pagesize=letter)
    width, height = letter
    
    if heavy:
        content_chunk = get_random_text(3000)
    else:
        content_chunk = get_random_text(200)

    for i in range(pages):
        c.setFont("Helvetica", 14)
        c.drawString(50, height - 50, f"Page {i+1} of {pages}")
        text_object = c.beginText(50, height - 50)

        lines_count = 100 if heavy else 20

        for _ in range(lines_count):
            text_object.textLine(content_chunk[:80])
            
        c.drawText(text_object)
        c.showPage()

    c.save()

# @app.command()
# def images(filename: str = "image.pdf", pages: int = 1, heavy: bool = False, 
#         output_dir: Path = typer.Option(
#         ...,
#         "-o",
#         "-output"
#         dir_okay = True,
#         file_okay = False,
#         exists = True,
#     )
# ):
#     ensure_dir(output_dir)
#     # construct full output filepath
#     # init reportlab canvas with filepath and letter size
#     # loop for the number of images (pages) requested:
#     #   generate random image using PIL (random size, random color)
#     #   save image temporarily to disk
#     #   draw page title
#     #   draw the temporary image onto the canvas
#     #   finish current page
#     #   remove temporary image file
#     # save canvas
#     # print success message


# @app.command()
# def empty(filename: str = "empty.pdf", pages: int = 1, output_dir: Path = typer.Option(
#         ...,
#         "-o",
#         "-output"
#         dir_okay = True,
#         file_okay = False,
#         exists = True,
#     )
# ):
#     # construct full output filepath
#     # init reportlab canvas
#     # call showPage to create an empty page
#     # save canvas
#     # print success message


# @app.command()
# def mixed(filename: str = "weird_layout.pdf",
#         output_dir: Path = typer.Option(
#         ...,
#         "-o",
#         "-output"
#         dir_okay = True,
#         file_okay = False,
#         exists = True,
#     )
# ):
#     # define command for mixed/weird pdf with arguments: filename
#     # ensure output directory exists
#     # construct full output filepath
#     # init reportlab canvas
#     # page 1: set size to Letter, add text, finish page
#     # page 2: set size to A4 Landscape, add text, finish page
#     # page 3: set size to Custom Square (300x300), add text, finish page
#     # page 4: set size to Long Strip (200x800), add text, finish page
#     # save canvas
#     # print success message


# @app.command()
# def all(
#     output_dir: Path = typer.Option(
#         ...,
#         "-o",
#         "-output"
#         dir_okay = True,
#         file_okay = False,
#         exists = True,
#     )
# ):
#     text("text_single.pdf", pages=1)
#     text("text_multi.pdf", pages=5)
#     text("large_text.pdf", pages=50, heavy=True)
#     images("image_heavy.pdf", count=5)
#     empty("empty.pdf")
#     mixed("weird_layout.pdf")

if __name__ == "__main__":
    app()
