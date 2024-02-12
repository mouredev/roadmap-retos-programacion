#06 Recursividad
"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).
"""


def decreaseFactorial(number: int)-> int:
    """in a recursive mode, decrease from a number to 0"""
    if number == 0:
        return print(0)
    else:
        print(number)
        return decreaseFactorial(number-1)

decreaseFactorial(100)

#DIFICULTAD EXTRA (opcional):

#factorial from a given number
def factorialRecursive(number: int) -> int:

    if number == 1:
        return 1
    else:
        return number * factorialRecursive(number-1)

print(factorialRecursive(7))

#calc the value in a Fibonacci list by the given position

def fiboList(position: int = 51) -> list:
    """this functions returns the value of a position in a Fibonacci list"""
    listFibo = [0,1]
    for i in range(2, position+1):
        listFibo.append(listFibo[i-2]+listFibo[i-1]) 
        #print(i)
        #print(i," - ", x)
    return print(listFibo[position])
    
fiboList(10)

# recursive Fibonacci

def fiboPositionRecursive(position: int)-> int:
    """function to return the value of a position in a Fibnonacci list"""

    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return(fiboPositionRecursive(position-1)+ fiboPositionRecursive(position-2))


print(fiboPositionRecursive(10))

