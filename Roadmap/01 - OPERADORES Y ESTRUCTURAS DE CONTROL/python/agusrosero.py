# Operadores
suma = 5 + 5
resta = 5 - 5
multiplicacion = 5 * 5
division = 5 / 5
modulo = 5 % 5
exponente = 5 ** 5
print(suma, resta, multiplicacion, division, modulo, exponente)

# Operadores de asignacion
x = 5
x += 5
x -= 5
x *= 5
x /= 5
x %= 5
x **= 5
print(x)

# Operadores logicos
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(not True)
print(not False)

# Operadores de comparacion
print(5 == 5)
print(5 != 5)
print(5 > 5)
print(5 < 5)
print(5 >= 5)
print(5 <= 5)

# Estructuras de control
if 5 == 5:
    print("5 es igual a 5")
else:
    print("5 no es igual a 5")
    
mi_lista = [1, 2, 3, 4, 5]
for i in mi_lista:
    print(i)
    
while 5 == 5:
    print("5 es igual a 5")
    break

try:
    print(5 / 0)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
    