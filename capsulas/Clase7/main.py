# %%
import requests
#%%

parametros = {
    "api_key": "8rwoFOQZ34OvaG1LwtQnOZWh72UfUooIiwbC601X"
}
datos = requests.get("https://api.nasa.gov/planetary/apod", params=parametros)
if datos.status_code == 200:
    results = datos.json()
    url = results["url"]
    # Si es una imagen guardar el archivo con el nombre imagen_del_dia.
    if results["media_type"] == "image":
        with open("imagen_del_dia.jpg", "wb") as img:
            img.write(requests.get(url).content)
    else:
        print(url)
else:
    print("No se pudo obtener la imagen.")

# %%
