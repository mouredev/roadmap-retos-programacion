"Ejercicio Recursividad"


def recursividad (number:int):
    if number>=0:
        print(number)
        recursividad(number-1)


recursividad(100)


def factorial(number: int) -> int:
    if number < 0:
        print("Los números negativos no son válidos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)
    
print(factorial(3))


def fibonacci(elemento: int) -> int:
    if elemento < 0:
        print("No puede ser menor de 0")
        return 0
    elif elemento == 0:
        return 0
    elif elemento == 1:
        return 1
    else:
        return fibonacci(elemento - 1) + fibonacci(elemento - 2)

# Ejemplo de uso
print(fibonacci(5))  # Salida: 5