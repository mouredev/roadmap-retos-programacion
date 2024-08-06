from datetime import datetime

### Ejercicio ###

# simple
def operation(x, fun):
  return fun(x)

def squere_root(x):
  return x**0.5

def squared(x):
  return x**2

result_1 = operation(16, squere_root)
result_2 = operation(8, squared)
print(result_1)
print(result_2)

# Otras funciones de orden superior podrian ser Filter, map, reduce...
# Ejemplo con filter
integers = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda x: x%2 == 0, integers))
print(even)


### EXTRA ###

# Datos de ejemplo de los estudiantes
students = [
    {"nombre": "Alex", "fecha_nacimiento": "2000-01-15", "calificaciones": [8.5, 9.0, 7.0]},
    {"nombre": "Carolina", "fecha_nacimiento": "1999-07-22", "calificaciones": [9.5, 9.0, 9.0]},
    {"nombre": "Gerard", "fecha_nacimiento": "2001-05-30", "calificaciones": [6.0, 7.5, 8.0]},
    {"nombre": "Sirius", "fecha_nacimiento": "2002-10-10", "calificaciones": [9.0, 9.5, 9.7]},
]

# funcion principal
def analysis(students):
  print(f"Promedios:\n{get_averages(students)}")
  print(f"Calificaciones mejores estudiantes con promedio igual o mayor a 9:\n{get_better_students(students)}")
  print(f"Alumnos ordenados de mas joven a mas mayor:\n{sort_by_date_of_birth(students)}")
  print(f"Mayor calificacion obtenida de entre todos los alumnos:\n{get_higher_qualification(students)}")

# 1. Promedio de calificaciones
def get_averages(students):
    return list(map(lambda est: {"nombre": est["nombre"], "promedio": sum(est["calificaciones"]) / len(est["calificaciones"])}, students))

def get_better_students(students):
    return list(filter(lambda est: sum(est["calificaciones"]) / len(est["calificaciones"]) >= 9, students))

def sort_by_date_of_birth(students):
    return sorted(students, key=lambda est: datetime.strptime(est["fecha_nacimiento"], "%Y-%m-%d"))

# 4. Mayor calificación
def get_higher_qualification(students):
    return max(max(est["calificaciones"]) for est in students)

results = analysis(students)
