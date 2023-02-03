#%%Con la librería OpenPyXL
from openpyxl import *
doc = load_workbook('PruebaExcel.xlsx')
# print(type(doc))
print(doc.get_sheet_names())
# %%
print(doc.get_sheet_by_name('Hoja 1'))
# %%
Hoja_1= doc.get_sheet_by_name('Hoja 1')
print (Hoja_1['A1'].value)
# %%
muchasCeldas = Hoja_1['A1':'A4']
for row in muchasCeldas:
    for cell in row:
        print(cell.value)
# %%
all_columns = Hoja_1.rows
print(all_columns)
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

df = pd.DataFrame(np.random.randint(0, 100,size=(3, 4)),columns=list('ABCD'))
print(df)
# %%
