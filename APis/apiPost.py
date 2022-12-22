#%%
import requests

## Usamos jsonplaceholder para ver la APO
url = "https://jsonplaceholder.typicode.com/posts"
usuario = {
    "title": "Título",
    "body": "El cuerpo",
}

# Le pasamos dos parametros, la url y el json con los 
# datos para usar en esa url.
respuesta = requests.post(url, json=usuario)

# Ahora decodificamos la respuesta para tenerla como json
como_json = respuesta.json()
print("La respuesta del servidor es:")
print(como_json)
# Vemos que nos devuelve el objeto que le pasamos  mas
# un id, por lo que podemos acceder al id de la forma:
id = como_json["id"]
print(f"El id es: {id}")
# %%

