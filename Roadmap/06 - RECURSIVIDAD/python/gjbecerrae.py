#función recursiva que imprima números del 100 al 0
def numeros(numero):
    if numero != 0:
        print(numero)
        return numeros(numero-1)
    else:
        print(numero)

#numeros(100)
        
def factorial(n):
    if n == 1:
        return  1
    else:        
        return (n * factorial(n-1))


def fibonacci(elemento):
    if elemento == 1:
        return 0
    elif elemento == 2:
        return 1
    else:
        return fibonacci(elemento - 1) + fibonacci(elemento - 2)


