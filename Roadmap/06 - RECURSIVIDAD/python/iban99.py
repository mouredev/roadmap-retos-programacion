#Recursividad

#Función que se llama a ella misma

def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number-1)
    

countdown(100)

#EXTRA
## Factorial de un número concreto
def factorial(number:int) -> int:
    if number < 0:
        print("Los números negativos no son válidos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))

## Valor de un elemento concreto en la sucesión de Fibonacci
def fibonacci(number: int) -> int:
    if number <= 0 : 
        print("La posición tiene que ser mayor que 0")
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number-2)
        

print(fibonacci(5))