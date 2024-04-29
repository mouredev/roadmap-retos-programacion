""" Reto 06: Recursividad """

# Ejercicio
def countdown(n: int):
    if n >= 0:
        print(n)
        countdown(n - 1)

countdown(100)



""" Reto extra """

def factorial(n: int) -> int:
    if n < 0:
        return "Los números negativos no son válidos"
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n: int) -> int:
    if n <= 0:
        return "La posición tiene que ser mayor que cero"
    if n <= 2:
        return n - 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
