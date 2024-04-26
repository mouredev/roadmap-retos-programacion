# #17 ITERACIONES
"""
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 """


print ("-"*60)
print ("Bucle While")

i=0
while i<10:
    print (f"Number: {i+1}")
    i +=1

print ("-"*60)
print ("Bucle For")

for i in range (10):
    print (f"Number: {i+1}")


print ("-"*60)
print ("Recursividad")

def contador(cont):
    if cont<11:
        print (f"Number: {cont}")
        cont+=1
        contador(cont)
contador(1)


"""
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
 """

print ("-"*60)
print ("While Infinito con break")

i=0
while True:
    if i<10:
        print (f"Number: {i+1}")
        i+=1
    else:
        break

print ("-"*60)
print ("Iterables")

mytuple = (1,2,3,4,5,6,7,8,9,10)
myit = iter(mytuple)

for i in range (len(mytuple)):
    print (next(myit))


print ("-"*60)
print ("Clases")

class Numbers:
    def __init__(self,number) -> None:
        self.number=number
        
    def print_numbers(self):
        for i in range (self.number):
                print (i+1)


cont = Numbers(10)
cont.print_numbers()

print ("-"*60)
print ("Compresión de Listas")

cont = [x+1 for x in range (10)]
for i in cont:
    print (i)

print ("-"*60)
print ("Con Numpy")

import numpy as np

def cont_numpy(cont):
    cont = np.array([i+1 for i in range (cont)])
    print (cont)
cont_numpy(10)

cont2 = np.arange(1,11)
for i in range (len(cont2)):
    print (cont2[i])