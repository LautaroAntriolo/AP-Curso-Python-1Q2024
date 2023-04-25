# Usamos Try y except pero podemos hacerlo con if y else.

# forma 1
def agregar_linea_archivo(nombre_archivo, linea):
    try:
        with open(f'C:\Lautaro\AprendeProgramando\CursoPython2023\Python\Clase9_Email\conArchivos\{nombre_archivo}', 'a') as archivo:
            archivo.write(linea + '\n')
    except FileNotFoundError:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(linea + '\n')

agregar_linea_archivo('mi_archivo.txt', 'Esta es la nueva línea')

# forma 2
def agregar_a_archivo(parametro):
    archivo = "C:\Lautaro\AprendeProgramando\CursoPython2023\Python\Clase9_Email\conArchivos\datos.txt"
    
    with open(archivo, "a") as archivo_txt:
        archivo_txt.write(parametro + "\n")

agregar_a_archivo('hola')
agregar_a_archivo('chau')