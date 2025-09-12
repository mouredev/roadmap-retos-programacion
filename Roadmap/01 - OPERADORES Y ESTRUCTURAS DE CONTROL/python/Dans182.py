"""
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

# Operadores

## Operadores aritméticos

suma = 2 + 2
print("Suma: 2 + 2 =", suma)

resta = 2 - 2
print("Resta: 2 - 2 =", resta)

multiplicación = 2 * 2
print("Multiplicación: 2 * 2 =", multiplicación)

division = 2 / 2
print("Division: 2 / 2 =", division)

modulo = 10 % 3 #El resto de la división
print("Módulo: 10 % 3 =", modulo)

potencia = 10 ** 3
print("Exponente: 10 ** 3 =", potencia)

division_entera = 10 // 3 #El resultado nos tiene que dar un n1 redondeado, entero. Evita la parte decimal.
print("Division Entera: 10 / 3 =", division_entera)

## Operadores de comparación

print(f"Operador de igualdad: 10 == 3: {10 == 3}")
print(f"Operador de desigualdad: 10 != 3: {10 != 3}")
print(f"Mayor que: 10 > 3: {10 > 3}")
print(f"Menor que: 10 < 3: {10 < 3}")
print(f"Mayor o igual que: 10 >= 3: {10 >= 3}")
print(f"Menor o igual que : 10 <= 3: {10 <= 3}")

## Operadores lógicos

print(f"And &&: 10 > 3 and 8 < 19: {10 > 3 and 8 < 19}")
print(f"Or ||: 10 > 3 and 8 > 19: {10 > 3 or 8 > 19}")
print(f"NOT !: 10 + 3 = 14: {not 10 + 3 == 14}")

## Operadores de asignación

my_number = 18 #asignacion
print(my_number)

my_number += 1 #suma y asignacion
print(my_number)

my_number -= 1 #resta y asignacion
print(my_number)

my_number *= 1 #multiplicacion y asignacion
print(my_number)

my_number /= 1 #division y asignacion
print(my_number)

my_number %= 1 #modulo y asignacion
print(my_number)

my_number **= 1 #exponente y asignacion
print(my_number)

my_number //= 1 #division entera y asignacion
print(my_number)

my_number_three = 3
print(my_number_three)

my_number_three &= 1 # y asignacion
print(my_number_three)

my_number_three |= 1 # y asignacion
print(my_number_three)

my_number_three ^= 1 # y asignacion
print(my_number_three)

my_number_three >>= 1 # y asignacion
print(my_number_three)

my_number_three <<= 1 # y asignacion
print(my_number_three)

## Operadores de identidad

#Los valores de identidad lo que buscan es comparar es el valor en memoria.
#Por eso dando el mismo valor, da false. Porque tienen direcciones en la memoria distintas
my_new_number = 0.0
print(my_number)
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_new_number is my_new_number es {my_new_number is my_new_number}")

## Operadores de pertenencia

print(f" 'd' in 'dans182' = {'d' in 'dans182'}")
print(f" 'd' not in 'dans182' = {'d' not in 'dans182'}")

## Operadores bit a bit
#8421
a = 10 #1010
b = 3  #0011

print(f"AND: 10 & 3 = {10 & 3}") #0010 -> 2 en decimal Compara bit a bit, y si los dos bits son "uno", devuelve uno
print(f"OR: 10 | 3 = {10 | 3}") #1011 -> 11 en decimal Compara bit a bit, y si al menos uno de los dos bits es uno, devuelve uno
print(f"XOR: 10 ^ 3 = {10 ^ 3}") #0101 -> 9 en decimal Compara bit a bit, y si los bits son diferentes, devuelve uno
print(f"NOT: ~10 = {~10}") #Invierte cada bit en el operando
print(f"Dezplazamiento a la derecha: 10 >> 2 = {10 >> 2}") #1010 >> 2 -> 0010 (2) 
print(f"Dezplazamiento a la izquierda: 10 << 2 = {10 << 2}") #1010 << 2 -> 101000 (40) 


## Operadores de pertenencia


# Estructuras de Control

##Condicioneales.

## If

my_string = "Dans182"

if my_string == "Dans182":
    print("my_string es 'Dans182'")
elif my_string == "Daniel":
    print("my_string es 'Daniel'")
else:
    print("my_string no es 'Dans182' ni 'Daniel'")

## Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

## Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)