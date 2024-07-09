def imprimir_descendente(n):
     """Imprime números de forma descendente desde n hasta 0."""

     if n < 0: # Caso base: detener la recursion cuando n es menor que 0
          return
     print(n) # Imprimir el número actual

     imprimir_descendente(n - 1)  # Llamada recursiva con n-1

# Llamada inicial a la función
imprimir_descendente(100)

# Ejercicio
def factorial(n):
    """Calcula el factorial de un número n (n!)."""
    if n == 0:  # Caso base: 0! = 1
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

def fibonacci(n):
    """Calcula el n-ésimo número de la sucesión de Fibonacci."""
    if n <= 1:  # Casos base: fib(0) = 0, fib(1) = 1
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Llamada recursiva

print("Factorial de 5:", factorial(5))  # 120
print("El 10º número de Fibonacci:", fibonacci(10))  # 55
