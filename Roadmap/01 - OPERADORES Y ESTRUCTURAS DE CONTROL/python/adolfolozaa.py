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
"""

"""
Operadores
"""

print(f"Suma: 10 + 3 = {10 + 3}")
print(f"resta: 10 + 3 = {10 - 3}")
print(f"Multiplicacion: 10 + 3 = {10 * .3}")
print(f"Modulo : 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"Division entera: 10 // 3 = {10 // 3}")


#  Operadores de comparacion

print(f"Iguldad: 10 == 3 es {10 ==3}")
print(f"desiguldad: 10 != 3 es {10 !=3}")
print(f"Mayor que: 10 > 3 es {10 >3}")
print(f"Menor que: 10 < 3 es {10 <3}")
print(f"Mayor o igual que: 10 >= 3 es {10 >=3}")
print(f"Menor o igual que: 10 <= 3 es {10 <=3}")

#  Operadores Logicos

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 4 == 13 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14  es {not 10 + 3 == 14 }")

# Operadores de Asignacion
my_number = 11   # asignacion
print(my_number)

my_number += 1   # suma y asignacion
print(my_number)

my_number -= 1  # resta y asignacion
print(my_number)

my_number *= 2  # Multiplicacion  y asignacion
print(my_number)
my_number /= 2  # division y asignacion
print(my_number)

my_number %= 2  # Modulo y asignacion
print(my_number)

my_number **= 1  # exponencial y asignacion
print(my_number)

my_number //= 1  # division entera y asignacion
print(my_number)


# Operadores de Identidad : compara los valores en memoria
my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")
# Operadores de Pertenencia
print(f"'o' in 'Adolfo = {'o' in 'Adolfo'}")
print(f"'c' not in 'Adolfo = {'c' not in 'Adolfo'}")

#  Operadores de bit

a = 10   # 1010
b = 3   # 0011

print(f"AND: 10 & 3 = {10 & 3}")  #compara bit a bit i si son iguales es 1
print(f"OR: 10 | 3 = {10 | 3}") #compara bit a bit y si alguno es 1 es 1
print(f"XOR: 10 ^ 3 = {10 ^ 3}") #compara bit a bit y si son diferentes es 1
print(f"NOT: ~10 = {~10}") #niega cada uno de los bits

print(f"Desplazamiento a la derecha: 10 >> 2 es {10 >> 2}")
print(f"Desplazamiento a la izquierda: 10 << 2 es {10 << 2}")

""" 
Estructuras de Control
"""
# Condicionales
my_string = "Loza1"
if my_string == "Adolfo":
    print("my_string es 'Adolfo")
elif my_string == "Loza":
    print("my_string es 'Loza'")
else: 
    print("my_string no es 'Adolfo'")

# Iterativas
for i in range(11):
    print(i)

i=0
while i<=10:
    print(i)
    i+=1

# Manejo de excepciones
try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
"""
for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
