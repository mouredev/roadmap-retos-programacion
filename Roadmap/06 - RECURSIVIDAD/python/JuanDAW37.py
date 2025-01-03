"""EJERCICIO
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""
def contarAtras(numero:int):
    if numero >= 0:
        print(numero)
        numero -= 1
        contarAtras(numero) #La función se llama aquí recursivamente, si se da la condición

contarAtras(100)

# DIFICULTAD EXTRA
#Factorial
def factorial(numero:int)->int:  
    if numero == 0:
        return 1
    elif numero < 0:
        print('Los números negativos no son válidos')   
        return 0
    else:
        return numero * factorial(numero -1)    

n = factorial(4)
print(n)

#Fibonacci
def fibonacci(posicion:int)->int:
    if posicion <= 0 or posicion == 1:        
        return 0    
    elif posicion == 2:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

print(fibonacci(10))