num = [[1,2,3,4,5,6,7,8], [11,21,31,41,51,61,71,81], [21,22,23,24,25,26,27,28]]
for a in num:
    for i in a:
        if(i%2==0):
            print(i)


# print("Tomate")

import pyqrcode
import png
def crearQR(Link, nombre):
    link = Link
    qr_code = pyqrcode.create(link, version=5)
    return qr_code.png(nombre, scale=5)

crearQR('https://youtu.be/0wuahFO6apg','Prueba3')