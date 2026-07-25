"""
Operadores aritméticos
"""

print(f"--------Operadores aritméticos--------")
a = 11
b = 7
print(f"Suma: {a + b}")          
print(f"Resta: {a - b}")         
print(f"Multiplicación: {a * b}") # 30
print(f"División: {a / b}")      # 3.3333...
print(f"División entera: {a // b}") # 3
print(f"Módulo: {a % b}")        # 1
print(f"Exponenciación: {a ** b}") # 1000

# Operadores de comparación
print(f"--------Operadores de comparación--------")
print(f"Igual a: {a == b}")      # False
print(f"Distinto de: {a != b}")  # True
print(f"Mayor que: {a > b}")     # True
print(f"Menor que: {a < b}")     # False
print(f"Mayor o igual que: {a >= b}") # True
print(f"Menor o igual que: {a <= b}") # False

# Operadores lógicos
print(f"--------Operadores lógicos--------")
x = True
y = False
print("AND lógico:", x and y)  # False
print("OR lógico:", x or y)    # True
print("NOT lógico:", not x)    # False

# Operadores de asignación
print(f"--------Operadores de asignación--------")
c = 5
c += 2  # c = c + 2
print("Asignación suma:", c)   # 7
c -= 2  # c = c - 2
print("Asignación resta:", c)  # 5
c *= 2  # c = c * 2
print("Asignación multiplicación:", c) # 10
c /= 2  # c = c / 2
print("Asignación división:", c) # 5.0
c //= 2 # c = c // 2
print("Asignación división entera:", c) # 2.0
c %= 2  # c = c % 2
print("Asignación módulo:", c)  # 0.0
c **= 2 # c = c ** 2
print("Asignación exponenciación:", c) # 0.0

# Operadores bit a bit
print(f"--------Operadores bit a bit--------")
d = 6  # 110 en binario
e = 2  # 010 en binario
print("AND bit a bit:", d & e)  # 2 (010 en binario)
print("OR bit a bit:", d | e)   # 6 (110 en binario)
print("XOR bit a bit:", d ^ e)  # 4 (100 en binario)
print("Desplazamiento a la izquierda:", d << 1) # 12 (1100 en binario)
print("Desplazamiento a la derecha:", d >> 1)  # 3 (011 en binario)

# Operadores de identidad
print(f"--------Operadores de identidad--------")
f = [1, 2, 3]
g = [1, 2, 3]
h = f
print("Es:", f is h)            # True
print("No es:", f is not g)     # True

# Operadores de pertenencia
print(f"--------Operadores de pertenencia--------")
print("En:", 1 in f)            # True
print("No en:", 4 not in f)     # True

"""
Estructuras de control
"""
print(f"--------Condicionales--------")
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")

# Estructuras iterativas
print(f"--------Estructuras iterativas--------")
for i in range(5):
    print(f"Iteración {i}")

contador = 0
while contador < 5:
    print(f"Iteración {contador}")
    contador += 1

# Manejo de excepciones
print(f"--------Manejo de excepciones--------")
try:
    resultado = a / 0
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Bloque finally ejecutado")

"""
Extra
"""

for i in range(10, 55+1):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)