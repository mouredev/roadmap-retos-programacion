"""
RECURSIVIDAD
"""

print("Recursividad:")  
def recursive(n):
    if n >= 0:
        print(n)
        recursive(n - 1)

recursive(100)

print("Factorial:") #Factorial de un número
def factorial(n):
    if n < 0:
        print("Los numeros negativos no tienen factorial")
        return 0
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(f"El factorial de 5 es {factorial(5)}")

print("Fibonacci:") #Fibonacci de un número
def fibonacci(n):
    if n <= 0:
        print("Los numeros negativos no tienen fibonacci")
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"El fibonacci de 5 es {fibonacci(5)}")

