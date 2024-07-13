"""
/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para 
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
 */
"""

# EJERCICIO:
from datetime import datetime


def operation(x, func):
    return func(x)


def squared(x):
    return x ** 2


result = operation(10, squared)
print(result)

# DIFICULTAD EXTRA:
estudiantes = [
    {
        "nombre": "Agustin",
        "fecha_nacimiento": "28-09-01",
        "lista_calificaciones": [10, 6, 7, 8]
    },
    {
        "nombre": "Hernan",
        "fecha_nacimiento": "03-08-00",
        "lista_calificaciones": [9, 8, 7, 6]
    },
    {
        "nombre": "Francisco",
        "fecha_nacimiento": "01-03-02",
        "lista_calificaciones": [9, 8, 9, 10]
    },
    {
        "nombre": "Alfred",
        "fecha_nacimiento": "09-02-03",
        "lista_calificaciones": [10, 10, 8, 8]
    }
]

# Promedio calificaciones: Obtiene una lista de estudiantes por nombre y promedio de sus calificaciones.


def promedio_calificaciones(calificaciones):
    return sum(calificaciones) / len(calificaciones)


for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    calificaciones = estudiante["lista_calificaciones"]
    print(f"Nombre: {nombre}, Calificaciones: {
          promedio_calificaciones(calificaciones)}")

# Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes que tienen calificaciones con un 9 o más de promedio.
for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    calificaciones = estudiante["lista_calificaciones"]
    if promedio_calificaciones(calificaciones) >= 9:
        print(f"Estudiantes con 9 o mas: {nombre}")

# Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.


def convertir_fecha(fecha_str):
    return datetime.strptime(fecha_str, "%d-%m-%y")


estudiantes_ordenados = sorted(estudiantes, key=lambda x: convertir_fecha(
    x["fecha_nacimiento"]), reverse=True)

for estudiante in estudiantes_ordenados:
    print(f"Nombre: {estudiante['nombre']}, Fecha de nacimiento: {
          estudiante['fecha_nacimiento']}")

# Mayor calificación: Obtiene la calificación más alta de entre todas las de los alumnos.
max_calificacion = float('-inf')

for estudiante in estudiantes:
    for calificacion in estudiante["lista_calificaciones"]:
        if calificacion > max_calificacion:
            max_calificacion = calificacion

print(f"La calificación más alta es: {max_calificacion}")
