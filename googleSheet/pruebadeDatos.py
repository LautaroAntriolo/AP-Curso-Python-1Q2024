import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credenciales = ServiceAccountCredentials.from_json_keyfile_name("GS_Credentials.json",scope)
cliente = gspread.authorize(credenciales)

sheet = cliente.create("PrimeraBases34")

sheet.share('antriololautaro@gmail.com', perm_type='user', role='writer')

