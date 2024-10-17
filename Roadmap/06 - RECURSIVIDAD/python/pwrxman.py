"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
"""

def imprime(hasta: int):
    if hasta >= 0:
       print(hasta)
       imprime(hasta-1)

imprime(5)

print("> > > > > > > > > > > > > > > > > INICIA EXTRA > > > > > > > > > > > > > > > > > \n\n")

"""
* DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:
* - Calcular el factorial de un número concreto (la función recibe ese número).
* - Calcular el valor de un elemento concreto (según su posición) en la 
*   sucesión de Fibonacci (la función recibe la posición).
"""


def fibonacci(num: int) -> int:
    if num <= 0:
        print("La posicion tiene que ser mayor a cero")
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def elfactorial(num:int) -> int:
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        return print("El número es menor que cero y no existe")
    else:
        return num * elfactorial(num-1)


print(f"El factorial es {elfactorial(5)}")

print(f"el fibonacci es {fibonacci(5)}")
# 0, 1, 1, 2, 3, 5, 8, 13, 21