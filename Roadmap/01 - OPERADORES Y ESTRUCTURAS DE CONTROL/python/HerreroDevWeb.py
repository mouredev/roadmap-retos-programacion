# https://www.python.org

'''
Operadores
'''

print(f"Suma: 20 + 5 = {20 + 5}") # Interpolar valores, imprimir texto y codigo
print(f"Resta: 20 - 5 = {20 - 5}")
print(f"Multiplicación: 20 * 5 = {20 * 5}")
print(f"División: 20 / 5 = {20 / 5}")
print(f"Módulo: 20 % 5 = {20 % 5}")
print(f"Exponente: 20 ** 5 = {20 ** 5}")
print(f"División entera: 20 // 5 = {20 // 5}")

# Operadores de comparación
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores lógicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 13 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignación
my_number = 7 # Asignación
print(my_number)
my_number += 2 # suma y asignación
print(my_number)
my_number -= 4 # resta y asignación
print(my_number)
my_number *= 6 # multiplicación y asignación
print(my_number)
my_number /= 6 # división y asignación
print(my_number)
my_number %= 2 # módulo y asignación
print(my_number)
my_number **= 2 # exponente y asignación
print(my_number)
my_number //= 6 # división entera y asignación
print(my_number)

# Operadores de identidad
my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number} ")
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number} ")
print(f"my_number is not my_new_number es {my_number is not my_new_number} ")

# Operadores de pertenencia
print(f"'a' in 'Carlos' = {'a' in 'Carlos'}")
print(f"'b' in 'Carlos' = {'b' in 'Carlos'}")

# Operadores de bit
a = 10 # 1010
b = 4 # 0100
print(f"AND: 10 & 4 = {10 & 4}")
print(f"OR: 10 | 4 = {10 | 4}")
print(f"XOR: 10 ^ 4 = {10 ^ 4}")
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 4 = {10 >> 4}")
print(f"Desplazamiento a la izquierda: 10 << 4 = {10 << 4}")

'''
Estructuras de control
'''

# Condicionales

my_string = "HerreroDevWeb"
my_string = "Carlos"

if my_string == "HerreroDevWeb":
    print("my_string es 'HerreroDevWeb'")
elif my_string == "Carlos":
    print("my_string es 'Carlos'")
else:
    print("my_string no es 'HerreroDevWeb' ni 'Carlos'")


# Iterativas
for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

'''
Estructura de control extra
'''

for number in range (10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)