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

factorial(int(input("de que numero entero desea calcular el factorial?: ")))

#def fibonacci(posicion: int, resultado)