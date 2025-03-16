'''
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
   que representen todos los tipos de estructuras de control que existan
   en tu lenguaje:
   Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.

DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
'''

# Operators (Operadores)

# Assignment Operators
my_number = 4621
print(f"Assignment (=) {my_number}")
my_number += 13
print(f"Addition and Assignment (+=) {my_number}")
my_number -= 3
print(f"Subtraction and assignment (-=) {my_number}")
my_number *= 3
print(f"Multiplication and assignment (*=) {my_number}")
my_number /= 3
print(f"Division and assignment (/=) {my_number}")
my_number %= 3
print(f"Modulus and assignment (%=) {my_number}")
my_number //= 3
print(f"Floor division and assignment (//=) {my_number}")
my_number **= 3
print(f"Exponentiation and assignment (**=) {my_number}")

# Bitwise AND and assignment (&=)
my_number = 10
my_number &= 3
print(f"Bitwise AND and assignment (&=) {my_number}")

# Bitwise OR assignment (|=)
my_number = 5
my_number |= 3
print(f"Bitwise OR assignment (|=) {my_number}")

# Bitwise XOR assignment (^=)
my_number = 5
my_number ^= 3
print(f"Bitwise XOR assignment (^=) {my_number}")

# Right shift assignment (>>=)
my_number = 5
my_number >>= 3
print(f"Right shift assignment (>>=) {my_number}")

# Left shift assignment (<<=)
my_number = 5
my_number <<= 3
print(f"Left shift assignment (<<=) {my_number}")

# Expression assignment operator (:=)
print(my_new_number := 6)

# Arithmetic Operators

# Addition Operator (+)
age_one = 15
age_two = 20
my_addition = age_one + age_two
print(f"The result of the addition is {my_addition}")

# Subtraction Operator (-)
fathers_age = 42
daughters_age = 8
age_differenece = fathers_age - daughters_age
print(f"The age difference is {age_differenece}")

# Multiplication Operator (*)
apples_per_box = 3
number_of_boxes = 43
total_apples = apples_per_box * number_of_boxes
print(f"The total amount of apples is {total_apples}")

# Exponentiation Operator (**)
my_base = 3
my_exponent = 2
my_result = my_base ** my_exponent
print(f"The result of the exponentiation is {my_result}")

# Division Operator (/)
my_dividend = 540
my_divisor = 9
division_result = my_dividend / my_divisor
print(f"The result of the division is {division_result}")

# Modulus Operator (%)
my_modulus_dividend = 369
my_modulus_divisor = 6
my_modulus = my_modulus_dividend % my_modulus_divisor
print(f"The result of the modulus operation is {my_modulus}")

# Floor Division Operator (//)
number_of_kids = 5
number_of_bananas = 16
bananas_per_kid = number_of_bananas // number_of_kids
print(f"Every kid receives {bananas_per_kid} bananas")

# Comparison Operators
a = 3
b = 9
print(f"Comparison Equal (==) {a == b}")
print(f"Comparison Not equal (!=) {a != b}")
print(f"Comparison Greater than (>) {a > b}")
print(f"Comparison Less than (<) {a < b}")
print(f"Comparison Greater than or equal to (>=) {a >= b}")
print(f"Comparison Less than or equal to (<=) {a <= b}")

# Logical Operators
print(f"Logical operation AND (and) {a < 10 and b < 10}")
print(f"logical operation OR (or) {a > 14 or b > 1}")
print(f"Logical operation NOT (not) {not (a < 4 and b < 10)}")

# Membership Operators
fruits = ["apple", "banana", "cherry"]
print(f"Is there an apple in the fruits basket? {"apple" in fruits}")
print(f"There is not a banana in the fruits basket {"banana" not in fruits}")

# Bitwise Operators

my_number_x = 10
my_number_y = 3
print(f"Bitwise AND (&) {my_number_x & my_number_y}")
print(f"Bitwise OR (|) {my_number_x | my_number_y}")
print(f"Bitwise XOR (^) {my_number_x ^ my_number_y}")
print(f"Signed right shift (>>) {my_number_x >> my_number_y}")
print(f"Zero fill left shift (<<) {my_number_x << my_number_y}")
print(f"Bitwise NOT (~){~ my_number_x}")

# Identity Operators
print(my_number_x is my_number_x)
print(my_number_x is not my_number_x)
print(my_number_x is my_number_y)


""" Control Statements """

my_number_x = 1
my_number_y = 6
# if statement
if my_number_x > my_number_y:
   print(f"{my_number_x} is greater than {my_number_y}")
else:
   print(f"{my_number_y} is grater than {my_number_x}")

# elif statement
if my_number_x > my_number_y:
   print(f"{my_number_x} is grater than {my_number_y}")
elif my_number_x == my_number_y:
   print(f"{my_number_x} is equal to {my_number_y}")
else:
   print(f"{my_number_x} is less than {my_number_y}")
print("\n")

# While loop
while my_number_x < my_number_y:
   print(f"{my_number_x} is less than {my_number_y}")
   my_number_x += 1

#For loop
cars = ["Ford", "Volvo", "BMW"]
for car in cars:
   print(car)

# try cath finally stastements 
try:
   print("Hello")
except:
   print("Something went wrong")
finally:
   print("The 'try except' is finished")

""" Extra
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

for i in range(10, 56):
   if i % 2 == 0:
      if i != 16 and i % 3 != 0:
         print(i)