import typer
from pathlib import Path
from operations import make_dir, Operations as ops

app = typer.Typer()

@app.command()
def compress(
    input_path: Path = typer.Argument(
        ...,
        exists=True,
        dir_okay=False,
        file_okay=True,
        help="Input PDF file"
    ),
    output_path: Path = typer.Option(
        ...,
        "-o",
        "--output",
        help="Output PDF file"
    ),
):
    make_dir(output_path)
    ops.compress(str(input_path), str(output_path))
    typer.echo(f"Successfully compressed {input_path} to {output_path}")
    return


@app.command()
def merge(
    input_paths: List[Path] = typer.Argument(
        ...,
        exists=True,
        dir_okay=False,
        file_okay=True,
        help="Input PDF files to merge"
    ),
    output_path: Path = typer.Option(
        ...,
        "-o",
        "--output",
        help="Output PDF file"
    ),
):
    make_dir(output_path)
    paths_str = [str(p) for p in input_paths]
    ops.merge(paths_str, str(output_path))
    typer.echo(f"Successfully merged {len(input_paths)} files into {output_path}")


@app.command()
def split(
    input_path: Path = typer.Argument(
        ...,
        exists=True,
        dir_okay=False,
        file_okay=True,
        help="Input PDF file"
    ),
    output_dir: Path = typer.Option(
        ...,
        "-o",
        "--output",
        help="Output directory"
    ),
):
    make_dir(output_dir)
    ops.split(str(input_path), str(output_dir))
    typer.echo(f"Successfully split {input_path} into {output_dir}")


@app.command()
def extract_text(
    input_path: Path = typer.Argument(
        ...,
        exists=True,
        dir_okay=False,
        file_okay=True,
        help="Input PDF file"
    ),
):
    text = ops.extract_text(str(input_path))
    typer.echo(text)


@app.command()
def add_page(
    source_pdf: Path = typer.Argument(
        ...,
        exists=True,
        dir_okay=False,
        file_okay=True,
        help="Source PDF file"
    ),
    page_num: int = typer.Argument(
        ...,
        help="Page number to add (1-based)"
    ),
    target_pdf: Path = typer.Argument(
        ...,
        exists=True,
        dir_okay=False,
        file_okay=True,
        help="Target PDF file"
    ),
    output_path: Path = typer.Option(
        ...,
        "-o",
        "--output",
        help="Output PDF file"
    ),
):
    make_dir(output_path)
    try:
        ops.add_page(str(source_pdf), page_num, str(target_pdf), str(output_path))
        typer.echo(f"Successfully added page {page_num} from {source_pdf} to {target_pdf} -> {output_path}")
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)


@app.command()
def remove_page(
    input_path: Path = typer.Argument(
        ...,
        exists=True,
        dir_okay=False,
        file_okay=True,
        help="Input PDF file"
    ),
    page_num: int = typer.Argument(
        ...,
        dir_okay=False,
        file_okay=True,
        help="Page number to remove (1-based)"
    ),
    output_path: Path = typer.Option(
        ...,
        "-o",
        "--output",
        help="Output PDF file"
    ),
):
    make_dir(output_path)
    try:
        ops.remove_page(str(input_path), page_num, str(output_path))
        typer.echo(f"Successfully removed page {page_num} from {input_path} -> {output_path}")
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)


@app.command()
def watermark(
    input_path: Path = typer.Argument(
        ...,
        exists=True,
        dir_okay=False,
        file_okay=True,
        help="Input PDF file"
    ),
    watermark_path: Path = typer.Argument(
        ..., 
        exists=True,
        dir_okay=False,
        file_okay=True,
        help="Watermark PDF file"
    ),
    output_path: Path = typer.Option(
        ..., 
        "-o", 
        "--output", 
        help="Output PDF file"
    ),
):
    make_dir(output_path)
    ops.watermark(str(input_path), str(watermark_path), str(output_path))
    typer.echo(f"Successfully watermarked {input_path} with {watermark_path} -> {output_path}")


if __name__ == "__main__":
    app()