def recursividad(number: int):
    if number >= 0:
        print(number)
        recursividad(number - 1)

recursividad(100)

def factorial(number: int) -> int:
    """Calcula el factorial de un número entero"""
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(5))