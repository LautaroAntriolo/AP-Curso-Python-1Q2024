#%%
# Importar las bibliotecas necesarias
import requests
from bs4 import BeautifulSoup

# Enviar una solicitud a la página web y obtener el código fuente
pagina_web = 'https://subslikescript.com/'
page = requests.get(pagina_web)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

# Encontrar los datos de interés utilizando las etiquetas HTML
datos = soup.find_all('div', class_='datos')

# Imprimir los datos
for dato in datos:
  print(dato.text)
#%%
# Importar las bibliotecas necesarias
import requests
from bs4 import BeautifulSoup

# Enviar una solicitud a la página web y obtener el código fuente
pagina_web = 'https://nuestrosanimales.netlify.app/index.html'
solicitud = requests.get(pagina_web)
contenido = solicitud.text

# La variable soup es muy importante porque nos permite localizar elementos
# en una página web

soup = BeautifulSoup(contenido, 'html.parser')
print(soup.prettify())

# Encontrar los datos de interés utilizando las etiquetas HTML
datos = soup.find_all('div', class_='datos')

# Imprimir los datos
for dato in datos:
  print(dato.text)
# %%
