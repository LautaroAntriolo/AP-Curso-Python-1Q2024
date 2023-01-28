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
    archivo = open('./Python/Clase10_IA_Script/Script/archivo.txt','a')
    archivo.write(f'\n{quiniela()}')
    archivo.close()
    
