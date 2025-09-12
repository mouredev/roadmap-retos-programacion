# OPERADORES ARITMÉTICOS

# Suma
n1 = 5 + 3 # 8

# Resta
n2 = 3 - 3 # 0

# Multiplicación
n3 = 10 * 2 # 20

# División
n4 = 10 / 3 # 3.3333333333333335

# División entera
n5 = 10 // 3 # 3

# Exponenciación
n6 = 2 ** 2 # 4

# Modulo o Residuo
n7 = 5 % 2 # 1

# OPERADORES DE COMPARACIÓN

# Mayor que...
c1 = 5 > 3 # True

# Menor que...
c2 = 1 < 3 # True

# Igual que...
c3 = 5 == 5 # True

# Mayor o igual que...
c4 = 5 >= 30 # False

# Menor o igual que...
c5 = 3 <= 3 # True

# Diferente que...
c6 = 6 != 6 # False

# OPERADORES LÓGICOS

# Y (AND)
l1 = (1 == 3) and (3 >= 3) # False

# O (OR)
l2 = (1 != 0) or (9 < 3) # True

# Negación (NOT)

l3 = not(9 == 9) # False

# OPERADORES BINARIOS

# & (AND binario)
b1 = 5 & 5 # 0b101 & 0b101 = 0b101 = 5

# | (OR binario)
b2 = 3 | 9 # 0b11 | 0b1001 = 0b1011

# ^ (XOR binario)
b3 = 8 ^ 2 # 0b1000 ^ 0b10 = 0b1010

# ~ (Binario inverso)
b4 = ~3 # -4

# << (Desplazamiento a la izquierda)
b5 = 8 << 3 # 0b1000 << 3 = 0b1000000 = 64

# >> (Desplazamiento a la derecha)
b6 = 4 >> 2 # 0b100 >> 2 = 0b1 = 1

# OPERADORES DE IDENTIDAD

# is
i1 = 5 is 5 # False
i2 = [1,2] is [1,2] # False

# is not
i3 = 5 is not 5 # True
i4 = [1,2] is not [1,2] # True

# OPERADORES DE PERTENENCIA

# in
p1 = 3 in [1,2,3] # True
p2 = [2,3] in [1,[2,3],4] # True

# not in
p3 = 3 not in [1,2,3] # False
p4 = [2,3] not in [1,[2,3],4] # False

# ESTRUCTURAS DE CONTROL

# CONDICIONAL
a = 4
b = 5
if a > b:
    print(f"{a} es mayor que {b}")
elif a == b:
    print(f"{a} es igual a {b}")
else:
    print(f"{b} es mayor que {a}")

# ITERATIVAS

# WHILE

c = 10
i = 1
while i <= c:
    print(i)
    i += 1

# FOR

d = [2,4,6,8,10]

for i in d:
    print(i)


# RETO OPCIONAL

i = 10
final = 55
while i <= final:
    if i != 16 and i % 3 != 0:
        print(i)
    i += 1
