""" Reto 01: Operadores y Estructuras de control """

""" Operadores """

# Operadores Aritméticos
print(f"Suma: 11 + 10 = {11 + 10}")
print(f"Resta: 32 - 11 = {32 - 11}")
print(f"Multiplicación: 3 * 7 = {3 * 7}")
print(f"División: 63 / 3 = {63 / 3}")
print(f"Módulo: 10 % 4 = {10 % 4}")
print(f"División entera: 4 // 3 = {4 // 3}")
print(f"Exponente: 2 ** 4 = {2 ** 4}")

# Operadores de Comparación
print(f"Igualdad: 21 == 12 es {21 == 12}")
print(f"Desigualdad: 21 != 12 es {21 != 12}")
print(f"Mayor que: 21 > 12 es {21 > 12}")
print(f"Menor que: 21 < 12 es {21 < 12}")
print(f"Mayor o igual que: 21 >= 21 {21 >= 21}")
print(f"Menor o igual que: 12 <= 21 es {12 <= 21}")

# Operadores Lógicos
print(f"AND: 21 > 12 and 12 < 21 es {21 > 12 and 12 < 21}")
print(f"OR: 21 < 12 or 12 < 21 es {21 < 12 or 12 < 21}")
print(f"NOT: not 21 < 12 es {not 21 < 12}")

# Operadores de Asignación
var = 21   # asignación
print(var)
var += 1   # suma y asignación
print(var)
var -= 1   # resta y asignación
print(var)
var *= 2   # multiplicación y asignación
print(var)
var /= 2   # división y asignación
print(var)
var %= 4   # módulo y asignación
print(var)
var **= 1  # exponente y asignación
print(var)
var //= 1  # división entera y asignación
print(var)

# Operadores de Identidad y Pertenencia
nueva_var = var
print(f"var is nueva_var es {var is nueva_var}")
print(f"var is not nueva_var es {var is not nueva_var}")
print(f"'T' in 'Tomu98' = {'T' in 'Tomu98'}")
print(f"'i' not in 'Tomu98' = {'i' not in 'Tomu98'}")

# Operadores de bit
a = 10  # 1010
b = 3   # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")   # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")   # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000



""" Estructuras de control """

# Condicionales
my_string = "Tomu98"
if my_string == "Tomu98":
    print("my_string es 'Tomu98'")
elif my_string == "Arlert":
    print("my_string es 'Tomu Arlert'")
else:
    print("my_string no es 'Tomu98' ni 'Tomu Arlert'")

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



""" Reto extra """

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number != 0:
        print(number)
