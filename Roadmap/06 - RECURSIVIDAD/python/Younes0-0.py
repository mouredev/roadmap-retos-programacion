def numero(num:int):
    if num == 0:
        return print(0)
    else:
        print(num),
        return numero(num -1)
numero(100)  
# Calcular el factorial de un número concreto (la función recibe ese número).
def factorial(num:int):
    if num <= 1:
        return 1
    else:
        return factorial(num -1 ) * num

# Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).
def fibonacci(posicion:int):
    if posicion <= 0:
        return 0
    if posicion == 1:
        return 1
    else:
        return fibonacci(posicion-1) + fibonacci(posicion-2)