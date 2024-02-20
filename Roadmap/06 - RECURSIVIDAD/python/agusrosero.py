# EJERCICIO:
def cuenta_atras(n):
    if n < 0:
        return
    cuenta_atras(n - 1)
    print(n)


print(cuenta_atras(100))

# DIFICULTAD EXTRA:
# Calcular el factorial de un número concreto (la función recibe ese número).


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(2))

# Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(7))
