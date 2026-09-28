"""
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
"""

from datetime import datetime

student1 = {
    "nombre": "Spinoza",
    "fecha_nacimiento": datetime(2009, 1, 25),
    "calificaciones": {
        "ma1": 5,
        "ma2": 6,
        "ma3": 8,
        "ma4": 9,
        "ma5": 7
    }
}

student2 = {
    "nombre": "Hilton",
    "fecha_nacimiento": datetime(2009, 4, 5),
    "calificaciones": {
        "ma1": 7,
        "ma2": 6,
        "ma3": 2,
        "ma4": 9,
        "ma5": 7
    }
}

student3 = {
    "nombre": "Paris",
    "fecha_nacimiento": datetime(2010, 1, 25),
    "calificaciones": {
        "ma1": 5,
        "ma2": 9,
        "ma3": 8,
        "ma4": 9,
        "ma5": 7
    }
}

student4 = {
    "nombre": "Loreal",
    "fecha_nacimiento": datetime(2009, 1, 1),
    "calificaciones": {
        "ma1": 8,
        "ma2": 8,
        "ma3": 8,
        "ma4": 9,
        "ma5": 7
    }
}

student5 = {
    "nombre": "Francis",
    "fecha_nacimiento": datetime(2009, 1, 15),
    "calificaciones": {
        "ma1": 10,
        "ma2": 8,
        "ma3": 8,
        "ma4": 10,
        "ma5": 9.5
    }
}

student6 = {
    "nombre": "Xuen",
    "fecha_nacimiento": datetime(2009, 2, 25),
    "calificaciones": {
        "ma1": 0,
        "ma2": 6,
        "ma3": 6,
        "ma4": 6,
        "ma5": 10
    }
}

student7 = {
    "nombre": "Lopez",
    "fecha_nacimiento": datetime(2008, 1, 25),
    "calificaciones": {
        "ma1": 10,
        "ma2": 10,
        "ma3": 6,
        "ma4": 0,
        "ma5": 0
    }
}

students = (student1, student2, student3, student4, student5, student6, student7)


# --- Promedio de calificaciones
def iterar_lista(lista, name_function, avg_function):
    new_list = []
    for elemento in lista:
        name, promedio = name_function(elemento), avg_function(elemento)
        new_list.append((name, promedio))
    return new_list


def obtener_nombre_estudiante(datos):
    return datos["nombre"]

def promedio_estudiante(numeros):
    contador = 0
    promedio = 0

    numeros = numeros["calificaciones"].values()

    for num in numeros:
        promedio += num
        contador += 1
    else:
        promedio /= contador
        return promedio

def obtener_calificaciones(lista) -> list[tuple[str, float]]:
    lista_pares = iterar_lista(lista, obtener_nombre_estudiante, promedio_estudiante)
    return lista_pares

print(obtener_calificaciones(students)); print()

# Obtener las mejores calificaciones
def obtener_mejores_estudiantes(lista):
    calificaciones = obtener_calificaciones(lista)

    mejores_estudiantes = [(name, promedio) for name, promedio in calificaciones if promedio >= 9]

    return mejores_estudiantes

print(obtener_mejores_estudiantes(students)); print()


# Ordenar estudiantes por edad ascedente
def iterar_lista(lista, name_function, birthdate_function):
    new_list = []
    for elemento in lista:
        name, promedio = name_function(elemento), birthdate_function(elemento)
        new_list.append((name, promedio))
    return new_list

def obtener_nombre_estudiante(datos):
    return datos["nombre"]

def obtener_fecha_nacimiento(datos):
    return datos["fecha_nacimiento"]

def ordenar_estudiantes_edad_asc(lista):
    birthdates = iterar_lista(lista, obtener_nombre_estudiante, obtener_fecha_nacimiento)

    for i in range(0, len(birthdates) - 1):
        for k in range(0, len(birthdates) - i - 1):
            if birthdates[k][1] > birthdates[k + 1][1]:
                tmp = birthdates[k]
                birthdates[k], birthdates[k + 1] = birthdates[k + 1], tmp

    return birthdates

print(ordenar_estudiantes_edad_asc(students)); print()


# Obtener mayor calificación
def obtener_mayor_calificación(lista):
    # obtener_mejores_estudiantes
    # iterar y guardar la mejor calificación
    # retornar el par (estudiante con mayor calificación, calificación)
    mejores_estudiantes = obtener_mejores_estudiantes(lista)

    max = [str(), -1]
    for name, grade in mejores_estudiantes:
        if grade >= max[1]:
            max = [name, grade]
    if max[0]:
        return tuple(max)
    return tuple()

print(obtener_mayor_calificación(students)); print()