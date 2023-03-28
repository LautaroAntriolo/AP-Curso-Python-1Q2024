# %%
import random
# %% temperaturas


def temperaturas(cantDeNumeros, minIni=18, minFin=24, maxMin=24, maxFin=40):
    tempMin = []
    tempMax = []
    for i in range(cantDeNumeros):
        numeros = round(random.uniform(minIni, minFin), 2)
        tempMin.append(numeros)
    for i in range(cantDeNumeros):
        numeros = round(random.uniform(maxMin, maxFin), 2)
        tempMax.append(numeros)
    return [tempMin, tempMax]

print(temperaturas(10))
# %% DNI


def DNI(n):
    DNI = []
    for i in range(n):
        numeros = int(random.uniform(33000000, 42000000))
        DNI.append(numeros)
    return DNI
# %% Edad


def edad(n):
    import random
    Edad = []
    for i in range(n):
        numeros = int(random.uniform(20, 60))
        Edad.append(numeros)
    return Edad
edades = edad(50)
print(edades)
# %% Nombres Completos


def elegirNombre(n):
    '''
    Los nombres y los apellidos es mejor que no sean compuestos
    '''
    nombres = ['Lautaro', 'Lionel',  'Nicolas', 'Manuela', 'Camila', 'Carmina', 'Angel',
        'Alexis', 'Nahuel', 'Emiliano', 'Angela', 'Julian', 'Enzo', 'Carla', 'Rocio', 'Lucrecia']
    apellidos = ['Messi', 'Scaloni', 'Ayala', 'María', 'Correa', 'Fernandez', 'Aguero', 'Gomez',
        'Martinez', 'Montiel', 'Molina', 'Tagliafico', 'Acuña', 'Romero', 'Otamendi', 'Paredes', 'Biglia']
    nombreCompleto = []
    for i in range(n):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        nombreCompleto.append(f'{nombre} {apellido}')
    return nombreCompleto
# %% Fechas


def fecha(n):
    from datetime import datetime
    Fecha = []
    for i in range(n):
        mes = int(random.uniform(1, 13))
        dia = int(random.uniform(1, 28))
        anio = int(random.uniform(1986, 2000))
        Fecha.append((f'{dia}/{mes}/{anio}'))

    return Fecha


for i in fecha(13):
    print(i)
# %% Marca temporal

def HMS(separados = True):
    import datetime
    ahora = datetime.datetime.now()
    hora, minutos,segundos =ahora.strftime("%H"),ahora.strftime("%M"),ahora.strftime("%S").split('.')
    if separados==True:
        return hora,minutos,segundos[0]
    else:
        hora_unida = f'{hora}:{minutos}:{segundos[0]}'
        return hora_unida

def MarcaTemporal(n):
    '''
    La idea es generar una función que cree marcas temporales pero sucesivas, ordenadas.
    Si no le pongo el Sleep quedan muchas func anidadas. Dificil de explicarlas
    '''
    import datetime
    import time
    MarcaTemp = []
    for i in range(n):
        MarcaTemp.append(f'{datetime.date.today()} {HMS(separados=False)}')
        time.sleep(0.2)
    return MarcaTemp

for i in MarcaTemporal(26):
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

# %% Mails
def mails(n):
    '''
    Acordate de ejecutar la función elegirNombre
    '''
    import random
    mails = []
    arrayDeNombres = elegirNombre(n)
    for nombrescompletos in arrayDeNombres:
        separacion = [f'{int(random.uniform(1,99))}','_']
        nombre = nombrescompletos.split()[0]
        apellido = nombrescompletos.split()[1]
        mails.append(f'{nombre}{random.choice(separacion)}{apellido}@gmail.com')
    return mails
    

for i in mails(26):
    print(i)

# %%
import random

random_float_list = [round(random.uniform(0, 1),3) for i in range(50)]

print(random_float_list)
# %%
listaRandom =["Esto es malo","Esto es bueno","Esto no se bien si es malo o bueno", "Este mensaje es confuso, pero me parece buena idea", "Creo que las cosas no pueden estar peor", "Colesterol Alto", "Sangre fria", "Sal en exceso","Bien","mal"]

def etiquetar_mensajes(lista_mensajes):
    etiquetas = []
    for mensaje in lista_mensajes:
        if "bueno" in mensaje or "buena" in mensaje or "Bien" in mensaje:
            etiquetas.append("Positivo")
        elif "malo" in mensaje or "mala" in mensaje or "peor" in mensaje or "confuso" in mensaje:
            etiquetas.append("Negativo")
        else:
            etiquetas.append("Neutral")
    return etiquetas

print(etiquetar_mensajes(listaRandom))
# %%

def letra_a_numero(letra):
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return abecedario.index(letra.lower()) + 1

def letraANumero(letra):
    abcd = 'abcdefghijklmnñopqrstuvwxyz'
    for index, valor in enumerate(abcd):
        if letra.lower() == valor:
            return index
    
print(letraANumero('f'))



# %%
