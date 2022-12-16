#%%
def Saludo(arg):
    """Este es el docstring de la función"""
    print("Hola " + arg + ". ¿Cómo estas?")
# %%
def multi(arg1, arg2):
    """
    Linea en la que vamos a resumir que hace nuestra función.

    Vamos a extender el resumen de la función.

    Parámetros:
    arg1 (int) : Descripción del arg1
    arg2 (int) : Descripción del arg2

    Returns:
    int: Descripción de lo que queramos retornar.
    """
    return (arg1 * arg2)

#%%
def multi(arg1, arg2):
    """
    Se multiplican dos números

    Recibimos dos valores numéricos y los multiplicamos entre ellos
    para obtener otro valor numérico.

    Parámetros:
    arg1 (int) : número entero, no importa el signo.
    arg2 (int) : número entero, no importa el signo.

    Returns:
    int: Descripción de lo que queramos retornar.
    """
    return (arg1 * arg2)
#%%
print(multi(4,5))
print(multi(4,"canciones"))
print(multi("letras", 3))
print(multi(True, 4))
# %%

nombre = "Lionel"
titulos = 41
print('El nombre del paciente es: %s y tiene %d titulos' % (nombre, titulos) )

#%%

nombre = "Lionel"
titulos = 41
print('El paciente se hace llamar: %r y dice tener %d titulos' % (nombre, titulos) )

#%%

nombre = "Lionel"
print("El nombre del paciente es: {}".format(nombre))


# %%

nombre = "Lionel"
apellido = "Messi" 
print("El nombre del paciente es:{1} y su apellido: {0}".format(nombre, apellido))
print("O al revez")


# %%
nombre = "Lionel"
apellido = "Messi" 
print(f"El nombre del paciente es:{nombre} y su apellido: {apellido}")
print(f"El nombre del paciente es:{nombre*2} y su apellido: {True if 4%2==0 else False}")
#%%

jugador = "Leandro Paredes"
JuegaEn =['Barcelona', 'Paris', 'Manchester', 'Turin']
print("el jugador, "+ jugador + " juega en " + JuegaEn[3])

#%%
nombre = "Lionel"
apellido = "Messi"

print(f"El jugador del partido es: {nombre} y su apellido es {apellido}")

#%%

kgBananas = 355.55 #1kg vale 355.55
balanza = 1.7 # compre 1.7kg
print(f'El kg de bananas está {kgBananas} y yo compré {balanza} gramos')
print(f'Tuve que pagar ${balanza*kgBananas}')


#%%

kgBananas = 355 #1kg vale 355.55
balanza = 2.5 
print(f'El kg de bananas está {kgBananas} y yo compré {balanza} gramos')
print(f'Tuve que pagar ${kgBananas*balanza if balanza<2 else (kgBananas*balanza -50)}')


# %%

import random as rm
def suerte(x):
    suerte = rm.randint(1,100)
    if (suerte == x):
        print("Estas de suerte")
    else:
        print("No estas de suerte")
suerte(3)

# %% SelecciónDeCartas
def suerteCartas():
    import random as rm
    import itertools
    numeros = ["1","2","3","4","5","6","7","8","9","10","11","12"]
    palos = ["basto", "espada", "copa", "oro"]
    carta =[]
    carta.append(rm.choices(numeros))
    carta.append(rm.choices(palos))

    carta = list(itertools.chain(*carta))
    carta1 = " ".join(carta)
    return carta1
print(suerteCartas())
# %%
'''
#2. Itertools – Chain
Usaremos un método llamado cadena de itertools módulo incorporado.

El método cadena itera sobre cada sublista y devuelve los elementos hasta que no hay 
sublistas en ella. Devuelve un iterable que tenemos que convertirlo en una lista.

Veamos los pasos necesarios para resolver el problema.

Inicialice la lista de listas con datos ficticios y asígnele el nombre datos.
Obtenga el iterable flatten usando itertools.chain (* datos).
Convierta el iterable resultante en una lista.
Imprima la lista plana.
Puede revisar el código en el siguiente fragmento.
'''

# %%
