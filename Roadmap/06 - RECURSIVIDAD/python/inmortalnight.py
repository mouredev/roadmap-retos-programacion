# 06 - Recursividad

# Función recursiva que imprime números 100-0
def imprimir():
    for i in range(100, -1, -1):
        print(i)
imprimir()
# EXTRA 1: Calcular factorial
def factorial(number):
    factorial = 1
    for i in range(number, 0, -1):
        factorial = factorial * i
        print(number)
    print("Factorial de ", number, " es ", factorial)
factorial(20)
# EXTRA 2: Calcular el valor según la posición introducida en la sucesión de Fibonacci
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
position = 4
print(f" Según la posición {position} fibonacci es {fibonacci(position)}")