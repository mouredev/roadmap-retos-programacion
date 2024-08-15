"""
Recursividad
"""


def recursividad(number: int):
    print(number)
    if number > 0:
        recursividad(number - 1)


recursividad(100)

"""
EXTRA
"""


def factorial_recursivo(number: int) -> int:  # Calcular factorial
    if number == 1:
        return 1
    else:
        return number * factorial_recursivo(number - 1)


print(f'Respuesta Factorial recursivo: {factorial_recursivo(3)}')


def fibonacci_recursivo(number: int) -> int:
    if number <= 0:
        print('La posisción tiene que ser mayor que cero ')
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci_recursivo(number - 1) + fibonacci_recursivo(number - 2)


print(f'Resultado Secuencia fibonacci recursivo: {fibonacci_recursivo(6)}')
