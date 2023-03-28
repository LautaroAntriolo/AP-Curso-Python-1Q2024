from lectura import *
import matplotlib.pyplot as plt
import os
from datetime import date
from collections import Counter
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
fechaActual = date.today()
def graficoEdadEstudios(secundario, terciario, universitario, primario,edad):
    plt.figure()

    # # Para tener una idea de los usuarios que tenemos, vamos a generar un gráfico de torta con porcentajes
    datos = [secundario, terciario, universitario, primario]
    categorias = [f'secundario completo', "terciario completo", "Universitario completo", "Primario completo"]
    colores = ["#FFD700", "#C0C0C0", "#FF6347", "#00FFFF", "#eeeFFF"]
    
    plt.subplot(2, 1, 1)#elijo la posición del gráfico dentro del subtplot
    plt.title("Estudios cursados")
    plt.pie(datos, labels=categorias, colors=colores, autopct="%0.1f %%")
        
    
    # #EDADES
    plt.subplot(2, 1, 2)
    plt.title("Edades")
    unicos = Counter(edad)
    # Define los datos que quieres graficar
    labels = unicos.keys()
    sizes = unicos.values()
    # Define las opciones de visualización para el gráfico
    plt.pie(sizes, startangle=90, pctdistance=0.85)
    plt.legend(labels, loc='center left', bbox_to_anchor=(1.05, 0.5))
    
    
    if not os.path.exists(f'./DSD/img/{fechaActual}'):
        os.makedirs(f'./DSD/img/{fechaActual}')

    # Guardar el gráfico en la carpeta img
    plt.savefig(f'./DSD/img/{fechaActual}/graficoEdadEstudios.png')

    if os.path.exists('C:/Lautaro/AprendeProgramando/CursoPython2023/Python/DSD/datos.json'):
            with open('C:/Lautaro/AprendeProgramando/CursoPython2023/Python/DSD/datos.json') as f:
                data = json.load(f)
                data[f'{fechaActual}']['imagenes']['graficoEdadEstudios'] = f'./DSD/img/{fechaActual}/graficoEdadEstudios.png'
                with open('C:/Lautaro/AprendeProgramando/CursoPython2023/Python/DSD/datos.json', 'w') as f:
                    json.dump(data, f)
    else:
        data = {'inicio': 'B2', f'{fechaActual}':{f'final':f'{final}','imagenes':{}}}
        data['imagenes']['graficoEdadEstudios'] = f'./DSD/img/{fechaActual}/graficoEdadEstudios'
        with open('C:/Lautaro/AprendeProgramando/CursoPython2023/Python/DSD/datos.json', 'w') as f:
            json.dump(data, f)

    # #Mostrar el gráfico
    # plt.show()
    # #está comentado porque detiene el Script

def EducacionEincentivos(educacion, incentivos):
    EduSi = contador_palabras(listasEnMinuscula(educacion),'si')
    EduNo = contador_palabras(listasEnMinuscula(educacion),'no')
    IncenNo = contador_palabras(listasEnMinuscula(incentivos),'no')
    IncenSi = contador_palabras(listasEnMinuscula(incentivos),'si')
    
    datos = [EduSi, EduNo]
    categorias = ["Quiere", "Niega"]
    colores = ["#FFD700", "#C0C0C0", "#FF6347", "#00FFFF", "#eeeFFF"]
    plt.figure()
    plt.suptitle("Educación Vs Incentivos")
    
    plt.subplot(1, 2, 1)#elijo la posición del gráfico dentro del subtplot
    plt.title("educación")
    plt.pie(datos, labels=categorias, colors=colores, shadow=True, startangle=90, autopct="%0.1f %%")
    datos = [IncenSi, IncenNo]
    categorias = ["Aceptaría", "No quiere"]
    colores = [ "#FF6347", "#00FFFF", "#eeeFFF","#FFD700", "#C0C0C0"]
    
    plt.subplot(1, 2, 2)#elijo la posición del gráfico dentro del subtplot
    plt.title("incentivos económicos")
    plt.pie(datos, labels=categorias, colors=colores,autopct="%0.1f %%")

    if not os.path.exists(f'./DSD/img/{fechaActual}'):
        os.makedirs(f'./DSD/img/{fechaActual}')
    # Guardar el gráfico en la carpeta img
    plt.savefig(f'./DSD/img/{fechaActual}/EducacionEincentivos.png')

    if os.path.exists('./DSD/datos.json'):
            with open('./DSD/datos.json') as f:
                data = json.load(f)
                data[f'{fechaActual}']['imagenes']['EducacionEincentivos'] = f'./DSD/img/{fechaActual}/EducacionEincentivos.png'
                with open('./DSD/datos.json', 'w') as f:
                    json.dump(data, f)
    else:
        data = {'inicio': 'B2', f'{fechaActual}':{f'final':f'{final}','imagenes':{}}}
        data['imagenes']['EducacionEincentivos'] = f'./DSD/img/{fechaActual}/EducacionEincentivos.png'
        with open('./DSD/datos.json', 'w') as f:
            json.dump(data, f)

    # #Mostrar el gráfico
    # plt.show()
    # #está comentado porque detiene el Script

