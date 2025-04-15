"""
OPERADORES
"""
# Ariméticos
print(f"Suma 5 + 5 =  {5+5}")
print(f"Resta 5 - 5 =  {5-5}")
print(f"Multiplicación 5 * 5 =  {5*5}")
print(f"División 6 / 5 =  {6/5}")
print(f"División entera 6 // 5 =  {6//5}")
print(f"Módulo 6 % 5 =  {6 % 5}")
print(f"Potencia 5 ** 5 =  {5**5}")

# Comparación
print(f"Igualdad 5 == 5 =  {5 == 5}")
print(f"Diferencia 5 != 5 =  {5 != 5}")
print(f"Mayor que 5 > 5 =  {5 > 5}")
print(f"Menor que 5 < 5 =  {5 < 5}")
print(f"Mayor o igual que 5 >= 5 =  {5 >= 5}")
print(f"Menor o igual que 5 <= 5 =  {5 <= 5}")
print(f"Comparación múltiple 5 < 6 < 7 =  {5 < 6 < 7}")

# Lógicos
print(f"And 5 == 5 and 5 == 5 =  {5 == 5 and 5 == 5}")
print(f"Or 5 == 5 or 5 == 5 =  {5 == 5 or 5 == 5}")
print(f"Not not 5 == 5 =  {not 5 == 5}")

# Asignación
x = 5
print(f"Asignación x = 5, x = {x}")  # 5
x += 5
print(f"Asignación x += 5, x = {x}")  # 10
x -= 5
print(f"Asignación x -= 5, x = {x}")  # 5
x *= 5
print(f"Asignación x *= 5, x = {x}")  # 25
x /= 5
print(f"Asignación x /= 5, x = {x}")  # 5.0
x //= 5
print(f"Asignación x //= 5, x = {x}")  # 1.0
x %= 5
print(f"Asignación x %= 5, x = {x}")  # 1.0
x **= 5
print(f"Asignación x **= 5, x = {x}")  # 1.0

# Identidad - posición de memoria
print(f"Identidad 5 is 5 =  {5 is 5}")
print(f"Identidad 5 is not 5 =  {5 is not 5}")
print(f"Identidad 5 is 5.0 =  {5 is 5.0}")
print(f"Identidad 5 is not 5.0 =  {5 is not 5.0}")

# Pertenencia
print(f"Pertenencia 5 in [5, 6, 7] =  {5 in [5, 6, 7]}")
print(f"Pertenencia 5 not in [5, 6, 7] =  {5 not in [5, 6, 7]}")
print(f"Pertenencia 'x' in 'franxisco' =  {'x' in 'franxisco'}")
print(f"Pertenencia 'x' not in 'franxisco' =  {'x' not in 'franxisco'}")

# Bitwise
print(f"Bitwise 5 & 5 =  {5 & 5}")  # 5
print(f"Bitwise 5 | 5 =  {5 | 5}")  # 5     0101
print(f"Bitwise 5 ^ 5 =  {5 ^ 5}")  # 0
print(f"Bitwise ~5 =  {~5}")  # -6
print(f"Bitwise 5 << 1 =  {5 << 1}")  # 10
print(f"Bitwise 5 >> 1 =  {5 >> 1}")  # 2

# estructuras de control
# if    elif    else
if 5 == 5:
    print("5 es igual a 5")
elif 5 == 6:
    print("5 es igual a 6")
else:
    print("5 no es igual a 5")

# iteración
# while
i = 0           # inicialización
while i < 5:    # condición
    print(i)
    i += 1      # incremento


# for
for i in range(5):
    print(i)    # 0 1 2 3 4

# for
for i in [5, 6, 7]:
    print(i)    # 5 6 7

# manejo de excepciones
try:
    print(5/0)  # ZeroDivisionError
except ZeroDivisionError as e:
    print(e)
finally:
    print("Final de le excepción")  # siempre se ejecuta

"""
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)    # 10 14 20 22 26 28 32 34 38 40 44 46 50 52
