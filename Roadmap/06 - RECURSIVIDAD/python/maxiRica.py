import os
import textwrap

def limpiar(): #creamos la función para limpiar la pantalla para poder aplicarla las veces que necesitemos sin repetir código
    while True:

        pregunta=input("quieres que limpie la pantalla? (si - no): ")
        if pregunta=="si":
        
            if os.name=="posix":
                os.system("clear")
                break
            else:
                os.system("cls")
                break
        elif pregunta=="no":
            break

"""
EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
"""
limpiar()

def recursividad(a=100):
    if a<0:
        return
    else:
        print(a)
        recursividad(a-1)

recursividad()

"""
DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""
limpiar()

# FACTORIAL
def factorial_(valor):
    if valor == 0:
       
       return 1
    else:
        fact=1
        for i in range(valor,0,-1):
            fact=fact*i
        return fact

print("\n\nVAMOS A CALCULAR EL FACTORIAL\n")
valor=input("introduce un número: ")
valor=int(valor)
print(factorial_(valor))

# POSICIÓN DE FIBO

def fibo(valor):
    if valor == 0:
        return 0
    elif valor == 1:
        return 1
    else: 
        fibonacci=[0,1]
        for i in range(2,valor+1):
            calculo=fibonacci[i-1]+fibonacci[i-2]
            fibonacci.append(calculo)
    print(fibonacci[valor])

print("\n\nVAMOS A CALCULAR EL FIBONACCI SEGÚN POSICIÓN\n")
valor=int(input("dame el valor de la posición de fibo: \n"))
fibo(valor)
