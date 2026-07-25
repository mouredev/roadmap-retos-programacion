"""* EJERCICIO:
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
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales)."""

from functools import reduce
import datetime

# Pueden recibir funciones como parámetros
def funcSuperior(funcion, param): # Recibe una función y un parámetro
    return funcion(param) 

longitud = funcSuperior(len, 'Juan') # Se pasa la función len, propia de Python, y una cadena, para que devuelva la longitud de dicha cadena.
print(f'La longitud del parámetro es -> {longitud}')

# Pueden devolver funciones como resultado
def aplicarOperacion(operando1, operador):
    def operacion(operando2):
        if operador == '+':
            return operando1 + operando2
        elif operador == '-':
            return operando1 - operando2
        elif operador == '*':
            return operando1 * operando2
        elif operador == '/':
            return operando1 / operando2
        else:
            return 'Operador no soportado o incorrecto'
    return(operacion) # Devuelve la función operacion

# Aplicar la operación 
resultado = aplicarOperacion(3,'+') # resultado va a contener una función
print(resultado(4)) # A la función retornada, le envío el argumento restante para completar la operación
print(aplicarOperacion(4, '+')(5)) # Otra forma de llamarla

# Hay funciones de orden superior, propias de Python
# map(): Aplica una función a cada elemento de una lista
letras = ['A', 'B', 'H', 'Y', 'J', 'P', 'R']
def ordenar(letras):
    return sorted(letras)

ordenacion = map(ordenar, letras)
print(list(ordenacion))

# filter(): Aplica una función a cada elemento de una lista y devuelve los elementos que cumplen
def mayorQue5(num):
    return num > 5

print(list(filter(mayorQue5, [6,4,8,14])))

# sorted() Ordena una lista
print(sorted(letras))
print(sorted(letras, reverse=True)) # Ordena en sentido inverso
print(sorted([6,4,8,14], key=lambda n: -n)) # Aquí se usa una lambda: Funciones anónimas a las que se le envía la lista, en este caso, y se recibe la lista ordenada al revés

# reduce(): Aplica una función a cada elemento de una lista y devuelve el resultado final. Tenemos que importarla de functools
def sumar(x, y):
    return x + y

print(reduce(sumar, [6,4,8,14])) # Devuelve la suma de los elementos de toda la lista (6 + 4 + 8 +14) = 32

# EXTRA
estudiantes = [
    {'nombre': 'Juan', 'fecha_nacimiento':'01-05-1968', 'notas':[7,8,9]},
    {'nombre': 'Mónica', 'fecha_nacimiento':'04-05-1968', 'notas':[8,7,9]},
    {'nombre': 'Luis', 'fecha_nacimiento':'06-07-1999', 'notas':[6,7,8]}
    ]
# Promedio calificaciones: Obtiene una lista de estudiantes por nombre y promedio de sus calificaciones.
def media(notas):
    return sum(notas) / len(notas)

print(list(map(lambda estudiante:{'nombre':estudiante['nombre'], 
                                'media':media(estudiante['notas'])}, estudiantes)))
#  Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes que tienen calificaciones con un 9 o más de promedio.

print(list(map(lambda estudiante: 
    estudiante['nombre'], filter(lambda estudiante: media(estudiante['notas']) >= 9, estudiantes))))

# Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
print(list(sorted(estudiantes,  key=lambda estudiante: datetime.datetime.strptime(estudiante['fecha_nacimiento'], '%d-%m-%Y'), reverse = True)))

# Mayor calificación: Obtiene la calificación más alta de entre todas las de los alumnos.
print(max(map(lambda estudiante: max(estudiante['notas']), estudiantes)))