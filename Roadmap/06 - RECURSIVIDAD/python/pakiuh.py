'''EJERCICIO:
Entiende el concepto de recursividad creando una función recursiva que imprima
números del 100 al 0.'''

def recursividad():
    x = 100 #caso base
    while x>0:
        x = x - 1 #llamada recursiva
        print(x)

recursividad()

'''DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la 
  sucesión de Fibonacci (la función recibe la posición).'''

def calculo_factorial(posicion: int):
    factorial = 1
    while posicion > 1:#método con bucle while
        factorial *= posicion
        posicion -= 1
        print(factorial)
    
    for i in range(posicion,0,-1):#método con bucle for
        factorial *= i
        print(factorial)


calculo_factorial(10)
