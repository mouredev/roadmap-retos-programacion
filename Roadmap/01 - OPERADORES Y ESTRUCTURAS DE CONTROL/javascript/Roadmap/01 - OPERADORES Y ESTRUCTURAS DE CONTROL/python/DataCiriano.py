"""
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""

# Operadores Aritméticos

print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"Módulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"División entera: 10 // 3 = {10 // 3}")


# Operadores Comparación

print(f"Igualdad: 5 == 7 {5 == 7}")
print(f"Desigualdad: 5 != 7 {5 != 7}")
print(f"Mayor que: 5 > 7 {5 > 7}")
print(f"Menoror que: 5 < 7 {5 < 7}")
print(f"Mayor o igual que: 5 >= 7 {5 >= 7}")
print(f"Menor o igual que: 5 <= 7 {5 <= 7}")


# Operadores lógicos

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")


# Operadores de asignación

number = 15  # asignación
print(number)
number += 1  # suma y asignación
print(number)
number -= 1  # resta y asignación
print(number)
number *= 2  # multiplicación y asignación
print(number)
number /= 2  # división y asignación
print(number)
number %= 2  # módulo y asignación
print(number)
number **= 1  # exponente y asignación
print(number)
number //= 1  # división entera y asignación
print(number)

# Operadores de identidad

new_number = number
print(f"number is new_number es {number is new_number}")
print(f"number is not new_number es {number is not new_number}")


# Operadores de bit

a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000


#Estructuras de control

#Condicionales

variable = 7

if variable > 10:
    print("La variable es mayor a 10")
elif variable < 10:
    print("La variable es menor a 10")
else:
    print("La variable es 10")
    
# Iterativos

for i in range(0,11,2):
    print(i)
    
iteracion = 1
    
while iteracion <= 10:
    print(f"Iteración: {iteracion}")
    iteracion += 1
    
#Manejo de excepciones

try:
    print(10/0)
except:
    print("Se produjo un error")
finally:
    print("Fin del contro de excepciones")
    
    
# Extra

for i in range(10,56):
    if i % 2 == 0 and i != 16 and not i % 3 == 0:
        print(i) 