#%% 
import lectura 
from datetime import datetime
from dateutil.relativedelta import relativedelta

resultados = lectura.sheet.values().get(spreadsheetId=lectura.SPREADSHEET_ID, range='Respuestas de Formulario 2!E2:E34',majorDimension='COLUMNS').execute()
valores = resultados.get('values',[])
print(valores[0])


def edad(Edades):
    edadNum = []
    edadStr = []
    
    for i in range(len(Edades)):
        fecha_nacimiento = datetime.strptime(valores[i][0], "%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        edadStr.append(f"{edad.years} años, {edad.months} meses y {edad.days} días")
        años = edad.years
        meses = edad.months
        dias = edad.days
        edadNum.append(f'{años}-{meses}-{dias}')
    return [edadStr,edadNum]
edad(valores[0])

# %%
