"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
"""

def imprimir_numeros(numero):
    if numero <= 0:
        print(numero)
        return
    else:
        print(numero)
        imprimir_numeros(numero - 1)

imprimir_numeros(100)

"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

def factorial_de_un_numero(numero, factorial = 1):

    if numero < 0:
        return "El numero es negativo"
    if numero != 0 :
        factorial= factorial * numero
        return factorial_de_un_numero(numero - 1, factorial)
    else:
        return f"El factorial es: {factorial}"
           
print(factorial_de_un_numero(5))



def fibonacci(posicion):
    if posicion <= 0:
        return "La posición debe ser mayor o igual a 0"
    elif posicion == 1:
        return 0
    elif posicion == 2:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

print(fibonacci(5)) 
