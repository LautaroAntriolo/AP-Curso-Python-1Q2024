import requests
#No es posible remover la imagende fondo de los helefantes porque no funiona la url => OK. Esperar actualización.

r = requests.post('https://clipdrop-api.co/replace-background/v1.',
  files = {
    'image_file': ('helefantes.png', 'image/jpeg'),
    },
  data = { 'prompt': 'una familia de helefantes caminando por una llanura de pastizales verdes bajos ' },
  headers = { 'x-api-key': '500dafa725c869a873dcdb437602ea1ae132a33f7c695c65c2afd6cd770baa7c955a95ab163cd2cec23bf19df3987f6b'}
)
if (r.ok):
  print("exito")
else:
  r.raise_for_status()