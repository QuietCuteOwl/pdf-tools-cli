import click
from pathlib import Path
from operations import Operations as ops, ensure_dir

@click.group()
def main():
    """
    Pdf tools suite\n
    Usgae: python3 script_name CMD [options]
    """
    pass


@main.command()
@click.argument('input_pdf', type=click.Path(exists=True, path_type=Path))
@click.option('-o', '--output', 'output_dir', required=False, default='.', help="Output dirertory")
def compress(input_pdf, output_dir):
    """"
    Usage: python3 script_name compress input_pdf [output_dir]\n
    Compresses a pdf
    """
    
    ops.compress(str(input_pdf), str(output_dir))


@main.command()
@click.argument('input_list', nargs=-1, type=click.Path(exists=True, path_type=Path))
@click.option('-o', '--output', 'output_dir', required=False, default='.', help="Output dirertory")
def merge(input_list, output_dir):
    ops.merge(input_list, str(output_dir))


@main.command()
@click.argument('input_pdf', type=click.Path(exists=True, path_type=Path))
@click.option('-o', '--output', 'output_dir', required=False, default='.', help="Output Directory")
def split(input_pdf, output_dir):
    ensure_dir(output_dir)
    ops.split(str(input_pdf), str(output_dir))


@main.command()
@click.argument('input_pdf', type=click.Path(exists=True, path_type=Path))
@click.option('-o', '--output', 'output_dir', required=False, default='.', help="Output Directory")
def extract(input_pdf, output_dir):
    print(ops.extract_text(str(input_pdf), str(output_dir)))


@main.command()
@click.argument('source_pdf', type=click.Path(exists=True, path_type=Path))
@click.argument('target_pdf', type=click.Path(exists=True, path_type=Path))
@click.argument('page_num', type=int)
@click.option('-o', '--output', 'output_dir', required=False, default='.', help="Output Directory")
def add(source_pdf, page_num: int, target_pdf, output_dir):

    ops.add_page(str(source_pdf), page_num, str(target_pdf), str(output_dir))


@main.command()
@click.argument('input_pdf', type=click.Path(exists=True, path_type=Path))
@click.argument('page_num', type=int)
@click.option('-o', '--output', 'output_dir', required=False, default='.', help="Output Directory")
def remove(input_pdf, page_num, output_dir):

    ops.remove_page(str(input_pdf), page_num, str(output_dir))


@main.command()
@click.argument('input_pdf', type=click.Path(exists=True, path_type=Path))
@click.argument('watermark_pdf', type=click.Path(exists=True, path_type-Path))
@click.option('-o', '--output', 'output_dir', required=False, default='.', help="Output Directory")
def watermark(input_pdf, watermark_pdf, output_dir):
    ops.watermark(str(input_pdf), str(watermark_pdf), str(output_dir))


if __name__ == "__main__":
    main()
