#####################################################################
###### Imprimir numeros del 100 al 0 mediante la recursividad. ######
#####################################################################
def imprimirNumeros (n):
    if n < 0:
        return
    print (n)
    
    imprimirNumeros(n-1)
    
imprimirNumeros(100)

#################################################
###### Calcular el factorial de un número. ######
#################################################

def calcularFactorial(f):
    if f == 0:
        return 1
    else:
        return f * calcularFactorial(f-1)

numero = 22
resultado = calcularFactorial(numero)

print(f"El factorial de {numero} es : {resultado}")

#########################################################################
###### Calcular valor de una posicion en la sucesión de Fibonacci. ######
#########################################################################
def valorFibonacci(fb):
    if fb <= 0:
        return 0
    elif fb == 1:
        return 1
    else:
        return valorFibonacci(fb-1) + valorFibonacci(fb-2)
posicion = 12
valor = valorFibonacci(posicion)
print(f"El valor de la posicion {posicion} es {valor}.")