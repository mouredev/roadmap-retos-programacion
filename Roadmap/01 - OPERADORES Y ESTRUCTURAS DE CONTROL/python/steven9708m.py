"""
Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 """
 # 1. Operadores aritméticos

from pickletools import pystring

num1 = 8
num2 = 6

print(f"Suma: 8 + 6 = {num1 + num2}") #SUMA
print (f"Resta: 8 - 6 = {num1 - num2}") #RESTA
print (f"Multiplicacion: 8 * 6 = {num1 * num2}") # Multiplicacion
print (f"Division: 8 / 6 = {num1 / num2}") # DIVISION DECIMALES
print (f"Division: 8 // 6 = {num1 // num2}") # DIVISION ENTERA
print (f"Resto de Division: 8 % 6 = {num1 % num2}") # MODULO (Resto de una division)
print (f"Potencia: 8 ** 6 = {num1 ** num2}") # Potencia

# 2. Operadores de comparación

print (f"Igual A: 8 == 6 = {num1==num2}") # Igual A
print (f"Distinto de: 8 != 6 = {num1 != num2}") # Distinto De
print (f"Mayor que: 8 > 6 = {num1 > num2}") # Mayor que
print (f"Menor que: 8 < 6 = {num1 < num2}") # Menor que
print (f"Mayor o Igual que: 8 >= 6 = {num1 >= num2}") # Mayor o Igual que
print (f"Menor o Igual que: 8 <= 6 = {num1 <= num2}") # Menor o Igual que

# 3. Operadores lógicos

print (f"And: 8 * 6 == 48 AND 48 < 52 es {num1*num2==48 and 48<52}") #TRUE
print (f"OR: 8 * 6 == 48 OR 48 > 52 es {num1*num2==48 or 48<52}") #TRUE
print (f"NOT: not 8 * 6 == 46 es {not num1*num2==46}") #TRUE

# 3. Operadores de asignación

S = 8
print(f"La letra S es = {S}")
S += 4
print(f"Suma y Asignacion = {S}")
S -= 2
print(f"Resta y Asignacion = {S}")
S *= 3
print(f"Multiplicacion y Asignacion = {S}")
S /= 10
print(f"Division y Asignacion = {S}")
S %= 5
print(f"Modulo y Asignacion = {S}")
S **= 4
print(f"Potencia y Asignacion = {S}")
S //= 4
print(f"Division Entera y Asignacion = {S}")

# 4. Operadores de identidad
SM=20.0
print(f"S is SM es: {S is SM}")
print(f"S is not SM es: {S is not SM}")

# 5. Operadores de Pertenecia

print(f"'A' in 'Steven' es: {'A' in 'Steven'}")
print(f"'A' not in 'Steven' es: {'A' not in 'Steven'}")

# 6. Operadores bit a bit

x = 15 # 1111
y = 10 # 1010

print(f"AND: 15 & 10 = {15 & 10}") # 1010
print(f"OR: 15 | 10 = {15 | 10}") # 1111
print(f"XOR: 15 ^ 10 = {15 ^ 10}") # 0101
print(f"NOT: ~15 = {~15}")
print(f"Desplazamiento a la Derecha: 10 >> 2 = {10 >> 2}") 
print(f"Desplazamiento a la Izquierda: 10 << 2 = {10 << 2}")


'''
ESTRUCTURAS DE CONTROL
'''

#CONDICIONALES

my_string = "Miranda"

if my_string == "Miranda":
    print ("My_String es 'Miranda'")
elif my_string == "Romero":
    print ("My_String es 'Romero'")
else:
    print ("My_String No es 'Miranda' ni 'Romero'")
    
# Iterativas

for i in range (11):
    print (i)

i = 0

while i <= 10:
    print(i)
    i += 1
    
# MANEJO DE EXCEPCIONES

try:
    print (10/0)

except:
    print ("Se ha producido un error")

finally:
    print ("Ha finalizadp el manejo de excepciones")
    
'''

DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
'''

for number in range (10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print (number)



















 
 