# 22 - FUNCIONES DE ORDEN SUPERIOR
from datetime import datetime
from functools import reduce

# Ejercicio


def operacion(x1, x2, fun):
    return fun(x1, x2)


def sumar(x1, x2):
    return x1+x2


def restar(x1, x2):
    return x1-x2


resultado = operacion(1, 2, restar)
print(resultado)

# Filter
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares)

# Map
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
cubo = list(map(lambda x: x**3, lista))
print(cubo)

# Reduce
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
sumacum = reduce(lambda a, b: a+b, lista)
print(sumacum)

# Dificultad Extra

estudiantes = [
    ("Juan", "26-02-2010", [6, 8, 9.5]),
    ("Sofia", "13-05-2010", [8.5, 9.8, 9.5]),
    ("Julia", "13-06-2010", [9, 8.5, 10]),
    ("Pedro", "16-03-2010", [6, 7, 7.5])
]


def calcular_promedio(notas):
    return round(sum(notas) / len(notas), 2)


promedio_estudiantes = [(estudiante[0], calcular_promedio(
    estudiante[2])) for estudiante in estudiantes]
print("Lista de las notas promedio de cada estudiante:")
print(promedio_estudiantes)

maximo = max([calcular_promedio(estudiante[2]) for estudiante in estudiantes])
print("Nota máxima del curso:")
print(maximo)

mejores_estudiantes = [estudiante[0] for estudiante in (
    list(filter(lambda x: x[1] >= 9, promedio_estudiantes)))]
print("Lista de los mejores estudiantes:")
print(mejores_estudiantes)


def convertir_fecha(fecha_str):
    return datetime.strptime(fecha_str, "%d-%m-%Y")


print("Lista por fecha de nacimiento de los estudiantes:")
orden = sorted(estudiantes, key=lambda x: convertir_fecha(x[1]), reverse=True)
for estudiante in orden:
    print(estudiante)
