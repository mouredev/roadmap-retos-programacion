"""
EJERCICIO:
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
"""

print("Aritmeticos")
num01 = 10
num02 = 3
print(f"Suma: {num01 + num02}")
print(f"Resta: {num01 - num02}")
print(f"Multiplicación: {num01 * num02}")
print(f"División: {num01 / num02}")
print(f"División Entera: {num01 // num02}")
print(f"Potencia: {num01 ** num02}")
print(f"Residuo: {num01 % num02}")

print("\nOperadores Lógicos")
#AND -> si ambos son TRUE el resultado es TRUE si no el resultado será FALSE
print(f"AND: True and True -> {True and True}, True and Flase -> {True and False}")
#OR -> si ambos son FALSE el resultado es FALSE si no el resultado será TRUE
print(f"OR: False or False -> {False or False}, True or Flase -> {True or False}")
#NOT -> Invierte los valores TRUE -> FALSE, FALSE -> TRUE
print(f"NOT: not True -> {not True}, not False -> {not False}")

print("\nOperadores de comparación")
# Mayor ">" => si el de la izquierda es mayor al de la derecha resultara TRUE si no sera FALSE
print(f"Mayor > : 10>5 -> {10>5}, 5>15 -> {5>15}")
# Menor "<" => si el de la izquierda es menor al de la derecha resultara TRUE si no sera FALSE
print(f"Menor < : 10<5 -> {10<5}, 5<15 -> {5<15}")
# Igual "==" => Si son iguales obtendra TRUE si no FALSE
print(f"Igual == : Bryan == Bryan -> {'Bryan' == 'Bryan'}, Bryan == Bryat -> {'Bryan' == 'Bryat'}")
# Distintos "!=" => Si son diferentes obtendra TRUE si no FALSE
print(f"Distinto != : 24 != 24 -> {24 != 24}, 15 != 16 -> {15 != 16}")

print("\nAsignación")
x = 5
print(f"Asignar valor : x=5 -> {x}")
x += 3
print(f"Asignar equivalente : x+=3 -> {x}")

print("\nIdentidad")
a = 2
b = 3
c = 2
print(f"Si 'a' es igual a b {a is b} o es igual a c {a is c}")

print("\nPertenencia")
p1 = [1, 2, 3, 5]
p2 = 2
p3 = 4
print(f"Si 'p2' pertenece a 'p1' {p2 in p1} o 'p3' pertenece a 'p1' {p3 not in p1}")

result = []
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        result.append(i)
    if i == 55:
        result.append(i)
print(f"\nExtra: {result}")