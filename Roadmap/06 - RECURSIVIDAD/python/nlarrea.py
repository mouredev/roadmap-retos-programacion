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


def print_number(number: int) -> None:
    print(number)

    if number == 0:
        return

    print_number(number - 1)


print_number(100)


"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""


def factorial(number: int) -> int:
    if number < 0:
        print("Number must be a positive number.")
        return -1
    elif number == 0:
        return 1

    return number * factorial(number - 1)


print("\nFactorial:")
number = 4
print(f"{number}! = {factorial(number)}")  # 24
print(f"{number + 1}! = {factorial(number + 1)}")  # 120


def fibonacci(position: int) -> int:
    if position <= 0:
        print("Only positive numbers are allowed.")
        return -1
    elif position == 1:
        return 0
    elif position == 2:
        return 1

    return fibonacci(position - 1) + fibonacci(position - 2)


print("\nFibonacci:")
print(f"The Fibonacci in position 3 is: {fibonacci(3)}")  # 1
print(f"The Fibonacci in position 7 is: {fibonacci(7)}")  # 8
