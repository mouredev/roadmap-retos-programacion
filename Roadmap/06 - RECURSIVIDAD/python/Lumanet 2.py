# La recursividad es una técnica en programación donde una función se llama a sí misma
def imprimir_num(n):
    if n < 0:
        return
    print(n)
    imprimir_num(n - 1)

imprimir_num(100)


"""
Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la 
  sucesión de Fibonacci (la función recibe la posición).
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1 # El factorial de 0 y 1 es 1
    else:
        return n * factorial(n - 1)

numero = 5
resultado = factorial(numero) # 5 * 4 * 3 * 2 * 1 = 120
print(f"El factorial de {numero} es {resultado}") # 120


def fibonacci(n):
    if n == 0:
        return 0 # El primer número de la sucesión de Fibonacci es 0
    elif n == 1:
        return 1 # El segundo número de la sucesión de Fibonacci es 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = 7
valor_fibonacci = fibonacci(posicion) # 0, 1, 1, 2, 3, 5, 8, 13
print(f"El valor de la posición {posicion} en la sucesión de Fibonacci es {valor_fibonacci}") # 13
