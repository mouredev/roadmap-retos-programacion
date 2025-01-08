""" /*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */ """


def recursive_print(start_value):
    print(start_value)
    if start_value > 0:
        recursive_print(start_value - 1)


""" recursive_print(100) """


def recursive_factorial(num: int):
    if num == 0:
        return 1
    return num * recursive_factorial(num - 1)


""" print(recursive_factorial(0))
print(recursive_factorial(1))
print(recursive_factorial(2))
print(recursive_factorial(3))
print(recursive_factorial(4))
print(recursive_factorial(5))
print(recursive_factorial(6))
print(recursive_factorial(7))
 """

def recursive_fibonacci(pos: int):
    if pos == 0 or pos == 1:
        return pos
    return recursive_fibonacci(pos - 1) + recursive_fibonacci(pos - 2)

""" print(recursive_fibonacci(6)) """