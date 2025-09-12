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

def cuenta_atras(n):
    if n < 0:
        return None
    cuenta_atras(n - 1)
    print(n)

#cuenta_atras(100)

def factorial(num):
    if num <= 0:
        return 1
    return factorial(num - 1) * num
    
#print(factorial(10))

def fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
#print(fibonacci(11))
