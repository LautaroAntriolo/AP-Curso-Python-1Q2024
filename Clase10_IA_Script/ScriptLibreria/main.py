if __name__ == "__main__":
    from numeros import *
    numero = numer()
    fecha = fechas()
    contrasenia = contra()
    orden = str(fecha[0])+ str(contrasenia)
    with open("C:\Lautaro\AprendeProgramando\CursoPython2023\Python\Clase10_IA_Script\ScriptLibreria\libreriaDeContras.txt", 'a+') as archivo:
        archivo.write(f'\n minutos: {fecha[1]}, contra: {orden}')