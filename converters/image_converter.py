from PIL import Image
import pytesseract

# Uncomment if Tesseract is not detected
# pytesseract.pytesseract.tesseract_cmd = (
#     r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# )

def convert_image(file_path):

    image = Image.open(file_path)

    text = pytesseract.image_to_string(
        image
    )

    return text