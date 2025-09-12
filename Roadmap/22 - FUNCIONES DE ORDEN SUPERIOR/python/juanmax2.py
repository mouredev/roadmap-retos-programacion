from functools import reduce
from datetime import datetime

"""
Ejercicio
"""

# Función como argumento

def apply_func(func, x):
    return func(x)

print(apply_func(len, "Juanma"))

# Retorno de función

def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

multiplier = apply_multiplier(2)
print(multiplier(4))
print(apply_multiplier(2)(4))

# Sistema

numbers = [1, 3 , 5, 2, 4]

# map()

def apply_duble(n):
    return n * 2

print(list(map(apply_duble, numbers)))

# filter()

def is_even(n):
    return n % 2 == 0 

print(list(filter(is_even, numbers)))

# sorted()

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

# reduce()

def sum(x, y):
    return x + y

print(reduce(sum, numbers))

"""
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

estudiantes = [
    {"name": "Maria", "birthdate" : "10-06-1997", "notas" : [10, 9, 8]},
    {"name": "Juanma", "birthdate" : "13-11-1992", "notas" : [7, 9, 8]},
    {"name": "David", "birthdate" : "24-10-1992", "notas" : [10, 9, 9]},
    
]

def media(notas):
    suma = 0
    for nota in notas:
        suma += nota
    longitud = len(notas)
    return suma / longitud

# Promedio

print(
    list(map(lambda estudiante: {
    "name" : estudiante["name"], 
    "media": media(estudiante["notas"])}, estudiantes)
         )
    )

# Los mejores


print(
    list(
        map(lambda estudiante: 
            estudiante["name"], 
            filter(lambda estudiante: media(estudiante["notas"]) >= 9, estudiantes)
            )
         )
    )

# Ordenar por mas joven

print(sorted(estudiantes, key=lambda estudiante: datetime.strptime(
    estudiante["birthdate"], "%d-%m-%Y"), reverse=True))

# Mayor calificación

print(max(map(lambda estudiante: max(estudiante["notas"]), estudiantes)))

