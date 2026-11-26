#01 - OPERADORES Y ESTRUCTURAS DE CONTROL

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

# Operadores Aritméticos:
print(f"Suma 4 + 3 =  {4 + 3}")#suma (+)
print(f"Resta 4 - 3 =  {4 - 3}")#resta (-)
print(f"multiplica 4 * 3 =  {4 * 3}")#multiplicación (*)
print(f"divide 4 / 3 =  {4 / 3}")#división (/)
print(f"divide entero 4 // 3 =  {4 // 3}")#división entera (//)
print(f"módulo 10 % 3 =  {10 % 3}")#módulo o residuo (%) es lo que nos queda después de dividir
print(f"exponente 10 ** 3 =  {10 ** 3}")# exponenciación (**).

# Operadores de Comparación
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores Lógicos
print(f"and {True == True and False == False}")#and
print(f"AND && 2 + 3 == 5 and 1 + 2 == 3 {2 + 3 == 5 and 1 + 2 == 3}")#And en representación con números

print(f"OR || {1 < 0 or 0 >= -3}")#O si se cumple una de las condiciones de la operación lógica es True
print(f"OR || 2 + 3 == 5 and 1 + 2 == 4 {2 + 3 == 5 or 1 + 2 == 4}")#Or en representación con números

print(f"NOT ! {not False}")#Not
print(f"NOT ! 1 + 3 == 14 {not 1 + 3 == 14}")#Not representada con números

# Operadores de Asignación.
my_number = 11;#asignación
another_number = 20#otra asignación
print("Operadores de asignación")

print(my_number)
my_number += 1#suma y asignación
print(my_number)
my_number -= 1#resta y asignación
print(my_number)
my_number *= 2#multiplicación y asignación
print(my_number)
my_number /= 2#división y asignación
print(my_number)
my_number %= 2#modulo y asignación
print(my_number)
my_number **= 1#exponente y asignación
print(my_number)
my_number //= 1#división entera y asignación
print(my_number)



# Operadores de identidad
my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}")# a pesar de tener el mismo valor numérico tiene diferente valor de memoria. False porque son diferentes en memoria
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")# True porque ahora apuntan al mismo objeto en memoria

print(f"my_number is my_new_number es {my_number is not my_new_number}")# False porque ahora apuntan al mismo objeto en memoria

#Operadores de Pertenencia
print(f"'a' in 'alexis' {'a' in 'alexis'}")
print(f"'a' not in 'alexis' {'j' not in 'alexis'}")

# Operadores de Bit
#0 1 10 11 100 101 111 1000 1001 1010 1011 1100 de 0 a 12.
a = 10 # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010 = 2 --- si los 2 bits es 1 el resultante es 1
print(f"OR: 10 | 3 = {10 | 3}")   # 1011 = 11 --- si en los 2 bits al menos uno es 1, es 1
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001 = 9 --- va a comparar si los bits son diferentes 1 si son iguales 0
print(f"NOT: ~10 = { ~10 }")      # NOT (~) invierte todos los bits: los 1 pasan a 0 y los 0 a 1. En Python, ~n equivale a -(n + 1), por eso ~10 = -11.
print(f"Desplazamiento a la derecha: 10 >> 2 = { 10 >> 2 } " ) # >> desplaza los bits hacia la derecha. Cada desplazamiento equivale aproximadamente a dividir entre 2. 10 = 1010 → 101 → 10 = 2
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # << desplaza los bits hacia la izquierda. Cada desplazamiento equivale a multiplicar por 2. 10 = 1010 → 10100 → 101000 = 40


"""
Estructura de control.

"""
# Condicionales
my_string = "Alexis-j"

if my_string == "Alexis-j":
    print("my_string es 'Alexis-j'")
elif my_string == "jimenez":
    print("my_string es 'Jimenez'")
else:
    print("my string no es 'Alexis-j' ni 'Jimenez'")


# Iterativas

for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1


# Manejo de excepciones

try:
    print(10 / 1)
except:
    print("Se ha ocurrido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

"""

for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3:
        print(num)
