"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 """

def recursividad_100_0(numero : int):
    if numero == 0:
        return 0
    else:
        print(numero)
        return recursividad_100_0( numero -1)
    
print(recursividad_100_0(100))

# EXtra

# factorial

def factorial(n :int):
    if n < 0:
        return 0
    if n == 0:
      return 1
    if n == 1:
         return  n
    else:
         return n*factorial(n-1)

print(factorial(5))

#fibonacci

def fibo(index :int):
    if index <= 1:
        return 0
    elif  index == 2 :
        return 1
     
    else:
        return fibo(index-2)+fibo(index-1)

print(fibo(8))

