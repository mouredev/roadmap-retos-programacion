"""
/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
 */
"""

lista = [] #lista para almacenar los numeros del 100 al 0
def Recursividad_del_100_al_0(numero = 100 ):

    if numero < 0: # si el numero es menor que 0 termina la funcion , para evitar la recursion infinita
        return lista

    lista.append(numero)
    return Recursividad_del_100_al_0(numero - 1) #se resta un numero del numero introducido

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def Fibonacci(numero , a = 1 , b = 0 ):
    if numero == 0 :
        return a

    return Fibonacci(numero -1 , a + b ,a )

print("recursividad , del 100 al 0 : " , Recursividad_del_100_al_0(100))
print("factorial de 5 es : " , factorial(5))
print("valor del numero 20 de la suceccion fibonacci : ", Fibonacci(20))
