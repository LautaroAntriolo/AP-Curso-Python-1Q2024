# import os
from email.message import EmailMessage # Viene con la instalación de Python
import ssl #  Viene con la instalación de Python
import smtplib #  Viene con la instalación de Python

email_emisor = 'lautaro.antriolo@bue.edu.ar'
# email_contrasena = os.environ.get('EMAIL_PASSWORD')
email_contrasena = "dzhwcxrtqyauxdpn"
email_receptor = 'antriololautaro@gmail.com'
asunto = 'Revisa mi video en YouTube'
cuerpo = "Vamos a ver si esto sale bien "


em = EmailMessage()
em ['From'] = email_emisor
em ['To'] = email_receptor
em ['Subject'] =asunto
em.set_content(cuerpo)

# Agregamos seguridad con SSL. Coneccion a internet segura 

contexto = ssl.create_default_context()
#tenemos que definir el servidor, el puerto y usar el contexto necesario
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor, email_receptor, em.as_string)


