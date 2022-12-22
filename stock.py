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
for i in range(15):
    numeros = int(random.uniform(30000000,40000000))
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
#%% Nombres




