"""
Ejercicio
"""
# Tiene que llamarse a ella misma y detenerse en algún momento
def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)

countdown(100)

"""
Extra
"""
# Factorial de 0 es 1
# Cuando una función se puede acabar diviendo en otros sub-problemas dentro del problema general
def factorial(number: int) -> int: 
    # Ej:  Subproblemas
    if number < 0:
        print("Tienen que ser números enteros y positivos.")
        return 0
    elif number == 0:
        return 1
    else: # Problema
        return number * factorial(number - 1) 

print(factorial(5))


def fibonacci(number: int) -> int:
    if number <= 0:
        print("La posición tiene que ser mayor que 0")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    elif number >= 3:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(5))

