import argparse
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileMerger


def merge(output_file, files):
    output_file = output_file[0]

    merger = PdfFileMerger()

    for file in files:
        merger.append(str(file))

    with Path(output_file).open(mode="wb") as fout:
        merger.write(fout)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge PDF files")
    parser.add_argument("-o", "--output_file", type=str, required=True,
                        nargs=1, help="Name of output file")
    parser.add_argument("-f", "--files", metavar="file", type=str, nargs="+",
                        help="Paths to files for merge", required=True)
    args = parser.parse_args()
    merge(args.output_file, args.files)
