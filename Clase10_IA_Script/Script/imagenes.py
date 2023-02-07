import openai
import random
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def img(mje):
    openai.api_key = os.getenv('clave_API')
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
    try: 
        with open(f'/Python/Clase10_IA_Script/Script/img/{nameIMG}', "wb") as f:
            f.write(response)
            return image_url, nameIMG
    except:
        with open(f'C:\Lautaro\AprendeProgramando\CursoPython2023\Python\Clase10_IA_Script\Script\img\{nameIMG}', "wb") as f:
            f.write(response)
            return image_url, nameIMG
        

## Prueba de funcionalidad
# imagen = img(f'Como sería la copa libertadores de futbol si fuera diseñada por el imperio romano')
# print(imagen)
