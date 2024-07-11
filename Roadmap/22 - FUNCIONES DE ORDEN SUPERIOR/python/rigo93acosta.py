'''
## 22 FUNCIONES DE ORDEN SUPERIOR
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
'''

"""
Ejercicio
"""

# Funcion con argumento
def apply_func(func, x):
    return func(x)

print(apply_func(len, "Hola mundo"))

# Retorno de funcion

def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

x = apply_multiplier(2)
print(x(5))

# Sistema
numbers = [3, 4, 1, 5, 2]

# map()
def applay_double(n):
    return n*2

print(list(map(applay_double, numbers)))

# filter()
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, numbers)))

# sorted()
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

# reduce 
from functools import reduce
def sum(x, y):
    return x + y

print(reduce(sum, numbers))

"""
Extra
"""

