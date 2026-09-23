"""ejercicio
"""



def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)


countdown(100) 

"""
EXTRA
"""

def factorial(number : int) -> int:
    if number < 0 :
        print("no se aceptan numeros negativos")
        return 0
    elif number == 0 :
        return 1
    else:
        return number * factorial(number - 1)



print(factorial(5))



def fibonacci(posicion: int) -> int:
    if posicion <= 0 :
        print("La posición debe ser mayor a cero")
        return 0
    
    elif posicion <= 2 :
        return posicion - 1
    else :
        return fibonacci(posicion - 1) + fibonacci(posicion -2)


print(fibonacci(12))


