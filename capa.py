import random

def temperaturas(cantDeNumeros, minIni=18, minFin=24, maxMin=24, maxFin=40):
    tempMin = []
    tempMax = []
    for i in range(cantDeNumeros):
        numeros = round(random.uniform(minIni, minFin), 2)
        tempMin.append(numeros)
    for i in range(cantDeNumeros):
        numeros = round(random.uniform(maxMin, maxFin), 2)
        tempMax.append(numeros)
    return [tempMin, tempMax]

print(temperaturas(10))