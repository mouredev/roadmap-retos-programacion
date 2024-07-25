"""
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
"""
# Ejercicio Base y Extra

lista = [1,2,3,4,5,6,7,8,9]

'''Primero: Bucle for'''
for numero in lista:
    print(f"Bucle for: {numero}")

'''Segundo: Bucle while'''
contador = 1
while contador < 10:
    print(f"Bucle while: {contador}")
    contador += 1

'''Tercero: Compresión'''
lista_compres = [print(f"Compresión: {n}") for n in range(1,10)]

'''Cuarto: Map'''
map_print = [print(f"Map: {x}") for x in map(lambda x: x*100,lista)]
map = list(map(lambda x: x*100,lista))

'''Quinto: Iter'''
itinerador = iter(lista)
try:
    while True:
        print(f"Iter: {next(itinerador)}")

except StopIteration:
    pass

'''Sexto: Generador'''
def generador():
    for n in range(1,10):
        yield n
for n in generador():
    print(f"Generador: {n}")

'''Septimo: Zip'''
for n,n_100 in zip(lista,map):
    print(f"Zip: {n} X 100 = {n_100}")

'''Octavo: Enumerate'''
for index,valor in enumerate(lista):
    print(f"Enumerate: {valor}")