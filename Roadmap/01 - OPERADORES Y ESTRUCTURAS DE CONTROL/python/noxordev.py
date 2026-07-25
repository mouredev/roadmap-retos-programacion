""" 
Operadores 
"""

# Operadores aritméticos
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"División entera: 10 // 3 = {10 // 3}")
print(f"Módulo: 10 % 3 = {10 % 3}")
print(f"Potencia: 10 ** 3 = {10 ** 3}")

# Operadores de comparación
print(f"Igualdad: 10 == 3 = {10 == 3}")
print(f"Desigualdad: 10 != 3 = {10 != 3}")
print(f"Mayor que: 10 > 3 = {10 > 3}")
print(f"Menor que: 10 < 3 = {10 < 3}")

base = 10
exponente = 3
print(f"Potencia: {base} ** {exponente} = {base ** exponente}")
print(f"Módulo: {base} % {exponente} = {base % exponente}")
print(f"División entera: {base} // {exponente} = {base // exponente}")

#Operadores lógicos
print(f"AND: 10 + 3 == 13 and 5 - 1 = {10 + 3 == 13 and 5 - 1 == 4}")
print(f"AND: 10 > 3 and 10 < 3 = {10 > 3 and 10 < 3}")
print(f"OR: 10 > 3 or 10 < 3 = {10 > 3 or 10 < 3}")
print(f"NOT: not 10 > 3 = {not 10 > 3}")

#Operadores de asignación
my_number = 10 #asignación
print(my_number)
my_number += 1 #suma y asignación
print(my_number)
my_number -= 1 #resta y asignación
print(my_number)
my_number *= 2 #multiplicación y asignación
print(my_number)
my_number /= 2 #división y asignación
print(my_number)
my_number %= 2 #módulo y asignación
print(my_number)
my_number **= 1 #exponente y asignación
print(my_number)
my_number //= 1 #división entera y asignación   
print(my_number)

#Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

#Operadores de pertenencia
print(f"'a' in 'apple' es {'a' in 'apple'}")
print(f"10 in [1, 2, 3, 4, 5] es {10 in [1, 2, 3, 4, 5]}")
print(f"10 not in [1, 2, 3, 4, 5] es {10 not in [1, 2, 3, 4, 5]}")

#Operadores de bit a bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}") # -11
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 10: 1010 >> 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 10: 1010 >> 101000

"""
Estructuras de control
"""

# Condicionales
my_string = "Victor"

if my_string == "MoureDev":
    print("my_string es 'MoureDev'")
elif my_string == "Victor":
    print("my_string es 'Victor'")
else:
    print("my_string no es 'MoureDev' ni 'Brais'")

# Iterativas

for i in range(5):
    print(i)

i = 0
while i <= 5:
    print(i)
    i += 1

# Manejo de excepciones

try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

# Extra

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
