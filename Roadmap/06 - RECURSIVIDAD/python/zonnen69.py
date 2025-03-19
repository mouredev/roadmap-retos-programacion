#  *
#  * EJERCICIO:
#  * Entiende el concepto de recursividad creando una función recursiva que imprima
#  * números del 100 al 0.

#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el concepto de recursividad para:
#  * - Calcular el factorial de un número concreto (la función recibe ese número).
#  * - Calcular el valor de un elemento concreto (según su posición) en la 
#  *   sucesión de Fibonacci (la función recibe la posición).
 
# Numeros del 100 al 0

def imprimir_numeros(n):
    if n < 0:
        return
    print(n)
    imprimir_numeros(n - 1)

imprimir_numeros(100)


#  * - Calcular el factorial de un número concreto (la función recibe ese número).
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = int(input("Ingrese el número para calcular su factorial: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}\n")


#  * - Calcular el valor de un elemento concreto (según su posición) en la 
#  *   sucesión de Fibonacci (la función recibe la posición).

def fibonacci(posicion):
    if posicion <= 1:
        return posicion
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

posicion = int(input("Ingrese la posición del elemento en la sucesión de Fibonacci: "))
valor = fibonacci(posicion)
print(f"El valor del elemento en la posición {posicion} de la sucesión de Fibonacci es {valor}.")


