"""
EJERCICIO:
funciones de orden superior
"""

# Ejemplo 1: Funciones como argumentos
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

def double(x):
    return x * 2

result_square = apply_function(square, 5)
result_double = apply_function(double, 5)

print(f"apply_function(square, 5) = {result_square}")  
print(f"apply_function(double, 5) = {result_double}")

# Ejemplo 2: Funciones que retornan otras funciones
def create_multiplier(multiplier):
    def multiplier_function(x):
        return x * multiplier
    return multiplier_function

double = create_multiplier(2)
triple = create_multiplier(3)

print(f"double(5) = {double(5)}")  # Salida: 10
print(f"triple(5) = {triple(5)}")  # Salida: 15

#Ejemplo 3: Usando map, filter y reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"map(lambda x: x ** 2, numbers) = {squared_numbers}")  

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter(lambda x: x % 2 == 0, numbers) = {even_numbers}")  

product = reduce(lambda x, y: x * y, numbers)
print(f"reduce(lambda x, y: x * y, numbers) = {product}")  


"""
Extra:
"""
from datetime import datetime
from functools import reduce

students = [
    {"name": "Ana", "dob": "2005-04-23", "grades": [8.5, 9.0, 7.5]},
    {"name": "Carlos", "dob": "2004-07-15", "grades": [9.5, 9.0, 8.5]},
    {"name": "Beatriz", "dob": "2006-01-10", "grades": [6.0, 7.5, 8.0]},
    {"name": "David", "dob": "2003-12-11", "grades": [7.0, 6.5, 6.0]},
    {"name": "Elena", "dob": "2005-10-29", "grades": [10.0, 9.5, 9.0]},
]

# 1. Promedio calificaciones
def calculate_average(grades):
    return sum(grades) / len(grades)

average_grades = list(map(lambda student: {"name": student["name"], "average": calculate_average(student["grades"])}, students))

print("Promedio de calificaciones:")
for student in average_grades:
    print(f"{student['name']}: {student['average']:.2f}")

# 2. Mejores estudiantes
top_students = list(filter(lambda student: calculate_average(student["grades"]) >= 9, students))
top_students_names = list(map(lambda student: student["name"], top_students))

print("Mejores estudiantes:")
print(top_students_names)

# 3. Nacimiento
def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

sorted_students_by_age = sorted(students, key=lambda student: parse_date(student["dob"]), reverse=True)

print("Estudiantes ordenados desde el más joven:")
for student in sorted_students_by_age:
    print(f"{student['name']} ({student['dob']})")

# 4. Mayor calificación
all_grades = reduce(lambda acc, student: acc + student["grades"], students, [])
highest_grade = max(all_grades)

print(f"La calificación más alta es: {highest_grade}")
