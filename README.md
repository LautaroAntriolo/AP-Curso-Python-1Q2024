En todas las clases van a ver que tienen contenidos extras. Cosas que son importantes y cosas que son detalles o no tan importantes para este caso. La idea fue generar contenido para que los chicos que ya vienen con algún conocimiento previo, vean que pueden hacerlo de diferentes formas. 

Por este motivo se decidieron temas, que tienen que ser los importantes a entender en la clase que terminarán por cumplir con los requisitos para el proyecto final. El curso se comenzó a pensar desde el proyecto, por lo que la estructura de la cursada es desde el proyecto final.

Se agradece la intervención de mentores que conozcan python en códigos y/o explicaciones. 🤓

## Clase 1️⃣

### Instalación de Python

Podemos tener algunos errores al instalar python, entre ellos que no hagamos el check al instalar python para conectarlo con el Path

**SOLUCION 1**: desinstalar python y volverlo a instalar. Esto funciona si no tenemos otra version de python en nuestra computadora o si nunca desinstalamos python.
**SOLUCION 2:** Para mac y linux : [otros sistemas operativos](https://www.neoguias.com/como-instalar-pip-python/#Como_instalar_PIP_en_Windows)
Para windows 7,8,10 seguir los siguientes pasos: 

1. Descarga el **[script de instalación get-pip-py](https://bootstrap.pypa.io/get-pip.py)**. Si utilizas Python 3.2, necesitarás utilizar **[esta versión de get-pip.py](https://bootstrap.pypa.io/3.2/get-pip.py)**. En el script, haz **clic derecho** en el documento y luego selecciona **Guardar como**, almacendo el script en un directorio que prefieras.
2. Seguidamente, abre la terminal de comandos y navega hasta el directorio en el que has guardado el **[archivo](https://www.neoguias.com/archivo/)** **get-pip.p**y.
3. Ejecuta el siguiente comando:
    
    ```
    python get-pip.py
    ```
    

Y ya está todo listo. El script de instalación instalará PIP en tu sistema.

### Entorno Virtual

Para una mejor organización, es recomendable crearse un entorno virtual para poder trabajar con todas las librerías y elementos de forma mas ordenada
Esto es teniendo en cuenta que podemos tener mas de una comisión asignada que vayan a ritmos diferentes
A los estudiantes recomiendo que se les explique unicamente a los avanzados para evitar confusión
A los principiantes, es mejor enseñarles como instalar y desinstalar paquetes manualmente 
con pip install y pip uninstall respectivamente

Video tutorial de como [crear entorno virtual](https://www.youtube.com/watch?v=7KoGJdGgwxk) 

<aside>
💡 Siempre recordar activarlo cuando arrancamos la clase y cerrarlo cuando termina!

</aside>

### Datos importantes de la clase:

1. Profundizar en los tipos de datos y particularmente en las  listas y strings como iterables.
2. Diferencias entre listas y tuplas.
3. La posición de los elementos dentro de un iterable.

## Clase 2️⃣

### Datos importantes de la clase:

1. Los condicionales como código mínimo:
No creo que lo usen demasiado, pero si lo logran usar va a simplificar mucho la lectura de los códigos del proyecto. Quedaría en cada uno ver que le queda mas cómodo.
2. La función enumerate será importante mas adelante: 
Lo que hacemos con el enumerate, lo podemos hacer igualmente con la variable del bucle for, pero es mas “pythonista” de esta forma. 
3. Bucle for y condicionales no puede faltar, como en todos 😄

## Clase 3️⃣

### Datos importantes de la clase:

1. Funciones:
Importante hacer incapié en que todas las funciones se pueden importar luego, por lo que será importante mantener un código limpio. Mas adelante veremos como con buenas prácticas documentarlas para que puedan ver lo que querian hacer.  
2. Intentar que cuando terminen la función no esté el print dentro para no demorar la ejecución del código mas adelante. 
3. Dentro de los parámetros, los parámetros optativos son un detalle importante. Recomiendo que los sigan usando aunque no sean tan necesarios, pero si queda la idea de un parámetro optativo bien plasmada sería genial.
4. Las funciones pre-definidas mas importantes serán: len, max, min, print, sum, range, lower, upper, int, join y split. La mayoría son intuitivas, pero las últimas dos son las mas “complicadas”. Es probarlo dos o tres veces. 
la función Input la podemos usar para mostrar como funciona y para generar una interacción pero al usar el formulario de google la olvidamos.
5. Return: Clave mostrar lo que pasa con el return cuando tiene y no tiene prints dentro. Para impulsar que usen el print por fuera de la función cuando las estén probando.
6. **Debugger:** No haremos una clase de debuggear, pero es importante que al crear una función comiencen a ver como va ejecutandose el código. Seguro nos sirve para mostrar lo del print y el return. 
    
    Video tutorial: [https://www.youtube.com/embed/wdZWeWub7vs?start=83](https://www.youtube.com/embed/wdZWeWub7vs?start=83)
    
7. La calculadora tiene varias funciones que podemos hacer con las funciones pre-definidas de Python. En este punto pueden crear:
    1. Una funcion suma que acepta un elemeto, con un elemento b con valor definido en 0. Si acepta varios elementos que sean en un array. Lo mismo con la resta.
    2. La clásica función que te dice si el número es par o impar… podemos hacer lo mismo con una lista si queremos pasar varios números.
    3. Podemos crear una función que le pasamos una letra y te devuelve la posición en el abecedario Podemos hacerlo así:
    
    ```python
    def letra_a_numero(letra):
        abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        return abecedario.index(letra.lower()) + 1
    
    ## También podriamos hacerlo de esta forma
    def letraANumero(letra):
        abcd = 'abcdefghijklmnñopqrstuvwxyz'
        for index, valor in enumerate(abcd):
            if letra.lower() == valor:
                return index
            else:
                continue
    ```
    
## Clase 4️⃣
    
### Datos importantes de la clase:
    
1. Importar paquetes de libererías: La idea es que en el proyecto final no creen todo en un mismo archivo, sino que se organicen en un archivo donde tomen todos los datos, otro donde creen las funciones y otro donde ejecuten el script. Que entiendan que las librerías las pueden crear ellos y tambien usar las de otros. Creemos que si entienden mejor el concepto de librería buscarán también la forma de crear la documentación correcta  y buscarla si no entienden una función. 
2. Al instalar las librerías puede que el comando `pip install nombreDeLibrería` no funcione. Si ese comando tira algún error, hay que probar instalar las librerías de la siguiente forma: 
    `python - m pip install nombreDeLibrería.`  .Si aún así sigue sin funcionar, hay que probar instalar pip de nuevo como se muestra en la clase 1.
3. Librerias: En esta parte **hay mas librerías de las que se usan**, pero es importante que las vayan teniendo presente de oído al menos para mas adelante. Las mas importantes en general serán **numpy, pandas, matplotlib, random y datetime**. Las demás las dejamos para aquellos alumnos que ya conozcan estas librerías y quieran practicar con alguna otra.
Random y datetime son mucho mas simples y se usan en ámbitos mas generales. 
    1. [Documentación de Numpy](https://numpy.org/doc/stable/user/quickstart.html) 
    2. [Documentación de Pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide), [resumen de 3Wschools](https://www.w3schools.com/python/pandas/default.asp)
    3. Documentación de matplotlib
    4.  [Documentación random](https://docs.python.org/es/3/library/random.html)
    5. [Documentación Datetime](https://docs.python.org/es/3/library/datetime.html)
        
4. Seaborn : Esta librería está muy buena pero se la dejamos solo a los alumnos que ya conozcan Matplotlib. 
5. **De las buenas prácticas F-string y Docstring es lo mas importante!** Lo demás está por si algun alumno lo vió en el colegio. Si lo vieron, seguramente vieron format y ya no se usa mucho. Al que no sabe nada, directamente f-string. Al que sabe algo, le mostramos por que f-string es tan potente.

## Clase 5️⃣

### Datos importantes de la clase:

1. Movernos entre el directorio:
    1. Comandos cd, cd..m mkdir, rmdir, rd, md ⇒ La idea es que sepan que es la consola, se puedan mover por el directorio y entiendan donde están parados. Saber que podemos acceder a cualquier archivo desde el directorio.
2. Ejecutar algún archivo desde el directorio con diferentes funciones. Lo mas importante es la sintaxis, el condicional if _ _ main_ _ == _ _main_ _ … Si crearon funciones, podrían trabajar toda la clase ejecutando las funciones desde el directorio, siempre y cuando las llamen dentro de este condicional. No podemos en este caso pasarle parámetros, pero podríamos usar la función input para crear un función que nos pida algún dato a completar.