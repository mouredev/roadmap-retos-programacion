
"""
 * EJERCICIO:
  Entiende el concepto de recursividad creando una función recursiva que imprima
  números del 100 al 0.
"""


def countdown(n: int):
    if n >= 0:
        print(n)
        countdown(n -1)

countdown(100)


"""
 * DIFICULTAD EXTRA (opcional):
   Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
    sucesión de Fibonacci (la función recibe la posición).
"""

def factorial(n: int) -> int:
    if n < 0:
        print ("Los numeros negativos no vale")
        return 0
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print (factorial(7))

def fibonacci(n: int) -> int:
    if n <= 0:
        print ("La posicion debe ser mayor a 0")
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n -2)

print (fibonacci(7))