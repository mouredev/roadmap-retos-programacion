import math 
from datetime import datetime
from functools import reduce


print("\n\n=======================================EJERCICIO=======================================\n\n")

'''
* EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
'''

def arithmetic(function, num):
    return function(num)
    
def cube_root(num):
    print(f"La raiz cubica de 125 es: {math.cbrt(num)}")

def elevate_cube(num):
    print(f"{num} elevado al cubo es: {num**3}")
    

arithmetic(cube_root, 125)
arithmetic(elevate_cube, 5)
    

print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")

'''
* DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para 
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de   sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o mas de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el mas joven.
 * - Mayor calificación: Obtiene la calificación mas alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
'''


# Lista de estudiantes
students = [
    {"name":"Rantam", "born_date":"29-05-2000", "grades":[7.2, 9.0, 8.6]},
    {"name":"Helena", "born_date":"12-02-2005", "grades":[9.8, 9.2, 8.7]},
    {"name":"Silvia", "born_date":"10-07-2003", "grades":[8.5, 8.0, 8.4]}, 
    {"name":"Jose Luis", "born_date":"22-10-2003", "grades":[7.0, 6.5, 7.4]},
    {"name":"Fernando", "born_date":"17-07-1998", "grades":[5.0, 3.8, 4.6]},
    {"name":"Brais", "born_date":"11-06-2003", "grades":[8.0, 9.4, 9.7]}
]

# Función para calcular la media
def calculate_average(grades):
    return round(sum(grades) / len(grades), 2)

# Función para calcular la nota media de los estudiantes
def get_average_grades(students, average_func):
    return list(map(lambda student: {"name": student["name"], "average_grade": average_func(student["grades"])}, students))

# Función para obtener los mejores estudiantes
def get_top_students(students, average_func, threshold=9.0):
    return list(filter(lambda student: average_func(student["grades"]) >= threshold, students))

# Función para obtener una lista de estudiantes ordenada desde el mas joven
def sort_students_by_age(students):
    return sorted(students, key=lambda student: datetime.strptime(student["born_date"], "%d-%m-%Y"), reverse=True)

# Función para obtener la calificación mas alta
def get_highest_grade(students):
    all_grades = reduce(lambda acc, student: acc + student["grades"], students, [])
    return max(all_grades)


average_grades = get_average_grades(students, calculate_average)
top_students = get_top_students(students, calculate_average)
students_sorted_by_age = sort_students_by_age(students)
highest_grade = get_highest_grade(students)


print("Promedio calificaciones:")
for student in average_grades:
    print(student)

print("\nMejores estudiantes:")
for student in top_students:
    print(student["name"], calculate_average(student["grades"]))

print("\nEstudiantes ordenados desde el mas joven:")
for student in students_sorted_by_age:
    print(student["name"], student["born_date"])

print("\nMayor calificación:", highest_grade)


