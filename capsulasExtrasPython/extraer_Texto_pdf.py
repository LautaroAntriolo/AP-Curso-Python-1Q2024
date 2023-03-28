from PIL import Image
import pytesseract

# Seleccionar la imagen a procesar
path_to_tesseract = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

path_to_image = 'C:/Lautaro/AprendeProgramando/CursoPython2023/Python/img/GenerarUnCaptchap.png'

#Seleccionar el idioma
pytesseract.tesseract_cmd = path_to_tesseract
img = Image.open(path_to_image)

text = pytesseract.image_to_string(img)

print(text)