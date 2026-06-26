# Operadores aritméticos
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

# Operadores lógicos
print(True and False)
print(True or False)
print(not True)

# Operadores de comparación
print(10 == 10)
print(10 != 5)
print(10 > 5)
print(10 < 5)
print(10 >= 10)
print(10 <= 9)

# if / elif / else
x: int = 15
if x > 10:
    print("mayor que 10")
elif x == 10:
    print("igual a 10")
else:
    print("menor que 10")

# for
for i in range(5):
    print(i)

# while
contador: int = 0
while contador < 3:
    print(contador)
    contador += 1

# Reto extra: números pares entre 10 y 55, sin el 16, sin múltiplos de 3
for n in range(10, 56):
    if n % 2 == 0 and n != 16 and n % 3 != 0:
        print(n)
