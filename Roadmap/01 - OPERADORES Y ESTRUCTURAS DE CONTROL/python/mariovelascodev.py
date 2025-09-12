#Operadores de asignación
print("Operadores de asignación")
a = 5
b = 10

print(f"Operador =: a = 5")
print(f"Operador =: b = 10")

a += b
print(f"Operador +=: a += b = {a}")

a -= b
print(f"Operador -=: a -= b = {a}")

a *= b
print(f"Operador *=: a *= b = {a}")

a /= b
print(f"Operador /=: a /= b = {a}")

a %= b
print(f"Operador %=: a %= b = {a}")

a //= b
print(f"Operador //=: a //= b = {a}")

a **= b
print(f"Operador **=: a **= b = {a}")
print("...............................")

#Operadores aritméticos
a = 18
b = 2
print("Operadores aritméticos")
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b}")
print(f"Modulo: {a} % {b} = {a % b}")
print(f"Exponente: {a} ** {b} = {a ** b}")
print(f"Cociente: {a} // {b} = {a // b}")
print("...............................")

#Operadores lógicos
print("Operadores lógicos")
print(f"and: True and True = {True and True}")
print(f"or: True or False = {True or False}")
print(f"not: not True = {not True}")
print("...............................")

#Operadores de comparación
print("Operadores de comparación")
print(f"Mayor: {a} > {b} = {a > b}")
print(f"Mayor o igual: {a} >= {b} = {a >= b}")
print(f"Menor: {a} < {b} = {a < b}")
print(f"Menor o igual: {a} <= {b} = {a <= b}")
print(f"Igual: {a} == {b} = {a == b}")
print(f"Distinto: {a} != {b} = {a != b}")
print("...............................")

#Operadores de identidad
print("Operadores de identidad")
print(f"is: {a} is {b} = {a is b}")
print(f"is not: {a} is not {b} = {a is not b}")
print("...............................")

#Operadores de pertenencia
print("Operadores de pertenencia")
print(f"in: {a} in [1, 2, 3] = {a in [1, 2, 3]}")
print(f"not in: {a} not in [1, 2, 3] = {a not in [1, 2, 3]}")
print("...............................")

#Operadores de bit
print("Operadores de bit")
bit_1 = 0b1101
bit_2 = 0b1011

print(f"&: {bin(bit_1)} & {bin(bit_2)} = {bin(bit_1 & bit_2)}")
print(f"|: {bin(bit_1)} | {bin(bit_2)} = {bin(bit_1 | bit_2)}")
print(f"~: ~{bin(bit_1)} = {bin(~bit_1)}")
print(f"^: {bin(bit_1)} ^ {bin(bit_2)} = {bin(bit_1 ^ bit_2)}")
print(f">>: {bin(bit_1)}>>2 = {bin(bit_1>>2)}")
print(f"<<: {bin(bit_1)}<<2 = {bin(bit_1<<2)}")
print("...............................")

#Estructuras de control
print("Estructuras de control")

print("Condicional if")
if a < b:
    print(f"{a} es menor que {b}")
elif a > b:
    print(f"{a} es mayor que {b}")
else:
    print(f"{a} es igual que {b}")
print("...............................")

print("Bucle for")
for i in "Python":
    print(i)
print("...........Recorrer un rango................")
for i in range(11):
    print(i)
print("...............................")

print("Bucle while")
num = 5
while num > 0:
    print(num)
    num -= 1
print("...............................")

#Excepciones
print("Excepciones")
num1 = 5
num2 = 0

try:
    num3 = num1 / num2
except Exception:
    print("Ha habido una excepción")

print("...............................")

#EXTRA
print("DIFICULTAD EXTRA")
for i in range(10,56):
    if i % 2 == 0 and i % 3 != 0:
        if i == 16:
            continue
        print(i)
        if i == 52:
            i += 3
            print(i)