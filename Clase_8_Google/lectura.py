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

# Llamamos a la API
resultados = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Respuestas de Formulario 2!F2:F34',majorDimension='COLUMNS').execute()
# print(resultados)
# Extraemos values del resultado
valores = resultados['values']
print(valores[0])

########################################################################################################################



# %%
