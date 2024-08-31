"""
*Recursividad
"""

def numeros(numero: int):
    if(numero<100):
        numero += 1
        numeros(numero)
        print(numero)
    

numeros(0)

"""
!Extra
"""

def factorial(numero: int, resultado = 1):
    if(numero <= 0):
        print(resultado)
    else:
        resultado *= numero
        numero -= 1
        factorial(numero, resultado)

#factorial(int(input("de que numero entero desea calcular el factorial?: ")))

def fibonacci(posicion: int, posactual = 2, resultado = [0,1,1]):
    if(posicion <= 2):
        print(resultado[posicion])
    elif(posactual == posicion):
        print(resultado[len(resultado)-1])
    else:
        resultado.append(resultado[len(resultado)-1] + resultado[len(resultado)-2])
        posactual += 1
        fibonacci(posicion, posactual, resultado)

#?posicion  0 1   2   3   4   5   6   7   8   9     10 (len(posicion 11))
#?fibonacci 0 1   1   2   3   5   8   13  21  34    55

fibonacci(10)