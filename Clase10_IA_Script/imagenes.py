import openai
import random
import requests

def img(mje):
    openai.api_key = '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'
    response = openai.Image.create(
    prompt=f'{mje}',
    n=1,
    size="1024x1024"
    )
    nameIMG = f'tomate{random.randint(0,99)}.png'
    image_url = response['data'][0]['url']

    # Las imagenes se guardarán fuera de la carpeta local.

    req = requests.get(image_url)
    req.headers['User-Agent']= 'Mozilla/5.0'
    response = req.content

    # tenemos que agregar rutas existentes => probar con copy relative path desde VsCode y agregarle le folder necesario.
    with open(f'./Python/Clase10_IA_Script/img/{nameIMG}', "wb") as f:
       f.write(response)
    return image_url, nameIMG

imagen = img("una pintura realista de un perro blanco con un traje de astronauta en la superficie de la luna")
print(imagen)
