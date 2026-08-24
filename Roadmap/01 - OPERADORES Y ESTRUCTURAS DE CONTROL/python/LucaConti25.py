# Operadores Aritméticos
print("Suma (5 + 3): ", 5 + 3)          # Suma
print("Resta (5 - 3): ", 5 - 3)         # Resta
print("Multiplicación (5 * 3): ", 5 * 3)   # Multiplicación
print("División (5 / 3): ", 5 / 3)       # División
print("División entera (5 // 3): ", 5 // 3)   # División entera
print("Módulo (5 % 3): ", 5 % 3)        # Módulo
print("Exponente (5 ** 3): ", 5 ** 3)     # Exponente

# Operadores de Comparación 
print("Igual a (5 == 3): ", 5 == 3)      # Igual a
print("Diferente de (5 != 3): ", 5 != 3)     # Diferente de
print("Mayor que (5 > 3): ", 5 > 3)      # Mayor que
print("Menor que (5 < 3): ", 5 < 3)      # Menor que
print("Mayor o igual que (5 >= 3): ", 5 >= 3)   # Mayor o igual que
print("Menor o igual que (5 <= 3): ", 5 <= 3)    # Menor o igual que

# Operadores Lógicos
print("AND (10==10 and 5==5): ", 10==10 and 5==5)   # AND
print("OR (10==10 or 5==3): ", 10==10 or 5==3)     # OR
print("NOT (not True): ", not True)     # NOT   

#Operadores de Asignación
x = 5 #asignación
print("x = 5: ", x) 
x += 3 #suma y asignación
print("x += 3: ", x)
x -= 2 #resta y asignación
print("x -= 2: ", x)
x *= 4 #multiplicación y asignación
print("x *= 4: ", x)
x /= 2 #división y asignación
print("x /= 2: ", x)

# Operadores de Identidad (memoria)
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a = [1, 2, 3]: ", a is a)
print("b = a: ", b is a)
print("c = [1, 2, 3]: ", c is not a)

# Operadores de Pertenencia
print("3 in a: ", 3 in a)      # Pertenencia
print("4 not in a: ", 4 not in a)  # No pertenencia

# Operadores Bit a Bit
num1 = 5  # 0101 en binario
num2 = 3  # 0011 en binario
print("AND (5 & 3): ", num1 & num2)   # AND 
print("OR (5 | 3): ", num1 | num2)    # OR
print("XOR (5 ^ 3): ", num1 ^ num2)   # XOR (compara bit a bit y devuelve 1 si son diferentes)
print("NOT (~5): ", ~num1)     # NOT (intercambia los bits)
print("Desplazamiento a la izquierda (5 << 1): ", num1 << 1)  # Desplazamiento a la izquierda
print("Desplazamiento a la derecha (5 >> 1): ", num1 >> 1)   # Desplazamiento a la derecha

# Estructuras de Control

# Condicionales
new_string = "Hi, Luca!"
if "Luca" in new_string:
    print("La cadena contiene 'Luca'")
else:
    print("La cadena no contiene 'Luca'")


new_number = 10
if new_number > 0:
    print("El número es positivo")
elif new_number < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# Bucles
for i in range(5):
    print("Iteración: ", i)

for i in range(1,101):
    print("Número: ", i)

num = 5
while num > 0:
    print("Número actual: ", num)
    num -= 1

#excepciones
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Bloque finally ejecutado")

#Extra: Imprimir números pares del 10 al 55, excluyendo el 16 y los múltiplos de 3
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
