
"""	
16 - Iteraciones

Autor de la solución: Oriaj3	

Teoría:	

Las iteraciones son una parte fundamental de la programación, ya que permiten
repetir un bloque de código varias veces. En Python, las iteraciones se pueden
realizar de varias formas, como con el bucle for o con el bucle while.
En este problema, se pide que se realice un programa que imprima los números
del 1 al 10 utilizando un bucle for.
"""
"""
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
"""
def mec1():
    for i in range(1, 11):
        print(i)

def mec2():
    num=1
    while (num <= 10):
        print(num)
        num+=1

def mec3(num: int = 1):
    if num <= 10:
        print(num)
        mec3(num+1)


print("******************MEC1")
mec1()
print("******************MEC2") 
mec2()
print("******************MEC3")
mec3()  
    
"""
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
"""

#For clásico 
numeros = [1, 2, 3]
for numero in numeros:
    print(numero)

#For con range
for i in range(5):
    print(i)

#For con enumerate
frutas = ["manzana", "pera", "sandía"]
for indice, fruta in enumerate(frutas):
    print(indice, fruta) 

#While
num=0
while num<5:
    print(num)
    num += 1

#Comprensión de las listas
cuadrados = [x**2 for x in range(1,6)]
print(cuadrados)

#Comprensión de conjuntos
pares = {x for x in range(10) if x % 2 ==0}
print(pares)

#Comprensión de diccionarios:
cuadrados_dict = {x: x**2 for x in range(1, 6)}
print(cuadrados_dict)

#Map
def cuadrado(x):
    return x**2

numeros = [1, 2, 3]
cuadrados = map(cuadrado, numeros)
print(list(cuadrados))

#Itertools.product
import itertools

letras = ["a", "b"]
numeros = [1, 2]
combinaciones = itertools.product(letras,numeros)
print(list(combinaciones))

#generadores
def generador_cuadrados(n):
    for i in range(n):
        yield i**2

for cuadrado in generador_cuadrados(5):
    print(cuadrado)


#TODO: Revisar
for e in [1, 2, 3, 4]:
    print(e)

for e in {1, 2, 3, 4}:
    print(e)

for e in (1, 2, 3, 4):
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}:
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}.values():
    print(e)

print(*[i for i in range(1, 11)], sep="\n")

for c in "Python":
    print(c)

for e in reversed([1, 2, 3, 4]):
    print(e)

for e in sorted(["m", "o", "u", "r", "e"]):
    print(e)

for i, e in enumerate(sorted(["m", "o", "u", "r", "e"])):
    print(f"Índice: {i}, valor: {e}")
