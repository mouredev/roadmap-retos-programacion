# Operadores Aritméticos
print(f"Suma: 12 + 10 = {12+10}")
print(f"Resta: 12 - 10 = {12-10}")
print(f"Multiplicación: 12 * 2 = {12*2}")
print(f"División: 12 / 2 = {12/2}")
print(f"Módulo: 12 % 5 = {12%5}")
print(f"Potencia: 12 ** 2 = {12**2}")
print(f"Div-Enteros: 12 // 7 = {12//7}")

# Operadores relacionales
print(f"Igualdad: 10 == 5 es {10 == 5}")
print(f"Desigualdad: 10 != 5 es {10 != 5}")
print(f"Mayor que: 10 > 5 es {10 > 5}")
print(f"Menor que: 10 < 5 es {10 < 5}")
print(f"Mayopr o igual: 10 >= 5 es {10 >= 5}")
print(f"Menor o igual: 10 >= 5 es {10 <= 5}")

# Operadores bit a bit
print(f"AND: 5 & 3 = {5&3}")
print(f"OR: 5 | 3 = {5|3}")
print(f"XOR: 5 ^ 3 = {5^3}")
print(f"NOT: ~ 5 = {~5}")
print(f"Desplazamiento a la izquierda: 5 << 2 = {5<<2}")
print(f"Desplazamiento a la derecha: 5 >> 2 = {5>>2}")

# Operadores de asignación
number = 5  # Asignación
print(number)
number += 2  # suma y asignación
print(number)
number -= 1  # Resta y asignación
print(number)
number *= 3  # Multiplicación y asignación
print(number)
number /= 2  # División y asignación
print(number)
number %= 2  # Módulo y asignación
print(number)
number **= 2  # Potenciación y asignación
print(number)
number //= 3  # División entera y asignación

# Operadores Lógicos
print(f"AND &&: 5 + 4 == 9 and 5 - 4 == 1 es {5 + 4 == 9 and 5 - 4 == 1}")
print(f"OR ||: 5 + 4 == 9 or 5 - 4 == 1 es {5 + 4 == 9 or 5 - 4 == 1}")
print(f"NOT !: not 5 + 4 == 9 es {not 5 + 4 == 9}")

# operadores de pertenencia
print(f"'u' in 'DGJuancho' = {'u' in 'DGJuancho'}")
print(f"'b' not in 'DGJuancho' = {'b' not in 'DGJuancho'}")

# Operadores de identidad
my_number = number
print(f"number is my_number es {number is my_number}")
print(f"number is not my_number es {number is not my_number}")

# Estructuras de control
x = 6
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")
else:
    print("Es otro")

# Operador Ternario
x = 5
print("Es 5" if x == 5 else "No es 5")

# Bucle for
for i in "DGJuancho":
    print(i)

# Usando range con for
for i in range(5, 0, -1):
    print(i)

# Bucle while
x = 5
while x > 0:
    x -= 1
    print(x)  # 4,3,2,1,0
else:  # No es común, pero se puede utilizar un else al final de un while
    print("El bucle ha finalizado")

# Ejercicio extra
for i in range(10, 56, 2):
    if i != 16 and i % 3 != 0:
        print(i)
