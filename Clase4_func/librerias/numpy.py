# Importar la librería numpy
import numpy as np

# Como crear un array unidimensional => Muy similar a un array
a = np.array([1, 2, 3, 4, 5])

# Como crear un array bidimensional => Como si fuera una matriz
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Operaciones con arrays
print("Suma de a:", np.sum(a)) # Suma de los elementos de a
print("Promedio de b:", np.mean(b)) # Promedio de los elementos de b
print("Máximo de a:", np.max(a)) # Valor máximo de a
print("Mínimo de b:", np.min(b)) # Valor mínimo de b

# Operaciones matemáticas
c = np.exp(a) # Raíz cuadrada de a
c = np.sqrt(a) # Raíz cuadrada de a

d = np.sqrt(b) # Exponencial de cada elemento de b
d = np.exp(b) # Exponencial de cada elemento de b

# Indexación y slicing
print("Segundo elemento de a:", a[1]) # Segundo elemento de a
print("Primer elemento de la segunda fila de b:", b[1,0]) # Primer elemento de la segunda fila de b
print("Última fila de b:", b[-1,:]) # Última fila de b

# Concatenar arrays
g = np.concatenate((a,c)) # Concatenar a y c en un solo array


# Imprimir los resultados
print("Raíz cuadrada de a:", c)
print("Exponencial de b:", d)
print("Segundo elemento de a:", a[1])
print("Primer elemento de la segunda fila de b:", b[1,0])
print("Última fila de b:", b[-1,:])
print("Concatenación de a y c:", g)
