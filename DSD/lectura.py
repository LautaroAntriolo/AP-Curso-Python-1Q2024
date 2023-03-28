from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import os
import json
from datetime import datetime, timedelta, date
from dotenv import load_dotenv

load_dotenv()
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'C:/Lautaro/AprendeProgramando/CursoPython2023/Python/DSD/key.json'
SPREADSHEET_ID = os.getenv("ID_DOCUMENTO")
creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Datos importantes de nuestra hoja de calculos
inicio = 'B2' # Cargo el inicio de la fila y la columna donde comenzaran a cargarse los archivos
nombreHoja = 'plasticos' # El nombre de la hoja donde tomaremos los datos
#Creo una función en google sheet para guardar el último valor de la fila. Guardo ese valor en una variable.
final = (sheet.values().get(spreadsheetId=SPREADSHEET_ID,range=f'{nombreHoja}!M2', majorDimension='COLUMNS').execute()['values'][0][0])


# Llamamos a la API con los datos guardados en las variables correspondientes. 

def archivoJSON(final):
    '''
    Buscaremos tener un registro de la cantidad de datos que ingresan diariamente.
    recibe el número de la última fila que tiene el archivo xlsx y lo agrega a un archivo JSON

    parámetros: recibe un int como número de fila
    return: crea un archivo llamado datos.json si este no existe, y si existe lo modifica para agregarle a la 
    clave de la fecha actual, el valor de la última fila
    '''
    fecha = date.today()
    if os.path.exists('./DSD/datos.json'):
            with open('./DSD/datos.json','r') as f:
                data = json.load(f)
                if fecha not in data:
                    data[f'{fecha}'] = {}
                    data[f'{fecha}']['final'] = final
                    data[f'{fecha}']['imagenes'] = {}
            with open('./DSD/datos.json', 'w') as f:
                json.dump(data, f)
    else:
        data = {'inicio': 'B2', f'{fecha}':{f'final':f'{final}','imagenes':{}}}
        with open('./DSD/datos.json', 'w') as f:
            json.dump(data, f)
    return final
def contador_palabras(lista, palabraClave):
    '''
    Le pasamos una lista y una palabra y nos devuelve la cantidad de veces que se repite esa palabra en la lista

    parámetros = una lista de strings
    retunr = un int con la # de veces que se repite la palabraClave en la lista
    '''
    contador = 0
    for elemento in lista:
        if elemento == palabraClave:
            contador += 1
    return contador
def listasEnMinuscula(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].lower()
    return lista

#!B:K => Coresponde a toda la hoja de cálculo sin la marca temporal
def todosLosValores(nombreHoja,inicio): 
     hoja = sheet.values().get(spreadsheetId=SPREADSHEET_ID,range=f'{nombreHoja}!{inicio}:K', majorDimension='COLUMNS').execute()['values']
     return hoja



allvalues = todosLosValores(nombreHoja,inicio)

#obtengo todos los nombres pero sin la primer linea que tiene todos los encabezados de las columnas
nombre, edad  = allvalues[0][1:], allvalues[1][1:]
mail = allvalues[2][1:]
nivelEstudios = allvalues[3][1:]
nuevosProyectos = allvalues[4][1:]
tiposDePlasticos =allvalues[5][1:]
Educacion = allvalues[6][1:]
Incentivos = allvalues[7][1:]
medidas = allvalues[8][1:]
responsabilidad = allvalues[9][1:]
