""" /*
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
 */ """

from functools import reduce
from datetime import datetime

#EJERCICIO

#Función como parámetro
def funcion_orden_superior(num1, num2, funcion):
    return funcion(num1, num2)

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print(funcion_orden_superior(16, 5, suma))
print(funcion_orden_superior(16, 5, resta))
print(funcion_orden_superior(16, 5, divide))
print(funcion_orden_superior(16, 5, multiplica))

#Función como valor de retorno
def cuadrado(num):
    return num ** 2

def cubo(num):
    return num ** 3

def funcion_orden_superior(operacion):
    if operacion == "doble":
        return cuadrado
    else:
        return cubo
    
resultado = (funcion_orden_superior("doble"))
print(resultado(5))
resultado = (funcion_orden_superior("triple"))
print(resultado(5))

#Función dentro de otra función(cierre)
def suma_dos():
    dos = 2
    def suma(num):
        return num + dos
    return suma

resultado = suma_dos()
print(resultado(2))
print(resultado(7))

#Map
numeros = [1, 2, 3, 4, 5]
cadena = map(str, numeros)
print(list(cadena))

#Filter
def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

pares = filter(par, numeros)
print(list(pares))
#Usando lambda
pares = filter((lambda x: x%2 == 0), numeros)
print(list(pares))

#Reduce
def suma(num1, num2):
    return num1 + num2

total = reduce(suma, numeros)
print(total)
#Usando lambda
total = reduce((lambda x, y: x + y), numeros)
print(total)

#Sort o sorted
numeros = [2, 0.2, 52, 41, 20]
print(sorted(numeros))
print(sorted(numeros, reverse=True))


#DIFICULTAD EXTRA

estudiantes = [["Estudiante1",[8, 9.8, 9, 9.5], "2/3/1995"], 
["Estudiante2",[5, 6.5, 7, 8], "9/6/2001"],
["Estudiante3",[9, 3.2, 10, 5], "15/8/2020"],
["Estudiante4",[9.2, 3.4, 7, 9.9], "23/8/1999"],
["Estudiante5",[9.7, 9.5, 8.8, 9], "1/1/2003"],
["Estudiante6",[1.2, 4.5, 7.6, 8.9], "31/12/1980"]]

print(f"\nLista Estudiantes: {estudiantes}\n")

lista_promedio = list(map(lambda estudiante: [estudiante[0], round((reduce(lambda x,y: x+y, estudiante[1]))/len(estudiante[1]),2)], estudiantes))
print(f"Promedio calificaciones: {lista_promedio}\n")

mejores = list(map(lambda x: x[0], (filter(lambda estudiante: estudiante[1] >= 9, lista_promedio))))
print(f"Mejores estudiantes: {mejores}\n")

def ordenar_fechas(lista):
    return datetime.strptime(lista[2], "%d/%m/%Y")
estudiantes.sort(key=ordenar_fechas, reverse=True)
print(f"Estudiantes ordenados por el más joven: {estudiantes}\n")

mayor_nota = max(list(map(lambda estudiante: max(estudiante[1]), estudiantes)))
print(f"Mayor calificación: {mayor_nota}\n")
