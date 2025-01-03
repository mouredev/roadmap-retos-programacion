# 01 - Python

# Operadores
# Aritméticos
print(f"Suma: 10 + 5 = {10 + 5}")
print(f"Resta: 10 - 5 = {10 - 5}")
print(f"Multiplicación: 10 * 5 = {10 * 5}")
print(f"División: 10 / 5 = {10 / 5}")
print(f"División entera: 10 // 5 = {10 // 5}")
print(f"Residuo: 10 % 5 = {10 % 5}")
print(f"Potencia: 10 ** 5 = {10 ** 5}")

# Lógicos
print(f"10 y 5 son mayores que 7? {10>7 and 5>7}") # AND
print(f"10 o 5 son mayores que 7? {10>7 or 5>7}") # OR
print(f"10 no es mayor que 7? {not 10>7}") # NOT

# Comparación
print(f"10 es igual a 5? {10 == 5}")
print(f"10 es diferente a 5? {10 != 5}")
print(f"10 es mayor a 5? {10 > 5}")
print(f"10 es menor a 5? {10 < 5}")
print(f"10 es mayor o igual a 5? {10 >= 5}")
print(f"10 es menor o igual a 5? {10 <= 5}")

# Asignación
a = 10
print(f"Valor de a: {a}")
a += 5
print(f"Valor de a al sumarle 5: {a}")
a -= 5
print(f"Valor de a al restarle 5: {a}")
a *= 5
print(f"Valor de a al multiplicarlo por 5: {a}")
a /= 5
print(f"Valor de a al dividirlo por 5: {a}")
a //= 5
print(f"Valor de a al dividirlo y redondearlo a la 5: {a}")
a %= 5
print(f"Valor de a al sacarle el residuo de dividirlo por 5: {a}")
a **= 5
print(f"Valor de a al elevarlo a la 5: {a}")

# Identidad
my_number = 10
new_variable = my_number 
print(f"my_number es igual a new_variable? {my_number is new_variable}") #Comprobamos si my_number y new_variable son el mismo objeto
new_variable = 5
print(f"my_number es igual a new_variable? {my_number is new_variable}") #Comprobamos si my_number y new_variable son el mismo objeto
print(f"my_number no es igual a new_variable? {my_number is not new_variable}") #Comprobamos si my_number y new_variable no son el mismo objeto

# Pertenencia
my_list = [1, 2, 3, 4, 5]
print(f"1 está en la lista? {1 in my_list}") # Comprobamos si 1 está en la lista
print(f"6 no está en la lista? {6 not in my_list}") # Comprobamos si 6 no está en la lista

# Bit
print(f"10 en binario: {bin(10)}") #es 1010
print(f"5 en binario: {bin(5)}") #es 101
print(f"10 & 5 = {10 & 5}") # 1010 & 0101 = 0000, AND
print(f"10 | 5 = {10 | 5}") # 1010 | 0101 = 1111, OR
print(f"10 ^ 5 = {10 ^ 5}") # 1010 ^ 0101 = 1111, XOR
print(f"~10 = {~10}") # ~1010 = -1011, NOT
print(f"10 << 2 = {10 << 2}") # 1010 << 2 = 101000, Desplazamiento a la izquierda 

# Estructuras de control
# Condicionales
if 10 > 5:
    print("10 es mayor que 5")
elif 10 == 5:
    print("10 es igual a 5")
else:
    print("5 es mayor que 10")

# Iterativas
for i in range(5,10):
    print(i)

# Excepciones
try:
    print(10 / 0)
except:
    print("Ha ocurrido un error")

# Extra: Programa que imprime los números entre 10 y 55, pares, que no son 16 ni múltiplos de 3
for i in range(10, 56):
    if 16 != i and i % 2 == 0 and i % 3 != 0:
        print(i)