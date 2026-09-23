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

def num_print(max):
    print(max)
    max -= 1

    if max == 0:
        print(max)
    else:
        num_print(max)

print(num_print(100)); print()

# EXTRA

def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(999))
# falta comprobar que factorial(999) sea correcto y no solo los primeros casos
# factorial(1000) Recursion Error: maximum recursion depth exceeded
print()

def fibonacci(posicion):
    if posicion == 1 or posicion == 2:
        return 1
    else:
        return fibonacci(posicion - 2) + fibonacci(posicion - 1)

print(fibonacci(40))