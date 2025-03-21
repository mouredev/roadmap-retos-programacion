# Operadores y Estructuras de Control
# Autor: byTiagoGhost

# Ejercicio 1
# Operadores Aritmeticos
print(3 + 4) # Suma
print(3 - 4) # Resta   
print(3 * 4) # Multiplicacion
print(3 / 4) # Division
print(3 ** 4) # Exponenciacion
print(3 % 4) # Modulo = Te da el residuo de la division
print(3 // 4) # Division Entera = Te da el cociente de la division

print("")

# Operadores de Asignacion
# = Igualacion. 
# Ejemplo: 
x = 5
print("Igualacion:", x) 
# Igual que: x = 5


# Nota: Estamos reservando la variable de la X, entonces eso signiica que la variable puede cambiar de valor.

# += Suma en asignacion
# Ejemplo:
x+=3
print("Suma:", x)
# Igual que: x = x + 3

# -= Resta en asignacion
# Ejemplo:
x-=3
print("Resta:", x)
# Igual que: x = x - 3

# *= Multiplicacion en asignacion
# Ejemplo:
x*=3
print("Multiplicacion:", x)
# Igual que: x = x * 3

# /= Division en asignacion
# Ejemplo:
x/=3
print("Division:", x)
# Igual que x = x / 3

# %= Modulo en asignacion
# Ejemplo:
x%=3
print("Modulo:", x)
# Igual que x = x % 3

# //= Division Entera en asignacion
# Ejemplo:
x//=3
print("Division Entera:", x)
# Igual que x = x // 3

# **= Exponenciacion en asignacion
# Ejemplo:
x**=3
print("Exponenciacion:", x)
# Igual que x = x ** 3

# &= AND en asignacion o bitside
# Ejemplo:
y = 5   # 5  en bits = 101
y&=3   # 3 en bits = 011
print("AND o BITSIDE:", y) # 1 en bits = 001
# Igual que y = y & 3

# |= OR en asignacion o bitside
# Ejemplo:
y = 5   # 5  en bits = 101
y|=3   # 3 en bits = 011
print("OR o BITSIDE:", y) # 7 en bits = 111
# Igual que y = y |

# ^= XOR en asignacion o bitside
# Ejemplo:
y = 5   # 5  en bits = 101
y^=3   # 3 en bits = 011
print("XOR o BITSIDE:", y) # 6 en bits = 110
# Igual que y = y ^ 3

# >>= Desplazamiento a la derecha en asignacion o bitside
# Ejemplo:
y = 5   # 5  en bits = 101
y>>=3   # 3 en bits = 011
print("Desplazamiento a la derecha:", y) # 0 en bits = 000
# Igual que y = y >> 3

# <<= Desplazamiento a la izquierda en asignacion o bitside
# Ejemplo:
y = 5   # 5  en bits = 101
y<<=3   # 3 en bits = 011
print("Desplazamiento a la izquierda:", y) # 40 en bits = 101000
# Igual que y = y << 3

print("")
# Operadores de Comparacion

# == Igual que
# Ejemplo:
print(3 == 4) # False
print(3 == 3) # True

# != Diferente que
# Ejemplo:
print(3 != 4) # True
print(3 != 3) # False

# > Mayor que
# Ejemplo:
print(3 > 4) # False
print(3 > 3) # False
print(4 > 3) # True

# < Menor que
# Ejemplo:
print(3 < 4) # True
print(3 < 3) # False
print(4 < 3) # False

# >= Mayor o igual que
# Ejemplo:
print(3 >= 4) # False
print(3 >= 3) # True
print(4 >= 3) # True

# <= Menor o igual que
# Ejemplo:
print(3 <= 4) # True
print(3 <= 3) # True
print(4 <= 3) # False

print("")
# Operadores Logicos

# and
# Ejemplo:
print(3 == 4 and 3 == 3) # False
print(3 == 3 and 3 == 4) # False
print(3 != 3 and 4 != 4) # False
print(3 == 3 and 4 == 4) # True

# or
# Ejemplo:
print(3 == 4 or 3 == 3) # True
print(3 == 3 or 4 == 4) # True
print(3 != 3 or 3 != 4) # True
print(3 != 3 or 4 != 4) # False

# not
# Ejemplo:
print(not 3 == 4) # True
print(not 3 == 3) # False
print(not (3 != 3 and 3 == 4)) # True

print("")
# Estructuras de Identidad

# is
# Ejemplo:
x = 5
y = 5
print(x is y) # True

# is not
# Ejemplo:
x = 5
y = 5
print(x is not y) # False

print("")
# Estructuras de Afiliacion

# in
# Ejemplo:
x = [1, 2, 3, 4, 5]
print(3 in x) # True
print(6 in x) # False

# not in
# Ejemplo:
x = [1, 2, 3, 4, 5]
print(3 not in x) # False
print(6 not in x) # True

print("")
# Estructuras de Procedencia de Operadores

# ()
# Ejemplo:
print(3 + 4 * 5) # 23
print((3 + 4) * 5) # 35

# **
# Ejemplo:
print(3 ** 4 * 5) # 405
print(3 ** (4 * 5)) # 810

# *, /, //, %
# Ejemplo:
print(3 * 4 / 5) # 2.4
print(3 * 4 // 5) # 2
print(3 * 4 % 5) # 2

# +, -
# Ejemplo:
print(3 + 4 - 5) # 2

# <<, >>
# Ejemplo:
print(3 << 4 >> 5) # 0

# &
# Ejemplo:
print(3 & 4) # 0

# ^
# Ejemplo:
print(3 ^ 4) # 7

# |
# Ejemplo:
print(3 | 4) # 7

# >, >=, <, <=
# Ejemplo:
print(3 > 4 >= 5) # False
print(3 < 4 <= 5) # True

# ==, !=
# Ejemplo:
print(3 == 4 != 5) # False
print(3 != 4 == 5) # True

print("")
# Estructuras de Control

# if
# Ejemplo:
x = 5
if x == 5:
    print("Es igual a 5")

# else
# Ejemplo:
x = 5
if x == 4:
    print("Es igual a 4")
else:
    print("No es igual a 4")

# elif
# Ejemplo:
x = 5
if x == 4:
    print("Es igual a 4")
elif x == 5:
    print("Es igual a 5")
else:
    print("No es igual a 4 o 5")

# while
# Ejemplo:
x = 0
while x < 5:
    print(x)
    x += 1

# for
# Ejemplo:
x = [1, 2, 3, 4, 5]
for i in x:
    print(i)

# break
# Ejemplo:
x = 0
while x < 5:
    print(x)
    x += 1
    if x == 3:
        break

# continue
# Ejemplo:
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print("Continue",x)

# pass
# Ejemplo:
x = 0
while x < 5:
    x += 1
    if x == 3:
        pass
    print("pass",x)

# else
# Ejemplo:
x = 0
while x < 5:
    print(x)
    x += 1
else:
    print("Fin del ciclo")

# try
# Ejemplo:
try:
    x = 5 / 0
except:
    print("Error")

# except
# Ejemplo:
try:
    x = 5 / 0
except ZeroDivisionError:
    print("No se puede dividir por 0")

print("")
# Mis ejemplos 
x = 5 
if (3 + 2) == x:
    print("Es igual a 5")

y = 5
if (x + y) == 10 or (x - y) == 0:
    print("Es igual a 10 o 0")

z = 7
if (x + y) == 10 and (z - y) != 0 or (z - y) == 2:
    print("Es igual a 10 y 2")

a = 5
if (x + y) == 10 and (z - y) != 0 or (a - y) == 2:
    print("Es igual a 10 y 2")
else:
    print("No es igual a 10 y 2")

while x <= 10:
    print("Esto es un ciclo:",x)
    x += 1

for i in range(1, 10):
    print("Esto es un ciclo:",i)

# Tarea 
i = 10
while i <= 55:
    if i % 2 == 0 and i % 3 != 0 and i != 16 or i == 55:
        print(i)
    i += 1
