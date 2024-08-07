#Funcion recursiva
def funcion_recursiva(numero_ingresado):
    numero_ingresado -= 1
    if numero_ingresado >= 0:
        print(numero_ingresado)
        funcion_recursiva(numero_ingresado) #recursividad de la funcion(que se llame a si misma)
    else:
        print('Fin de la cuenta regresiva.')
funcion_recursiva(101)

'''Dificultad extra.-.-.-.-'''
#Factorial con funcion recursiva
def factorial(numero): 
    if numero > 1: 
        numero = numero * factorial(numero -1)
    return numero
print('factorial:', factorial(5)) 

#Calcular el valor de un elemento concreto (según su posición) en la 
# sucesión de Fibonacci '''
def fibo (num):
    if num < 2:
        return num
    else: 
        return fibo(num -1) + fibo(num -2)
print('fibo:', fibo(10)) #55
#0 1 1 2 3 5  8
#1 2 3 4 5 6  7 TE QUIERU MUCHITU DADDU :3
        