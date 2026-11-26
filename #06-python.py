# Una función recursiva que decuente entre 0 y 100

def contar(numero:int):
    if numero >= 0:
        print(numero)
        contar(numero - 1)

contar(100)

#Una función recursiva que calcule el factorial

def factorial(numero:int) -> int:
    if numero < 0:
        print("Sólo positivos")
        return ""
    elif numero == 0:
        return 1
    else:
      return numero * factorial(numero-1)

print(factorial(10))

#Una funcion recursiva que calcule el elemento concreto de una sucesión de fibonacci

def fibonacci(posicion:int) -> int:
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    elif posicion == 2:
        return 1
    else:
        return fibonacci(posicion-1) + fibonacci(posicion-2)

print(fibonacci(10))
    


        