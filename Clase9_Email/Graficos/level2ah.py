import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import random


# Genero listas como comprensión de lista.
lista_1 = [np.random.randint(0, 50) for _ in range(50)]
lista_2 = [np.random.randint(0, 50) for _ in range(25)]
lista_3 = [20, 30, 10, 5, 15]

# Gráfico de línea
plt.plot(lista_1)
plt.title("Gráfico de línea")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()

# Gráfico de dispersión 
plt.scatter(np.arange(len(lista_2)), lista_2)
plt.title("Gráfico de dispersión")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()

# Gráfico de barras
plt.bar(np.arange(len(lista_3)), lista_3)
plt.title("Gráfico de barras")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()


def generar_palabras(x):
    consonantes = "bcdfghjklmnpqrstvwxyz" # lista de consonantes
    vocales = "aeiou" # lista de vocales
    palabras = []
    
    for i in range(x):
        palabra = "" 
        
        for j in range(3):
            if j % 2 == 0: # si el índice es par, generar una consonante
                palabra += random.choice(consonantes)
            else: # si el índice es impar, generar una vocal
                palabra += random.choice(vocales)
        
        palabras.append(palabra) 
    
    return palabras

# Gráfico pastel
n = 10
lista_4 = [np.random.randint(0, 50) for _ in range(n)]

plt.pie(lista_4, labels=generar_palabras(n))
plt.title("Gráfico circular")
plt.show()
