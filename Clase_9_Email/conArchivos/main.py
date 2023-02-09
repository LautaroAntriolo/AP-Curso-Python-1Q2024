## Hoy vamos a ver como escribir en un archivo txt y como escribir en nuestas hojas de calculo de google
# La idea es que podamos escribir en ambos lugares para poder generar registros tanto en mi computadora, 
# Como en Google, lo que me permite tener un registro de los datos desde cualquier dispositivo

# open('archivo','modo')

archivo = open('Python/Clase_9_Email/conArchivos/texto.txt','r+')
# print(archivo.read())
archivo.close()

## Vemos que lo que sale por la terminal esta todo junto
archivo = open('Python/Clase_9_Email/conArchivos/texto.txt','r+')
# print(archivo.read())
archivo.write("Esto es una estrofa creada por mi")
# print(archivo.read())
archivo.close()

## Corroboramos que sale todo junto y vemos como sale con readline y readlines
archivo = open('Python/Clase_9_Email/conArchivos/texto.txt','r+')
# print(archivo.readlines())
archivo.close()

# Si agregamos el salto de lineal \n pasa lo siguiente: 

# archivo.write("\nEsto es una estrofa creada por mi")
# print(archivo.read())

archivo = open('Python/Clase_9_Email/conArchivos/texto.txt','r')
print(archivo.read())
archivo.write("\nvamos a ver donde agrego estsoo")



#Contexto
# with open('Python/Clase_9_Email/conArchivos/texto.txt', 'r+') as texto:
#     # print(texto.read())
#     print(texto.read)

# # por lo tanto si corro... tira un error
# print(texto.readline())

## EScribir en Las hoja de google Sheets
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import random

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'Clase_9_Email\escritura\key.json'
SPREADSHEET_ID = '1WOSvX9Cvv5c7NRLAzbwa_z1CybiQHkC2VzsU31QOZAw'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Debe ser una matriz por eso el doble [[]]

values = [['Esto es un poema que quiero mandar', f'Esto puede ser cualquier cosa.', f'=IMAGE("https://cloudfront-us-east-1.images.arcpublishing.com/infobae/EFDNZZ7FEEPSQNE4ATMVMKGXBE.jpg";4;70;70)']]

# Llamamos a la api
for i in range(10,20):
	resultados = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
								range=f'H{i}',
								valueInputOption='USER_ENTERED',
								body={'values':values}).execute()

# print(f"Datos insertados correctamente.\n{(resultados.get('updates').get('updatedCells'))}")