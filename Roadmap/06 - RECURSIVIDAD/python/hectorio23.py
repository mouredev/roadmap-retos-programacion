# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23


# EJERCICIO:
# Entiende el concepto de recursividad creando una función recursiva que imprima
# números del 100 al 0.
#
# DIFICULTAD EXTRA (opcional):
# Utiliza el concepto de recursividad para:
# - Calcular el factorial de un número concreto (la función recibe ese número).
# - Calcular el valor de un elemento concreto (según su posición) en la 
#   sucesión de Fibonacci (la función recibe la posición).


def recursiveFoo(valorInicial):
    # Esta función imprime números desde valorInicial hasta 0 recursivamente
    if valorInicial < 0:
        return
    print(valorInicial, end=", ")
    recursiveFoo(valorInicial - 1)

def factorial(ivalue):
    # Calcula el factorial de ivalue recursivamente
    if ivalue == 1:
        return 1
    return ivalue * factorial(ivalue - 1)

def fibonacci(n):
    # Calcula el valor en la posición n de la sucesión de Fibonacci
    if n <= 0:
        print("La posición debe ser un entero positivo")
        return -1  # o manejo de error según sea necesario
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            temp = b
            b = a + b
            a = temp
        return b

# Programa principal
if __name__ == "__main__":
    numeroCalcularFactorial = 3
    posicion = 10

    print("********* NUMEROS DEL 100 - 0 *********")
    recursiveFoo(100)
    print("\n")

    print(f"El factorial de <<{numeroCalcularFactorial}>> es: {factorial(numeroCalcularFactorial)}")

    valor = fibonacci(posicion)
    print(f"El valor en la posición {posicion} de la sucesión de Fibonacci es: {valor}")
