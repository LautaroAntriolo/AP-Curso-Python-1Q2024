La idea de este DSD es generar un formulario que podamos trabajar y analizar desde python, para luego enviar un mail a las personas que sepan o no ciertas cosas.

El DSD se debería pensar desde los temas de la clase, viendo las librerías y funciones en base al proyecto. Es bueno pensar que el Docstring será importante para... con F-string podrán hacer....

## Clase a clase

### Clase 4

funciones y documentacion

**contenidos importantes de la clase:**

1. librerías (Numpy, Matplotlib, Pandas, Seaborn, Math)
2. Docstring
3. f-string

**Del DSD comenzamos a hacer:**

<aside>
💡 **Crear funciones y documentarlas**

1. Importante entender que es y como funciona una librería porque luego van a trabajar con sus archivos como si fuera un libreria. Van a importar funciones y variables de un archivo creado por ellos.
2. Crear una función que te devuelva la cantidad de veces que se repite un parámetro en un array con numpy
3. Crear una función que retorne ‘Si’ si la función anterior retorna un número mayor a x y ‘No’ si el numero es menor.
4. Crear una función que retorne todos sus elementos en minúscula.
   </aside>

### Clase 5

funciones y directorio

**Contenidos de la clase:**

1. Consola (Windows-Mac) (cd, dir, mkdir, help).
2. Librería os
3. Estructura de Scripts.

   * Estructuras
     La idea es que tengan en carchivos diferentes funciones diferentes, esto les permitirá en esta clase, importar las funciones necesarias a un archivo [main.py](http://main.py) desde donde lo ejecutarán como Script principal. Generan el Script con su estructura correspondiente y lo corren.
     Una posible estructura del archivo principal (el [main.py](http://main.py)) podría ser:
     Desde la linea 1 hacia abajo podemos agregar diferentes cosas al archivo para simplificar su escalabilidad.
     1. **Comentarios:** Podemos agregar algunos comentarios al inicio del script para explicar qué hace el script, quién lo escribió, la fecha de creación y cualquier otra información relevante.
     2. **Importaciones** : Importar cualquier biblioteca o módulo necesario para ejecutar el script.
     3. **Variables globales:** Si necesitamos definir variables globales, lo hacemos al inicio del script.
     4. **Funciones** : Si tenemos funciones en el script, las podemos defínir después de las variables globales. Las funciones deben ser **autosuficientes** y no depender de otras partes del script. Puede ser la función de contar palabras o
     5. **Código principal:** El código principal del script debe venir después de las definiciones de funciones. Si el script es sencillo, todo el código podría estar dentro de esta sección. Si es más complejo, sería mejor dividirlo en secciones separadas.
     6. **Ejecución:** Al final del script, llama a la función principal o al código que deseas ejecutar dentro del condicional.
     7. **Comentarios:** Agrega comentarios al final de tu script para explicar cualquier cosa que no sea obvia en el código. (optativo para cuando el archivo principal tenga funciones autosuficientes dentro del main)
4. Vamos a crear funciones con Scripts.
5. Matemáticas ⇒ extra

**Del DSD comenzamos a hacer:**

<aside>
💡 **Crear funciones y documentarlas para movernos por el directorio**

1. Creamos una función que le pasamos una ruta y nos devuelva la cantidad de elementos que hay en esa carpeta.
2. Creamos una función que le pasamos una ruta y nos devuelva el nombre de los elementos que hay dentro de la carpeta.
3. La misma función la ejecutamos desde la terminal con un Script.
4. Importante la librería **os** con:
   1. **makedirs**
   2. **os.path.exists**

      </aside>

### Clase 6

Toma de datos

**contenidos de la clase:**

* Tomar datos desde un archivo de Excel.
* Graficar datos utilizando: Matplotlib - pandas

Del DSD comenzamos a hacer:

Haremos una breve conexión con el excel y conectaremos los datos. Aprenderemos lo básico de pandas, recalcando que si queremos mejorar en esta librería, estaá el curso de ciencia de datos. La idea es tener una idea de sus estructuras y mostrar que se pueden manejar como listas. Que guardemos los datos que queremos en variables y así organicemos los elementos para graficar.

<aside>
💡 **Crear funciones para graficar**
Guardamos en variables los datos que queremos graficar
Creamos una función que grafica cuando le pasamos dos listas

</aside


### **Clase 7** 

API, JSON y gráficos

**contenidos de la clase:**

* Tomar datos desde una API.
* API y JSON.
* Graficar Datos utilizando Matplotlib y pandas.

**Del DSD comenzamos a hacer:**

<aside>
💡 **Probando las funciones graficar**
Probamos si las funciones que creamos, grafican tambien los datos que tomamos de la NASA.
Les mostramos como podemos guardar la información en un JSON (manualmente). Si podemos, también en un txt. Mas adelante veremos como guardamos la info en un JSON automaticamente. Si llegamos probamos hacerlo acá.

</aside>

### Clase 8

**contenidos de la clase:**

* Llamada a la APIs de Google Cloud.
* Los Forms de Google.

**Del DSD comenzamos a hacer:**

Creamos la integración co google cloud. Podemos pensar las preguntas para un formulario y ver como nos devuelve los datos a python. Guardamos la info necesaria en variables y probamos que todo funciones bien.

<aside>
💡 **Probando formulario y python**
Vemos la salida por la terminal de las respuestas al formulario de Google. Podemos armar ya un formulario para usar en el DSD o uno de prueba para mostrar como funciona todo.
El código lo tienen los profes por lo que se tiene que compartir el código para que tomen los datos y hacer las conexiones con python.
🐍Será importante guardar  **la api key y demas en un txt en VsCode** ! 🐍

</aside>

### Clase 9

**contenidos de la clase:**

* Crear fórmulas con los datos obtenidos ⇒ otras funciones.
* Archivos txt y escribiendo en el archivo de google sheets.
* Graficar los datos tomados desde Forms.
* Envío de correos.

**Del DSD comenzamos a hacer:**

La idea es transpolar lo visto con las funciones y librerías con los datos obtenidos del Form.

El txt lo usaremos para tener como una guía que no sea la terminal de lo que va ejecutando el programa…Si hay alguna duda, los alumnos mandaran el txt para corregir.

<aside>
💡 **Funciones-graficos-envio de correos- txt (opcional)**
A medida que se van desarrollando los temas, y tomamos los datos del google sheets, podemos crear las funciones para graficar estos datos.
La escritura en la hoja de cálculo de Google la podemos dejar para el final, dependiendo lo que quiera lograr el grupo con el proyecto final. La escritura del txt no es la mas importante porque quedaría unicamente para registrar información. Se podría pasar el código dependiendo el proyecto que presenten los alumnos.

</aside>

### Clase 10 

**contenidos de la clase:**

IA y Scripts

**Del DSD comenzamos a hacer:**

<aside>
💡 **Scrips e IA**
Lo mas importante es crear un script con una estructura básica para correrlo desde VsCode. Si da el tiempo creamos el bat para ejecutarlo automaticamente. Usaremos la IA como herramienta sencilla para crear los mensaje que mandaremos por mail.

</aside>
