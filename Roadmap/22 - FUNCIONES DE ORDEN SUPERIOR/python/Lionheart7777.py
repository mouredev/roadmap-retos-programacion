from functools import reduce
from datetime import datetime
#Ejercicio

def apply_func(func, x):
    return func(x)
print(apply_func(len, "Ricardo"))

#Retorno de función

def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = apply_multiplier(2)

print(double(5))
print(apply_multiplier(3)(4))

triple = apply_multiplier(3)   # triple es una función
resultado = triple(4)          # llamas esa función con 4
print(resultado)               # 12

def apply_power(n):
    def power(x):
        return x ** n
    return power

potencia = apply_power(3)
result = potencia(5)
print(result)
print(apply_power(3)(5))

# SISTEMA
numbers = [1, 3, 4, 2, 5]

# map()
double_number = list(map(lambda x: x *2, numbers))
print(double_number)

def apply_double(n):
    return n * 2
print(list(map(apply_double, numbers)))

# filter()

def is_two(n):
    return n == 2
print(list(filter(is_two, numbers)))
print(list(filter(lambda n: n == 2, numbers)))

def is_even(n):
    return n % 2 == 0
print(list(filter(is_even, numbers)))
print(list(filter(lambda n: n % 2 == 0, numbers)))

# sorted()
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

# reduce()

def sumar(x, y):
    return x + y
print(reduce(sumar, numbers))

print(reduce(lambda x, y: x + y, numbers))

# TAREA
students = [
    {"name" : "Rick","birthdate" : "27-02-1969", "grades" : []},
    {"name" : "Moure","birthdate" : "04-08-1995", "grades" : [1, 9.5, 2, 4]},
    {"name" : "mourdev","birthdate" : "15-12-2000", "grades" : [4, 6.5, 5, 2]},
    {"name" : "SuperRick","birthdate" : "03-09-1996", "grades" : [10, 9, 9.7, 9.9]}
]

def average(grades):
    if not grades:
        return 0
    return sum(grades)/len(grades)

print(list(map(lambda student: {"nombre": student["name"], "notas": student["grades"]}, students)))
print(list(map(lambda student: {"nombre": student["name"], "promedio": average(student["grades"])}, students)))

print(list(map(
    lambda student: {
        "nombre": student["name"],
        "promedio": (lambda grades: sum(grades) / len(grades) if grades else 0)(student["grades"])
    },
    students
)))

print(list(map(
    lambda student: {
        "nombre": student["name"],
        "promedio": sum(student["grades"]) / len(student["grades"]) if student["grades"] else 0
    },
    students
)))

# estudiantes con mayor promedio
print(
    list(
        map(lambda student: 
            student["name"], 
            filter(lambda student: average(student["grades"]) >= 9, students)
            )
        )
    )

# Fecha de nacimiento de estudiantes en orden

print(sorted(students, key=lambda student: datetime.strptime(student["birthdate"], "%d-%m-%Y"), reverse=True))

# Calificación más alta entre todos los alumnos

print(max(map(lambda student: max(student["grades"], default=0), students)))
    

