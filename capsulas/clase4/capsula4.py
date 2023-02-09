import math
# from math import sin
# from math import sin as s

import datetime
import random

def matematica(n):
    sen = math.sin(n)
    # sen = sin(n)
    # sen = s(n)
    return sen
print(matematica(45)) #0.8509035245341184

def fecha():
    dia = datetime.datetime.now().day
    microsegundos = datetime.datetime.now().microsecond
    anio = datetime.datetime.now().year
    return dia, microsegundos, anio
print(fecha()) #(2, 264399, 2023)

# lista = [0,1,2,3,4,5,55,66,7,23,432,123,67,34,87,23,123,78,34]
# lista = ("lautaro", "Messi", " Lisandro", "La Araña")
lista = range(0,10)

def azar():
    # numero = random.randint(0,90)
    # numero= random.randrange(1,90,3)
    numero = random.choice(lista)
    return numero

print(azar())

############ DOCSTRINGS! 
# formato => explicaciòn, (abajo) parametros (abajo) return
# help(azar)
# help(fecha)
# help(matematica)
############ f-string! 
