# EJERCICIO:
# Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0."""


def recursive_function(n=100):
    if n < 0:
        return
    else:
        print(n, end=' ')
        recursive_function(n - 1)


""" DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


recursive_function()
fac = int(input('\nEnter a number to calculate the factorial: '))
print(f'The factorial of {fac} is:', factorial(fac))
fib = int(input('Enter a number to calculate fibonacci: '))
print(f'The fibonacci of {fib} is:', fibonacci(fib))

