import yagmail
email = 'al dirección de gmail donde saldrán los correos'
contrasena = "La contraseña seguraa"

yag = yagmail.SMTP(user=email, password=contrasena)
destinatarios = ['correo del destinatario']

asunto = 'Prueba de correo'
mensaje = "Mensaje de prueba"
titulo = "<center><h1>¡Gracias por participar!</h1></center>"

#Con el ./ le decimos al archivo que vamos a manejarnos en la ruta en la que estamos
# por lo que te recomiendo que crees una carpeta para agregar todas las imagenes que quieras.
img = './APV_logo2.png'
#enviamos el correo
yag.send(destinatarios,asunto, [titulo, mensaje], attachments=[img])




#%%
asunto = 'Prueba de correo'
mensaje = "Mensaje de prueba"
titulo = '<center><h1 style="color:red;">¡Gracias por participar!</h1></center>'
img = './APV_logo2.png'
#enviamos el correo
yag.send(destinatarios,asunto, [titulo, mensaje], attachments=[img])

# %%
