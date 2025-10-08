"""
Operadores
"""

# Operadores aritmeticos
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicacion: 10 * 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Modulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"Division entera: 10 // 3 = {10 // 3}")

# Operadores de comparacion
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor que: 10 >= 10 es {10 >= 10}")
print(f"Menor que: 10 <= 3 es {10 <= 3}")

# Operadores logicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignacion
my_number = 11 # asignacion
print(my_number)
my_number += 1 # suma y asignacion
print(my_number)
my_number -= 1 # resta y asignacion
print(my_number)
my_number *= 3 # multiplicacion y asignacion
print(my_number)
my_number /= 2 # division y asignacion
print(my_number)
my_number %= 1 # modulo y asignacion
print(my_number)
my_number **= 1 # exponente y asignacion
print(my_number)
my_number //= 1 # division entera y asignacion
print(my_number)

# Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
print(f"'u' in 'mooure' = {'u' in 'moure'}")
print(f"'b' not in 'mooure' = {'b' not in 'moure'}")

# Operadores de bit
a = 10 #  1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}") # 0101
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 1000

"""
Estructuras de control
"""

# Condicionales

my_string = "Saul"

if my_string == "toonsaul":
    print("my_string es 'toonsaul'")
elif my_string == "Saul":
    print("my_string es 'Saul'")
else:
    print("my_string no es 'toonsaul' ni 'Saul'")

# Iterativas

for i in range(11):
    print(i)

i = 0

while i  <= 10:
    print(i)
    i += 1

# Manejo de excepciones

try:
    print(10 / 1)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de instrucciones")

"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)