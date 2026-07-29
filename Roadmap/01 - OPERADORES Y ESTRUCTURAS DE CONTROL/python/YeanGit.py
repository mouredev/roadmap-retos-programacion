"""
Respuesta al ejercicio 01
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

"""
Operadores
"""

# Operadores aritméticos
sum = 10 + 7
print(f"Suma: 10 + 7 = {10 + 7}")
print(f"Resta: 10 - 7 = {10 - 7}")
print(f"Multiplicación: 10 * 7 = {10 * 7}")
print(f"División: 10 / 7 = {10 / 7}")
print(f"Módulo: 10 % 7 = {10 % 7}")
print(f"Exponente: 10 ** 7 = {10 ** 7}")
print(f"División entera: 10 // 7 = {10 // 7}")

# Operadores de comparación
print(f"Igualdad: 10 == 7 es {10 == 7}")
print(f"Desigualdad: 10 != 7 es {10 != 7}")
print(f"Mayor que: 10 > 7 es {10 > 7}")
print(f"Menor que: 10 < 7 es {10 < 7}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 7 es {10 <= 7}")

# Operadores lógicos
print(f"AND &&: 10 + 7 == 17 and 5 - 1 == 4 es {10 + 7 == 17 and 5 - 1 == 4}")
print(f"OR ||: 10 + 7 == 17 or 5 - 1 == 4 es {10 + 7 == 18 or 5 - 1 == 4}")
print(f"NOT ! : not 10 + 7 == 18 es {not 10 + 7 == 18}") # negación

# Operadores de asignación
my_number = 11 # asignación
print(my_number)
my_number += 1 # suma y asignación
print(my_number)
my_number -= 1 # resta y asignación
print(my_number)
my_number *= 2 # multiplicación y asignación
print(my_number)
my_number /= 2 # división y asignación
print(my_number)
my_number %= 2 # módulo y asignación
print(my_number)
my_number **= 1 # exponente y asignación
print(my_number)
my_number //= 1 # división entera y asignación
print(my_number)

# Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
print(f"'e' in 'yean' = {'e' in 'yeangit'}")
print(f"'z' not in 'yean' = {'z' not in 'yeangit'}")

# Operadores de bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000

"""
Estructuras de control
"""