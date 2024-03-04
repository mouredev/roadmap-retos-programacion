import Foundation

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


# Operadores aritméticos
suma = 5 + 3
resta = 10 - 2
multiplicacion = 4 * 6
division = 15 / 3
modulo = 7 % 2
potencia = 2 ** 4

print("Operadores aritméticos:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potencia:", potencia)

# Operadores lógicos
and_resultado = True and False
or_resultado = True or False
not_resultado = not True

print("\nOperadores lógicos:")
print("AND:", and_resultado)
print("OR:", or_resultado)
print("NOT:", not_resultado)

# Operadores de comparación
igual = 5 == 5
distinto = 5 != 10
mayor = 10 > 5
menor = 3 < 8
mayor_o_igual = 7 >= 7
menor_o_igual = 6 <= 6

print("\nOperadores de comparación:")
print("Igual:", igual)
print("Distinto:", distinto)
print("Mayor:", mayor)
print("Menor:", menor)
print("Mayor o igual:", mayor_o_igual)
print("Menor o igual:", menor_o_igual)

# Operadores de asignación
x = 5
x += 3
x -= 2
x *= 4
x /= 2

print("\nOperadores de asignación:", x)

# Operadores de identidad
a = [1, 2, 3]
b = [1, 2, 3]
identidad = a is b
no_identidad = a is not b

print("\nOperadores de identidad:")
print("Identidad:", identidad)
print("No identidad:", no_identidad)

# Operadores de pertenencia
lista = [1, 2, 3, 4, 5]
pertenencia = 3 in lista
no_pertenencia = 6 not in lista

print("\nOperadores de pertenencia:")
print("Pertenencia:", pertenencia)
print("No pertenencia:", no_pertenencia)

# Operadores de bits
bitwise_and = 5 & 3
bitwise_or = 5 | 3
bitwise_xor = 5 ^ 3
bitwise_not = ~5
shift_izquierda = 5 << 1
shift_derecha = 5 >> 1

print("\nOperadores de bits:")
print("AND:", bitwise_and)
print("OR:", bitwise_or)
print("XOR:", bitwise_xor)
print("NOT:", bitwise_not)
print("Shift izquierda:", shift_izquierda)
print("Shift derecha:", shift_derecha)

# Estructuras de control

# Condicionales
if 5 > 3:
    print("\nCondicionales:")
    print("5 es mayor que 3")

# Iterativas
print("\nIterativas:")
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)

# Excepciones
print("\nExcepciones:")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: división por cero")
