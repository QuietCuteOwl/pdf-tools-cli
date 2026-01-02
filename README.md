# PDF Tools CLI

A comprehensive command-line interface tool suite for various PDF operations, built with Python.

## Features

This tool provides a set of utilities to manipulate PDF files directly from your terminal:

*   **Compress**: Reduce the file size of a PDF.
*   **Merge**: Combine multiple PDF files into a single document.
*   **Split**: Split a PDF document into individual pages.
*   **Extract**: Extract text content from a PDF.
*   **Add Page**: Append a specific page from one PDF to another.
*   **Remove Page**: Remove a specific page from a PDF.
*   **Watermark**: Apply a watermark (from another PDF) to all pages of a PDF.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/QuietCuteOwl/pdf-tools-cli.git
    cd pdf-tools
    ```

2.  **Install dependencies:**
    Ensure you have Python 3.* installed. It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

    *Note: The project relies on `pikepdf`, `PyMuPDF`, `pypdf`, and `click`.*

## Usage

Run the tool using `python cli.py` followed by the command and arguments.

### Global Options
*   `-o, --output`: Specify the output directory (default is the current directory `.`).

### Commands

#### 1. Compress
Compresses a PDF file to reduce its size.
```bash
python cli.py compress input.pdf -o /path/to/output
```

#### 2. Merge
Merges multiple PDF files into one.
```bash
python cli.py merge file1.pdf file2.pdf file3.pdf -o /path/to/output
```

#### 3. Split
Splits a PDF into individual files for each page.
```bash
python cli.py split input.pdf -o /path/to/output
```

#### 4. Extract Text
Extracts and prints text from a PDF.
```bash
python cli.py extract input.pdf
```

#### 5. Add Page
Appends a specific page from a source PDF to a target PDF.
*   Argument order: `SOURCE_PDF` `TARGET_PDF` `PAGE_NUM`
```bash
# Add page 5 from source.pdf to the end of target.pdf
python cli.py add source.pdf target.pdf 5 -o /path/to/output
```

#### 6. Remove Page
Removes a specific page (by page number) from a PDF.
```bash
# Remove page 3 from input.pdf
python cli.py remove input.pdf 3 -o /path/to/output
```

#### 7. Watermark
Overlays the first page of a watermark PDF onto every page of the input PDF.
```bash
python cli.py watermark input.pdf watermark.pdf -o /path/to/output
```

## Project Structure

*   `cli.py`: The main entry point for the CLI, handling command-line arguments.
*   `operations.py`: Contains the implementation logic for all PDF manipulations using libraries like `pikepdf`, `fitz` (PyMuPDF), and `pypdf`.
*   `requirements.txt`: List of Python dependencies.

## License

Licensed under the MIT license.
See the `LICENSE` file for details.
