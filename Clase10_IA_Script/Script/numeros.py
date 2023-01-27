import random
def numeros(n):
    lista = []
    for i in range(n):
        numeroRandom = random.randint(0,99)
        lista.append(numeroRandom)
    return lista

N10 = numeros(10)
