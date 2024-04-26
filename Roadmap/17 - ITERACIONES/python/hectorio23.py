# /bin/python3
# Author: Héctor Adán
# GitHub: https://github.com/hectorio23
'''
EJERCICIO:
Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
números del 1 al 10 mediante iteración.

DIFICULTAD EXTRA (opcional):
Escribe el mayor número de mecanismos que posea tu lenguaje
para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
'''

##################################################################
############################ EJERCICIO ###########################
##################################################################
print("[ Mecanismo 1 ] -> objeto range") # objeto RANGE
for element in range(1, 11):
    print(element, end=", ")

print("\n\n[ Mecanismo 2 ] -> usando una lista") # lista por comprension -> lista normal
for element in [item for item in range(1,11)]:
    print(element, end=", ")

print("\n\n[ Mecanismo 3 ] -> usando un set") # set por comprension -> set normal
for element in {item for item in range(1,11)}:
    print(element, end=", ")

print("\n\n[ Mecanismo 4 ] -> usando un diccionario") # dictionary por comprension -> dictionary normal
for element in {item:item for item in range(1,11)}:
    print(element, end=", ")

print("\n\n[ Mecanismo 5 ] -> usando una cadena") # iterar los elementos de una cadena 
for element in "0123456789":
    print(int(element) + 1, end=", ")

print("\n\n[ Mecanismo 6 ] -> usando recursividad") # recursivo n veces -> en python el limite por defecto es 1,000
def recursivo(n):
    print(n, end=", ")

    if n == 1:
        return 1
    
    return n * recursivo(n - 1)

recursivo(10)

print("\n\n[ Mecanismo 7 ] -> usando un 'iterator'") # usando iterador
for element in iter(range(1,11)): 
    print(element, end=', ')

print("\n\n[ Mecanismo 8 ] -> usando zip") # usando zip
for element in zip(range(1,11), [x for x in range(1,11)]):
    print(element[0], end=', ')

print("\n\n[ Mecanismo 9 ] -> usando enumerate") # usando enumerate
for element in enumerate([x for x in range(1,11)], 1):
    print(element[0], end=', ')

print("\n\n[ Mecanismo 10 ] -> usando bucle while")
n = 1
while n <= 10:
    print(n, end=', ')
    n += 1
log = lambda value: print(value, end=', ') 
print("\n\n[ Mecanismo 11 ] -> usando la funcion map")
list(map(log, [ x for x in range(1, 11) ] ))


