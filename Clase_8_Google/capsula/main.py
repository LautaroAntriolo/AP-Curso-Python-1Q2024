from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime
from dateutil.relativedelta import relativedelta

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'capsula8\key.json'
# KEY = 'key.json'

# Escribe aquí el ID de tu documento:
SPREADSHEET_ID = '1E5XSFoTLALMfRR3joYZdaXSlyqBT9KkV6ZCXqdLfBcM'


creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
# Llamamos a la API
resultados = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='RTA_form!C2:C7',majorDimension='COLUMNS').execute()

edades = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='RTA_form!F2:F7',majorDimension='COLUMNS').execute()['values'][0]
# print(edades)


# Extraemos values del resultado
valores = resultados['values'][0]
# print(valores)



########################################################################################################################
def dicUsers(Edades):
    diccionario = {}
    for i in range(0,len(Edades)):
        fec = str(Edades[i])
        fecha_nacimiento = datetime.strptime(fec,"%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        años = edad.years
        meses = edad.months
        dias = edad.days
        diccionario[f'alumno{i}'] = {'year': f'{años}','meses': f'{meses}','dias': f'{dias}'}
    return diccionario

print(dicUsers(edades))