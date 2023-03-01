import numpy as np

# Dos funciones que podemos usar tranquilamente desde la consola y que 
# son fáciles de implementar
def factorial(x):
    fac = np.math.factorial(x)
    return fac

def cantEnteros(n,k):
    resultado = factorial(n)/factorial(n-k)
    print(resultado)
    return resultado

def cantLetras(palabra):
    cant = len(palabra)
    return cant

def cantLetras2(palabra):
    cant = 0
    letras = 'abcdefghijklmnñopqrstuvwxyz'
    # probar que hay que tener en cuenta los acentos.
    # letras = 'aábcdeéfghiíjklmnñoópqrstuúvwxyz'

    for i in (palabra):
        if i in letras:
            cant +=1
    return cant

if __name__=='__main__':
    ## Acá dentro ejecutamos las funciones que queremos:
    cantidad = cantLetras2("El agua no se mexcla con el aceite")
    print(cantidad)
    numero = int(input("ingresá un numero: \n"))
    print(factorial(numero))


