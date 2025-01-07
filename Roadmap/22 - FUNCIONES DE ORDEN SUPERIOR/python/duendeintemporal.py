#22 { Retos para Programadores } FUNCIONES DE ORDEN SUPERIOR

# Bibliography reference
#Secrets of the JavaScript Ninja (John Resig, Bear Bibeault, Josip Maras) (z-lib.org)
#Eloquent Javascript A Modern Introduction to Programming by Marijn Haverbeke (z-lib.org)
#Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)
# Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.

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
import random
from datetime import datetime

log = print

log('Retos para Programadores #22')

# Higher-order function example: power function
def powder(n):
    return lambda m: 1 if n == 0 else m * powder(n - 1)(m)

powder2 = powder(2)
log(powder2(10))  # 100

# Higher-order function to apply a function to an array
def apply_to_array(func):
    return lambda *arr: func(*arr)

def total_amount(*args):
    return sum(args)

sales = [123, 45, 67, 865, 76, 54, 3254, 23]
log(apply_to_array(total_amount)(*sales))  # 4507

# Control flow function
def unless(test, then):
    if not test:
        then()

def is_odd_num(n):
    return n % 2 != 0

# Higher-order function to add odd numbers up to n
def add_odd_nums(n):
    total = 0
    while n > 0:
        if is_odd_num(n):  # Check if n is odd
            total = add_to_total(n, total)  # Update total
        n -= 1
    return total

# Helper function to add to total
def add_to_total(n, total):
    return total + n

log(add_odd_nums(100))  # Should print 2500


# EXTRA DIFFICULTY EXERCISE

# Student class definition
class Student:
    def __init__(self, name, birthday, calification):
        self.name = name
        self.birthday = datetime.strptime(birthday, '%Y-%m-%d')
        self.calification = calification

    def get_name(self):
        return self.name

    def get_birthday(self):
        return self.birthday

    def get_calification(self):
        return self.calification

    def set_name(self, name):
        self.name = name

    def set_birthday(self, birthday):
        self.birthday = datetime.strptime(birthday, '%Y-%m-%d')

    def set_calification(self, calification):
        self.calification = calification

# List of students
students = [
    Student('Juan Rulfo', '1986-06-07', 7),
    Student('Moure Dev', '1982-03-08', 8.5),
    Student('Calvin Maker', '2000-04-02', 9.8),
    Student('Adela Jimenez', '1976-01-09', 7.9),
    Student('Crist Renegate', '2001-07-09', 5),
    Student('Gautama Buda', '0623-05-23', 9),
    Student('Niko Zen', '1983-08-08', 10)
]

# Function to get a list of students with their average grades
def students_average_list(arr):
    return sorted(
        [{'name': student.get_name(), 'average': student.get_calification()} for student in arr],
        key=lambda x: x['average'],
        reverse=True
    )

# Function to get a list of students with grades of 9 or higher
def higher_than_9_students(arr):
    return [student.get_name() for student in arr if student.get_calification() >= 9]

# Function to sort students by their birth date
def sort_students_by_birthday(arr):
    return [student.get_name() for student in sorted(arr, key=lambda student: student.get_birthday())]

# Function to find the highest grade among all students
def highest_calification(arr):
    return max(student.get_calification() for student in arr)

# Execute the functions and store the results
average_list = students_average_list(students)
best_students = higher_than_9_students(students)
sorted_students = sort_students_by_birthday(students)
highest_grade = highest_calification(students)

# Display the results in the console
log("Average grades:", average_list)
log("Best students (9 or higher):", best_students)  # Best students (9 or higher): ['Calvin Maker', 'Gautama Buda', 'Niko Zen']
log("Students sorted by birth date:", sorted_students)  # Students sorted by birth date
log("Highest grade:", highest_grade)  # Highest grade: 10

# Output Example:
"""  
Average grades: [{'name': 'Niko Zen', 'average': 10}, {'name': 'Calvin Maker', 'average': 9.8}, {'name': 'Gautama Buda', 'average': 9}, {'name': 'Moure Dev', 'average': 8.5}, {'name': 'Adela Jimenez', 'average': 7.9}, {'name': 'Juan Rulfo', 'average': 7}, {'name': 'Crist Renegate', 'average': 5}]
Best students (9 or higher): ['Calvin Maker', 'Gautama Buda', 'Niko Zen']
Students sorted by birth date: ['Gautama Buda', 'Adela Jimenez', 'Moure Dev', 'Niko Zen', 'Juan Rulfo', 'Calvin Maker', 'Crist Renegate']
Highest grade: 10

"""

