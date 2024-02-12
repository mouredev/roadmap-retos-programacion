# Python divide sus operadores en los siguientes grupos:
#   * Operadores Aritmeticos
#   * Operadores de Asignacion
#   * Operadores de Comparacion
#   * Operadores logicos
#   * Operadores de identidad
#   * Operadores de pertenencia
#   * Operadores a nivel de bit

# OPERADORES ARITMETICOS

# SUMA +
x = 2
y = 3
z = x + y
print(z)

# RESTA -
x = 7
y = 5
z = x - y
print(z)

# MULTIPLICACION *
x = 5
y = 2
z = x * y
print(z)

# DIVISION /
x = 10
y = 2
z = x / 2
print(z)

# MODULUS %

x = 3
y = 2
z = x % y
print(z)

# Exponenciación

x = 2
y = 3
z = 2**3
print(z)

# Floor division (en Python es una operación matemática
# que devuelve el mayor número entero posible).
x = 7
y = 2
z = x // y
print(z)

# OPERADORES DE ASIGNACION

# Operador (=)
x = 10
print(x)

# Operador (+=)
x = 10
x += 5
print(x)

# Operador (-=)
x = 10
x -= 5
print(x)

# Operador (*=)
x = 10
x *= 5
print(x)

# Operador (/=)
x = 10
x /= 5
print(x)

# Operador (%=)
x = 10
x %= 5
print(x)

# Operador (//=)
x = 10
x //= 5
print(x)

# Operador (**=)
x = 2
x **= 5
print(x)

# Operador (&=)
a = 12  # in binary: 1100
b = 10  # in binary: 1010
a &= b  # now 'a' becomes 8, which is 1000 in binary
print(a)

# Operador (|=)
a = 12  # in binary: 1100
b = 10  # in binary: 1010
a |= b  # now 'a' becomes 14, which is 1110 in binary
print(a)

# Operador (^=)
a = 12  # in binary: 1100
b = 10  # in binary: 1010
a ^= b  # now 'a' becomes 6, which is 0110 in binary
print(a)

# Operador (>>=)
a = 12  # in binary: 1100
a >>= 2  # now 'a' becomes 3, which is 0011 in binary
print(a)

# Operador (<<=)
a = 3  # in binary: 0011
a <<= 2  # now 'a' becomes 12, which is 1100 in binary
print(a)

# OPERADORES DE COMPARACION
# Operador igual (==)
x = 5
y = 3
print(x == y)   # Retorna falso porque x no es igual a y

# Operador no igual (!=)
x = 5
y = 3
print(x != y)   # Retorna verdadero porque x no es igual a y

# Operador mayor que (>)
x = 5
y = 3
print(x > y)   # Retorna verdadero porque x no es mayor a y

# Operador menor que (>)
x = 5
y = 3
print(x < y)   # Retorna falso porque x no es menor a y

# Operador mayor o iqual que (>=)
x = 5
y = 3
print(x >= y)   # Retorna verdadero porque x es mayor a y

# Operador menor o iqual que (<=)
x = 5
y = 3
print(x <= y)   # Retorna falso porque x es mayor a y

# OPERADORES LOGICOS

# Operador AND
x = 5
print(3 < x and x < 10) # Retorna verdadero porque x es mayor que 3 y
                        # tambien es menor que 10

# Operador OR
x = 5
print(3 < x or x < 2) # Retorna True porque cumple con alguna de las condiciones,
                      # en este caso x es mayor que 3

# Operador NOT
x = 5
print(not(3 < x and x < 10)) # Revierte el resultado, retorna falso si el resultado es verdadero
                             # para nuestro caso retorna falso

# OPERADORES DE IDENTIDAD

# Operador IS
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)   # Retorna verdadero porque z es el mismo objeto que x

# Operador IS NOT
x = ["apple", "banana"]
y = ["orange", "banana"]
print(x is y)   # Retorna falso porque x no es el mismo objeto que y

# OPERADORES DE PERTENENCIA

# Operador IN
x = ["apple", "banana"] # Devuelve verdadero si una secuencia con el valor
                        # especificado está presente en el objeto.
print("banana" in x)

# Operador NOT IN
x = ["apple", "banana"] # Retorna verdadero porque en la secuencia el
                        # valor de "pineapple"  no se encuentra en la lista
print("pineapple" not in x)

# OPERADORES A NIVEL DE BIT

# Operador & (AND)
print(6 & 3)
"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================
"""

# Operador | (OR)
print(6 | 3)
"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================
"""

# Operador | (XOR)
print(6 ^ 3)
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================
"""

# Operador ~ (NOT)
print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100
"""

# Operador << (Zero fill left shift)
print(3 << 2)
"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100
"""

# Operador >> (Signed right shift)
print(8 >> 2)
"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010
"""

# ESTRUCTURAS DE CONTROL

# CONDICIONALES
# IF
x = 7
y = 5

if x > y:
    print("x es mayor que y")

# ELIF

x = 5
y = 7

if x > y:
    print("x es mayor que y")
elif y > x:
    print("y es mayor que x")

# ELSE

x = 7
y = 7

if x > y:
    print("x es mayor que y")
elif y > x:
    print("y es mayor que x")
else:
    print("x es igual que y")

# SHORT HAND IF

x = 7
y = 5

if x > y: print("x es mayor que y")

# SHORT HAND IF... ELSE

x = 5
y = 7

print("x es mayor que y") if x > 7 else print("y es mayor que x")

# MATCH CASE

fruta = "manzana"

match fruta:
    case "naranja":
        print("Es una naranja")
    case "platano":
        print("Es un platano")
    case "frutilla":
        print("Es una frutilla")
    case "manzana":
        print("Es una manzana")

# ITERATIVAS

# FOR
frutas = ["manzana", "naranja", "platano"]
for fruta in frutas:
    print(fruta)

# WHILE
i = 0
while i < 3:
    print("meow")
    i += 1

# EXCEPCIONES

while True:
    try:
        user_input = int(input("Que es n?: "))

    except ValueError:
        print("valor incorrecto, trate nuevamente")
        pass

    else:
        print("El valor de n es:", user_input)
        break

# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for n in range(10, 56):
    if n % 2 == 0 and n % 3 != 0 and n != 16:
        print(n)

