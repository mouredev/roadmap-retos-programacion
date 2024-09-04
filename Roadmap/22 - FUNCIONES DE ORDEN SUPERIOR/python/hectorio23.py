# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

from datetime import datetime
from functools import reduce

# EJERCICIO:
# Explora el concepto de funciones de orden superior en tu lenguaje 
# creando ejemplos simples (a tu elección) que muestren su funcionamiento.
#
# DIFICULTAD EXTRA (opcional):
# Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
# lista de calificaciones), utiliza funciones de orden superior para 
# realizar las siguientes operaciones de procesamiento y análisis:
# - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
#   y promedio de sus calificaciones.
# - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
#   que tienen calificaciones con un 9 o más de promedio.
# - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
# - Mayor calificación: Obtiene la calificación más alta de entre todas las
#   de los alumnos.
# - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).

# Definimos una clase para representar a un estudiante
class Student:
    def __init__(self, name, birthdate, grades):
        self.name = name
        self.birthdate = birthdate
        self.grades = grades

# Función para calcular el promedio de una lista de calificaciones
def average(grades):
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

# Lista de estudiantes
students = [
    Student("Adán", "2004-06-28", [9.7, 10.0, 9.9]),
    Student("Andy", "2006-07-17", [9.5, 9.0, 9.0]),
    Student("Mauricer", "2004-03-15", [6.0, 7.5, 8.0]),
    Student("David", "2005-06-30", [10.0, 9.5, 9.5])
]

# Promedio de calificaciones
print("Promedio de calificaciones:")
for student in students:
    avg = average(student.grades)
    print(f"{student.name}: {avg:.2f}")

# Mejores estudiantes
print("\nMejores estudiantes (promedio >= 9):")
for student in students:
    if average(student.grades) >= 9.0:
        print(student.name)

# Ordenar estudiantes por fecha de nacimiento, de más joven a más viejo
students_sorted_by_age = sorted(students, key=lambda student: datetime.strptime(student.birthdate, "%Y-%m-%d"), reverse=True)

print("\nEstudiantes ordenados por nacimiento (de más joven a más viejo):")
for student in students_sorted_by_age:
    print(f"{student.name}: {student.birthdate}")

# Mayor calificación entre todos los estudiantes
all_grades = [grade for student in students for grade in student.grades]
highest_grade = max(all_grades)

print(f"\nMayor calificación entre todos los estudiantes: {highest_grade}")
