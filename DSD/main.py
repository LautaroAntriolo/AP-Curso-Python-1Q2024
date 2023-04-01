from lectura import *
from graficos import graficoEdadEstudios, EducacionEincentivos,MedidasResponsabilidad
from mails import enviarMail



primario = contador_palabras(listasEnMinuscula(nivelEstudios),'primario completo')
secundario = contador_palabras(listasEnMinuscula(nivelEstudios),'secundario completo')
terciario = contador_palabras(listasEnMinuscula(nivelEstudios),'terciario completo')
universitario = contador_palabras(listasEnMinuscula(nivelEstudios),'universitario completo')

if __name__ == '__main__':
    todosLosValores(nombreHoja,inicio)
    archivoJSON(final)
    graficoEdadEstudios(secundario, terciario, universitario, primario,edad)
    EducacionEincentivos(Educacion, Incentivos)
    MedidasResponsabilidad(medidas,responsabilidad)
    enviarMail(ultimosmails,'Probando el for', 'este sirve menos')