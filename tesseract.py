from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import PyPDF2
import io

def convertPdf(filePath, newFilePath):
    # create list of images from pdf. each image represents one page of pdf
    print("From tesseract.py: converting pdf to images...\n")
    images = convert_from_path(filePath)

    print("From tesseract.py: converting images to pdfs...\n")
    #convert each image into a pdf and merge them together
    pdf_writer = PyPDF2.PdfWriter()
    for image in images:
        page = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
        pdf = PyPDF2.PdfReader(io.BytesIO(page))
        pdf_writer.add_page(pdf.pages[0])


    print("From tesseract.py: writing to newFilePath\n")
    # export as one single pdf to location of newFilePath
    with open(newFilePath, "wb") as f:
        pdf_writer.write(f)
    