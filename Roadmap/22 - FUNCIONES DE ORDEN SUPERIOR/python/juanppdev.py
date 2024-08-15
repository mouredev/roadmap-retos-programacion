"""
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
"""

def aplicar_funcion(func, valor):
    return func(valor)

def cuadrado(x):
    return x * x

resultado = aplicar_funcion(cuadrado, 5)
print(resultado)  # Salida: 25


def crear_multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

multiplicar_por_3 = crear_multiplicador(3)
print(multiplicar_por_3(10))  # Salida: 30

from functools import reduce

# `map` aplica una función a cada elemento de una lista
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(cuadrado, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

# `filter` filtra elementos de una lista según una condición
def es_par(x):
    return x % 2 == 0

pares = list(filter(es_par, numeros))
print(pares)  # Salida: [2, 4]

# `reduce` aplica una función acumulativa a los elementos de una lista
def sumar(x, y):
    return x + y

suma_total = reduce(sumar, numeros)
print(suma_total)  # Salida: 15


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

from datetime import datetime

# Lista de estudiantes
estudiantes = [
    {"nombre": "Ana", "fecha_nacimiento": "2005-05-14", "calificaciones": [8.5, 9.0, 7.5]},
    {"nombre": "Luis", "fecha_nacimiento": "2004-08-22", "calificaciones": [9.5, 9.0, 9.5]},
    {"nombre": "Carlos", "fecha_nacimiento": "2006-01-30", "calificaciones": [6.0, 7.0, 8.0]},
    {"nombre": "Marta", "fecha_nacimiento": "2003-12-10", "calificaciones": [9.0, 9.5, 10.0]}
]

# Promedio calificaciones
promedios = list(map(lambda est: {"nombre": est["nombre"], "promedio": sum(est["calificaciones"]) / len(est["calificaciones"])}, estudiantes))
print("Promedio calificaciones:", promedios)

# Mejores estudiantes
mejores_estudiantes = list(filter(lambda est: sum(est["calificaciones"]) / len(est["calificaciones"]) >= 9, estudiantes))
mejores_estudiantes_nombres = list(map(lambda est: est["nombre"], mejores_estudiantes))
print("Mejores estudiantes:", mejores_estudiantes_nombres)

# Nacimiento (ordenado desde el más joven)
estudiantes_ordenados = sorted(estudiantes, key=lambda est: datetime.strptime(est["fecha_nacimiento"], "%Y-%m-%d"), reverse=True)
print("Estudiantes ordenados por fecha de nacimiento:", list(map(lambda est: est["nombre"], estudiantes_ordenados)))

# Mayor calificación
mayor_calificacion = max(map(lambda est: max(est["calificaciones"]), estudiantes))
print("Mayor calificación:", mayor_calificacion)
