# Operadores Aritméticos 
print('Operadores Aritméticos')
num= 2 + 2 # suma
print(num)
print(num - 1) # resta
print(num * 2) # multiplicación
print(num / 3) # división
print(num % 2) # módulo; Devuelve el resto de la división
print(num ** 2) # exponente
print(num // 3) # Devuelve el entero del resultado de la división, sin decimales.

# Operadores de Comparación
print('Operadores de Comparación')
num2= 8
print(num == num2) # igual a
print(num != num2) # diferente a
print(num > num2) # mayor que
print(num < num2) # menor que
print(num >= num2) # mayor o igual que
print(num <= num2) # menor o igual que

# Operadores de Asignación
print('Operadores de Asignación')
num3= 9 # Asigna un valor a un elemento. Puede ser  variable, lista, diccionario, tupla, etc.
print(num3)
num3 += 1 # Suma uno a num3 y lo guarda en num3
print(num3)
num2 -= 1 # Resta uno a num2 y lo guarda en num2
print(num2)
num2 *= 2 # Multiplica por 2 a num2 y lo guarda en num2
print(num2)
num2 /= 2 # Divide entre 2 a num2 y lo guarda en num2
print(num2)
num2 %= 2 # Divide entre 2 a num2 y el resto lo guarda en num2
print(num2)
num3 **= 2 # Eleva num3 a 2 y lo guarda en num3
print(num3)

# Operadores Lógicos
print('Operadores Lógicos')
print(10 > 5 and 3 < 5) # Es verdadero cuando TODAS las expresiones son ciertas.
print(10 > 5 or 3 < 2) # Es verdadero cuando al menos una expresión sea verdadera.
print(not 10 < 5) # Será verdadera cuando la expresión sea falsa y viceversa.

# Operadores Pertenencia - si un valor está presente dentro de una secuencia (como una cadena, lista, tupla, o un conjunto).
print('Operadores Pertenencia')
hay_letra= ('n' in 'Python') 
print(hay_letra)
hay_letra= ('a' not in 'Python')
print(hay_letra)

# Operadores Identidad - Verifica si dos variables se refieren al mismo objeto en la memoria.
print('Operadores de Identidad')
num = 100
num2 = num

print(num is num2)
print(num is not num2)

# Operadores Bitwise
print('Operadores Bitwise')
a = 10  # 1010 en binario
b = 3   # 0011 en binario
print(a and b) # and(&) 1010 & 0011 = 0010 (decimal 2)
print(a or b) # or(|) 1010 | 0011 = 1011 (decimal 11)
print(a ^ b) # xor(^) 1010 ^ 0011 = 1001 (decimal 9)

# ESTRUCTURAS DE CONTROL https://www.luisllamas.es/python-condicionales/
print('ESTRUCTURAS DE CONTROL')
# if, elif y else
print('if, elif y else')
x= 10
y= 5
z= 30
if x < y: # ejecuta un bloque de código si una condición es verdadera
    print('x es menos que y')
elif y == z: # se ejecuta si la  anterior condicion es falsa y esta es verdadera
    print('y es igual a z')
else: # Se ejecuta si todas las anteriores condiciones son falsas
    print('Las anteriores son falsas')

#Bucle for
print('Bucle for')
word= 'Python'
for char in word:
    print(char)
nombres= ['Edu', 'Kike', 'Toni', 'Isa', 'Mónica', 'Bego']
for nombre in nombres:
    print(nombre)
for num in range(2,25,2):
    print(num)

# Bucle While
print('Bucle While')
count=0
while count < 6:
    print(count)
    count += 1

print('Bucle While con Break')
while count < 13:
    print(count)
    if count == 10:
        break # Cuando se ejecute el BREAK, se detendrá el bucle 
    count += 1

print('Bucle while con continue')
while count < 20:
    if count % 2 == 0:
        count += 1
        continue
    print(count)
    count += 1

print('EJERCICIO OPCIONAL')
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for num in range(10,56,2):
    if num == 16 or num % 3 == 0:
        continue
    else:
        print(num)