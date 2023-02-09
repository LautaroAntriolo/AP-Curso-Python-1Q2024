import requests
import json

# URL de la API
url = "http://httpbin.org/post"

# Datos a enviar en el cuerpo de la solicitud
datos = {
    "nombre": "Lionel",
    "edad": 34,
    "pais": "Argentina",
    "CampenDelMundo" : "si"
}
args = {
    "nombre": "Python",
    "duración":4,
    "programa": "Aprende Programando"
    }
# Encabezados de la solicitud
headers = {
    "Content-Type": "PruebaPost/json",
    "Authorization": "Aquí iría algún tooken de acceso."
}

# Realizamos la solicitud POST
response = requests.post(url,params =args, data=json.dumps(datos), headers=headers)

# Comprobamos el código de estado de la respuesta
if response.status_code == 200:
    # Si el código de estado es 200 (creado), imprimimos la respuesta
    print(response.json())
elif response.status_code == 401:
    # Si el código de estado es 401 (no autorizado), mostramos un mensaje de error
    print("Error de autenticación. Comprueba tu token de acceso.")
else:
    # En cualquier otro caso, mostramos un mensaje de error genérico
    print("Error con la solicitud. Código de estado:", response.status_code)