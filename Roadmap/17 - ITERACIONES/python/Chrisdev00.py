"""
* EJERCICIO:
* Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
* números del 1 al 10 mediante iteración.
*
* DIFICULTAD EXTRA (opcional):
* Escribe el mayor número de mecanismos que posea tu lenguaje
* para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""

print("a.- Utilizando un bucle 'for' con 'range()' ")
for i in range(1,11):
    print(i, end=" ")
print()

print("b.- Utilizando un bucle 'for' con una lista")
numeros = [1,2,3,4,5,6,7,8,9,10]
for num in numeros:
    print(num, end=" ")
print()

print("c.- Utilizando un bucle 'while'")
cont = 1
while cont <= 10:
    print(cont, end=" ")
    cont += 1
print()


############  ----------------------------- EXTRA ------------------------------- #############

# 1.- Bucle for con range()

print("1.- Utilizando un bucle 'for' con 'range()' ")
for i in range(1,11):
    print(i, end=" ")
print()

# 2.- Bucle for con una Lista

print("2.- Utilizando un bucle 'for' con una lista")
numeros = [1,2,3,4,5,6,7,8,9,10]
for num in numeros:
    print(num, end=" ")
print()

# 3.-  Bucle while

print("3.- Utilizando un bucle 'while'")
cont = 1
while cont <= 10:
    print(cont, end=" ")
    cont += 1
print()

# 4.- Bucle for con enumerate()

print("4.- Utilizando bucle for con enumerate")
languages = ["Python", "JavaScript", "C#"]
for indice, language in enumerate(languages, start=1):
    print(f"Lenguaje {indice}: {language}", end=" ")
print()

# 5.- Bucle for con zip()

print("5.- Utilizando bucle for con zip")
nombres = ['Juan', 'María', 'Pedro']
edades = [30, 25, 35]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.", end=" ")
print()

# 6.- Iteradores Personalizados

print("6.- Utilizando iteradores personalizados __iter__() y __next__()")

class Contador:
    def __init__(self, inicio, fin):
        self.actual = inicio
        self.fin = fin
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.actual > self.fin:
            raise StopIteration
        else:
            valor = self.actual
            self.actual += 1
            return valor

contador = Contador(1, 10)
for num in contador:
    print(num, end=" ")
print()

# 7.- Utilizando itertools

print("7.- Utilizando itertools")
import itertools
for i in itertools.count(1):
    if i > 10:
        break
    print(i, end=" ")
print()

# 8.- Bucle for con dict.items()

print("8.- Utilizando bucle for con dict.items")
student = {"name": "Juan", "edad": 30, "lenguaje": "Python"}
for clave, valor in student.items():
    print(f"{clave}: {valor}.", end=" ")
print()

# 9.- Bucle for con set

print("9.- Utilizando un bucle for con set")
languages = {'Python', 'Java', 'JavaScript'}
for language in languages:
    print(language, end=" ")
print()

# 10.- Bucle for con os.listdir()

print("10.- Utilizando un bucle for con os.listdir()")
import os
for archivo in os.listdir():
    print(archivo)
print()

