from lectura import *
import matplotlib.pyplot as plt
import os
from datetime import date

def listasEnMinuscula(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].lower()
    return lista

primario = contador_palabras(listasEnMinuscula(nivelEstudios),'primario completo')
secundario = contador_palabras(listasEnMinuscula(nivelEstudios),'secundario completo')
terciario = contador_palabras(listasEnMinuscula(nivelEstudios),'terciario completo')
universitario = contador_palabras(listasEnMinuscula(nivelEstudios),'universitario completo')
# print(secundario,terciario, universitario,primario)

#Vamos a generar gráficos que representen la audiencia hasta el momento
#Subplot en matplotlib
'''
El primer argumento indica el número de filas de subplots, 
el segundo argumento indica el número de columnas de subplots, 
y el tercer argumento indica el índice del subplot actual. 
En este caso, tenemos una sola fila y 3 columnas de subplots, 
y especificamos que el primer subplot está en la primera columna 
(1) y el segundo subplot está en la tercer columna (2).
Dejamos la segunda columna libre para que se vea bien el gráfico.
'''

def graficoEdadEstudios():
    # # Para tener una idea de los usuarios que tenemos, vamos a generar un gráfico de torta con porcentajes
    datos = [secundario, terciario, universitario, primario]
    categorias = ["Secundario completo", "terciario completo", "Universitario completo", "Primario completo"]
    colores = ["#FFD700", "#C0C0C0", "#FF6347", "#00FFFF", "#eeeFFF"]
    plt.subplot(1, 3, 1)#elijo la posición del gráfico dentro del subtplot
    plt.pie(datos, labels=categorias, colors=colores, autopct="%0.1f %%")

    # #Para graficar las edades, voy a graficar un histograma
    # #Crear el histograma
    plt.subplot(1, 3, 3) #elijo la posición del gráfico dentro del subtplot
    plt.hist(edad, bins=6, edgecolor='black')

    # #Configurar el gráfico
    plt.title('Distribución de edades')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    if not os.path.exists('./DSD/img'):
        os.makedirs('./DSD/img')

    # Guardar el gráfico en la carpeta img
    plt.savefig(f'./DSD/img/{date.today()}')

    if os.path.exists('C:/Lautaro/AprendeProgramando/CursoPython2023/Python/DSD/datos.json'):
            with open('C:/Lautaro/AprendeProgramando/CursoPython2023/Python/DSD/datos.json') as f:
                data = json.load(f)
                data[f'{date.today()}']['imagenes']['graficoEdadEstudios'] = f'./DSD/img/graficoEdadEstudios.png'
                with open('C:/Lautaro/AprendeProgramando/CursoPython2023/Python/DSD/datos.json', 'w') as f:
                    json.dump(data, f)
    else:
        data = {'inicio': 'B2', f'{datetime.now().date()}':{f'final':f'{final}','imagenes':{}}}
        data['imagenes']['graficoEdadEstudios'] = f'./DSD/img/graficoEdadEstudios-{date.today()}'
        with open('C:/Lautaro/AprendeProgramando/CursoPython2023/Python/DSD/datos.json', 'w') as f:
            json.dump(data, f)

    # #Mostrar el gráfico
    # plt.show()
    # #está comentado porque detiene el Script
