from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime
from dateutil.relativedelta import relativedelta

import numpy as np

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'capsula8\key.json'
SPREADSHEET_ID = "1E5XSFoTLALMfRR3joYZdaXSlyqBT9KkV6ZCXqdLfBcM"

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'V4', credentials=creds)
sheet = service.spreadsheets()

apellidos =sheet.values().get(spreadsheetId = SPREADSHEET_ID, range='RTA_form!C2:C17', majorDimension='COLUMNS').execute()['values'][0]
fechaNac = sheet.values().get(spreadsheetId = SPREADSHEET_ID, range='RTA_form!F2:F17', majorDimension='COLUMNS').execute()['values'][0]
cursosAP = sheet.values().get(spreadsheetId = SPREADSHEET_ID, range='RTA_form!E2:E17', majorDimension='COLUMNS').execute()['values'][0]
mails = sheet.values().get(spreadsheetId = SPREADSHEET_ID, range='RTA_form!D2:D17', majorDimension='COLUMNS').execute()['values'][0]

# print(fechaNac)

def edades(Edades):
    '''
    Calculamos las edades a partir de un formato de dia/mes/año

    #Parámetros: 
    Una lista con la fehca en el formato indicado

    #Return
    DEvuelve un diccionario compuesto con el nombre del alumno como clave
    y como valor, un diccionario con clave dia, mes y año.
    
    '''
    diccionario = {}
    for i in range(0, len(Edades)):
        fec = str(Edades[i])
        fecha_nacimiento = datetime.strptime(fec,"%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        años = edad.years
        meses = edad.months
        dias = edad.days
        diccionario[f'alumno{i}'] = {'year': f'{años}','meses': f'{meses}','dias': f'{dias}'}
    return diccionario

print(edades(fechaNac)) # Necesario

def ElegirDatoDeEdad(diccionarioCompuesto, dato):
    key = []
    key.extend(diccionarioCompuesto.values())
    fact = []
    for i in range(len(key)):
        fact.append(key[i][f'{dato}'])
    return fact

'''
Append: Agrega cualquier valor pero completo:  si enviamos un objeto, agrega el objeto, si enviamos una lista, agrega 
la lista, si enviamos un string, agrega un string...Agrega todo el objeto en lugar de sus elementos.

Extend: agrega elementos de cualquier estructura iterable, por ejemplo, si enviamos un objeto, no lo agrega y tira error, pero
si enviamos ese mismo objeto dentro de un iterable como puede ser una lista, 
escaneará la lista y agregará ese objeto
'''

# print(edades(fechaNac))
edadAnios = ElegirDatoDeEdad(edades(fechaNac),'year')
print(edadAnios)

def deStringaNumbre(listaDeString):
    lista = []
    for x in listaDeString:
        lista.append(int(x))
    return lista

edadAnios = deStringaNumbre(edadAnios)
print(edadAnios) # obtengo una lista 

## No se puede hacer porque los números están en formato de número, entonces tenemos que pasarlos a int
# def promedio(numeros):
#     return np.mean((numeros))
# print(promedio(Edades))


def promedio(list):
    lista = []
    for x in list:
        lista.append(int(x))
    return sum(lista) / len(lista)




def cantidad(datos):
    name_counts = {}
    for name in datos:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
    return name_counts

# print(cantidad(apellidos))

import matplotlib.pyplot as plt
import random
# Gráfico de líneas: 
# se utiliza para representar datos en un formato continuo a lo largo del tiempo o una serie de valores numéricos.

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.figure()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title("Cantidades")
# plt.plot(x, y)
# plt.show()


# Gráfico de barras: se utiliza para comparar diferentes valores numéricos en diferentes categorías.

# plt.figure()
# plt.xlabel('Tecnologia')
# plt.ylabel('Edad')
# plt.bar(cantidad(apellidos).keys(), cantidad(apellidos).values())
# plt.show()


# Gráfico de dispersión: se utiliza para representar la relación entre dos variables.
# plt.figure()
# plt.xlabel('Tecnologia')
# plt.ylabel('Edad')
# plt.title("Cantidad de apellidos de AP")
# plt.scatter(edadAnios,apellidos)
# plt.show()


#Gráfico de histograma: se utiliza para representar la distribución de datos.
# plt.hist(apellidos, bins=len(apellidos))
# plt.xlabel('apellidos')
# plt.ylabel('Frecuencia')
# plt.title('Gráfico de Histograma')
# plt.show()


## ESCRITURA 

# values = [[f'Esto es un poema que quiero mandar', f'=IMAGE("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNTSPrkF5G-GPLgP44NUhfaMdt6RtHtCjenflis4rKvQ&s";4;70;70)']]

# # Llamamos a la api
# for i in range(2,17):
# 	resultados = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
# 								range=f'G{i}',
# 								valueInputOption='USER_ENTERED',
# 								body={'values':values}).execute()



# ## ENVIAR MAILS


# import yagmail

# mails = ['mail1','mail2']
# email = 'lautaro.antriolo@bue.edu.ar'
# contrasena = "rkkbzxgxlckspsbd"

# yag = yagmail.SMTP(user=email, password=contrasena)
# destinatarios = mails

# asunto = 'Prueba de correo'
# mensaje = "Mensaje de prueba"
# yag.send(destinatarios,asunto, mensaje)
# asunto = 'Prueba de correo'
# mensaje = "Mensaje de prueba"
# titulo = '<center><h1 style="color:red;">¡Gracias por participar!</h1></center>'
# img = 'Python\Clase_9_Email\sendMails\APV_logo2.png'
# #enviamos el correo
# yag.send(destinatarios,asunto, [titulo, mensaje], attachments=[img])

