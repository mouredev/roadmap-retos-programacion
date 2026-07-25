
def recursividad(numero: int):
    if numero >= 0:
        print(numero)
        recursividad(numero - 1)
        
recursividad(100)

#DIFICULTAD EXTRA:

def factorial(numero: int):
    if numero < 0:
        print("El número debe ser positivo")
        return 0
          
    elif numero == 1:
        return 1
        
    else:
        return numero * factorial(numero - 1)

print(factorial(5))


def fibonacci(numero: int):
    if numero <= 0:
        print("El número debe ser mayor a 0")
        return 0
    elif numero == 1:
        return 0
    elif numero == 2:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2) 
        
print(fibonacci(5))