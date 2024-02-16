# #06 RECURSIVIDAD


"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
"""

def recursividad (num):
    if num >= 0:
        print (num)
        num-=1
        recursividad(num)
    else:
        print ("El programa recursivo a finalizado correctamente")

recursividad(100)

"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

def rec_factorial(num:int,result=1):
    if num == 0:
        print (f"El factorial de {x} = {result}")
    else:
        return rec_factorial(num-1,result*num)

x=int( input("Ingrese número que desea saber el factorial: "))
rec_factorial(x)


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
        
y = int (input("Ingrese la posición de sucesió de fibonacci que desea conocer:"))    
resultado= fib(y)
print (f"El valor en la posición {y} de fibonacci = {resultado}")