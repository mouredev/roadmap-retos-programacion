""" Orden superior """

from datetime import datetime
from functools import reduce


def apply_func(func, x):
    return func(x)


print(apply_func(len, "Lucas"))


def apply_multiplier(n):
    def multiplier(x):
        return x * n

    return multiplier


multiplier = apply_multiplier(2)

print(multiplier)
print(multiplier(5))

# Funciones del sistema

# MAP
numeros = [2, 54, 8, 79, 454, 6]
mapped_numeros = map(lambda n: n * 2, numeros)
print(mapped_numeros)
print(list(mapped_numeros))

# FILTER
filtered_numeros = filter(lambda x: x % 2 == 0, numeros)
print(filtered_numeros)
print(list(filtered_numeros))

# SORTED
sorted_numeros = sorted(numeros)
sorted_numeros_2 = sorted(numeros, reverse=True)
sorted_numeros_3 = sorted(numeros, key=lambda x: x % 2 == 0)
print(sorted_numeros)
print(sorted_numeros_2)
print(sorted_numeros_3)

# REDUCE
nombre = ["L", "U", "C", "A", "S"]
concated_nombre = reduce(lambda x, y: x + y, nombre)
added_numeros = reduce(lambda x, y: x + y, numeros)
print(added_numeros)
print(concated_nombre)


# EXTRA

estudiantes = [
    {"nombre": "Martin", "fecha_nac": "15-06-2000", "notas": [7, 8, 6, 9.5, 9.9, 3]},
    {"nombre": "Lucas", "fecha_nac": "10-02-1997", "notas": [9, 8, 8, 9.5, 10, 9.9]},
    {"nombre": "Marta", "fecha_nac": "20-04-1998", "notas": [5, 6, 7, 9.5, 5, 8]},
]


# PROMEDIOS
def promedio(notas: list):
    return sum(notas) / len(notas)


promedios = list(
    map(
        lambda x: {"nombre": x["nombre"], "promedio": promedio(x["notas"])}, estudiantes
    )
)
print(promedios)


# MEJORES ESTUDIANTES
mejores_estudiantes = list(filter(lambda x: x["promedio"] >= 9.0, promedios))
print(mejores_estudiantes)

# ORDENACION POR FECHA DE NACIMIENTO
estudiantes_ordenados = sorted(
    estudiantes,
    key=lambda x: datetime.strptime(x["fecha_nac"], "%d-%m-%Y"),
    reverse=True,
)
print(estudiantes_ordenados)

# CALIFICACION MAS ALTA

calificacion_mas_alta = sorted(
    list(
        map(
            lambda x: {"nombre": x["nombre"], "nota_max": max(x["notas"])},
            estudiantes,
        )
    ),
    key=lambda x: x["nota_max"],
    reverse=True,
)[0]

print(calificacion_mas_alta)
