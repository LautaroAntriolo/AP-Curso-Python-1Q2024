import random
def numeros(n):
    lista = []
    for i in range(n):
        numeroRandom = random.randint(0,45)
        lista.append(numeroRandom)
    return lista


def quiniela():
    dia = datetime.datetime.now()
    cadenaDeTExto = f'{dia} = {numeros(10)}'
    return cadenaDeTExto

## Si sigue sin funcionar el programador de tareas, buscar hacer un bucle for y un time para que espere cierto tiempo
if __name__ == '__main__':
    import datetime
    from texto import prompt
    from imagenes import img
    mensaje = prompt("escribir una frase de motivación corta de menos de 10 palabras")
    url, nombre = img("Una foto de la cara de un gato marron claro contento ")
    with open('C:\Lautaro\AprendeProgramando\CursoPython2023\Python\Clase10_IA_Script\Script\quiniela.txt', 'a+') as archivo:
        archivo.write(f'\n{quiniela()}, {mensaje}, {url}')
    
