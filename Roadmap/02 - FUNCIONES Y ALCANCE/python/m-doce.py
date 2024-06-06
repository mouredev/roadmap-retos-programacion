#Ejemplo de función sin retorno y sin parámetros
def Saludo():
    print("Hola gente!")

Saludo()

#Ejemplo de función sin retorno con un parámetro
def Saludo(name):
    print("Hola {}!".format(name))

Saludo("m-doce")

#Ejemplo de función con retorno sin parámetros
def Usuario():
    return "m-doce"

print(Usuario())

#Ejemplo de función con retorno y un parámetro
def CambiarSigno(number):
    return (number * -1)

print(CambiarSigno(9))

#Ejemplo de función con retorno y parámetros
def Suma(numA, numB):
    return (numA + numB)

print(Suma(5, 3))

#Variable global: puede ser accedida desde cualquier parte del código
porcentajeIVA = 1.21

#Variable local: sólo podemos acceder a ella dentro del bloque de código que se haya declarado
def CalcularIVA(value):
    resultado = value * porcentajeIVA
    print(resultado)

CalcularIVA(100)
#print(resultado) | Al pertenecer a un bloque de código en particular, no puede ser utilizada fuera del mismo

#EJERCICIO EXTRA

def Extra(stringA, stringB):
    counter = 0
    for i in range(1,101):
        if(((i % 3) == 0) and ((i % 5) == 0)):
            print("[+] " + stringA + " y " + stringB)
        elif((i % 3) == 0):
            print("[+] " + stringA)
        elif((i % 5) == 0):
            print("[+] " + stringB)
        else:
            print(i)
            counter+=1
    return counter

total = Extra("Azul", "Amarillo")
print("En total se imprimieron {} numeros".format(total))