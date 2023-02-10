# comenzamos viendo la forma de movernos, crear y eliminar archivos desde el cmd
# Crearemos funciones, que contengan otras funciones y otros llamados => dos funciones arman una tercera, una cuarta y una uinta arman una sexta
# Ejecutaremos el código desde la terminal
# documentarla para ver como queda con el help

import numpy as np
import random 
# Crearemos una funcion que te arroja un array con cantNumeros de elementos
def numeros(cantNumeros):
    num = []
    for i in range(0,abs(cantNumeros)):
        num.append(random.randint(0,cantNumeros))
    return num

# diezNumeros = numeros(10)

# Creamos un diccionario que te tira cuantas veces se repite cada numero, puede ser tambien cuantas veces
# Se repite un nombre o distintas cosas
def cantNumeros(lista):
    existe= {}
    for numero in lista:
        if numero in existe:
            existe[numero]+=1
        else:
            existe[numero]= 1
    orden = dict(sorted(existe.items(), key=lambda item: item[1], reverse=True))
    return orden



# Cuantas veces aparece el número en la lista
# cantVeces = cantNumeros(diezNumeros)

# Creamos una funcion para generar una lista nueva sin duplicados
def sinDuplicados(lista, puntoFinal):
    existe= []
    for numero in lista:
        if numero not in existe:
            existe.append(numero)
        else:
            existe.append(random.randint(0,puntoFinal))
    return existe

# sinDupli = sinDuplicados(numeros(10),14)


# print(f'la lista de diez numeros es {diezNumeros}')
# print(f'Los números se repiten en este orden {cantVeces}')
# print(f'La Lista sin duplicados queda {sinDupli} y son {len(sinDupli)} numeros')

def main():
    numero = int(input("Ingrese la cantidad de numeros"))
    listaNumeros = numeros(numero) # devuelve una lista 
    repeticiones= cantNumeros(listaNumeros) # ordena el diccionario con la cantidad de veces que se repite cada uno
    duplicados = sinDuplicados(listaNumeros,numero)
    print(f'''la cantidad de numeros es de {numero}, por lo que la lista quedó así:
    {listaNumeros} \nque tenía el orden de {repeticiones}, 
    pero como tenía duplicados quedó: {duplicados}''')

main()