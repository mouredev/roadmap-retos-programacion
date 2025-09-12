def print_sep(title: str = None) -> None:
    sep = "-"
    print_var = sep * 8 + title + sep * 8 if title else sep * 16
    print(print_var)


"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
"""


def my_function(n: int) -> None:
    if n == 0:
        print(0)
    else:
        print(n)
        my_function(n - 1)


print_sep("Ejercicio")

my_function(100)


"""
* DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""


# Factorial de un número
def factorial(n: int) -> int:
    if n < 0:
        print("Número no válido")
        return 0
    elif n == 0:
        return 1
    return n * factorial(n - 1)


print_sep("Factorial")

print(factorial(9))


# Calcular valor de elemento en la sucesión de fibonacci


def fibonacci(position: int) -> int:
    """
    Esta función tiene complejidad algorítmica de O(2^n).
    Es decir que es muy ineficiente para valores grandes de position
    """
    if position <= 0:
        print("Número no válido")
        return 0
    elif position <= 2:
        return position - 1

    return fibonacci(position - 1) + fibonacci(position - 2)


print_sep("Fibonacci")

print(fibonacci(15))

print_sep()
