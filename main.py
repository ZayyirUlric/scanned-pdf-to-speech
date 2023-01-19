import gtts
import pytesseract
import PIL.ImageOps
from pdfreader import PDFDocument, SimplePDFViewer

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

filename = ""
lang = "tl"

with open(filename,"rb") as pdf:
    pdf_view = SimplePDFViewer(pdf)
    pdf_docu = PDFDocument(pdf)
    all_pages = [p for p in pdf_docu.pages()]
    no_pages = len(all_pages)
    for i in range(no_pages):
        pdf_view.navigate(int(i)+1)
        pdf_view.render()
        for key in pdf_view.canvas.images.keys():
            curr_img = pdf_view.canvas.images[key].to_Pillow()
            curr_img.save(f"page_{i}.png")

            result = pytesseract.image_to_string(curr_img)
            result = result.strip()
            result = result.rstrip()
            result = result.replace('-\n','')
            result = result.replace('\n',' ')

            tts = gtts.gTTS(result,lang=lang)
            tts.save(f'page_{i}.mp3')
