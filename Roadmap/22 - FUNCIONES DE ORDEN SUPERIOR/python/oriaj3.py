"""
22 - FUNCIONES DE ORDEN SUPERIOR
Autor de la solución: Oriaj3

Teoría:
Las funciones de orden superior son funciones que toman una o más funciones como argumentos
y/o devuelven una función como resultado. En Python, las funciones de orden superior se
pueden utilizar para crear funciones más flexibles y reutilizables.

Las funciones de orden superior se utilizan para abstraer la lógica de un programa y
hacer que sea más fácil de entender y mantener. También se utilizan para crear funciones
más genéricas y reutilizables.

Las funciones de orden superior se utilizan en muchos lenguajes de programación, como
JavaScript, Java, C++ y Python. En Python, las funciones de orden superior se pueden
implementar utilizando funciones o clases.

Un ejemplo de función de orden superior es la función map(), que toma una función y una
secuencia como argumentos y aplica la función a cada elemento de la secuencia.

Ejemplo de función de orden superior:
def cuadrado(x):
    return x * x

numeros = [1, 2, 3, 4, 5]
cuadrados = map(cuadrado, numeros)
print(list(cuadrados))

"""

"""
```
/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
"""
# Ejemplo de función de orden superior:
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def operar(x, y, operacion):
    return operacion(x, y)

resultado = operar(5, 3, sumar)
print(resultado)

resultado = operar(5, 3, restar)
print(resultado)

# Ejemplo con map():
def cuadrado(x):
    return x * x

numeros = [1, 2, 3, 4, 5]

cuadrados = map(cuadrado, numeros)
print(list(cuadrados))

# Ejemplo con filter():
def es_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5]
pares = filter(es_par, numeros)
print(list(pares))

# Ejemplo con lambda:
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x + x, numeros)
print(list(cuadrados))

# Retorna una función:

def aplicar_multiplicador(n: int):
    def multiplicar(x: int):
        return x * n
    return multiplicar

multiplicar = aplicar_multiplicador(2)

print(multiplicar(5))
print(aplicar_multiplicador(3)(2))


"""
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
 */
```
"""
from datetime import datetime
from math import e

# Ejemplo con funciones de orden superior y listas de estudiantes:
lista_estudiantes = [
    {"name": "Juan", "birthdate": "2000-01-01", "grades": [8, 9, 7, 10]}, 
    {"name": "Maria", "birthdate": "2001-02-03", "grades": [9, 9, 9, 9]},
    {"name": "Pedro", "birthdate": "1999-03-04", "grades": [7, 8, 6, 9]},
    {"name": "Ana", "birthdate": "2002-04-05", "grades": [6, 7, 5, 8]},
    {"name": "Luis", "birthdate": "1998-05-06", "grades": [5, 6, 4, 7]},
    {"name": "Elena", "birthdate": "2003-06-07", "grades": [4, 5, 3, 6]}
]

# Promedio calificaciones:
def medias(estudiante):
    notas = estudiante["grades"]
    return [estudiante["name"], sum(notas)/len(notas)]

medias_estudiantes = list(map(medias, lista_estudiantes))
print(medias_estudiantes)

#Mejores
mejores_estudiantes = list(sorted(medias_estudiantes, key=lambda x: x[1], reverse=True))
alfabeticos_estudiantes = list(sorted(medias_estudiantes, key=lambda x: x[0]))

print(mejores_estudiantes)
print(alfabeticos_estudiantes)

#Edad
def convertir_a_datetime(estudiante):
    fecha_str = estudiante["birthdate"]
    return datetime.strptime(fecha_str, "%Y-%m-%d")

estudiantes_ordenados = sorted(lista_estudiantes, key=convertir_a_datetime, reverse=True)

print(estudiantes_ordenados)

#Obtiene la nota mayor de todos los estudiantes
def nota_mayor(estudiante):
    return [estudiante["name"], max(estudiante["grades"])]

mejores_notas = list(map(nota_mayor, lista_estudiantes))
mejor_nota = max(mejores_notas, key=lambda x: x[1])

print(mejor_nota)


### Correción de la solución MoureDev

lista_estudiantes = [
    {"name": "Juan", "birthdate": "2000-01-01", "grades": [8, 9, 7, 10]}, 
    {"name": "Maria", "birthdate": "2001-02-03", "grades": [9, 9, 9, 9]},
    {"name": "Pedro", "birthdate": "1999-03-04", "grades": [7, 8, 6, 9]},
    {"name": "Ana", "birthdate": "2002-04-05", "grades": [6, 7, 5, 8]},
    {"name": "Luis", "birthdate": "1998-05-06", "grades": [5, 6, 4, 7]},
    {"name": "Elena", "birthdate": "2003-06-07", "grades": [4, 5, 3, 6]}
]

def media(grades):
    return sum(grades) / len(grades)

# Promedio calificaciones
print(
    list(
        map(
            lambda estudiante:
                {
                    "name": estudiante["name"],
                    "grades": media(estudiante["grades"])
                }, lista_estudiantes
        )
    )
)

#Mejores"
print(
    list(
        map(
            lambda estudiante:
                    estudiante["name"],
                    filter(lambda estudiante:
                            media(estudiante["grades"])>=9, 
                        lista_estudiantes)
        )
    )
)

#Fecha de nacimiento ordenada
print(
    sorted( 
        lista_estudiantes, 
        key=lambda student: 
            datetime.strptime(
            student["birthdate"], "%Y-%m-%d"), 
        reverse=True
        )
)