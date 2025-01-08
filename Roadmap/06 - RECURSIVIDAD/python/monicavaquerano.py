# 06 RECURSIVIDAD
# Mónica Vaquerano
# https://monicavaquerano.dev

"""
EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 */
"""


def printNumbers(n: int):
    if n < 0:
        return
    else:
        print(n, end=" ")
        printNumbers(n - 1)


print("Recursividad\n")
print("Cuenta regresiva de 100 a 0")
printNumbers(100)
print()
"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
"""
print("\nDIFICULTAD EXTRA (opcional):\n")


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial de un número")
cinco = factorial(5)
print(f"Factorial de 5 = {cinco}")


# 1, 2, 3, 4, 5, 6
# 1, 1, 2, 3, 5, 8, ...


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("\nSecuencia Fibonacci:")
x = 6
print(f"Valor de la posición N°{x} es {fibonacci(x)}")
