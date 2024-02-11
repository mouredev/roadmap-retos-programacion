# Operators:
print("Operadores aritméticos:")
print(f"1 + 1 = {1+1}")
print(f"1 - 1 = {1-1}")
print(f"2 * 2 = {2*2}")
print(f"6 / 2 = {6/2}")
print(f"6 // 2 = {6//2}")
print(f"7 % 2 = {7%2}")
print(f"2**3 = {2**3}")

# Logic:
print("\nOperadores lógicos:")
print(f"not True = {not True}")
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"False or False = {False or False}")

# Comparison:
print("\nOperadores de comparación:")
print(f"1 == 1 = {1==1}")
print(f"1 != 1 = {1==1}")
print(f"1 > 1 = {1>1}")
print(f"1 >= 1 = {1>=1}")
print(f"1 < 1 = {1<1}")
print(f"1 <= 1 = {1<=1}")
print(f"1 < 2 < 3 = {1 < 2 < 3}")

# Assignment:
print("\nOperadores de asignación:")
a = 1
print(f"a = 1 -> {a}")
a += 1
print(f"a += 1 -> {a}")
a -= 1
print(f"a -= 1 -> {a}")

# Identity:
print("\nOperadores de identidad:")
print(f"None is None = {None is None}")
print(f"False is not None = {False is not None}")

# Membership:
print("\nOperadores de pertenencia:")
print(f"1 in [1, 2, 3] = {1 in [1, 2, 3]}")
print(f"1 not in [4, 5, 6] = {1 not in [4, 5, 6]}")

# Bitwise:
print("\nOperadores de bits:")
print(f"~0b1 = {bin(~0b1)}")
print(f"0b101 & 0b011 = {bin(0b101&0b011)}")
print(f"0b101 | 0b011 = {bin(0b101|0b011)}")
print(f"0b101 ^ 0b011 = {bin(0b101^0b011)}")
print(f"0b100 >> 2 = {bin(0b100>>2)}")
print(f"0b100 << 2 = {bin(0b100<<2)}")

# Control structures:
print("\nCondicional:")
if 2 > 1:
    print("2 es mayor que 1")
else:
    print("Nunca llegaremos aquí, porque 2 no es igual o menor que 1")

print("\nIteración con bucle for:")
for i in range(3):
    print(f"ciclo {i}")

print("\nIteración con while:")
a = 1
while a < 3:
    print(f"{a} es menor que 3")
    a += 1

print("\nExcepción:")
denominator = input("Introduce un número: ")
try:
    denominator = float(denominator)
except ValueError:
    print(f"Chacho, has introducido un valor que no puede convertirse en float ({denominator})")

try:
    print(f"1.0 / {denominator} = {1./denominator}")
except ZeroDivisionError:
    print(f"Pillín, introdujiste cero, y no puedo hacer la división")
except TypeError:
    print("Como te dije, el valor introducido no es un número, así que omito la división")
finally:
    print("Habrás visto una división, si introdujiste un valor válido")

# Extra:
print("\nTodos los pares entre 10 y 55 (inclusive), que no son ni 16 ni múltiplos de 3:")
for i in range(10, 56, 2):
    if not i % 3 or i == 16:
        continue

    print(i)
