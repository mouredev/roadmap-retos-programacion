def reducir(n):
    """Función recursiva que devuelve los números del 100 al 1."""
    if n == 0:
        return []
    else:
        return [n] + reducir(n - 1)

# Ejemplo de uso de la función recursiva
numeros = reducir(100)
print(numeros)

# Factorial #
def factorial(n):
    """Función recursiva para calcular el factorial de un número."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso de la función factorial
numero = 5  # Aquí puedes ingresar el número para calcular su factorial
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

# Fibonaci #
def fibonacci(posicion):
    """Función recursiva para calcular el valor de un elemento en la secuencia de Fibonacci."""
    if posicion <= 1:
        return posicion
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

# Ejemplo de uso de la función para encontrar el valor en la posición deseada
posicion = 7  # Aquí puedes ingresar la posición del elemento que deseas calcular
valor = fibonacci(posicion)
print(f"El valor en la posición {posicion} de la secuencia de Fibonacci es {valor}")
