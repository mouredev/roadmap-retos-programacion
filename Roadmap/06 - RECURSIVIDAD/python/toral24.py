'''
EJERCICIO:
Entiende el concepto de recursividad creando una función recursiva que imprima
números del 100 al 0.
'''

def nums():
    list=[]
    i=1
    while i <= 100:
        list.append(i)
        i +=1
    return list

print(nums())
'''
DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:
    - Calcular el factorial de un número concreto (la función recibe ese número).
    - Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).
'''

def fact(num):
    cont = 1
    resul = 1
    while cont <=num:
        resul *= cont
        cont += 1
    return resul

print(fact(5))

def fibo(num):
    num1 = 1
    num2 = 1
    aux = 0
    cont = 1
    while num >= cont:
        aux = num2
        num2 += num1
        num1 = aux
        cont += 1
    return num2

print(fibo(15))


