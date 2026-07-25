"""
Recursivdidad
"""

# imprime los numeros del 1 al 100
def print_numbers(number: int)-> int:
    if number >= 0 and number <= 100:  
        print(number)
        print_numbers(number + 1)
print_numbers(1)

"""Dificultad extra"""

def factorial(num:int)-> int:
    if num < 0:
        print("No se puede calcular el factorial de un numero negativo")
        return 0
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    

val = 4
print(f"el factorial de {val} es {factorial(val)}")


def fibonacci(num:int)-> int:
    if num <= 0:
        print("No se puede calcular el fibonacci de un numero negativo")
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)