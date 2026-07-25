#RECURSIVIDAD

def disminuidor(numero : int):
    if numero >= 0:
        print(numero)
        disminuidor(numero - 1) 

disminuidor(100)


#EJERCICIO EXTRA

def factorial(n : int) -> int:
    if n < 0:
        print("Los numeros negativos no son validos")
        return 0
    elif n == 0:
        return 1
    return n * factorial(n -1)

print(factorial(4))


def fibonacci(n : int) -> int:
    if n <= 0:
        print("La posicion tiene q ser mayor a 0")
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
