"""
Recursividad
"""

def cuenta_atras(number:int):
    if number >= 0:
        print(number)
        cuenta_atras(number - 1)

cuenta_atras(100)


## Extra

# numero factorial

def factorial(number:int) -> int:

    if number < 0:
        print("no aceptamos negativos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number -1)

print(factorial(4))

def fibonacci(number:int ) ->int:
    if number <= 0:
        print("no se valen negativos")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else: 
        return fibonacci(number-1) + fibonacci(number-2)
    
print(fibonacci(5))