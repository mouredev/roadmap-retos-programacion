"""
/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 
 */"""
 
"""i = 100
while(0<=i):
    print(i)
    i-=1
  """
n = 10
i = 0
def factorial(n):
    while(0<=n):
        
        if n < 1:
            return 1
        else:
            resultado = n * factorial(n-1) 
            return resultado
        i+=1
print(factorial(n))

def finobacci(n):
    while(0<=n):
        if n <= 1:
            return n
        else:
            return finobacci(n-1)+finobacci(n-2)
    i+=1



n = 10
print(finobacci(n))