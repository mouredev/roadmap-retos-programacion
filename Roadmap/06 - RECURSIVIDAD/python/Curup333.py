"""
Ejercicio
"""


def count_down(number: int):
    if number >= 0:
        print(number)
        count_down(number - 1)


count_down(100)

"""
Extra
"""


def factorial(number: int) -> int:
    if number < 0:
        print("El número no puede ser negativo")
        return 0
    elif number == 0:
        return 1

    return number * factorial(number - 1)


print(factorial(5))


def fibonacci(number: int) -> int:
    if number <= 0:
        print("La posicion tiene que ser mayor a 0")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(10))
