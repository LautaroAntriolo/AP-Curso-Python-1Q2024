# Funciones para una calculadora
# Estaría bueno mostrar las diferentes formas de hacer una misma función. por ejemplo la función de sumar dos o mas números:
# Es lo mismo para la multiplicación, división y demás.


# Con valores por defecto. Estaría bueno ver como lo podemos debugger y que pasa si agregamos mas elementos..
def sumarUno(a, b, c=0, d=0):
    resultado = a + b + c + d
    return resultado

# eleigiendo como parámetro una o varias listas
def sumarDos(lista):
    resultado = sum(lista)
    return resultado

# Una forma por si alguno conoce que son los argumentos posicionales
def sumarTres(a, b, *args):
    resultado = a + b
    for num in args:
        resultado += num
    return resultado

def sumarcuatro(*args):
    resultado = sum(args)
    return resultado


print(sumarUno(4,5))
print(sumarUno(4,5,9))
print(sumarUno(4,5,9,8))
# print(sumarUno(4,5,9,8,7))

# print(sumarDos(1,2,3,4,)) # Error porque no es una lista. Lo declaramos antes o lo pasamos con corchetes
print(sumarDos([1,2,3,4]))
print(sumarDos([1,2,3,4,5,6,7,8,9]))
lista = [9,8,463,12,4,5,67,23,56,12,10]
print(sumarDos(lista))

print(sumarTres(4,5))
print(sumarTres(4,5,6,7,8,9))
print(sumarTres(4,5,[4,5,6,7,2,3])) # Tira error porque estamos sumando la lista a un entero. Se puede crear una función para arreglarlo 