""" /*
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
 */ """

num_1 = 24
num_2 = 54
num_3 = 2.45

#* Aritméticos
print()
print("OPERADORES ARITMÉTICOS")
print(f"Esto es una suma {num_1} + {num_2}: {num_1 + num_2}")
print(f"Esto es una resta {num_1} - {num_2}: {num_1 - num_2}")
print(f"Esto es una división {num_1} / {num_2}: {num_1 / num_3}")
print(f"Esto es una división entera {num_1} // {num_2}: {num_1 // num_3}")
print(f"Esto es una multiplicación {num_1} * {num_2}: {num_1 * num_2}")
print(f"Esto es modulo o resto {num_1} % {num_2}: {num_1 % num_3}")
print(f"Esto es una potencia {num_1} ** {num_2}: {num_1 ** num_3}")

#* Comparación
print()
print("OPERADORES DE COMPARACIÓN")
print(f"Igual que {num_1} == {num_2}: {num_1 == num_2}")
print(f"Distinto de {num_1} != {num_2}: {num_1 != num_2}")
print(f"Mayor que {num_1} > {num_2}: {num_1 > num_2}")
print(f"Menor que {num_1} < {num_2}: {num_1 < num_2}")
print(f"Mayor o igual que {num_1} >= {num_2}: {num_1 >= num_2}")
print(f"Menor o igual que {num_1} <= {num_2}: {num_1 <= num_2}")
