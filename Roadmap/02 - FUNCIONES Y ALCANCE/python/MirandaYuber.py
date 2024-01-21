# Funciones
import random


def hola():  # Función sencilla
    print('Hola Mundo')


hola()


def suma(num1=1, num2=10):  # Con argumentos
    print(f'{num1} + {num2} = {num1 + num2}')


suma(5, 9)


def resta(num1, num2):  # Con argumentos y retorno
    resultado = num1 - num2
    return f'{num1} - {num2} = {resultado}'


print(resta(10, 9))


def imprimir_numeros_pares():  # Función dentro de una función
    def es_par(num):
        return num % 2 == 0

    for i in range(0, 21):
        if es_par(i):
            print(i)


imprimir_numeros_pares()


variable_global = 'Yuber'


def global_local():
    variable_local = 'Miranda'
    print(f'{variable_global} {variable_local}')


global_local()

print('######  EXTRA  ######')


def extra(param1, param2):
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(param1 + param2)
        elif numero % 3 == 0:
            print(param1)
        elif numero % 5 == 0:
            print(param2)
        else:
            print(numero)
            contador += 1

    return contador


print(extra("Yuber", "Python"))
