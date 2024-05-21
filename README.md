# TIFF to PDF conversion guide

In many situations, especially with large-scale document leaks such as bank scans, you may encounter a significant number of documents in TIFF format. These multi-page TIFF files are often used for scanned documents due to their high quality and support for multiple images within a single file. However, TIFF files are not widely supported by most software applications, making it challenging to view and process these documents. In contrast, PDF is a universally accepted format that is compatible with a wide range of programs and devices, making it a preferred choice for document management and recognition.

## Online

- [tiff2pdf.com](https://tiff2pdf.com/) - up to 20 files, max 200 Mb

## Windows

See instruction: https://github.com/scrub-dev/tiff2pdf

## Linux / MacOS

To convert **all** TIFF files in a folder, do:

```sh
pip3 install Pillow fitz PyMuPDF
```

Convert all TIFF document to PDFs in user's Documents folder:
```sh
python3 tiff_to_pdf.py --folder-path ~/Documents
```

You'll get a `TIFF to PDF converted DATE TIME` folder in ~/Documents.
