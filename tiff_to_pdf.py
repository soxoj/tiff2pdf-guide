import os
import argparse
import logging
import fitz
from PIL import Image
from datetime import datetime


def tiff2pdf(folder_path):
    timestamp = datetime.now().strftime("%d%m%Y %H%M")
    output_folder = os.path.join(folder_path, f"TIFF to PDF converted {timestamp}")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith('.tiff') or file_name.lower().endswith('.tif'):
            try:
                tiff_image = Image.open(file_name)
                pdf_doc = fitz.open()

                for page_num in range(tiff_image.n_frames):
                    tiff_image.seek(page_num)
                    rgb_image = tiff_image.convert('RGB')
                    temp_file_path = f"temp_page_{page_num}.png"
                    rgb_image.save(temp_file_path)
                    img_pdf = fitz.open(temp_file_path)

                    rect = fitz.Rect(0, 0, rgb_image.width, rgb_image.height)
                    pdf_page = pdf_doc.new_page(width=rgb_image.width, height=rgb_image.height)
                    pdf_page.insert_image(rect, filename=temp_file_path)

                pdf_doc.save(os.path.join(output_folder, f"{file_name}.pdf"), deflate=True)
                pdf_doc.close()
            except Exception as e:
                logging.error(f"error converting {file_name}: {e}", exc_info=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='convert tiff to pdf')
    parser.add_argument('--folder-path', required=True, help='path to folder with tiff files')
    args = parser.parse_args()

    tiff2pdf(args.folder_path)
