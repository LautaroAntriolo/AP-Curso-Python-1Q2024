#%%
import calculos
import lectura 

fechanac = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID, range='Respuestas de Formulario 2!F2:F34',majorDimension='COLUMNS').execute()
fecha = fechanac.get('values',[])
# print(valores[0])

print(calculos.dicUsers(fecha[0]))


# %%
import lectura
fechanac = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID, range='Respuestas de Formulario 2!F2:F34',majorDimension='COLUMNS').execute()
fecha = fechanac.get('values',[])
name = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID, range='Respuestas de Formulario 2!B2:B34',majorDimension='COLUMNS').execute()
nombre = name.get('values',[])
surname = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID, range='Respuestas de Formulario 2!C2:C34',majorDimension='COLUMNS').execute()
apellido = surname.get('values',[])
print(nombre[0])

# %%
# %%
# print(dicUsers(fecha[0]).keys())
# print(dicUsers(fecha[0]).values())
# print(dicUsers(fecha[0]).values())

# %%
# for i in (dicUsers(fecha[0]).values()):
#     print(i['año'])

# %%
