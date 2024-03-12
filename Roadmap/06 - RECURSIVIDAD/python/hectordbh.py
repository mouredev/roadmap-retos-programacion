"""EJERCICIO"""

def decrease(num):
    """Función que devuelve valores decrecientes uno a uno
    hasta cero.

    Args:
        num (int): valor inicial

    Returns:
        int: valores
    """
    # Caso final
    if num < 0:
        return num
    print(num)
    decrease(num-1)

decrease(100)

# DIFICULTAD EXTRA

# Factorial
def factorial(num, result = 1):
    """Función que devuelve el valor del factorial de un
    número

    Args:
        num (int): valor al que hacerle el factorial
        result (int, optional): _description_. Defaults to 1.

    Returns:
        int: valor de cálculo
    """
    if num == 0:
        return result
    else:
        result *= num
        return factorial(num-1, result)

factorial(3)

# Fibonacci
def fibo(n):
    """FUnción que devuelve el valor de una posición
    en la sucesión de Fibonacci

    Args:
        n (int): posición

    Returns:
        int: valor de la posición
    """
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

fibo(4)
