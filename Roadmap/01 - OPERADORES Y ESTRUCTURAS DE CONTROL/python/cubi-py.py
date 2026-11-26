### Operadores Aritméticos ###

print(f"suma: 2 + 3 = {2 + 3}") # suma
print(f"resta: 2 - 3 = {2 -3}") # resta
print(f"multiplicación: 2 * 3 = {2 * 3}") # multiplicación
print(f"división: 2 / 3 = {2 / 3}") # división
print(f"módulo de: 6 % 4 = {6 % 4}") # módulo o resto
print(f" división de piso: 6 // 4 = {6 // 4}") # división de piso
print(f"exponenciación: 2 ** 3 = {2 ** 3}") # exponenciación

### Operadores Comparativos ###

print(f"mayor que: 5 > 7 = {5 > 7}") # mayor que
print(f"menor que: 5 < 7 = {5 < 7}") # menor que
print(f"mayor o igual que: 5 >= 7 = {5 >= 7}") # mayor o igual que
print(f"menor o igual que: 5 <= 7 = {5 <= 7}") # menor o igual que
print(f"igual que: 5 == 7 = {5 == 7}") # igual que
print(f"distinto de: 5 != 7 = {5 != 7}") # distinto de 

### Operadores Lógicos ###

print(f"AND &&: 2 > 1 and 3 < 2 es {2 > 1 and 3 < 2}")
print(f"OR ||: 2 > 1 or 3 < 2 es {2 > 1 or 3 < 2}")
print(f"NOT !: not(3 < 2) es {not(3 < 2)}")

"""
(DIFICULTAD EXTRA)
Crear un programa que imprima todos los números comprendidos entre 10 y 55 (incluidos),
pares, y que no son ni el 16 ni múltiplos de 3.
"""
print("Números del 10 al 55 sin el 16 ni los múltiplos de 3")

numero = 10

while numero >= 10 and numero <= 55:
    if(numero % 3 != 0 and numero != 16):
        print(numero)
        numero = numero + 1
    else: numero = numero + 1


