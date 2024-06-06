'''
/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
'''

### Ejercicio intro

def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number-1)

countdown(100)

### Extra
# Factorial
def factorial(number: int) -> int:
    if number < 0:
        print("Los números negativos no son válidos.")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number-1)

n = 4
print(f'Factorial: {n} = {factorial(n)}')

def fibonacci(number: int) -> int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)

n = 10
print(f'Fibonacci: {n} = {fibonacci(n)}')