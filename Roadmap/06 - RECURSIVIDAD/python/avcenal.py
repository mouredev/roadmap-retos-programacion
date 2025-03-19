"""
* EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
"""

def recursive_100(number):
    if number == 0:
        print (0)
        return 0
    else:
        print(number)
        return number- recursive_100(number-1)

recursive_100(100)

"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)
print(factorial(5))

def fibonacci_pos(position):
    if position == 2 or position == 1:
        return 1
    else:
        return fibonacci_pos(position-1) + fibonacci_pos(position-2)
    
print(fibonacci_pos(10))

