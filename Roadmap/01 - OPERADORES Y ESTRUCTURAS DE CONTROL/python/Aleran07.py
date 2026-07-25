# 01
x = 2
y = 5
z = 1+2
print(z)
z = 2-6
print(z)
z = 2/6
print(z)
z = 2*6
print(z)

z = 1//2
print(z)
z = 2%6
print(z)
z = 2**6
print(z)


z = 1==2
print(z)
z = 2!=6
print(z)
z = 2<6
print(z)
z = 2>6
print(z)
z = 2>=6
print(z)
z = 2<=6
print(z)

# Operadores lógicos
z = (1==2) and (2<6)
print(z)
z = (1==2) or (2<6)
print(z)
z = not(1==2)
print(z)
z = not(2<6)
print(z)


# Operadores de asignación
x = 2
x += 2  # x = x + 2
print(x)
x -= 2  # x = x - 2
print(x)
x *= 2  # x = x * 2
print(x)
x /= 2  # x = x / 2
print(x)
x //= 2  # x = x // 2
print(x)
x %= 2  # x = x % 2
print(x)
x **= 2  # x = x ** 2
print(x)

# operadores de identidad
x = 2
y = 5
z = x is y
print(z)
z = x is not y
print(z)
y = 2
z = x is y
print(z)
z = x is not y
print(z)

# operadores de pertenencia
x = "Hola"
y = "H"
z = "H" in x
print(z)
z = "H" not in x
print(z)


# operadores bit a bit
x = 2  # 10 en binario
y = 5  # 101 en binario
z = x & y  # AND bit a bit
print(z)  # 0 en binario

z = x | y  # OR bit a bit
print(z)  # 7 en binario


z = x ^ y  # XOR bit a bit
print(z)  # 7 en binario
z = ~x  # NOT bit a bit
print(z)  # -3 en binario
z = x << 1  # Desplazamiento a la izquierda
print(z)  # 4 en binario

# Ejercicios
import random
print("Operadores en Python\n")
# OPERADORES ARITMÉTICOS
print("Operadores Aritméticos")
a = random.randint(1, 10)
b = random.randint(1, 10)
print(f'    - La suma de {a} + {b} es igual a {a + b}')
print(f'    - La resta de {a} - {b} es igual a {a - b}')
print(f'    - La multiplic de {a} x {b} es igual a {a * b}')
print(f'    - La división de {a} entre {b} es igual a {a / b}')
print(f'    - El resto de {a} entre {b} es igual a {a % b}')
print(f'    - La división de piso de {a} entre {b} es igual a {a // b}')
print(f'    - La potencia de {a} elevado a {b} es igual a {a ** b}\n')



print("Ejercicio de dificultad extra")
a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)
d = random.randint(1, 10)
e = random.randint(1, 10)
f = random.randint(1, 10)
print(f'    - El resultado de la operación ({a} + {b}) * ({c} - {d}) / ({e} + {f}) es igual a {((a + b) * (c - d)) / (e + f)}')
print(f'    - El resultado de la operación ({a} + {b}) * ({c} - {d}) // ({e} + {f}) es igual a {((a + b) * (c - d)) // (e + f)}')
print(f'    - El resultado de la operación ({a} + {b}) * ({c} - {d}) % ({e} + {f}) es igual a {((a + b) * (c - d)) % (e + f)}')


# Ejercicio de dificultad extra
# Crea un programa que imprima por consola todos los números comprendidos
# * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)

x = 13
y = x % 2
print(y)
