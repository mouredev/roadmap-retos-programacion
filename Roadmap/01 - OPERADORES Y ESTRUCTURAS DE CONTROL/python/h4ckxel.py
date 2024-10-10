"""
Operadores 
"""

# Aritmeticos 
print(f"Suma: 10 + 8 = {10 + 8}")
print(f"Resta: 10 - 8 = {10 - 8}")
print(f"Multiplicacion: 10 * 8 = {10 * 8}")
print(f"Division: 10 / 8 = {10 / 8}")
print(f"Modulo: 10 % 8 = {10 % 8}")
print(f"Exponente: 10 ** 0 = {10 ** 8}")
print(f"División entera: 10 // 8 = {10 // 8}")

# Comparacion 
print(f"igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# Lógicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 -1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Asignacón 
my_number = 11  
print(my_number)
my_number += 1  
print(my_number)
my_number -= 1  
print(my_number)
my_number *= 2  
print(my_number)
my_number /= 2  
print(my_number)
my_number %= 2  
print(my_number)
my_number **= 1  
print(my_number)
my_number //= 1  
print(my_number)

# Identida 
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Pertenencia 
print(f"'y' in 'Python' = {'y' in 'Python'}")
print(f"'b' not in 'Python' = {'b' not in 'Python'}")

# Bit 
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

"""
Estructuras de control
"""
# Condicionales

my_string = "Python"

if my_string == "Rust":
    print("my_string es 'Rust'")
elif my_string == "Python":
    print("my_string es 'Python'")
else:
    print("my_string no es 'Rust' ni 'Python'")

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

"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)