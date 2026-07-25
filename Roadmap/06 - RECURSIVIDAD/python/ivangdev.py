# # -------------- Recursividad ------------------
def recursividadNumeros(numero=100):
    print(numero)
    if numero == 0:
        return 0
    else:
        recursividadNumeros(numero - 1)


recursividadNumeros()


# DIFICULTAD EXTRA (opcional):
#  * Utiliza el concepto de recursividad para:
#  * - Calcular el factorial de un número concreto (la función recibe ese número).
#  * - Calcular el valor de un elemento concreto (según su posición) en la
#  *   sucesión de Fibonacci (la función recibe la posición).


def recursividadFactorial(numero):
    if numero == 1:
        return 1
    else:
        factorial = numero * recursividadFactorial(numero - 1)
        return factorial


def recursividadFibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return recursividadFibonacci(posicion - 1) + recursividadFibonacci(posicion - 2)


print(recursividadFactorial(3))
print(recursividadFibonacci(10))
