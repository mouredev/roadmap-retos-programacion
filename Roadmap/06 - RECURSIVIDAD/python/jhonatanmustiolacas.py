#!/usr/bin/env

# EJERCICIO:
# Entiende el concepto de recursividad creando una función recursiva que imprima
# números del 100 al 0.
#
# DIFICULTAD EXTRA (opcional):
# Utiliza el concepto de recursividad para:
# - Calcular el factorial de un número concreto (la función recibe ese número).
# - Calcular el valor de un elemento concreto (según su posición) en la 
#   sucesión de Fibonacci (la función recibe la posición).

# TODO: función recursiva que imprime números del 100 al 0
def imprime_del_cien_al_cero_recursivo() -> None:
    """
    Imprime los números del 100 al cero recursivamente

    >>> imprime_del_cien_al_cero_recursivo()

    """
    if hasattr(imprime_del_cien_al_cero_recursivo, "count"):
        if imprime_del_cien_al_cero_recursivo.count < 0:
            return
        else:
            print(imprime_del_cien_al_cero_recursivo.count)
            setattr(imprime_del_cien_al_cero_recursivo, "count", imprime_del_cien_al_cero_recursivo.count - 1)
    else:
        imprime_del_cien_al_cero_recursivo.count = 100
    imprime_del_cien_al_cero_recursivo()


# TODO: funcion recursiva para calcular factorial de un número dado
def calculo_factorial_recursivo(numero: int) -> int:
    """
    Retorna el cálculo factorial del argumento numero

    >>> calculo_factorial_recursivo(5)
    120
    """
    if numero == 0:
        return 1
    return numero * calculo_factorial_recursivo(numero - 1)


# TODO: funcion recursivo para calcular valor de un número fibonacci en una posición dada
def fibonacci_en_recursivo(posicion: int) -> int:
    """
    Retorna el valor del número fibonacci en la posición dada con el argumento posicion

    >>> fibonacci_en_recursivo(10)
    55
    """
    return 0 if (posicion == 0) else 1 if (posicion == 1) else  (fibonacci_en_recursivo(posicion-1) + fibonacci_en_recursivo(posicion-2))



# TEST

resultado = imprime_del_cien_al_cero_recursivo()
print(resultado)

resultado = calculo_factorial_recursivo(5)
print(resultado)

resultado = fibonacci_en_recursivo(10)
print(resultado)

import doctest

doctest.testmod()