# /*
#  * EJERCICIO:
#  * Entiende el concepto de recursividad creando una función recursiva que imprima
#  * números del 100 al 0.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el concepto de recursividad para:
#  * - Calcular el factorial de un número concreto (la función recibe ese número).
#  * - Calcular el valor de un elemento concreto (según su posición) en la 
#  *   sucesión de Fibonacci (la función recibe la posición).
#  */

#la funcion recursiva es una que se llama asi misma

def counter(value):
    print(value) #imprimimos nuestro valor, en este caso es 100
    # value -=1 #restamos uno
    if value >= 0:
        counter(value-1) #verificamos condicion y ejecutamos la funcion

counter(100)

def factorial(value):
    if value == 1:
        return 1
    else:
        return value * factorial(value-1)

def fibonacci(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    else:
        return fibonacci(value-1) + fibonacci(value-2)
    
print(factorial(5))
print(fibonacci(7))

