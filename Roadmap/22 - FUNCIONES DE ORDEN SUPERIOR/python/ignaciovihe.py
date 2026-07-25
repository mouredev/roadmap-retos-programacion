"""
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
"""

#Pasar una funcion como argumento.
def aplicar_funcion(f, valor):
    return f(valor)

def cuadrado(l):
    if isinstance(l, list):
        return [e ** 2 for e in l]
    else:
        return l ** 2

resultado = aplicar_funcion(cuadrado, [1, 2, 3, 4, 5, 6, 7, 8]) #Le paso como argumento una función
print(resultado)

#Retornar una función
def multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar  # Retorna una función

triplicar = multiplicador(3)
print(triplicar(5))
print(multiplicador(3)(2))  

#Python ya tiene algunas fucciones de orden superior
#map
my_data_str = ["1","2","3","4","5"]
print(my_data_str)
my_data_int = list(map(int,my_data_str))
print(my_data_int)


#filter
def is_even(number):
    return number % 2 == 0

even = list(filter(is_even,my_data_int))
print(even)


#reduce
from functools import reduce

numeros = [1, 2, 3, 4, 5]
suma_total = reduce(lambda x, y: x + y, numeros)
print(suma_total)

#sorted con funcion clave
nombres = ["Ana", "Juan", "Pedro", "Luis"]  # Ordena por longitud de nombre
print(sorted(nombres, key=len))
print(sorted(nombres, reverse=True))
print(sorted(nombres, key=lambda x: x[::-1]))# Ordena los nombres segun su version invertida. Pero imprime los elementos normal.


""" * DIFICULTAD EXTRA (opcional):
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
import random

students = [
    {"name": "Ignacio", "birth_date":datetime(1985,2,23).date(), "grades": [round(random.uniform(0,10),2) for i in range(4)] },
    {"name": "Miguel", "birth_date":datetime(1985,2,24).date(), "grades": [round(random.uniform(0,10),2) for i in range(4)] },
    {"name": "Lorena", "birth_date":datetime(1984,1,25).date(), "grades": [round(random.uniform(0,10),2) for i in range(4)] },
    {"name": "Francisca", "birth_date":datetime(2001,12,3).date(), "grades": [round(random.uniform(0,10),2) for i in range(4)] }
]

def analise_data(data: list, f):
    return f(data)


def average(grades):
    return round(sum(grades) / len(grades), 2)

def students_average(data):
    return list(map(lambda student: {"name": student["name"], "average": average(student["grades"])}, data))

def best_students(data):
    return list(map(lambda student: student["name"], filter(lambda student: average(student["grades"]) > 6, data)))

def order_by_date(data):
    return sorted(data, key=lambda x: x["birth_date"],reverse=True)

def best_grade(data):
    return max(list(map(lambda student: max(student["grades"]), data)))


print(analise_data(students, students_average))
print(analise_data(students, best_students))
print(analise_data(students, order_by_date))
print(analise_data(students, best_grade))