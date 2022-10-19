import numpy as np

def factorial(x):
    fac = np.math.factorial(x)
    return fac

def cantEnteros(n,k):
    resultado = factorial(n)/factorial(n-k)
    print(resultado)
    return resultado

cantEnteros(6,3)
