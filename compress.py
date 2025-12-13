import typer
from pathlib import Path
from pypdf import PdfReader, PdfWriter

app = typer.Typer()

@app.command()
def compress(
    input_pdf: Path = typer.Argument(
        ...,
        help="Input PDF file",
        exists=True, 
        file_okay=True, 
        dir_okay=False,
        readable=True
    ), 
    output_pdf: Path = typer.Option(
        None,
        "-o",
        "--output",
        help="Output compressed PDF file")
):
    
    if output_pdf is None:
        output_pdf = input_pdf.parent / f"{input_pdf.stem}_compressed.pdf"
    
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # loop through every page in reader and add in to writer
    for page in reader.pages:
        writer.add_page(page)

    # loop through every page in writer and compress it
    for page in writer.pages:
        page.compress_content_streams()

    # add meta data to writer from reader
    writer.add_metadata(reader.metadata)

    # open output pdf in mode "wb" and write to it from writer
    with open(output_pdf, "wb") as f:
        writer.write(f)

if __name__ == '__main__':
    app()
