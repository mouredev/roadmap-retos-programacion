# 06 -RECURSIVIDAD

# EJERCICIO: Entiende el concepto de recursividad creando una función recursiva que imprima
# numeros del 100 al 0.

def imprimir_numeros(n):
    if n >= 0:
        print(n)
        imprimir_numeros(n - 1)


imprimir_numeros(100)

# EJERCICIO EXTRA: Utiliza el concepto de recursividad para:
# - Calcular el factorial de un número concreto (la función recibe ese número).


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        resultado = 1
    elif n > 1:
        resultado = n*factorial(n-1)
    return resultado


numero = int(input("Por favor ingrese un número a factorizar: "))
resultado = factorial(numero)
print(resultado)

# - Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).


def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


posicion = int(input("Por favor ingrese un número entero de posicion: "))
valor = fibonacci(posicion)
print(
    f"El valor en la posición {posicion} de la secuencia de Fibonacci es: {valor}")
