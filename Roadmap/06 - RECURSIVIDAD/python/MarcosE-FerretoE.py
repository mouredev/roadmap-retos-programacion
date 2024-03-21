""" EJERCICIO """


def counter(value: int):
    if value == 0:
        print(value)
    else:
        print(value)
        counter(value - 1)


number = 100
counter(number)

""" DIFICULTAD EXTRA """

n = 17


def factorial(value: int):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)


print(f"The factorial of {n} is {factorial(n)}")


def fibonacci(value: int):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    else:
        return fibonacci(value - 1) + fibonacci(value - 2)


print(f"The {n}° Fibonacci number is {fibonacci(n)}")
