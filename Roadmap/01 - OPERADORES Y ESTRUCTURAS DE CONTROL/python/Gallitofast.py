#No se si alguien lea esto pero deje c por que se me hizo muy dificil para proyectos personales 
# y no quiero que se me olvide como se hace
# =======================
# OPERADORES EN PYTHON
# =======================

print("=== Operadores Aritméticos ===")
a = 10
b = 3
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

print("\n=== Operadores de Comparación ===")
print("Igualdad:", a == b)
print("Diferente:", a != b)
print("Mayor que:", a > b)
print("Menor que:", a < b)
print("Mayor o igual:", a >= b)
print("Menor o igual:", a <= b)

print("\n=== Operadores Lógicos ===")
x = True
y = False
print("and:", x and y)
print("or:", x or y)
print("not:", not x)

print("\n=== Operadores de Asignación ===")
c = 5
print("Inicial:", c)
c += 2
print("c += 2:", c)
c *= 3
print("c *= 3:", c)
c -= 1
print("c -= 1:", c)
c /= 2
print("c /= 2:", c)

print("\n=== Operadores de Identidad ===")
m = [1, 2]
n = m
z = [1, 2]
print("m is n:", m is n)
print("m is z:", m is z)
print("m is not z:", m is not z)

print("\n=== Operadores de Pertenencia ===")
print("2 in m:", 2 in m)
print("3 not in m:", 3 not in m)

print("\n=== Operadores de Bits ===")
x = 4  # 0100
y = 1  # 0001
print("x & y:", x & y)  # 0000
print("x | y:", x | y)  # 0101
print("x ^ y:", x ^ y)  # 0101
print("~x:", ~x)        # complemento
print("x << 1:", x << 1)  # 1000
print("x >> 1:", x >> 1)  # 0010

# =======================
# ESTRUCTURAS DE CONTROL
# =======================

print("\n=== Condicionales ===")
edad = 20
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres niño")

print("\n=== Bucle while ===")
i = 0
while i < 3:
    print("i vale:", i)
    i += 1

print("\n=== Bucle for ===")
for letra in "hey":
    print("Letra:", letra)

print("\n=== Manejo de excepciones ===")
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("Bloque finally siempre se ejecuta")

# =======================
# DIFICULTAD EXTRA
# =======================
print("\n=== Dificultad extra: Números pares entre 10 y 55, sin 16 ni múltiplos de 3 ===")
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num, end=" ")
    
print()  # Salto de línea final
import sys
print(sys.version)