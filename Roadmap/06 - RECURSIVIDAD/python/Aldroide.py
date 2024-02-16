# Concepto de recursividad: función que se llama así misma

def contador(number: int):
    if number >= 0:
        print(number)
        contador(number - 1)


contador(100)


"""
    Dificultad Extra
    Calcular el factorial y el fibonacci usando recursividad.
"""


def factorial(num: int) -> int:
    if num < 0:
        print("Los números negativos no tienen fibonacci")
        return 0
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(4))


def fibonacci(num: int) -> int:
    if num <= 0:
        print("La posición tiene que ser mayor que cero")
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(5))
