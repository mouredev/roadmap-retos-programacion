'''
Ejercicio Recursividad
'''

def countdown(number : int):
    if number >= 0:
        print(number)
        countdown(number - 1)

countdown(100)

'''
Ejercicio extra
'''

def factorial(number : int) -> int:
    if number < 0:
        print("Números negativos no válidos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))


def fibonacci(posicion) -> int:
    
    if posicion <= 0:
        print("Posición tiene que ser mayor que 0")
        return 0
    elif posicion == 1:
        return 0
    elif posicion == 2:
        return 1
    else:
        return fibonacci(posicion-1) + fibonacci(posicion - 2)

print("Fibonacci!")
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))

