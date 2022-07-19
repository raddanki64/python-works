import pytesseract
from pdf2image import convert_from_path

pages = convert_from_path(r'.\pdffiles\example2.pdf', 500, poppler_path=r'C:\Users\17328\Applications\poppler-0.68.0\bin')

for pageNum,imgBlob in enumerate(pages):
    text = pytesseract.image_to_string(imgBlob, lang='eng')
    with open(f'{pdf_path[:-4]}_page{pageNum}.txt', 'w') as the_file:
        the_file.write(text)