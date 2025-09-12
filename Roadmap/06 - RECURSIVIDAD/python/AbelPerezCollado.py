# EJERCICIO: Función recursiva que imprima números del 100 al 0

def countdown(n : int):
    print(n)
    if n > 0:
        countdown(n-1)
        


#DIFICULTAD EXTRA
# Calcular el factorial de un número.

def factorial(n : int):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1
    
# Calcular valor elemento concreto en la sucesión de Fibonacci

def fibonacci(n : int):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
