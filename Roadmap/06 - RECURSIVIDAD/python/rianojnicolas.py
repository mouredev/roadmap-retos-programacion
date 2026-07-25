###################################
# Dev: rianojnicolas              #
###################################

# EJERCICIO:
# función recursiva que imprima números del 100 al 0.
def print_numbers(n):
    if n >= 0:
        print(n)
        print_numbers(n-1)

print_numbers(100)  # Imprime los números del 100 al 0

# DIFICULTAD EXTRA:
# 1. Factorial de un numero n
def calc_factorial(n):
    if n == 0:
        return 1
    else:
        return n*calc_factorial(n-1)

print(calc_factorial(5))  # Imprime el factorial de 5

# 2. Valor de un elemento en la sucesión de Fibonacci segun su posición
# secuencia -> 0, 1, 1, 2, 3, 5, 8, 13
# Posición ->  0, 1, 2, 3, 4, 5, 6, 7
def calc_fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return calc_fibonacci(pos-1) + calc_fibonacci(pos-2)

print(calc_fibonacci(5))  # Imprime el valor de la posición 5
