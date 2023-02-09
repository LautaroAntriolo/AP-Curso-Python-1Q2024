#%%
import calculos
import lectura 

fechanac = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID, range='Respuestas de Formulario 2!F2:F34',majorDimension='COLUMNS').execute()
fecha = fechanac.get('values',[])
name = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID, range='Respuestas de Formulario 2!B2:B34',majorDimension='COLUMNS').execute()
nombre = name.get('values',[])
surname = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID, range='Respuestas de Formulario 2!C2:C34',majorDimension='COLUMNS').execute()
apellido = surname.get('values',[])
# print(len(fecha[0]))


def ElegirDato(diccionarioCompuesto, dato):
    key = []
    key.extend(diccionarioCompuesto.values())
    fact = []
    for i in range(len(key)):
        fact.append(key[i][f'{dato}'])
    return fact
print(ElegirDato(dicUsers(fecha), 'dias'))
print(len(ElegirDato(calculos.dicUsers(fecha),'year')))
# ElegirDato(calculos.dicUsers(fecha[0]),'year')


# %%
# for valores in diccionarioCompuesto[0].values():
#         valor = valores[f'{dato}']
#         key.append(valor)
#         print(valor)
#     return key