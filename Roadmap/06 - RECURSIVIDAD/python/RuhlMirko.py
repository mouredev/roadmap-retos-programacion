def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)


countdown(100)

print("\nDificultad extra:")


def factorial(numero: int):
    if numero < 0:
        return 0
    elif numero == 0:
        return 1

    return numero * factorial(numero - 1)


def fibonacci(posicion: int) -> int:
    if posicion <= 0:
        return 0
    elif posicion == 1:
        return 0
    elif posicion == 2:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)


print(factorial(6))
print(fibonacci(10))
