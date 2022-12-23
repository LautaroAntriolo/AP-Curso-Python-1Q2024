#%%
import random
#%%

tempMin = []
for i in range(15):
    numeros = round(random.uniform(18,24),2)
    tempMin.append(numeros)
    print(numeros)

tempMax = []
for i in range(15):
    numeros = round(random.uniform(24,40),2)
    tempMax.append(numeros)
    print(numeros)

# print(tempMin)
# print(tempMax)
#%%
DNI = []
for i in range(26):
    numeros = int(random.uniform(33000000,42000000))
    DNI.append(numeros)
    print(numeros)
#%% Edad
import random
Edad = []
for i in range(15):
    numeros = int(random.uniform(20,37))
    Edad.append(numeros)
    print(numeros)

#%% Nombres Completos
nombres = ['Lautaro', 'Lionel',  'Nicolas', 'Manuela', 'Camila', 'Carmina', 'Angel', 'Alexis', 'Nahuel', 'Emiliano', 'Angela','Julian', 'Enzo', 'Carla', 'Rocio', 'Lucrecia']
apellidos = ['Messi', 'Scaloni', 'Ayala', 'Di María', 'Correa', 'Fernandez','Aguero','Gomez','Martinez','Montiel','Molina', 'Tagliafico', 'Acuña', 'Romero','Otamendi','Paredes','Biglia']
nombreCompleto = []
for i in range(15):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    nombreCompleto.append(f'{nombre} {apellido}')
print(nombreCompleto)
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

# data=fecha(13)
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
