import click
from operations import Operations as ops, ensure_dir

@click.group()
def main():
    """
    Pdf tools suite\n
    Usgae: python3 script_name CMD [options]
    """
    pass


@main.command()
@click.argument('input_pdf')
@click.option('-o', '--output', 'output_dir', required=False, help="Output dirertory")
def compress(input_pdf, output_dir):
    """"
    Usage: python3 script_name compress input_pdf [output_dir]\n
    Compresses a pdf
    """
    ensure_dir(output_dir)
    
    ops.compress(str(input_pdf), str(output_dir))


if __name__ == "__main__":
    main()