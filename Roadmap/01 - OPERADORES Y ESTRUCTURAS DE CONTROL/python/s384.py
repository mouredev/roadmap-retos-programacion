"""/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */"""

# Operadores aritméticos
a = 4
b = 2
# Suma
print(a + b)  # 6
# Resta
print(a - b)  # 2
# Multiplicación
print(a * b)  # 8
# División
print(a / b)  # 2.0
# Potencia
print(a ** b)  # 16
# Resto
print(a % b)  # 0
# División con resultado entero
print(a // b)  # 2

# Operadores lógicos
a = True
b = False
# AND lógico
print(a and b)  # False
# OR lógico
print(a or b)  # True
# NOT lógico
print(not a)  # False

# Operadores de comparación
a = 5
b = 3
# Igualdad
print(a == b)  # False
# Desigualdad
print(a != b)  # True
# Mayor que
print(a > b)  # True
# Menor que
print(a < b)  # False
# Mayor o igual que
print(a >= b)  # True
# Menor o igual que
print(a <= b)  # False

# Operadores de asignación
a = 5
# =
a = 5
# +=
a += 5
# -=
a -= 5
# *=
a *= 5
# /=
a /= 5
# %=
a %= 5
# **=
a **= 5
# // 5
a //= 5

# Operadores de identidad
a = 5
b = 5
# is
print(a is b)  # True
# is not
print(a is not b)  # False

# Operadores de pertenencia
a = [1, 2, 3]
b = 2
# in
print(b in a)  # True
# not in
print(b not in a)  # False

# Operadores de bits
a = 10
b = 6
# &
print(a & b)  # 2
# |
print(a | b)  # 14
# ^
print(a ^ b)  # 8
# <<
print(a << b)  # 40
# >>
print(a >> b)  # 2

# Estructuras de control

# if
# elif
# else
a = -5
if a > 0:
    print("El valor de a es positivo")
elif a < 0:
    print("El valor de a es negativo")
else:
    print("El valor de a es cero")

# while
a = 4
while a > 0:
    print("El valor de a es positivo")
    a -= 1

# for
a = 4
for i in range(a):
    print(f"El valor de a es {a}")

# break
a = 4
for i in range(a):
    print(f"El valor de a es {a}")
    if i == 2:
        break

# continue
a = 4
for i in range(a):
    print(f"El valor de a es {a}")
    if i == 2:
        continue

# pass
a = 4
for i in range(a):
    print(f"El valor de a es {a}")
    if i == 2:
        pass

# try
# except
# finally
a = 4
try:
    print(f"El valor de a es {a}")
except:
    print("Se ha producido un error")
finally:
    print("La ejecución ha finalizado")

# Dificultad Extra
for i in range(10, 56):
    if (i % 2) != 0:
        if i == 16 or i % 3 == 0:
            continue
        else:
            print(i)