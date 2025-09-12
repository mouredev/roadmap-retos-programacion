# #06 RECURSIVIDAD
#### Dificultad: Difícil | Publicación: 05/02/24 | Corrección: 12/02/24

## Ejercicio


#
# EJERCICIO:
# Entiende el concepto de recursividad creando una función recursiva que imprima
# números del 100 al 0.
#
# DIFICULTAD EXTRA (opcional):
# Utiliza el concepto de recursividad para:
# - Calcular el factorial de un número concreto (la función recibe ese número).
# - Calcular el valor de un elemento concreto (según su posición) en la 
#   sucesión de Fibonacci (la función recibe la posición).
#

# IMPRIME NUMEROS DEL 100 al 0
def imprimir_numeros(n):
    if n >= 0:
        print(n)
        imprimir_numeros(n - 1)

imprimir_numeros(100)

# FACTORIAL
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Calcular factorial: ")
numero = int(input())
print(factorial(numero))

# POSICION FIBONACCI
memoria = {}

def fibonacci(posicion):
    if posicion in memoria:
        return memoria[posicion]
    elif posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        resultado = fibonacci(posicion - 1) + fibonacci(posicion - 2)
        memoria[posicion] = resultado
        return resultado

print("Calcular Fibonacci")
posicion = int(input())
valor = fibonacci(posicion)
print(f"Posición {posicion} su Fibonacci es: {valor}")






