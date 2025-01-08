"""Función para imprimir números del 110 al 0."""

def my_print(number: int):
    print(number)
    if number > 0:
        my_print(number - 1)
    return

#my_print(6) # "Descomentar"


"""Función para calcular el factorail."""

def factorial(num: int) -> int:
    if num < 0:
        return 0
    elif num == 0:
        return 1
    else:
        return num*factorial(num-1)
    
#print(factorial(4))
    

"""Sucesión de Fibonacci"""

def fibo(num: int) -> int:
    if num <= 1:
        return 0
    elif num == 2:
        return 1
    
    else:
        return fibo(num - 2) + fibo(num - 1)
    
print(fibo(9))