# #06 RECURSIVIDAD
## Ejercicio
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
#RECURSIVIDAD
#La recursividad es una función que se llama a sí misma
def imprimir_numero(n):
    if n >= 0:
        print(n)
        imprimir_numero(n-1)
        
imprimir_numero(100)

#DIFICULTAD EXTRA
def factorial(n): #5! = 5*4*3*2*1
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
#La funcion fibonacci es una sucesion de numeros que se obtiene sumando los dos anteriores    
def fibonacci(n): #0,1,1,2,3,5,8,13,21,34,55,89,144,233,377...
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def menu():
    print("1.- Factorial")
    print("2.- Fibonacci")
    print("3.- Salir")
    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        num = int(input("Ingresa un numero: "))
        print(factorial(num))
    elif opcion == 2:
        num = int(input("Ingresa un numero: "))
        print(fibonacci(num))
    elif opcion == 3:
        print("Adios")
    else:
        print("Opcion invalida")
        menu()
menu()  