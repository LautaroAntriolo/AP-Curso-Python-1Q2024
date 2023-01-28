import random
def numeros(n):
    lista = []
    for i in range(n):
        numeroRandom = random.randint(0,99)
        lista.append(numeroRandom)
    return lista


def quiniela():
    dia = str(datetime.datetime.now().date())
    cadenaDeTExto = f'{dia} = {numeros(10)}'
    return cadenaDeTExto


if __name__ == '__main__':
    import datetime
    with open('C:\Lautaro\AprendeProgramando\CursoPython2023\Python\Clase10_IA_Script\Script\quiniela.txt', 'a+') as archivo:
        archivo.write(f'\n{quiniela()}')
    
