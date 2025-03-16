# Crea una función recursiva que imprima los números del 100 al 0.
def print_numbers(n=100):
    if n >= 0:
        print(n)
        print_numbers(n - 1)


# Calcular el factorial de un número concreto (la función recibe ese número)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Calcular el valor de un elemento concreto (según su posición) en la sucesión de
# Fibonacci (la función recibe la posición).
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print_numbers()
    print(factorial(5))
    print(fibonacci(3))
