import random
import datetime
def numer():
    lista = []
    for i in range(1,11,1):
        numero = random.randrange(0,100,i)
        lista.append(numero)
    return lista

def fechas():
    microsegundos = datetime.datetime.now().microsecond
    minutos = datetime.datetime.now().minute
    return microsegundos, minutos

def contra():
    clave = ''
    lista ='abcdefghijklmnopqrstuvwxyz'
    for i in range(9):
        menorOMayor = random.randint(0,3)
        if menorOMayor == 1:
            clave += lista[random.randint(0,len(lista)-1)].upper()
        else:
            clave += lista[random.randint(0,len(lista)-1)].lower()
    return clave
        
# print(contra())
