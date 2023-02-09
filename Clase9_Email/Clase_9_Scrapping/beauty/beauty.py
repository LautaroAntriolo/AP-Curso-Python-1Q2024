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
#   Find es mucho mas óptima que find_all, pero como no sabemos bien cual es el contenido, usamod find_all hasta saber que existe un solo elemento.
# acceder a los hijos => Abuelo.padre.hijo . Solo devuelve el primer hijo que corresponda con esta estructura/etiqueta
# Podemos acceder a el contenido de la etiqueta de ls siguiente forma:
#   titulo = entrada.find('h2', {'class' : 'titulo'}).getText() # Encuentro los h2 que tengan la clase titulo y con getText() extraigo su contenido. 
#   Si no uso el método getText() entonces mostraría la etiqueta e incluso el contenido, pero solo quiero el contenido.
# class_ => Para encontrar los elementos por las clases de CSS . soup.find_all(class_ ="Clase1 Clase2 ClsaeN")
# Id => Para encontrar los elementos por el id de CSS soup.find_all(id='footer')




#%%
# Encontrar los datos de interés utilizando las etiquetas HTML
# datos = soup.find_all('div', class_='datos')
for link in soup.find_all('a'):
  if 'http' in link:
    print(link.get('href'))
  else:
    print(link.get('href'))

# Imprimir los datos
#%%
for dato in datos:
  print(dato.text)
# %%
