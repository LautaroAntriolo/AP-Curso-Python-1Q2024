#%%
import lectura 
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import numpy as np
#%%
#Obtenemos la fecha de nacimiento que está en el formulario
fechanac = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID,range='Respuestas de Formulario 2!F2:F34',majorDimension='COLUMNS').execute()
fecha = fechanac.get('values',[])
# print(len(fecha[0]))
#Obtenemos el nombre que está en el formulario
name = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID,range='Respuestas de Formulario 2!B2:B34',majorDimension='COLUMNS').execute()
nombre = name.get('values',[])
# print(len(nombre[0]))
#Obtenemos el apellido que está en el formulario
surname = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID,range='Respuestas de Formulario 2!C2:C34',majorDimension='COLUMNS').execute()
apellido = surname.get('values',[])

#%%
def dicUsers(Edades):
    diccionario = {}
    for i in range(0,len(Edades[0])):
        fec = str(Edades[0][i])
        fecha_nacimiento = datetime.strptime(fec,"%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        años = edad.years
        meses = edad.months
        dias = edad.days
        diccionario[f'{nombre[0][i]}_{apellido[0][i]}'] = {'year': f'{años}','meses': f'{meses}','dias': f'{dias}'}
    return diccionario

#%%
def ElegirDato(diccionarioCompuesto, dato):
    key = []
    key.extend(diccionarioCompuesto.values())
    fact = []
    for i in range(len(key)):
        fact.append(key[i][f'{dato}'])
    return fact
# %%
'''
Para graficarlo voy a generar una función que cree un diccionario 
para saber la cantidad de ocurrencias de cada dato.
'''
name_counts = {}
datos = ElegirDato(dicUsers(fecha), 'year')
# print(datos)
for name in datos:
    if name in name_counts:
        name_counts[name] += 1
  # Si el nombre no existe en el diccionario, lo añadimos y le asignamos el valor 1
    else:
        name_counts[name] = 1
# print(name_counts)
# %%
import matplotlib.pyplot as plt

# Creamos una lista con los nombres y otra con el número de ocurrencias



# Creamos el gráfico de barras
plt.bar(names, counts)

# Mostramos el gráfico
plt.show()

# %%
