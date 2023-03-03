#%% Con la librería OpenPyXL

from openpyxl import *
# Con esta importación importamos todas las funciones dentro de la librería,
# lo que nos permite usar todas las funciones sin referenciar al módulo.

doc = load_workbook('PruebaExcel.xlsx')
# print(type(doc))
print(doc.get_sheet_names()) # obtenemos el nombre de la hoja
# Si sabemos que la hoja existe podemos buscarla por su nombre
# print(doc.get_sheet_by_name('Hoja 1')) 

#guardamos la hoja uno en la variable y accedemos a su posición A1
Hoja_1= doc.get_sheet_by_name('Hoja 1')
print (Hoja_1['A1'].value)

# Hay que reconocer las dimensiones de la hoja y crear una función 
# que la recorra. Desde VsCode podemos hacer click derecho open preview
# Sino está también la extensión Excel Viewer
muchasCeldas = Hoja_1['A1':'A4']
for row in muchasCeldas:
    for cell in row:
        print(cell.value)

# Tambien podemos 

# abrir el libro de trabajo y la hoja de cálculo
workbook = load_workbook('PruebaExcel.xlsx')
sheet = workbook.active

# obtener todas las filas y columnas. De esta forma generamos un objeto con todas las filas y columnas

Todasrows = sheet.rows
Todascolumns = sheet.columns

# imprimir los datos como filas
for row in Todasrows:
    for cell in row:
        print(cell.value, end='\t')
    print()

# Imprimo los datos como columnas
for column in Todascolumns:
    for cell in column:
        print(cell.value, end='\t')
    print() 


# %% Usando Pandas
import pandas as pd
#%%

serie = pd.Series([1,2,3,4,5])
print(f'La cantidad de elementos en la serie es de: {serie.count()}')


# %% función Sum, min, max

serie = pd.Series([1,2,3,4,5])
print(f'La suma es: {serie.sum()}')
print(f'El minimo es: {serie.min()}')
print(f'El maximo es: {serie.max()}')

datafram1 = pd.DataFrame([[1, 2, 3, 4, 5],
                          [11,22,33,44,55], 
                          [15,24,33,42,51]])
print(f'La suma es: \n\
{datafram1.sum()}')

print(f'El minimo es:\n\
{datafram1.min()}')

print(f'El maximo es: \n\
{datafram1.max()}')

# %% Datasets con pandas


datafram = pd.DataFrame([[1,2,3,4,5],
                         [11,22,33,44,55], 
                         [15,24,33,42,51]])
print(datafram.count())


# %% Funcion Describe()

datafram = pd.DataFrame([[1,2,3,4,5],
                         [11,22,33,44,55], 
                         [15,24,33,42,51]])
print(round(datafram.describe()))

#%%

serie = pd.Series([1,2,3,4,5])
print(f'{serie.describe()}')

# %% Funcion aplly()
def multiply(a):
    return float(a) * 2

serie = pd.Series([-1,2,-3,4,-5])
# print(f'{serie.apply(multiply)}')

datafram = pd.DataFrame([[1,2,3,4,5],
                         [11,22,33,44,55], 
                         [15,24,33,42,51]])
print(f'{datafram.apply(multiply,axis=1, args=())}')

# %%
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(0, 100,size=(3, 4)),columns=list('ABCD'))
print(df)
# %%
