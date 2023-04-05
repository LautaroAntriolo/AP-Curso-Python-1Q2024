# Introducciòn a VsCode

#Tipos de datos 
 # enteros, booleanos, flotantes, cadena de caracteres, 
 # tuplas : conjunto de datos del mismo o diferente tipos ("hola", 4, False)
 # Listas []  conjunto de datos del mismo tipo ("hola", 4, False)
 # diccionarios {}

# VAriables, => Como nombrarlas
# Comentarios
"""
Este comentario ocupa muchas lineas

"""
# Función print 


def contador(n):
    count = 0
    for i in range(0, len(n)):
        valorDen = n[i]
        if valorDen % 3 == 0 or valorDen % 5 == 0:
            count += 1
    return count


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(contador(numeros))



