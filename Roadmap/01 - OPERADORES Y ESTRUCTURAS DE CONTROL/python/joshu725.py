# Operadores

# Operadores aritmeticos
print(f"Suma: {8 + 3}")
print(f"Resta: {8 - 3}")
print(f"Multiplicacion: {8 * 3}")
print(f"Division: {8 / 3}")
print(f"Potencia: {8 ** 3}")
print(f"Modulo: {8 % 3}")
print(f"Division entera: {8 // 3}")

# Operadores logicos
print(f"AND: {8 + 3 == 11 and 8 - 3 == 2}")
print(f"OR: {8 + 3 == 11 or 8 - 3 == 2}")
print(f"NOT: {not 8 + 3 == 11}")

# Operadores de comparacion
print(f"Mayor que: {8 > 3}")
print(f"Menor que: {8 < 3}")
print(f"Mayor o igual que: {8 >= 3}")
print(f"Menor o igual que: {8 <= 3}")
print(f"Igualdad: {8 == 3}")
print(f"Desigualdad: {8 != 3}")

# Operadores de asignacion
number = 22
print(number)
number += 2
print(number)
number -= 2
print(number)
number *= 3
print(number)
number /= 2
print(number)
number %= 3
print(number)
number **= 2
print(number)
number //= 2
print(number)

# Operadores de identidad
number = 18
second_number = 15

print(number is second_number)
print(number is not second_number)

# Operadores de pertenencia
print("a" in "gato")
print("b" in "perro")

# Operadores de bits
a = 3  # 0011
b = 5  # 0101
print(f"AND : {a & b}")  # 0001
print(f"OR : {a | b}")  # 0111
print(f"XOR : {a ^ b}")  # 0110
print(f"NOT : {~b}")  # 1010

# Estructuras de control

# Condicionales
number = 11
if number > 15:
    print("Mayor a 15")
elif number > 12:
    print("Mayor a 12")
else:
    print("Menor a 15 y 12")

# Iterativas
for i in range(1, 10):
    print(i)

c = 0
while c < 5:
    print(c)
    c += 1

# Excepciones
try:
    print(25/0)
except:
    print("Error")

# Extra
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
