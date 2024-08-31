# Operadores aritmeticos
suma = 5 + 5
resta = 5 - 5
multiplicacion = 5 * 5
division = 5 / 5
modulo = 5 % 5
exponente = 5 ** 5
print(suma, resta, multiplicacion, division, modulo, exponente)

# Operadores de asignacion

y = 5
x = 5
print(x)
x += 5
print(x)
x -= 5
print(x)
x *= 5
print(x)
x /= 5
print(x)
x %= 5
print(x)
x **= 5
print(x)
x //= 5
print(x)

# Operadores de comparacion
print(5 == 5)
print(5 != 5)
print(5 > 5)
print(5 < 5)
print(5 >= 5)
print(5 <= 5)

# Operadores logicos
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(not True)
print(not False)

# Operadores de identidad
print(5 is 5)
print(5 is not 5)

# Estructuras de control
if 5 == 5:
    print("5 es igual a 5")
else:
    print("5 no es igual a 5")
    
while 5 == 5:
    print("5 es igual a 5")
    break

for i in range(5):
    print(i)
    
try:
    print(5 / 0)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
    