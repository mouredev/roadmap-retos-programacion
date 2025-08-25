""""
La recursividad en Python (y en otros lenguajes) es una técnica de programación donde una función se llama a sí misma para resolver un problema.

¿Para qué se usa?
Se usa generalmente para resolver problemas que pueden dividirse en subproblemas más pequeños del mismo tipo, como:

Factoriales

Fibonacci

Búsqueda en estructuras como árboles

Problemas como las torres de Hanoi

hay que evaluar cuando tiene sentido utilizar recursividad y cuando es necesario utilizar un bucle 

"""

#Ejercicio 

#def hello ():
#    hello ()



#hello ()

def countdown (number: int):
    if number >= 0: 
        print(number)
        countdown (number - 1)

countdown  (100)


"""
Extra

"""
def factorial (number: int) -> int:
    if number < 0:
        print ("Los números negativos no son  validos")
        return 0 
    elif number == 0:
        return 1
    else:
        return number * factorial (number -1) 

print(factorial (5))


"""
🔁 CUÁNDO USAR BUCLES (for, while)
Usá bucles cuando:

✅ El número de repeticiones es conocido o fácilmente controlable.
✅ No necesitás dividir el problema en subproblemas más pequeños.
✅ Querés mantener eficiencia en memoria y velocidad.
✅ El lenguaje (como Python) no optimiza bien la recursividad.

🔹 Ejemplos:

Recorrer listas, diccionarios, archivos, etc.

Ejecutar una acción hasta que se cumpla una condición.

Contar, filtrar, sumar elementos.
"""
"""
🔁 CUÁNDO USAR RECURSIVIDAD
Usá recursividad cuando:

✅ El problema puede dividirse naturalmente en subproblemas del mismo tipo.
✅ La estructura del problema es jerárquica o en forma de árbol (como árboles binarios, carpetas, etc).
✅ Es más intuitivo o limpio usar recursividad (aunque menos eficiente).
✅ No te importa tanto la eficiencia o trabajás con un caso pequeño.

🔹 Ejemplos:

Factorial de un número.

Sucesión de Fibonacci.

Búsqueda en estructuras recursivas (como árboles o grafos).

Recorrer carpetas o estructuras anidadas.

"""


def fibonacci (number: int) -> int: 
    if number <= 0:
        print ("Los posición tiene que ser mayor que cero")
        return 0
    elif number == 1:
        return  0
    elif number == 2:
        return 1
    else: 
        return fibonacci (number - 1) + fibonacci(number - 2)

print (fibonacci (4))