# Operadores aritméticos

print("eradores aritméticos")
print()
print("Suma: 3 + 2 = ", 3 + 2)
print("Resta: 3 - 2 = ", 3 - 2)
print("Multiplicación: 3 * 2 = ", 3 * 2)
print("División: 3 / 2 = ", 3 / 2)
print("División entera: 3 // 2 = ", 3 // 2)
print("Módulo: 3 % 2 = ", 3 % 2)
print("Potencia: 3 ** 2 = ", 3 ** 2)

# Operadores de comparación

print()
print("Operadores de comparación")
print()
print("Igualdad: 3 == 2 = ", 3 == 2)
print("Diferencia: 3 != 2 = ", 3 != 2)
print("Mayor que: 3 > 2 = ", 3 > 2)
print("Menor que: 3 < 2 = ", 3 < 2)
print("Mayor o igual que: 3 >= 2 = ", 3 >= 2)
print("Menor o igual que: 3 <= 2 = ", 3 <= 2)

# Operadores lógicos

print()
print("Operadores lógicos")
print()
print("And: True and False = ", True and False)
print("Or: True or False = ", True or False)
print("Not: not True = ", not True)

# Operadores de asignación

print()
print("Operadores de asignación")
print()
a = 11
print("a = 11") # Asignación
a += 2
print("a += 2: ", a) # Suma
a -= 2
print("a -= 2: ", a) # Resta
a *= 2
print("a *= 2: ", a) # Multiplicación
a /= 2
print("a /= 2: ", a) # División
a //= 2
print("a //= 2: ", a) # División entera
a %= 2
print("a %= 2: ", a) # Módulo
a **= 2
print("a **= 2: ", a) # Potencia

# Operadores de identidad

print()
print("Operadores de identidad")
print()
a = 11
b = 11
print("a = 11, b = 11")
print("a is b: ", a is b)
print("a is not b: ", a is not b)

# Operadores de pertenencia

print()
print("Operadores de pertenencia")
print()
lista = [1, 2, 3, 4, 5]
print("lista = [1, 2, 3, 4, 5]")
print("1 in lista: ", 1 in lista)
print("1 not in lista: ", 1 not in lista)
print("6 in lista: ", 6 in lista)
print("6 not in lista: ", 6 not in lista)

# Operadores de bits
print()
print("Operadores de bits")
print()
print("AND: 5 & 3 = ", 5 & 3) # 101 & 011 = 001
print("OR: 5 | 3 = ", 5 | 3) # 101 | 011 = 111
print("XOR: 5 ^ 3 = ", 5 ^ 3) # 101 ^ 011 = 110
print("Desplazamiento a la izquierda: 5 << 3 = ", 5 << 3) # 101 << 3 = 101000
print("Desplazamiento a la derecha: 5 >> 3 = ", 5 >> 3) # 101 >> 3 = 000
print("Inversión: ~5 = ", ~5) # ~101 = 010

# Estructuras de control

# Condicional if
print()
print("Condicional if")
print()

a = 2
if a > 3:
    print("a es mayor que 3")
elif a == 3:
    print("a es igual a 3")
else:
    print("a es menor que 3")

# Bucle while
print()
print("Bucle while")
print()
a = 0
while a < 5:
    print(a)
    a += 1

# Bucle for
print()
print("Bucle for")
print()
for i in range(5):
    print(i)

# Exception
print()
print("Exception")
print()
try:
    a = 1 / 0
except ZeroDivisionError:
    print("Error: división por cero")
finally:
    print("Finalizado")

# Extra
print()
print("Extra")
print()
for i in range(10,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print (i)

# THE END