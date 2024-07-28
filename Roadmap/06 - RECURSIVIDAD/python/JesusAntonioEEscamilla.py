# #06 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
# Definimos la función
def imprimir_números(n):
    if n < 0:
        return
    print(n)
    # Aquí es donde realiza la Recursividad
    imprimir_números(n - 1)

print("Recursividad")
imprimir_números(100)



"""
EXTRA
"""
# Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial")
print(factorial(5))

# Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1 ) + fibonacci(n - 2)

print("Fibonacci")
print(fibonacci(10))