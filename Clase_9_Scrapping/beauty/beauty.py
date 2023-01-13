#%%
# Importar las bibliotecas necesarias
import requests
from bs4 import BeautifulSoup

# Enviar una solicitud a la página web y obtener el código fuente
pagina_web = 'https://lautaroantriolo.netlify.app/'
solicitud = requests.get(pagina_web)
# print(solicitud)
#%%
# .text te devuelve todo el contenido de la página inluidas las APIS, urls etc
contenido = solicitud.text
# print(contenido)
#%%
# La variable soup es muy importante porque nos permite localizar elementos
# en una página web
soup = BeautifulSoup(contenido, 'html.parser')

##### PROPIEDADES #####

# print(soup.prettify())


# print(soup.find_all('article'))
articulo = soup.find('article')
print(articulo.attrs)
#%% DOCUMENTACION
# Prettify => te devuelve el código HTML 
# find => Te devuelve la primer etiqueta que le pasemos como parámetro
# find_all => Te devuelve todas las etiquetas que le pasemos como parámetro
# acceder a los hijos => Abuelo.padre.hijo . Solo devuelve el primer hijo que corresponda con esta estructura/etiqueta


#%%
# Encontrar los datos de interés utilizando las etiquetas HTML
datos = soup.find_all('div', class_='datos')

# Imprimir los datos
for dato in datos:
  print(dato.text)
# %%
