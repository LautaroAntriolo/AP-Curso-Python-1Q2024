#%%
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# KEY = 'Python\Clase_8_Google\key.json'
KEY = 'key.json'
# Escribe aquí el ID de tu documento:
SPREADSHEET_ID = '1WOSvX9Cvv5c7NRLAzbwa_z1CybiQHkC2VzsU31QOZAw'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Llamada a la api
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Respuestas de Formulario 1!E2:E14').execute()
# Extraemos values del resultado
values = result.get('values',[])
# print(len(values))
#%%
from datetime import datetime
from dateutil.relativedelta import relativedelta
def edad(Edades):
    edadarr = []
    for i in range(len(Edades)):
        fecha_nacimiento = datetime.strptime(values[i][0], "%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        print(f"{edad.years} años, {edad.months} meses y {edad.days} días")
        años = edad.years
        meses = edad.months
        dias = edad.days
        edadarr.append(f'{años}-{meses}-{dias}')
    return edadarr
edad(values)
# %%
