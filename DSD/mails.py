from lectura import mail
import os
import yagmail
from dotenv import load_dotenv
import json
from lectura import ultimosmails


load_dotenv()
def enviarMail(ultimosmails,asuntoNuevo, mensajeNuevo):
    #Configuración de salida
    email = os.getenv("MAIL1")
    contrasena = os.getenv("ClaveSegura")
    yag = yagmail.SMTP(user=email, password=contrasena)

    # destinatarios puede ser un array de n elementos
    destinatarios = ultimosmails

    asunto = asuntoNuevo
    mensaje =mensajeNuevo
    titulo = '<center><h1 style="color:red;">¡Ya tenemos tus resultados!</h1></center>'
    img = 'C:\Lautaro\AprendeProgramando\CursoPython2023\Python\Clase9_Email\sendMails\APV_logo2.png'
    for i in destinatarios:
        try:
            yag.send(to=i, subject=f'{asunto}', contents=f'{[titulo, mensaje]}',  attachments=[img])
        except Exception as e:
            print(f"No se pudo enviar el correo electrónico a {i}. Error: {e}")
    
    # Cerrar la conexión con el servidor SMTP
    yag.close()
    
