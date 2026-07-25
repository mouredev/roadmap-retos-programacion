'''Operadores y estructuras de control'''

# Operadores aritméticos
print(f"Suma: 10 + 45 = {10 + 45}")
print(f"Resta: 10 - 45 = {10 - 45}")
print(f"Multiplicación: 10 * 45 = {10 * 45}")
print(f"División: 10 / 45 = {10 / 45}")
print(f"División entera: 10 // 45 = {10 // 45}")
print(f"Módulo: 10 % 45 = {10 % 45}")
print(f"Exponente: 10 ** 45 = {10 ** 45}")

#Operadores de comparación
print(f"Igualdad: 10 == 45: {10 == 45}")
print(f"Desigualdad: 10 != 45: {10 != 45}")
print(f"Mayor que: 10 > 45: {10 > 45}")
print(f"Menor que: 10 < 45: {10 < 45}")
print(f"Mayor o igual que: 10 >= 45: {10 >= 45}")
print(f"Menor o igual que: 10 <= 45: {10 <= 45}")

#Operadores lógicos
print(f"AND: True and False: {True and False}") 
print(f"AND: True and False: {True and True}")
print(f"OR: True or False: {True or False}")
print(f"NOT: not True: {not True}")

#Operadores de asignación
x = 10
print(f"Asignación: x = {x}")
x += 5
print(f"Asignación con suma: x += 5: {x}")
x -= 3
print(f"Asignación con resta: x -= 3: {x}")
x *= 2
print(f"Asignación con multiplicación: x *= 2: {x}")
x /= 4
print(f"Asignación con división: x /= 4: {x}")
x //= 2
print(f"Asignación con división entera: x //= 2: {x}")
x %= 3
print(f"Asignación con módulo: x %= 3: {x}")
x **= 2
print(f"Asignación con exponente: x **= 2: {x}")

#Operadores de identidad
my_number = 10
my_new_number = my_number
print(f"Identidad: my_number is my_new_number: {my_number is my_new_number}")
print(f"Identidad: my_number is not my_new_number: {my_number is not my_new_number}")

#Operadores de pertenencia
print(f"Pertenencia: 'a' in 'Winston': {'a' in 'Winston'}")
print(f"Pertenencia: 'a' not in 'Winston': {'a' not in 'Winston'}")

#Operadores bit a bit
a = 20 # 20 en binario es 10100
b = 10 # 10 en binario es 01010

print(f"AND bit a bit: {a} & {b} = {a & b}")  
print(f"OR bit a bit: {a} | {b} = {a | b}")    
print(f"XOR bit a bit: {a} ^ {b} = {a ^ b}")    
print(f"Desplazamiento a la izquierda: {a} << 2 = {a << 2}")  
print(f"Desplazamiento a la derecha: {a} >> 2 = {   a >> 2}")  

'''
Estructuras de control
'''

# Condicionales
X = 10    
if 10 > 5:
    print("10 es mayor que 5")
elif 10 == 5:
    print("10 es igual a 5")
else: 
    print("10 no es mayor que 5")

#Iterativas
for i in range(20):
    print(i)

i = 0
while i <= 20:
    print(i)
    i += 1

#Manejo de excepciones
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Bloque finally ejecutado, independientemente de si hubo error o no")


'''

Extra

'''

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
