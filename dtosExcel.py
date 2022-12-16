from this import d
import pandas as pd

archivo = "archivos/Tabla1.xlsx"

#Guardo el archivo en la variable df
df = pd.read_excel(archivo)
# pandas toma al archivo excel como un diccionario, 
# donde podemos acceder a cada elemento por el nombre de su clave (columna en este caso)

#Saco el promedio de la primer columna de puntos. Para eso uso las funciones que tenemos en python
# como la funcion suma (sum) y la función len (longitud)
#En una linea, hago la suma de todos los elementos de la columna ptos y la divido por la cantidad de elementos, 
# 6 en este caso (0 + 5)

# print(sum(df.Puntos)/len(df.Puntos))

#Obtengo el mayor puntaje
print(max(df.Puntos))

# ¿De quién es ese puntaje?
print(df.max())

