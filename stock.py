#%%
import random
#%% temperaturas
def temperaturas(cantDeNumeros, minIni=18, minFin=24, maxMin=24, maxFin=40):
    tempMin = []
    tempMax = []
    for i in range(cantDeNumeros):
        numeros = round(random.uniform(minIni,minFin),2)
        tempMin.append(numeros)
    for i in range(cantDeNumeros):
        numeros = round(random.uniform(maxMin,maxFin),2)
        tempMax.append(numeros)
    return[tempMin,tempMax]

#%% DNI
def DNI(n):
    DNI = []
    for i in range(n):
        numeros = int(random.uniform(33000000,42000000))
        DNI.append(numeros)
    return DNI
#%% Edad
def edad(n):
    import random
    Edad = []
    for i in range(n):
        numeros = int(random.uniform(20,37))
        Edad.append(numeros)
    return Edad

#%% Nombres Completos
def elegirNombre(n):
    nombres = ['Lautaro', 'Lionel',  'Nicolas', 'Manuela', 'Camila', 'Carmina', 'Angel', 'Alexis', 'Nahuel', 'Emiliano', 'Angela','Julian', 'Enzo', 'Carla', 'Rocio', 'Lucrecia']
    apellidos = ['Messi', 'Scaloni', 'Ayala', 'Di María', 'Correa', 'Fernandez','Aguero','Gomez','Martinez','Montiel','Molina', 'Tagliafico', 'Acuña', 'Romero','Otamendi','Paredes','Biglia']
    nombreCompleto = []
    for i in range(15):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        nombreCompleto.append(f'{nombre} {apellido}')
    return nombreCompleto
#%% Fechas

def fecha(n):
    from datetime import datetime
    Fecha = []
    for i in range(n):
        mes = int(random.uniform(1,13))
        dia = int(random.uniform(1,28))
        anio = int(random.uniform(1986,2000))
        Fecha.append((f'{dia}/{mes}/{anio}'))

    return Fecha
for i in fecha(13):
    print(i)



# %% elegir tecnología
def elegirTecnologia(n): 
    import random
    data = ['Python', 'Desarrollo web','Desarrollo de aplicaciones móviles' ,'Robótica e impresión 3D','Autogestivo de Notion']
    tecno = []
    for i in range(n):
        tech = random.choice(data)
        tecno.append(tech)
    return tecno

for i in elegirTecnologia(13):
    print(i)

# %%
