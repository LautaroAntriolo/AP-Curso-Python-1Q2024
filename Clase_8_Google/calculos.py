import lectura 
from datetime import datetime
from dateutil.relativedelta import relativedelta

fechanac = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID, range='Respuestas de Formulario 2!F2:F34',majorDimension='COLUMNS').execute()
fecha = fechanac.get('values',[])
name = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID, range='Respuestas de Formulario 2!B2:B34',majorDimension='COLUMNS').execute()
nombre = name.get('values',[])
surname = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID, range='Respuestas de Formulario 2!C2:C34',majorDimension='COLUMNS').execute()
apellido = surname.get('values',[])
# print(nombre)
def dicUsers(Edades):
    '''
    a esta función le paso un array de números y lo que hago es obtener un diccionario
    donde la clave sea el nombre y apellido, y como valor tenga otro diccionario con claves y valores referentes
    a años, meses y días.
    la rta tien este formato: 
    {
        nombre_apellido = {year: añosActuales, meses: mesesActuales, dias: diasActuales}
        nombre_apellido = {year: añosActuales, meses: mesesActuales, dias: diasActuales}
        
        }
    '''
    diccionario = {}
    for i in range(len(Edades)):
        fecha_nacimiento = datetime.strptime(fecha[0][i],"%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        años = edad.years
        meses = edad.months
        dias = edad.days
        diccionario[f'{nombre[0][i]}_{apellido[0][i]}'] = {'year': f'{años}','meses': f'{meses}','dias': f'{dias}'}
    return diccionario
# dicUsers(fecha[0])


def ElegirDato(diccionarioCompuesto, dato):
    key = []
    for valores in dicUsers(fecha[0]).values():
        valor = valores[f'{dato}']
        key.append(valor)
    return key

print(ElegirDato(dicUsers(fecha[0]),'year'))


