"""CONDICIONALES"""

# OPERADORES ARITMÉTICOS
a = 10
b = 3
print("Arithmetic Operators:")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")
print()

# OPERADORES RELACIONALES O DE COMPARACIÓN
print("Operadores Relacionales")
print(f"Mayor que: 101 > 100 es {101 > 100}")
print(f"Mayor que: 100 > 101 es {100 > 101}")
print(f"Menor que: 101 < 100 es {101 < 100}")
print(f"Menor que: 100 < 101 es {100 < 101}")
print(f"Igualdad: 999 == 999 es {999 == 999}")
print(f"Igualdad: 999 == 1000 es {999 == 1000}")
print(f"Mayor o igual que: 101 >= 100 es {101 >= 100}")
print(f"Mayor o igual que: 99 >= 101 es {99 >= 101}")
print(f"Menor o igual que: 101 <= 100 es {101 <= 100}")
print(f"Menor o igual que: 99 <= 101 es {99 <= 101}")
print(f"Desigualdad: 1 != 1 es {1 != 1}")
print(f"Desigualdad: 10 != 20 es {10 != 20}")

# OPERADORES LÓGICOS
print("Operadores Lógicos")
print(f"AND: 10 + 33 == 43 and 20 + 20 == 40 es {10 + 33 == 43 and 20 + 20 == 40}")
print(f"OR: 10 + 33 == 43 or 20 + 20 == 40 es {10 + 33 == 43 or 20 + 20 == 40}")
print(f"NOT: 21 + 20 == 40 es {not 21 + 20 == 40}")

# OPERADORES DE ASIGNACIÓN
print("Operadores de Asignación")
numberPy = 25
print(numberPy)
numberPy += 25 # suma y asignación
print(numberPy)
numberPy -= 25 # resta y asignación
print(numberPy)
numberPy *= 25 # multiplicación y asignación
print(numberPy)
numberPy /= 25 # división y asignación
print(numberPy)
numberPy **= 25 # exponente y asignación
print(numberPy)
numberPy //= 25 # división entera y asignación
print(numberPy)
numberPy %= 25 # módulo y asignación
print(numberPy)

# OPERADORES DE IDENTIDAD
print("Operadores de Identidad")
error = 404
error2 = 404
print(f"error is error2 es {error is error2}")
print(f"error is not error2 es {error is not error2}")

# OPERADORES DE PERTENENCIA
print("Operadores de Pertenencia")

indie = "hollow knight"
print('hollow' in indie)
print('undertale' in indie)
print('undertale' not in indie)

pi = [1,2,3,4,5,99]
print(99 in pi)
print(99 not in pi)
print(9 in pi)
print(9 not in pi)

print(f"'x' in 'hunter x hunter' is {'x' in 'hunter x hunter'}")
print(f"'x' not in 'hunter x hunter' is {'x' not in 'hunter x hunter'}")

# OPERADORES DE BIT

print("Operadores de Bits")

a = 5     
b = 3     

# AND - 1 si ambos bits son 1, 0 si no
print(a & b)      # (0101 & 0011 = 0001)

# OR - 1 si al menos uno de los bits es 1
print(a | b)      # (0101 | 0011 = 0111)

# XOR - 1 si los bits son diferentes, 0 si son iguales
print(a ^ b)      # (0101 ^ 0011 = 0110)

# NOT - invierte todos los bits xd
print(~a)         # (~0101 = -(5 + 1) = -6)

# LEFT SHIFT - mueve los bits a la izquierda y agrega un 0 al final
print(a << 1)     # (0101 becomes 1010)

# RIGHT SHIFT - mueve los bits a la derecha y agrega un 0 al inicio
print(a >> 1)     # (0101 becomes 0010)

"""
ESTRUCTURAS DE CONTROL 
"""
# CONDICIONALES

my_taco = "taco de cochinita"

if my_taco == "taco de pastor":
    print("my_taco es 'taco de pastor'")
elif my_taco == "taco de surtido":
    print("my_taco es 'taco de surtido'")
else:
    print("my_taco no es 'taco de pastor' ni 'taco de surtido'")

# ITERATIVAS

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# MANEJOR DE EXCEPCIONES
try:
    print(99 / 1)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de sesiones")

# EJERCICIO EXTRA

for num in range(10, 56):  # del 10 al 55 (56 no se incluye)
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
