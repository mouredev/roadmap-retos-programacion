## Operadores en Python
a: int = 7
b: int = 2

# Operadores de comparación
a == b  # Igual a
a != b  # No igual a
a < b  # Menos que
a <= b  # Menos que o igual a
a >= b  # Mas grande que
a >= b  # Mayor que o igual a


# Operadores aritméticos
+a  # Positivo
-b  # Negativo
a + b  # Suma
a - b  # Resta
a * b  # Multiplicación
a / b  # División
a % b  # Modulo
a // b  # División de piso o división entera
a**b  # Exponenciación


# Operadores de asignación
number: int = 26
day = 19
digits = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
vocals = ["a", "e", "i", "o", "u"]


# Operadores lógicos
print(
    a > b and b == a
)  # and ej. a and b ambos valores deben cumplirse True and True = True
print(a > b and a != b)
print(
    a > b or b == a
)  # or ej. a or b uno o ambos se debe cumplir True and False = True
print(a > b or a != b)
print(not True)  # not ej. True = False; False = True


# Operadores de identidad
x: int = 1001
y: int = "1001"
a: str = "Hello, Pythonista!"
b: str = a
print(x is y)  # x is y
print(a is b)
print(id(x))
print(id(y))
print(x is not y)  # x is not y


# Operadores de membresía
print(5 in [32, 5, 3, 9, 0])  # Valor dentro de la colección
print(5 not in [32, 5, 3, 9, 0])  # El valor no esta dentro de la colección


# Operadores y expresiones de concatenación
print("Hello, " + "world!")  # Concatenación
print([1, 6, 9, 8] + [1, 9, 9, 7])
print(3 * "hello")  # Repetición
print(3 * [1, 9, 9, 7])


# Operador morsa y las expresiones de asignación
# Devuelve el resultado de la expresión.
# Asigna el resultado a una variable.
def validate_length(string):
    if (n := len(string)) < 8:
        print(f"La longitud {n} es demasiado corta, necesita al menos 8")
    else:
        print(f"La longitud {n} está bien!")


validate_length("Pythonista")

validate_length("Python")


# Operadores bit a bit y expresiones
# Bitwise AND
#   0b1100    12
# & 0b1010    10
# --------
# = 0b1000     8
bin(0b1100 & 0b1010)

print(12 & 10)

# Bitwise OR
#   0b1100    12
# | 0b1010    10
# --------
# = 0b1110    14
bin(0b1100 | 0b1010)

print(12 | 10)


# Operadores y expresiones de asignación aumentada
x, y = 2, 4
x += y  # x = x + y
x -= y  # x = x - y
x *= y  # x = x * y
x /= y  # x = x / y
x //= y  # x = x // y
x %= y  # x = x % y
x **= y  # x = x ** y

x &= y  # x = x & y [Y bit a bit aumentado ( conjunción )]
x |= y  # x = x | y [OR bit a bit aumentado ( disyunción )]
x ^= y  # x = x ^ y [XOR bit a bit aumentado ( disyunción exclusiva )]
x >>= y  # x = x >> y [Desplazamiento a la derecha bit a bit aumentado]
x <<= y  # x = x << y [Desplazamiento bit a izquierda aumentado]

## Condicionales
# if
x: int = 3
y: int = 5

'''
if x < y:
    print(True)
if x > y:
    print(True) 
if y:
    print(True)
if x or y:
    print(True)
if x and y:
    print(True)
'''
if "python" in "Hola python":
    print(True)

if 2 in [32, 1, 56, 2]:
    print(True)

# if else
x = 0
y = 0
if x < y:
    print(x, "Es menor que", y)
else:
    print(y, "Es mayor que", x)

# if elif

name = "Elkin"
greetings = "Hola"
if name == "Pedro":
    print(greetings, name)
elif name == "Juan":
    print(greetings, name)
elif name == "Elkin":
    print(greetings, name)
elif name == "Carlos":
    print(greetings, name)
else:
    print("No se a encontrado el nombre de", name)

# if en una sola linea
if "s" in "Elkin": print("1"); print("2"); print("3")

# Operadores ternarios
print(True) if 3 > 5 else print(False)

# Bucles en python (while: Mientras)
n = 5
while n > 0:
    n -= 1
    print(n)
a = ["foo", "bar", "baz"]
while a:
    print(a.pop(-1))
#  while and break

n = 0
while n < 10:
    n += 1
    if n == 2:
        break
    print(n)
print("Loop ended.")

# While and continue
n = 0
while n < 10:
    n += 1
    if n == 2:
        continue
    print(n)
print("End loop")

# while and clause
n = 0
while n < 3:
    n += 1
    print(n)
else:
    print("End loop")

a = ["foo", "bar", "baz"]
while True:
    if not a:
        break
    print(a.pop(-1))
print(a)
# bucles anidados
age = 45
gender = "F"

if age < 18:
    if gender == "M":
        print("hijo")
    else:
        print("hija")
elif age >= 18 and age < 65:
    if gender == "M":
        print("Padre")
    else:
        print("Madre")
else:
    if gender == "M":
        print("Abuelo")
    else:
        print("Abuela")

a = ["foo", "bar"]
while len(a):
    print(a.pop(0))
    b = ["baz", "qux"]
    while len(b):
        print(">", b.pop(0))
# Bucles de ultima linea
n = 5
while n > 0: n -= 1; print(n)

nums = [1, 3, 9, 10, 27]
for n in nums:
    print(n)
# Esta es la forma de saber si un objeto es un iterable
nums = [1, 3, 9, 10, 27]
it = iter(nums)
print(next(it))

valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for v in valores.values():
    print(v)
    
for k in valores.keys():
    print(k)
valores = {"A": 4, "E": 3, "I": 1, "O": 0}

for k, v in valores.items():
    print("Keys:", k, "Values:", v)

for n in range(10):
    print(n)

for n in range(1, 10 , 3):
    print(n)
coleccion = [2, 4, 5, 7, 8, 4, 3, 4]
for e in coleccion:
    if e == 4:
        break
    print(e)

for e in coleccion:
    if e == 4:
        continue
    print(e)
coleccion = [2, 4, 5, 7, 8, 4, 3, 4]
v = 10
for n in coleccion:
    if n == v:
        break
    print(n)
else:
    print("No se encontró el numero", v)



""" 
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

n = 10
while n <= 55:
    if n % 2 == 0 and not n == 16 and not n % 3 == 0:
        print(n)
    n += 1
