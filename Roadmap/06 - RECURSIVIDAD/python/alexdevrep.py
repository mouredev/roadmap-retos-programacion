'''
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
'''

#Ejercicio
'''
La recursuvidad en programación es una función que se llama a sí misma durante su ejecucción
'''

def recursiva(n):
    if (n<=100):
        print(n)
    else:
        return recursiva

    recursiva(n+1)

    
    
recursiva(0)

print("------------------------------")
#Dificultad extra

def factorial (numero):
    if (numero==0):
        return 1
    else :
        return numero * factorial(numero-1) 

numero=int(input("Por favor ingrese un número: "))
resultado = factorial(numero)
print(resultado)

print("------------------------------")

def fibonacci(posicion):
    if(posicion<=1):
        return posicion
    else :
        return fibonacci(posicion-1)+ fibonacci (posicion -2) 


posicion = int(input("Por favor ingrese el valor de la posición: "))
resultado2= fibonacci(posicion)
print(resultado2)







