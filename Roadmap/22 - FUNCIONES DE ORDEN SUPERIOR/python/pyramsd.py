from datetime import datetime
from functools import reduce
'''
Las funciones de orden superior son funciones que cumplen con al menos
una de las siguientes características:

1. Reciben una o más funciones como argumentos.
2. Devuelven una función como resultado.
'''

# ejemplo 1
def aplicar_func_sumar(funcion, valor1, valor2):
    return funcion(valor1, valor2)
def sumar(x, y):
    return x + y
resultado = aplicar_func_sumar(sumar, 5, 8)
print(resultado)


# ejemplo 2
def al_cuadrado():
    def multiplicador(z):
        return z * z
    return multiplicador
d = al_cuadrado()
print(d(4))


# ejemplo 3
nums = [1,2,3,4,5]
resultados = list(map(lambda x: x ** 3, nums))
print(list(resultados))


# ejemplo 4
diccionarios = [{'nombre': 'Ana', 'edad': 25}, {'nombre': 'Juan', 'edad': 22}, {'nombre': 'Luis', 'edad': 30}]
diccionarios.sort(key=lambda x: x['edad'])
print(diccionarios)  


'''
EXTRA
'''
Estudiantes = [
    {"nombre": "Sergio", "nacimiento":"12-07-2005", "calificaciones": [8.0, 10.0, 5.0, 7.0]},
    {"nombre": "Javier", "nacimiento":"10-05-2003", "calificaciones": [5.0, 10.0, 4.0, 6.0]},
    {"nombre": "Maria", "nacimiento":"07-05-2000", "calificaciones": [10.0, 10.0, 8.0, 9.0]},
    {"nombre": "Julia", "nacimiento":"20-01-2002", "calificaciones": [5.0, 4.0, 2.0, 10.0]},
    {"nombre": "Julian", "nacimiento": "01-01-2001", "calificaciones": [10.0, 8.0, 10.0, 10.0]}
]

def promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

promedios = list(map(
    lambda estudiante: [estudiante['nombre'], promedio(estudiante['calificaciones'])], Estudiantes
))

for estudiante in promedios:
    print(f"{estudiante[0]}: {estudiante[1]}")


tops = list(filter(lambda estudiante: promedio(estudiante['calificaciones']) >= 9.0, Estudiantes))
top_names = list(map(lambda estudiante: estudiante['nombre'], tops))
print(top_names)


def dates(date_str):
    return datetime.strptime(date_str, "%d-%m-%Y")

sorted_students_by_age = sorted(Estudiantes, key=lambda estudiante: dates(estudiante["nacimiento"]), reverse=True)

for student in sorted_students_by_age:
    print(f"{student['nombre']} - {student['nacimiento']}")

mayor_calificacion = max(Estudiantes, key=lambda estudiante: promedio(estudiante['calificaciones']))
print(f"{mayor_calificacion['nombre']} - {sum(mayor_calificacion['calificaciones']) / len(mayor_calificacion['calificaciones'])}")
