from PIL import Image
import pytesseract

def convert_image(file_path):
    return pytesseract.image_to_string(Image.open(file_path))
