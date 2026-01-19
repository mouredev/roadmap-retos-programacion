# Operadores y estructuras de control

# Operadores aritméticos

print(f"Suma 3 + 4: {3 + 4}")
print(f"Resta 5 - 1: {5 - 1}")
print(f"Multiplicación 2 * 6: {2 * 6}")
print(f"División 10 / 2: {10 / 2}")
print(f"Módulo 10 % 3: {10 % 3}")
print(f"Exponente 2 ** 4: {2 ** 4}")
print(f"División entera 10 // 3: {10 // 3}")

# Operadores comparativos

print(3 < 5)
print(3 > 5)
print(3 == 5)
print(3 != 5)
print( 3<= 5)
print(3 >= 5)

# Operadores lógicos

print((3 < 4) and (5 > 2))
print((3 > 5) or (5 > 1))
print(not(5 > 2))

# Operadores de asignación

my_number = 11
my_number += 1 # Suma y asignación
print(my_number)
my_number -= 1 # Resta y asignación
print(my_number)
my_number *= 2 # Multiplicación y asignación
print(my_number)
my_number /= 2 # División y asignación
print(my_number)
my_number %= 2 # Módulo y asignación
print(my_number)
my_number **= 1 # Exponente y asignación
print(my_number)
my_number //= 1 # Dvisión entera y asignación
print(my_number)

# Operadores de identidad

my_new_number = my_number
print(f"my_new_number is my_number es {my_new_number is my_number}")
print(f"my_new_number is not my_number es {my_new_number is not my_number}")

# Operadores de pertenencia

print(f"'a' in 'David' es {'a' in 'David'}")
print(f"'c' not in 'David' es {'c' not in 'David'}")

# Operadores de bit

a = 10
b = 3
print(f"AND 10 & 3 = {10 & 3}")
print(f"OR 10 | 3 = {10 | 3}")
print(f"XOR 10 ^ 3 = {10 ^ 3}")
print(f"NOT ~10 = {~10}")
print(f"Desplazamiento a la derecha 10 >> 2 = {10 >> 2}")
print(f"Desplazamiento a la izquierda 10 << 2 = {10 << 2}")

# Estructuras de control

# Condicionales

my_name = "David"
if my_name == "David":
    print("Mi nombre es David")
elif my_name == "Oriol":
    print("Mi nombre es Oriol")
else:
    print("Mi nombre no es ni David ni Oriol")

# Iterativas

for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones

try:
    print (10 / 0)
except: 
    print("Error división entre 0")
finally:
    print("Finalizado el manejo de excepciones")

# Ejercicio extra

for number in range(10, 56):
    if((number %2 == 0) and (number != 16) and (number %3 != 0)):
        print(number)