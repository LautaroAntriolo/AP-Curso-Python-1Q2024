#%%
import requests

datos = requests.get("https://www.afa.com.ar/es/")
datoshtml = datos.text ## Tomo todo el contenido HTML de la página. Se ve muy mal
datosheader = datos.headers
print(datosheader)
#%%
datos_put = requests.put("https://www.afa.com.ar/es/")

print(datos_put)
# %%

parametros = {
    "api_key": "vDjkgJzZqrTySWVdli7YNAa8DP5MKDa6IAnZp2ag"
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

parametros = {
    "api_key": "vDjkgJzZqrTySWVdli7YNAa8DP5MKDa6IAnZp2ag"
}
datos = requests.get("https://api.nasa.gov/planetary/apod", params=parametros)
if datos.status_code == 200:
    results = datos.json()
    print(results)
else:
  print("No se pudo obtener la imagen.")
# %%
# Viblioteca de imagenes y videos de la nasa
def infoAPI():
  url_img = "https://api.nasa.gov/EPIC/api/natural/"
  params = {
      'api_key':"vDjkgJzZqrTySWVdli7YNAa8DP5MKDa6IAnZp2ag",
  }
  response = requests.get(url_img,params=params).json()
  print(response)
infoAPI()
# %%
def fetchEPICImage():
  anio = '2019'
  mes = '06'
  dia = '27'
  Id_imagen = 'epic_1b_20151031074844'
  url_img = "https://epic.gsfc.nasa.gov/archive/natural/"
  url_img = url_img + anio +'/' + mes + '/'+dia
  url_img = url_img + '/png'
  url_img = url_img + '/' + Id_imagen + '.png' 
  print(url_img)
  
fetchEPICImage()

# %%
