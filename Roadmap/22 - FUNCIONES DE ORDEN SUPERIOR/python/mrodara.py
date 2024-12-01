### FUNCIONES DE ORDEN SUPERIOR EN PYTHON

'''
Una función de orden superior es aquella que:
 Acepta una función como argumento.
 Devuelve otra función como resultado.
 O ambas cosas.
'''

# Ejemplo de función que acepta otra como argumento:
def calculator(x: float, y: float, operation) -> float:
    return operation(x, y)

def sum(a: float, b: float) -> float:
    return a + b

def product(a: float, b: float) -> float:
    return a * b

print(calculator(10,20, sum)) # Salida 30
print(calculator(10,20, product)) # Salida 200

# Ejemplo devolviendo otra función como resultado (lambda):
def new_calculator(operation):
    if operation.lower() == "sum":
        return lambda a, b: a + b
    elif operation.lower() == "product":
        return lambda a, b: a * b
    else:
        return lambda a, b: None

my_sum = new_calculator("sum")
my_product = new_calculator("product")

print(my_sum(5,5)) # Salida 10
print(my_product(5,5)) # Salida 25

# Python ofrece varias funciones de orden superior predefinidas, como map, filter, y reduce.

my_list = [i for i in range(1,11)]

square = map(lambda x: x**2, my_list)
print(list(square))

pairs = filter(lambda x: x%2 == 0, my_list)

print(list(pairs))

# Para reduce necesitamos importar functools
from functools import reduce

sum = reduce(lambda x, y: x + y, my_list)
print(sum) # Salida 55

### EJERCICIO EXTRA
students = [
    {
        "name": "Manuel Rodriguez",
        "birth_date": "2002-05-14",
        "grades": [8.5, 7.0, 9.0, 6.5]
    },
    {
        "name": "Lucia Perez",
        "birth_date": "2003-11-22",
        "grades": [7.5, 9.0, 8.0, 9.5]
    },
    {
        "name": "Pedro Sanchez",
        "birth_date": "2001-08-05",
        "grades": [6.0, 5.5, 7.0, 6.5]
    },
    {
        "name": "Ana Fernandez",
        "birth_date": "2004-01-30",
        "grades": [9.0, 8.5, 9.5, 10.0]
    },
    {
        "name": "Carlos Garcia",
        "birth_date": "2002-07-19",
        "grades": [7.0, 7.5, 6.0, 8.0]
    }
]

# Promedio de calificaciones:
def analysis(iterable: list, operation):
    return operation(iterable)

def avg(iterable: list) ->list:
    
    avg_students = []
    
    for element in iterable:
        avg = 0
        for grade in element["grades"]:
            avg += grade
        avg /= len(element["grades"])
        
        avg_students.append({
            "name": element["name"],
            "avg": avg
        })
        
    return avg_students

avg_students = analysis(students, avg)

print(list(avg_students))

# Aprovechamos la lista avg_students para obtener los mejores estudiantes, en este caso usaremos filter
best_students = filter(lambda x: x['avg'] >=9 and x['avg']<=10, avg_students)
print(list(best_students))

# Lista de estudiantes ordenada por fecha de nacimiento
students_by_birthday = sorted(students, key=lambda p: p['birth_date'])
print(list(students_by_birthday))

# Obtención de la nota más alta de entre todas las obtenidas por los estudiantes
max_grade = reduce(lambda x,y: max(x,y), [grade for student in students for grade in student["grades"]])
print(max_grade)

### FIN EJERCICIO EXTRA


### FIN FUNCIONES DE ORDEN SUPERIOR EN PYTHON
