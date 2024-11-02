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

#* Lógicos
print()
print("OPERADORES LÓGICOS")
print(f"{num_1} es igual a {num_2} y {num_2} es igual a {num_3}: {num_1 == num_2 and num_2 == num_3}")
print(f"{num_1} es menor {num_2} o {num_2} es igual a {num_3}: {num_1 < num_2 or num_2 == num_3}")
print(f"{num_1} no es igual a {num_2}: {not num_1 ==  num_2}")

#* Comparación
print()
print("OPERADORES DE COMPARACIÓN")
print(f"Igual que {num_1} == {num_2}: {num_1 == num_2}")
print(f"Distinto de {num_1} != {num_2}: {num_1 != num_2}")
print(f"Mayor que {num_1} > {num_2}: {num_1 > num_2}")
print(f"Menor que {num_1} < {num_2}: {num_1 < num_2}")
print(f"Mayor o igual que {num_1} >= {num_2}: {num_1 >= num_2}")
print(f"Menor o igual que {num_1} <= {num_2}: {num_1 <= num_2}")

#* Asignación
print()
print("OPERADORES DE ASIGNACIÓN")
num_1 = 25
print(f"asignar un valor 25: {num_1}")
num_1 += 2
print(f"sumar dos: {num_1}")
num_1 -= 2
print(f"restar dos: {num_1}")
num_1 *= 4
print(f"multiplicar por cuatro: {num_1}")
num_1 /= 1
print(f"dividir entre uno: {num_1}")
num_1 //= 2
print(f"división entera entre dos: {num_1}")
num_1 %= 3
print(f"Modulo de tres: {num_1}")
num_1 **= 3
print(f"elevación al cubo: {num_1}")

#* Identidad
print()
print("OPERADORES DE IDENTIDAD")
objeto_1 = [1,2,3]
objeto_2 = objeto_1
objeto_3 = [1,2,3]
print(f"objeto_2 se refiere al mismo objeto que objeto_1: {objeto_1 is objeto_2}")
print(f"objeto_3 no se refiere al mismo objeto que objeto_1: {objeto_3 is not objeto_1}")

