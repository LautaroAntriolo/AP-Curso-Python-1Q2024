from PIL import Image # python3 -m pip install Pillow
import os

CarpetaElejida =  'C:/Lautaro/Python-personal/Mastodon/mastodonConIA/img/'
print()
if __name__ == "__main__":
    for archivo in os.listdir(CarpetaElejida):
        name, extension = os.path.splitext(CarpetaElejida+archivo)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(CarpetaElejida + archivo)
            picture.save(CarpetaElejida+ "comprimido_"+ archivo, optimize=True, quality=60)