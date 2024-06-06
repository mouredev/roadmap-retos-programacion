"""
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
 */"""

def print_numbers(number: int) -> int:
    if number >= 0:
        print(number)
        return print_numbers(number-1)

print(print_numbers(100))

def factorial(number: int) -> int:
    try:
        if number <= 1:
            return number
        return number * factorial(number-1)
    except ValueError:
        print('El valor ingresado no es apropiado para el calculo')
        
print(factorial(5))

def fibonacci(number: int) -> int:
    if number <= 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(8))
    