import pyqrcode
import png
def crearQR(Link, nombre):
    link = Link
    qr_code = pyqrcode.create(link, version=5)
    return qr_code.png(nombre, scale=5)

crearQR('https://youtu.be/0wuahFO6apg','Prueba3')