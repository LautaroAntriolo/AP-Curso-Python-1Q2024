from lectura import *
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
import os
from datetime import date
from collections import Counter
import random
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
def ModificarJSON_IMG(fechaActual,rutaJSON,nombreArchivo):
    if os.path.exists(f'{rutaJSON}'):
                with open(f'{rutaJSON}') as f:
                    data = json.load(f)
                    data[f'{fechaActual}']['imagenes'][f'{nombreArchivo}'] = f'./DSD/img/{fechaActual}/{nombreArchivo}'
                    with open(f'{rutaJSON}', 'w') as f:
                        json.dump(data, f)
    else:
        data = {'inicio': 'B2', f'{fechaActual}':{f'final':f'{final}','imagenes':{}}}
        data['imagenes'][f'{nombreArchivo}'] = f'./DSD/img/{fechaActual}/{nombreArchivo}'
        with open(f'{rutaJSON}', 'w') as f:
            json.dump(data, f)
def graficoEdadEstudios(secundario, terciario, universitario, primario,edad):
    if not os.path.exists(f'./DSD/img/{fechaActual}'):
        os.makedirs(f'./DSD/img/{fechaActual}')

    plt.figure()
    # # Para tener una idea de los usuarios que tenemos, vamos a generar un gráfico de torta con porcentajes
    datos = [secundario, terciario, universitario, primario]
    categorias = [f'secundario completo', "terciario completo", "Universitario completo", "Primario completo"]
    colores = ["#FFD700", "#C0C0C0", "#FF6347", "#00FFFF", "#eeeFFF"]
    
    # plt.subplot(2, 1, 1)#elijo la posición del gráfico dentro del subtplot
    plt.title("Estudios cursados")
    plt.pie(datos, labels=categorias, colors=colores, autopct="%0.1f %%")
    plt.savefig(f'./DSD/img/{fechaActual}/graficoEstudios.png')
    
    # #EDADES
    plt.figure()
    plt.title("Edades")
    unicos = Counter(edad)
    # Define los datos que quieres graficar
    labels = []
    sizes = unicos.values()
    for key, value in unicos.items():
        labels.append(f'{key} ({value})')
    # Ordena las etiquetas de mayor a menor
    labels, sizes = zip(*sorted(zip(labels, sizes), key=lambda x: x[1], reverse=True))
    # Define las opciones de visualización para el gráfico
    plt.pie(sizes, startangle=90, pctdistance=0.85)
    plt.legend(labels, loc='center left', bbox_to_anchor=(1.05, 0.5))
    plt.savefig(f'./DSD/img/{fechaActual}/graficoEdad.png')
    
    
    
    # Guardar el gráfico en la carpeta img
    plt.savefig(f'./DSD/img/{fechaActual}/graficoEdad.png')

    ModificarJSON_IMG(fechaActual,'./DSD/datos.json','graficoEdad')

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

    ModificarJSON_IMG(fechaActual,'./DSD/datos.json','EducacionIntensivos')

def MedidasResponsabilidad(medidas,responsabilidad):
    medidasSi = contador_palabras(medidas,'si')
    medidasNo = contador_palabras(medidas,'no')
    empresa = contador_palabras(responsabilidad,'empresa')
    individuo = contador_palabras(responsabilidad,'individuo')
    
    datos = [medidasSi, medidasNo]
    categorias = ["Quiere", "Niega"]
    colores = ["#FFD700", "#C0C0C0", "#FF6347", "#00FFFF", "#eeeFFF"]
    plt.figure()
    plt.suptitle("Medidas vs Responsabilidad")
    
    plt.subplot(1, 2, 1)#elijo la posición del gráfico dentro del subtplot
    plt.title("Accion vs Inacción")
    plt.pie(datos, labels=categorias, colors=colores, shadow=True, startangle=90, autopct="%0.1f %%")


    datos = [empresa, individuo]
    categorias = ["empresa", "individuo"]
    colores = [ "#FF6347", "#00FFFF", "#eeeFFF","#FFD700", "#C0C0C0"]
    
    plt.subplot(1, 2, 2)#elijo la posición del gráfico dentro del subtplot
    plt.title("Empresas e individuos")
    plt.pie(datos, labels=categorias, colors=colores,autopct="%0.1f %%")

    if not os.path.exists(f'./DSD/img/{fechaActual}'):
        os.makedirs(f'./DSD/img/{fechaActual}')
    # Guardar el gráfico en la carpeta img
    plt.savefig(f'./DSD/img/{fechaActual}/MedidasYResponsabilidad.png')

    ModificarJSON_IMG(fechaActual,'./DSD/datos.json','MedidasYResponsabilidad')

     
