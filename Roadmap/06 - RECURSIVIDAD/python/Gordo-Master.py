""" 
Recursividad
"""

def numb_print(value:int):
    print(value)
    if value > 0:
        numb_print(value-1)

# numb_print(100)


"""
Ejercicio extra
"""



# Factorial de un número

def factorial(value:int) -> int:
    if value > 1:
        fact = value * factorial((value-1))
    elif value <= 1 and value >= 0:
        fact = 1
    else:
        return None
    return fact

numero_factorial = 5

if factorial(numero_factorial) != None:
    print(f"{numero_factorial}! es: {factorial(numero_factorial)}")
else:
    print(f"No existe el factorial de un numero negativo: {numero_factorial}")




# Buscador de Fibonacci


def fibonacci(pos:int) -> int:
    if pos < 1:
        return None
    elif pos == 1:
        return 0
    elif pos == 2:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)
    

pos_fibo = 0
if pos_fibo >= 1:
    print(f"El valor en la {pos_fibo}º posicion de la sucesión de fibonacci es: {fibonacci(pos_fibo)}")
else:
    print("La posición debe ser mayor que 0")
