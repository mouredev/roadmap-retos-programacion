"""
/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 */
"""

# Funciones de Orden Superior
'''Acepta función como argumento'''

def timbre(funcion,sonido):
    print("Suena el timbre:")
    funcion(sonido)

def funcion(sonido):
    print((sonido + " ") * 2)

# Pruebas
timbre(funcion,"Ding-Dong")

'''Devuelve una funcion'''
import random
def torneo(nombre):
    def ganador(participantes):
        ganador = random.choice(participantes)
        return f"Ganador del torneo {nombre.upper()} es {ganador}"
    return ganador

# Pruebas
torneo_wwe = torneo("wwe")
ganador = torneo_wwe(["Rey Misterio","John Cena","The Rock"])
print(ganador)

"""
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para 
 * realizar las siguientes operaciones de procesamiento y análisis:
 * x Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * x Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * x Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * X Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * X Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
"""
import datetime

# Lista de esudiantes
estudiantes = [
    {"nombre":"Juan","fecha":"5/12/1994","notas":[5.6,6.2,8.6,5.2,3.4]},
    {"nombre":"Abel","fecha":"12/1/1995","notas":[9.2,9.4,9.6,9.9,9.5]},
    {"nombre":"Jose","fecha":"7/2/1993","notas":[5.2,5.8,6.2,5.9,5.4]},
    {"nombre":"Maria","fecha":"21/6/1994","notas":[7.6,6.4,6.6,7.2,5.4]},
    {"nombre":"Isabel","fecha":"30/10/1995","notas":[4.6,6.5,7.6,5.7,4.2]},
]

def lista(estudiantes,funcion):
    return funcion(estudiantes)

def promedio(estudiantes):
    resultado = []
    for alumno in estudiantes:
        ciclo_notas = 0
        total = 0
        for notas in alumno["notas"]:
            total += notas
            ciclo_notas += 1
        resultado.append((f"{alumno["nombre"]}",total/ciclo_notas))
        # print(f"{alumno["nombre"]} -> {total/ciclo_notas}")
    return resultado

def mejores_alumnos(estudiantes):
    promedio_alumnos = lista(estudiantes,promedio)
    resultado = [alum for alum in promedio_alumnos if alum[1] >= 9]
    return resultado

def mas_joven(estudiantes):
    resultado = []
    for estudiante in estudiantes:
        dia,mes,ano = estudiante["fecha"].split("/")
        consulta = datetime.datetime(int(ano),int(mes),int(dia)) - datetime.datetime.now()
        resultado.append((estudiante["nombre"],consulta))
    resultado.sort(key=lambda x: x[1])
    solicitud = []
    for l in resultado:
        for estudiante in estudiantes:
            if estudiante["nombre"] == l[0]:
                solicitud.append((estudiante["nombre"],estudiante["fecha"]))
    return solicitud

def mayor_nota(estudiantes):
    mejor = []
    for estudiante in estudiantes:
        mejor_n = 0
        for nota in estudiante["notas"]:
            if nota > mejor_n:
                mejor_n = nota
        mejor.append((estudiante["nombre"],mejor_n))
    mejor.sort(key=lambda x: x[1],reverse=True)
    return mejor

# Pruebas
promedio_alumnos = lista(estudiantes,promedio)
mej_alumnos = lista(estudiantes,mejores_alumnos)
mas_alumnos = lista(estudiantes,mas_joven)
may_alumnos = lista(estudiantes,mayor_nota)

print(promedio_alumnos)
print(mej_alumnos)
print(mas_alumnos)
print(may_alumnos)