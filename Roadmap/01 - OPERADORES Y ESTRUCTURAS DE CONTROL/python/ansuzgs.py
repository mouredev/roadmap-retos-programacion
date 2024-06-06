# Operatdores

# Aritméticos
print(f"Suma: 2 + 2 = {2 + 2}")
print(f"Resta: 2 - 2 = {2 - 2}")
print(f"Multiplicacion: 2 * 2 = {2 * 2}")
print(f"Division: 2 / 2 = {2 / 2}")
print(f"Modulo: 2 % 2 = {2 % 2}")
print(f"Exponente: 2 ** 2 = {2 ** 2}")
print(f"Division entera: 2 // 2 = {2 // 2}")

# Comparación
print(f"Igual: 2 == 2 es {2 == 2}")
print(f"Diferente: 2 != 2 es {2 != 2}")
print(f"Mayor que: 2 > 2 es {2 > 2}")
print(f"Menor que: 2 < 2 es {2 < 2}")
print(f"Mayor o igual que: 2 >= 2 es {2 >= 2}")
print(f"Menor o igual que: 2 <= 2 es {2 <= 2}")

# Lógicos
print(f"And: True and True es {True and True}")
print(f"Or: True or False es {True or False}")
print(f"Not: not True es {not True}")
print(f"Xor: True ^ False es {True ^ False}")

# Asignación
a = 5
print(f"Asignación: a = 2, a es {a}")
a += 2
print(f"Suma: a += 2, a es {a}")
a -= 2
print(f"Resta: a -= 2, a es {a}")
a *= 2
print(f"Multiplicación: a *= 2, a es {a}")
a /= 2
print(f"División: a /= 2, a es {a}")
a %= 2
print(f"Módulo: a %= 2, a es {a}")
a **= 2
print(f"Exponente: a **= 2, a es {a}")
a //= 2
print(f"División entera: a //= 2, a es {a}")

# Identidad
print(f"Es: 2 is 2 es {2 is 2}")
print(f"No es: 2 is not 2 es {2 is not 2}")

# Pertenencia
print(f"Está: 'a' in 'hola' es {'a' in 'hola'}")
print(f"No está: 'a' not in 'hola' es {'a' not in 'hola'}")

# Binarios
print(f"And binario: 0b100 & 0b110 es {0b100 & 0b110}")
print(f"Or binario: 0b100 | 0b110 es {0b100 | 0b110}")
print(f"Xor binario: 0b100 ^ 0b110 es {0b100 ^ 0b110}")
print(f"Desplazamiento izquierda: 0b100 << 2 es {0b100 << 2}")
print(f"Desplazamiento derecha: 0b100 >> 2 es {0b100 >> 2}")

# Estructuras de control

# If
a = 5
if a == 5:
    print(f"a es {a}")
elif a == 3:
    print(f"a es {a}")
else:
    print(f"a no es 5 ni 3")

# While
a = 0
while a < 5:
    print(f"a es {a}")
    a += 1

# For
for a in range(5):
    print(f"a es {a}")

# Break
a = 0
while True:
    if a == 5:
        break
    print(f"a es {a}")
    a += 1

# Continue
for a in range(5):
    if a == 2:
        continue
    print(f"a es {a}")

# Excepciones
try:
    a = 5 / 0
except ZeroDivisionError:
    print("No se puede dividir por 0")

# Extra
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
