#####################################################################
###### Imprimir numeros del 100 al 0 mediante la recursividad. ######
#####################################################################
def imprimirNumeros (n):
    if n < 0:
        return
    print (n)
    
    imprimirNumeros(n-1)
    
imprimirNumeros(100)

print(f"-----------------------------------------")
#################################################
###### Calcular el factorial de un número. ######
#################################################

def calcularFactorial(f):
    if f == 0:
        return 1
    else:
        return f * calcularFactorial(f-1)

numero = 5
resultado = calcularFactorial(numero)

print(f"El factorial de {numero} es : {resultado}")

print(f"-----------------------------------------")

#########################################################################
###### Calcular valor de una posicion en la sucesión de Fibonacci. ######
#########################################################################
def valorFibonacci(fb):
    if fb <= 1:
        return fb
    else:
        return valorFibonacci(fb-1) + valorFibonacci(fb-2)
posicion = 15

#Para corregir el problema en la indexación se añade la siguiente linea
valor = valorFibonacci(posicion - 1)

print("El valor de la posicion", posicion, "es:", valor)