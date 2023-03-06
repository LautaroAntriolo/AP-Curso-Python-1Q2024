import yagmail
import os
from dotenv import load_dotenv

load_dotenv()
email = os.getenv("MAIL2")
contrasena = os.getenv("ClaveSegura")

yag = yagmail.SMTP(user=email, password=contrasena)
destinatarios = [os.getenv("MAIL1")]

asunto = 'Prueba de correo 2'
mensaje = "Mensaje de prueba"
yag.send(destinatarios,asunto, mensaje)
asunto = 'Prueba de correo'
mensaje = "Mensaje de prueba"
titulo = '<center><h1 style="color:red;">¡Gracias por participar!</h1></center>'
img = 'C:\Lautaro\AprendeProgramando\CursoPython2023\Python\Clase9_Email\sendMails\APV_logo2.png'

#enviamos el correo
yag.send(destinatarios,asunto, [titulo, mensaje], attachments=[img])

