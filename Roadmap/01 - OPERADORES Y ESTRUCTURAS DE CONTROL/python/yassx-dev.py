"""
OPERADORES
"""


print(f"Suma: 2 + 1 = {2 + 1} ")
print(f"Resta: 2 - 1 = {2 - 1} ")
print(f"Multiplicación: 2 * 1 = {2 * 1} ")
print(f"División: 2 / 1 = {2 / 1} ")
print(f"Módulo: 2 % 1 = {2 % 1} ")
print(f"Exponente 2 ** 2 = {2 ** 2} ")
print(f"División Entera: 2 // 1 = {2 // 1} ")

# Operadores de comparación 

print(f"Igualdad: 6 == 2 es: {6 == 2}")
print(f"Desigualdad: 6 != 2 es: {6 != 2}")
print(f"Mayor que: 6 > 2 es: {6 > 2}")
print(f"Menor que: 6 < 2 es: {6 < 2}")
print(f"Mayor o igual que: 6 >= 2 {6 >= 2}")
print(f"Menor o igual que: 6 <= 2 es: {6 <= 2}")

# Operadores lógicos

print(f"AND: 6 + 2 == 8 and 8 * 2 == 16 es: { 6 + 2 == 8 and 8 * 2 == 16}")
print(f"OR: 2 * 1 == 3 or 3 / 1 == 3 es: {2 * 1 == 3 or 3 / 1 == 3}")
print(f"NOT 2 + 1 == 4 es: {not 2 + 1 == 4}")

# Operadores de asignación

number = 11 # Asignación
print(number)

number += 1 # Suma y Asignación
print(number)

number -= 1 # Resta y Asignación
print(number)

number *= 2 # Multiplicación y Asignación
print(number)

number /= 2 # División y Asignación
print(number)

number %= 2 # Módulo y Asignación
print(number)

number **= 1 # Exponente y Asignación
print(number)

number //= 1 # Division Entera y Asignación
print(number)

# Operadores de Identidad

variable = 1.0
print(f"variable is number es: {variable is number}")
print(f"variable is not number es: {variable is not number}")

# Operadores de Pertenencia 

print(f"'N' in 'Neslin mi amor' es: {'N' in 'Neslin mi amor'}")
print(f"'X' not in 'Neslin mi amor' es: {'X' not in 'Neslin mi amor'}")

# Operadores de Bits

a = 10 # 1010
b = 3 # 0011

print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000

# Condiciionales 

string = "Monica"

if string == "Monica":
    print("string es 'Monica'")
elif string == 'Neslin':
    print("string es: 'Neslin'")
else:
    print("string no es 'Monica' ni 'Neslin'")

# Iterativas

for i in range(7):
    print(i)


num = 2
i = 0
while i <= num:
    print(i)
    i += 1
    
# Manejo de Excepciones

try:
    print(6 / 0)
except:
    print("Se ha producido un error") 
finally:
    print("Ha terminado el manejo de excepciones")  

"""   
EJERCICIO EXTRA
"""

i = 0
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
