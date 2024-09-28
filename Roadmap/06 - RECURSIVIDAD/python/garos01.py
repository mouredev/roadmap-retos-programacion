# Recursividad


def decremento(numero):
    if numero < 0:
        return
    print(numero)
    decremento(numero - 1)


decremento(100)


# Ejercicio extra


# Factorial
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)


print(f"Factorial {factorial(5)}")


# Fibonacci
def fibonacci(posicion):
    if posicion == 1 or posicion == 2:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)


print(f"Numero {fibonacci(10)}")
