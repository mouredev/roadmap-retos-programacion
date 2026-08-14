# Operadores de Python.

# Aritméticos:
print(f"Suma: 2 + 3 = {4 + 3}")
print(f"Resta: 2 - 3 = {4 - 3}")
print(f"Multiplicación: 3 * 2 = {3 * 2}")
print(f"División: 7 / 2 = {7 / 2}")
print(f"División entera: 7 // 2 = {7 // 2}")
print(f"Módulo o resto: 7 % 2 = {7 % 2}")
print(f"Potencia: 2 ** 3 = {2**3}")

# Comparación
print(f"Igual: 3 == 3 es {3 == 3}")
print(f"Distinto: 2 != 3 es {2 != 3}")
print(f"Menor que: 2 < 3 es {2 < 3}")
print(f"Mayor que: 4 > 3 = es {4 > 3}")
print(f"Menor o igual que: 2 <= 2 es {2 <= 2}")
print(f"Mayor o igual que: 6 >= 6 es {6 + 6}")

# Lógicos
print(f"and: (verdadero y falso) True and False {True and False}")
print(f"or: (verdadero o falseo) True or False {True or False}")
print(f"not: (negación) not True {not True}")

# Asignación
a = 11  # asigna 1 a la variable
print(a)
a += 1  # suma 1 al valor de la variable
print(a)
a -= 1  # resta 1 al valor de la variable
print(a)
a *= 1  # multiplica por 1 el valor de la variable
print(a)
a /= 2  # divide por 2 el valor de la variable
print(a)
a %= 2  # divide por 2 y asigna el resto (módulo) a la variable
print(a)
a **= 2  # eleva el valor de a a la potencia y asigna el valor
print(a)
a //= 2  # divide a por 2 y asigna a a la división entera
print(a)

# Identidad
b = 1.0
print(f"a is b es: {a is b}")  # compara si 2 objetos son igual
print(f"a is not b: {a is not b}")

# Pertenencia
print(f"'o' in 'oscar' = {'o' in 'oscar'}")
print(f"'o' not in 'oscar' = {'o' not in 'oscar'}")

# bit
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 & 3}")  # 1011
print(f"XOR 10 ^ 3 = {10 & 3}")  # 1001
print(f"NOT ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

"""
Estructuras de control
"""

# Condicionales
my_string = "Oscarrrrrr"

if my_string == "Oscar":
    print("my_string es 'Oscar'")
elif my_string == "car":
    print("my_string es 'Car'")
else:
    print("my_string no es 'Oscar'")

# Iterativas
for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 1)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de errores")

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
