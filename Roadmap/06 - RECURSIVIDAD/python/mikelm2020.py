# Recursividad
# Crea una función recursiva que imprima números del 100 al 0


def numbers(number: int = 100):
    if number >= 0:
        print(number)
        numbers(number - 1)


# Dificultad extra
# Utiliza el concepto de recursividad para:
# Calcular el factorial de un número concreto (la funcion recibe ese número)


def factorial(number: int):
    if number == 1:
        return 1

    if number >= 2:
        return number * factorial(number - 1)


# Calcular el valor de un elemento concreto (según su posición) en la
# sucesión de Fibonacci (la función recibe la posición).


def fibonacci(position: int):
    if position == 0:
        return 0
    if position == 1:
        return 1
    if position >= 2:
        return fibonacci(position - 2) + fibonacci(position - 1)


if __name__ == "__main__":
    # numbers()
    print(factorial(5))
    print(fibonacci(15))
