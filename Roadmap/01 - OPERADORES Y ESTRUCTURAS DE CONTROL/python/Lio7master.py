'''
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
'''
"""
OPERADORES
"""
#Operadores aritméticos
print("Operadores aritméticos")

print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"División entera: 10 // 3 = {10 // 3}") #La división entera es la parte entera de la división
print(f"Modulo: 10 % 3 = {10 % 3}") #El modulo es el resto de la división
print(f"Potencia: 10 ** 3 = {10 ** 3}")
print(f"Raíz cuadrada: 10 ** (1/2) = {10 ** (1/2)}")
print(f"Raíz cúbica: 10 ** (1/3) = {10 ** (1/3)}")
#Raízes a la n: 10 ** (1/n) = {10 ** (1/n)})

#Operadores de comparación
print("Operadores de comparación")
print(f"Mayor que: 10 > 3 = {10 > 3}")
print(f"Menor que: 10 < 3 = {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 = {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 = {10 <= 3}")
print(f"Igual que: 10 == 3 = {10 == 3}")
print(f"Diferente que: 10 != 3 = {10 != 3}")

print("Operadores lógicos")
print(f"AND &&: 10 +3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14  or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es { not 10 + 3 == 14}")

#Operadores de asignacion
my_number = 11 #asiganación
print(my_number)
my_number += 1#Suma y asignación
print(my_number)
my_number -= 1 #Resta y asignación
print(my_number)
my_number *= 2 #Multiplicación y asignación
print(my_number)
my_number /=2 #División y asignación
print(my_number)
my_number %= 2 #Modulo y asignación
print(my_number)
my_number **= 2 #Exponenete y asignación
print(my_number)
my_number //= 1 #Division enterea y asignación
print(my_number)

#Operadores de identidad 
my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}") #Es False porque aunque tienen el mismo valor ocupan diferentes direciones de memoria

my_new_var = my_number

print(f"my_new number is my_number es: {my_new_number is my_new_number}") #Ahora si es true porque hemos indicado que se apunte el mismo valor de memoria
print(f"my_new number is not my_number es: {my_new_number is not my_new_number}")

#Operadores de pertenencia
print(f"'m' in 'Lio7master' = {'m' in 'Lio7master'}")
print(f"'u' not in 'Lio7master' = {'u' not in 'Lio7master'}")

#Operadores de bit
a = 10 # 1010
b = 3 # 0011

print(f"AND: 10 & 3= {10 & 3}") # 0010 el resultado devuelve en bit la comparacion
print(f"OR: 10 | 3= {10 & 3}") # 1011
print(f"XOR: 10 ^ 3= {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}") # 0101
print(f"Dezplazamiento a la derecha: 10 >> 2 = {10 >> 2}")# 0010
print(f"Dezplazamiento a la izquierda: 10 >> 2 = {10 << 2}")# 101000

"""
ESTRUCTURAS DE CONTROL
"""

#Condicionales
my_string = "Lio7master"

if my_string == "Leonardo":
    print("my_string es 'Leonardo'")
elif my_string == "Lio7master":
    print("my_string es 'Lio7master'")
else:
    print("my_string no es 'Leonardo' ni es 'Lio7master")

#Interactivas
for i in range(11): #Range excluye el ultimo numero indicado siendo el 11 el resultado dara 10
    print(i)

i = 0
while (i<= 10):
    print(i)
    i += 1

#Manejo de excepciones
try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("finalizado el manejo de excepciones")