"""
Funcion recursiva que va del 100 al 0
"""

def recursiva(n):
    if n == 0:
        print(n)
        
    else:
        print(n)
        recursiva(n - 1)
        

recursiva(100)

"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */

"""

print("------------------")
print("------------------")

# Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

print("------------------")
print("------------------")


# Fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n -2)
    
print(fibonacci(10))