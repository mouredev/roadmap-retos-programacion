# EJERCICIO:


"""
    Entiende el concepto de recursividad creando una función recursiva que imprima
    números del 100 al 0.
"""


def recursividad(n):
    if n >= 0:
        print(n)
        recursividad(n - 1)


recursividad(100)


"""
    Calcular el factorial de un número concreto (la función recibe ese número).
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

"""
    Calcular el valor de un elemento concreto (según su posición) en la 
    sucesión de Fibonacci (la función recibe la posición).
 """


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(3))
