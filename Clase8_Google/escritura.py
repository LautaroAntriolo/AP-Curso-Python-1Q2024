
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import random

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'Python\Clase_8_Google\key.json'
SPREADSHEET_ID = '1WOSvX9Cvv5c7NRLAzbwa_z1CybiQHkC2VzsU31QOZAw'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

nombres = [['Lautaro', 'Lionel',  'Nicolas', 'Manuela', 'Camila', 'Carmina', 'Angel', 'Alexis', 'Nahuel', 'Emiliano', 'Angela','Julian', 'Enzo', 'Carla', 'Rocio', 'Lucrecia']]
# Debe ser una matriz por eso el doble [[]]

values = [['Lautaro', 'Martinez', '40090987', '30']]

# Llamamos a la api
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range='B1:C4',
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")
# %%
