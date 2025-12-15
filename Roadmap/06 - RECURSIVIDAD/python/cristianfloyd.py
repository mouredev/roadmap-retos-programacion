"""  
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 * """
 
def imprimir_numeros(n=100):
    if n < 0:
        return
    print(n)
    imprimir_numeros(n - 1)

# imprimir_numeros(10)

""" 
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */ """

 # Factorial

"""
 El factorial (representado por un signo de exclamación "!") es una operación 
 matemática que consiste en multiplicar un número entero positivo por todos 
 los enteros positivos menores que él hasta llegar a 1.

 Definición: El factorial de un número entero positivo n (escrito n!) 
 es el producto de todos los enteros positivos desde 1 hasta n.
 Ejemplos: 5! = 5 × 4 × 3 × 2 × 1 = 120
"""

def factorial(n: int) -> int:
    if n < 0:
        print("Los números negativos no son válidos")
        return 0
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Introduce un número para calcular su factorial: "))
print(f"El factorial de {n} es {factorial(n)}")

# fibonacci
def fibonacci(n: int) -> int:
    if n <= 0:
        print("Los números negativos no son válidos")
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Introduce la posición para calcular el valor en la sucesión de Fibonacci: "))
print(f"El valor en la posición {n} de la sucesión de Fibonacci es {fibonacci(n)}")