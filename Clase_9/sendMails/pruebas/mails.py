from email.mine.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mine.text import MIMEText
from email.encoders import encode_base64
from smtplib import SMTP
import os
emisor = input('Ingrese su correo electronico:') #Correo electronico a usar para hacer el envio ....
contra = input('Ingrese contraseña de su correo elctronico: ') #Contraseña con la que inicia sesion en su correo
asunto = input('Ingrese el asunto del correo electronico: ') #Asunto o encabezado del correo a enviar
cuerpo = input('Ingrese mensaje o cuerpo del correo electronico: ') #Mensaje o cuerpo del correo electronico
archivo = input('Ingresar el nombre del archivo a enviar con su respectiva extension: ')
receptor = input('Ingrese el nombre del archivo de texto que contiene los correos de destino: ')
lista = [] #Variable Recorded with iTops Screen Recorderardados en el archivo de texto
with open (receptor +'.txt') as f: #mail.txt: Es el archivo de texto que contiene los correos electronicos de destino
    for line in f:
        lista = [elt.strip() for elt in line.split(',')]

for i in lista:
    mensaje=MIMEMultipart("plain")
    mensaje['From']=emisor
    mensaje['To']=i
    mensaje['subject']=asunto
    mensaje['subject']=cuerpo
    tema = MIMEText(cuerpo, 'html')
    mensaje.attach(tema)
    adjunto = MIMEBase("application", "octect-stream")
    adjunto.set_payload (open(archivo, "rb").read())
    encode_base64(adjunto)
    adjunto.add_header("content-Disposition","attachment; filename='APV_logo2.png'")
    mensaje.attach(adjunto)
    smtp = SMTP(host="smtp.gmail.com",port=587)
    smtp.starttls()
    smtp.login(emisor, contra)
    smtp.sendmail(emisor,i,mensaje.as_string())
    smtp.quit()
    print('Correo enviado exitosamente a:, 1')
    print()
    print(' Programa ejecutado y finalizado correctamente')
    print ()