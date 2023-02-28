![Logo de aprende programando](https://aprendeprogramandoinscripciones.bue.edu.ar/img/Recursos-AP/Imagenes/LogoAP.png)
# Organización de las clases y posibles errores

# Clase 1️⃣ 
## 1. Instalación de Python

Podemos tener algunos errores al instalar python, entre ellos que no hagamos el check para conectarlo con el Path en windows.
Para eso...

También podemos tener algun error con el paquete pip que viene instalado por defecto en las ultimas versiones pero por las dudas jeje

Si no se reconoce a pip como comando, y queremos instalarlo, tenemos que hacer lo siguiente: 

**SOLUCION 1**: desinstalar python y volverlo a instalar. Esto funciona si no tenemos otra version de python en nuestra computadora o si nunca desinstalamos python.
**SOLUCION 2:** Para mac y linux : [otros sistemas operativos](https://www.neoguias.com/como-instalar-pip-python/#Como_instalar_PIP_en_Windows)
Para windows 7,8,10 seguir los siguientes pasos: 

1. Descargá en el lugar del directorio que prefieras el archivo get-pip.py que está en este repo. Si utilizas Python 3.2, necesitarás utilizar **[esta versión de get-pip.py](https://bootstrap.pypa.io/3.2/get-pip.py)**. .
2. Seguidamente, abre la terminal de comandos y navega hasta el directorio en el que has guardado el **[archivo](https://www.neoguias.com/archivo/)** **get-pip.p**y.
3. Ejecuta el siguiente comando:
    
    ```
    python get-pip.py
    ```
    

4. Y ya está todo listo. El script de instalación instalará PIP en tu sistema. Te recomiendo probar con instalar alguna librería como numpy o pandas de la siguiente forma:

    ```
    pip install numpy
    ```


## 2. Entorno Virtual

Para una mejor organización, es recomendable crearse un entorno virtual para poder trabajar con todas las librerías y elementos de forma mas ordenada
Esto es teniendo en cuenta que podemos tener mas de una comisión asignada que vayan a ritmos diferentes
A los estudiantes recomiendo que se les explique unicamente a los avanzados para evitar confusión
A los principiantes, es mejor enseñarles como instalar y desinstalar paquetes manualmente 
con pip install y pip uninstall respectivamente

Video tutorial de como [crear entorno virtual](https://www.youtube.com/watch?v=7KoGJdGgwxk) 

<aside>
💡 Siempre recordar activarlo cuando arrancamos la clase y cerrarlo cuando termina!
</aside>

