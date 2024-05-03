"""
Operadores
"""

# Operadores aritmeticos
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicacion: 10 * 3 = {10 * 3}")
print(F"Division: 10 / 3 = {10 / 3}")
print(f"Modulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"Division entera: 10 // 3 = {10 // 3}")

# Operadores de comparacion
print("Igualdad: 10 == 3 es {10 == 3}")
print("Desgualdad: 10 != 3 es {10 != 3}")
print("Mayor que: 10 > 3 es {10 > 3}")
print("Menor que: 10 < 3 es {10 < 3}")
print("Mayor o igual que: 10 >= 10 es {10 >= 10}")
print("Menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores logicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignacion
my_number = 11 # asignacion
print(my_number)
my_number += 1 # suma y asignacion
print(my_number)
my_number -= 1 # resta y asigancion
print(my_number)
my_number *= 1 # multiplicacion y asignacion
print(my_number)
my_number /= 2 # division y asignacion
print(my_number)
my_number %= 2 # modulo y asignacion
print(my_number)
my_number **= 1 # exponente y asignacion
print(my_number)
my_number //= 1 # division entera y asignacion
print(my_number)

# Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
print(f"'g' in 'angel' = {'g' in 'angel'}")
print(f"'o' not in 'miguel' = {'o' not in 'miguel'}")

# Operadores de bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 0010
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000

"""
Estructuras de control 
"""

# Condicionales

my_string = "Angel"

if my_string == "Angel":
    print("my_string es 'Angel'")
elif my_string == "Miguel":
    print("my_string es 'Miguel'")
else:
    print("my_string no es 'Angel' ni 'Miguel'")

# Iterativas

for i in range(11):
    print(1)

i <= 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha procucido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)