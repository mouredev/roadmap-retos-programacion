"""
#01 OPERADORES Y ESTRUCTURAS DE CONTROL
"""

# EJERCICIO:
# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)


# Operadores Aritméticos
print(f"1 + 2 = {1 + 2}")
print(f"5 - 4 = {5 - 4}")
print(f"10 * 2 = {10 * 2}")
print(f"10 / 2 = {10 / 2}")
print(f"7 / 5 = {7 / 5}")
print(f"7 % 5 = {7 % 5}")

print(f"2 ** 10 = {2 ** 10}")
print(f"7 // 5 = {7 // 5}")
print()

# Operadores de asignación
my_number = 200
print(f"my_number = {my_number}")
my_number += 100
print(f"my_number += 100 = {my_number}")
my_number -= 200
print(f"my_number -= 200 = {my_number}")
my_number *= 5
print(f"my_number *= 5 = {my_number}")
my_number /= 5
print(f"my_number /= 5 = {my_number}")
my_number %= 6
print(f"my_number %= 6 = {my_number}")
my_number **= 4
print(f"my_number **= 4 = {my_number}")
my_number //= 3
print(f"my_number //= 3 = {my_number}")
print()

# Operadores de comparación
print("Comparando cantidad de caracteres:")
my_str_1 = "ajedrez"
my_str_2 = "damas"
my_str_3 = "parchis"
print(f"'ajedrez' > 'damas' is {len(my_str_1) > len(my_str_2)}")
print(f"'ajedrez' < 'damas' is {len(my_str_1) < len(my_str_2)}")
print(f"'ajedrez' >= 'damas' is {len(my_str_1) >= len(my_str_2)}")
print(f"'ajedrez' <= 'damas' is {len(my_str_1) <= len(my_str_2)}")
print(f"'ajedrez' == 'parchis' is {len(my_str_1) == len(my_str_3)}")
print(f"'ajedrez' != 'parchis' is {len(my_str_1) != len(my_str_3)}")
print()

# Operadores Lógicos
a = 1
b = 2
c = 3

print(f"a = {a}, b = {b}, c = {c}")
print(f"c > b and c > a is {c > b and c > a}")
print(f"a < b and a == c is {a < b and a == c}")
print(f"c >= b or c <= a is {c >= b or c <= a}")
print(f"a >= b or a == c is {a >= b or a == c}")
print(f"not c > b and c > a is {not c > b and c > a}")
print(f"not a >= b or a == c is {not a >= b or a == c}")
print(f"not True is {not True}")
print(f"not not not False is {not not not False}")
print()

# Operadores de identidad
d = 3
e = c

print(f"c = {c}, d = {d}, e = c")
print(f"d is e? {d is e}")
print(f"d is c? {d is c}")
print(f"e is c? {e is c}")

print(f"c is not e? {c is not e}")
print(f"c is not d? {c is not d}")
print(f"e is not d? {e is not d}")
print()

# Operadores de pertenencia
fruits = ["apple", "banana", "cherry"]

print(f"fruits: {fruits}")
print(f"'banana' in fruits? {'banana' in fruits}")
print(f"'pear' in fruits? {'pear' in fruits}")
print(f"'pineapple' not in fruits? {'pineapple' not in fruits}")
print(f"'cherry' not in fruits? {'cherry' not in fruits}")

# Operadores de bits
x = 2 # 0010
y = 1 # 0001

print(f"x = {x}, y = {y}")
print(f"x & y = {x & y}")   # 0000 
print(f"x | y = {x | y}")   # 0011
print(f"x ^ y = {x ^ y}")   # 0011
print(f"~x = {~x}")         # 1101
print(f"~y = {~y}")         # 1110
print(f"x << 1 = {x << 1}") # 0100
print(f"x >> 1 = {x >> 1}") # 0001
print(f"y << 1 = {y << 1}") # 0010
print(f"y >> 1 = {y >> 1}") # 0000
print()

# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
#   Condicionales, iterativas, excepciones...

# Condicionales
username = "HaloGabriel"
is_admin = True

if username == "admin" or is_admin:
    print("Access Granted!");
else:
    print("Access Denied!")
print()

puntaje = 15

if (puntaje == 20):
    print("¡Nota perfecta!")
elif (puntaje >= 13):
    print("¡Aprobado!")
else:
    print("¡Sigue estudiando!")
print()

# Iterativas
for number in range(1, 21):
    if number % 2 == 0:
        print(f"{number} es par")
    else:
        print(f"{number} es impar")
print()

my_other_number = 1
while my_other_number <= 100:
    print(my_other_number)
    my_other_number += 1
    if (my_other_number == 25):
        print("25 encontrado")
        break
print()

# Excepciones

my_str_4 = "4"
try:
    result = int(my_str_4)
    print(f"result es un int: {result}")
except:
    result = len(my_str_4)
    print(f"my_str_4 es un str con {result} caracteres")
finally:
    print("¡Prueba terminada!")
print()

# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

conteo = 0
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        conteo += 1
        print(number)
print(f"Total de matches: {conteo}")