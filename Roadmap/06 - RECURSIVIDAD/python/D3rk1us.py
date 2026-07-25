"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

# Función recursiva

def recurFuncion(num):

    if num == 0:
        return num
    else:
        print(num)
        return recurFuncion(num - 1)

print(recurFuncion(100))


# /////////////////////////////////////////////////  DIFICULTAD EXTRA  /////////////////////////////////////////////////

# Factorial
def factorial(num):

    if num == 1:
        return num
    else:
        return num * factorial(num - 1)

print(factorial(5))


# Posición Fibonacci

def fibonacci(posicion):

    if posicion == 0:
        return 0

    elif posicion == 1:
        return 1

    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

print(fibonacci(10))