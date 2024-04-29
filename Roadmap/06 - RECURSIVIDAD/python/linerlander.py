"""
Ejercicio de Recursividad
"""
def countdown(num: int):
    if num >= 0: # Condicional que indica hasta que valor asumira num
        print(num)
        countdown(num -1)

countdown(100)

"""
Extra
"""

def factorial_number(num: int)-> int:
    if num < 0:
        print('Los números negativos no son válidos')
        return 0
    elif num == 0:
        return 1
    else:
        return num * factorial_number(num - 1)
print(factorial_number(5))

def fibonacci_position(number: int)-> int:
    if number <= 0:
        print('Los posición tiene que ser mayor a 0')
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci_position(number - 1) + fibonacci_position(number - 2)

print(fibonacci_position(10))
