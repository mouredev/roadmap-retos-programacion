'''
EJERCICIO:
 Entiende el concepto de recursividad creando una función recursiva que imprima
 números del 100 al 0.
'''

#### funciones recursivas ####

'''una funcion recursiva es una funcion que sellama asi misma
en su propia ejecucion'''

def imprimir (value):
    value -= 1
    if value >=0:
        print(value)
        imprimir(value)
    else:
        print("fin de la funcion recursiva")
       
valor = 101
imprimir(valor)

'''
DIFICULTAD EXTRA (opcional):
 Utiliza el concepto de recursividad para:
 - Calcular el factorial de un número concreto (la función recibe ese número).
 - Calcular el valor de un elemento concreto (según su posición) en la 
 - sucesión de Fibonacci (la función recibe la posición).
'''
##### Calcular el factorial de un número concreto (la función recibe ese número). #####

def factorial_number (numero):
    if numero == 1:
        return 1
    else: 
        fact= numero * factorial_number(numero-1)
        return fact
       
number = int(input("proporcione un numero para calcular su factorial: "))
resultado = factorial_number(number)
print(f'el factorial de {number} es : ',{resultado})
