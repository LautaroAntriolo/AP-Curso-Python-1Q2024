#%%
import yagmail
email = 'lautaro.antriolo@bue.edu.ar'
contrasena = "dzhwcxrtqyauxdpn"

yag = yagmail.SMTP(user=email, password=contrasena)
destinatarios = ['antriololautaro@gmail.com']

asunto = 'Prueba de correo'
mensaje = "Mensaje de prueba"
yag.send(destinatarios,asunto, mensaje)
#%%
asunto = 'Prueba de correo'
mensaje = "Mensaje de prueba"
titulo = '<center><h1 style="color:red;">¡Gracias por participar!</h1></center>'
img = './APV_logo2.png'
#enviamos el correo
yag.send(destinatarios,asunto, [titulo, mensaje], attachments=[img])

# %%
