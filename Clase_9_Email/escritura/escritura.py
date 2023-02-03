
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
# %%
