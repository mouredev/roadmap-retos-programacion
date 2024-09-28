
# Imprime del número al 100, de forma recursiva
def imprimir_recursiva(num: int):
    print(num)
    if num != 0:
        imprimir_recursiva(num-1)

imprimir_recursiva(100)

#Factorial
def factorial(num:int):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(15))

#Posición en la sucesión de Fibonacci
def fibonacci(num:int):
    if num <= 0:
        print('Introduce un valor positivo')
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(15))
