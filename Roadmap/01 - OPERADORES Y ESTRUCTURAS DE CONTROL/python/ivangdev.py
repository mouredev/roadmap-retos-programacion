# Suma
suma = 10 + 10
print("Suma:", suma)

# Resta
resta = 10 - 5
print("Resta:", resta)

# Multiplicacion
multiplicacion = 10 * 5
print("Multiplicacion:", multiplicacion)

# Division
division = 10 / 2
print("Division:", division)

# Modulo
modulo = 10 % 3
print("Modulo:", modulo)

# Potencia
potencia = 2**3
print("Potencia:", potencia)

# --------------------------- Comparacion---------------------------

if 1 == 1:
    print("1 es igual a 1")
if 5 > 4:
    print("5 es mayor que 4")
if 3 < 4:
    print("3 es menor que 4")
if 7 >= 6:
    print("7 es mayor o igual que 6")
if 1 <= 2:
    print("1 es menor o igual que 2")
if 3 != 2:
    print("3 es distinto de 2")

# ------------------------------ Logicos -------------------------
A = 3
B = 2
if A > B and isinstance(A, int):
    print("A es mayor que B y A es un entero")

if A > B or B > A:
    print("A es mayor que B o B es mayor que A")

if not A == B:
    print("A no es igual a B")
# ------------------------------ Asignacion ------------
C = 5
print("Valor inicial de C:", C)
C += 2
print("Despues de sumar 2:", C)
C -= 1
print("Despues de restar 1:", C)
C *= 3
print("Despues de multiplicar por 3:", C)
C /= 2
print("Despues de dividir entre 2:", C)
C %= 2
print("Despues de aplicar modulo 2:", C)
C **= 2

# ----------------- Operadores a nivel de Bits -----------------

# & es un AND lógico pero aplicado a cada bit del número
a = 3
b = 3
a &= B
print(a)

# |=   # OR a nivel de bits y asigna
a |= B
print(a)

# ^=   # XOR a nivel de bits y asigna
a ^= B
print(a)

# >>=  # corrimiento a la derecha y asigna
a = 8
a >>= 1
print(a)

# <<=  # corrimiento a la izquierda y asigna
a <<= 1
print(a)

# ----------------- Operadores de Identidad -----------------
x = ["a", "b", "c"]
y = x
z = ["a", "b", "c"]

print(x is y)
print(x is z)
print(x is not z)  # No son el mismo objeto

# ----------------- Operadores de Pertenencia -----------------

numeros = [1, 2, 3, 4, 5]
print(3 in numeros)
print(6 in numeros)
print("b" in "base")
print("z" not in "base")  # Z no aparece en casa


# ----------------- Estructuras de control ------------------
if 6 > 5:
    print("6 es mayor que 5")
elif 8 == 8:
    print("8 no es igual a 8")
else:
    print("6 no es mayor que 5")

for i in range(5):
    print("Iteracion:", i)

while i <= 5:
    print("i es menor que 5")
    i += 1

# ---------------- Iterativas -----------------------------
# for
# while
# break, continue, pass, else

for numero in numeros:
    print(numero)

i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1

nums = [1, 2, 3, 4, 5, 8, 9, 0]
for numero in nums:
    if numero < 0:
        print("Es negativo")
        break
    elif numero == 0:
        print("Es 0, continuamos...")
        continue
    elif numero % 2 == 0:
        print("Es par")
        pass
else:
    print("No hay negativos")


# ---------------- excepciones -----------------------------
# try ... except
texto = "hola"
try:
    d = int(texto)
except ValueError:
    print("Error: Imposible convertir en numero")

# try ... except ... else
g = 5
try:
    d = int(g)
except ValueError:
    print("Error: Imposible convertir en numeroo")
else:
    print("Conversion correcta, x =", g)

# try ... except ... finally
try:
    d = int(texto)
except ValueError:
    print("Error: Imposible convertir en numero")
finally:
    print("Se termino el intento de conversion")

# raise → lanzar excepciones
a = "hola"
# try:
#     numero = int(a)
# except ValueError:
#     raise ValueError("No se puede convertir a entero")


# ---------------- Otras -----------------------------
# match - case
opcion = 1
match opcion:
    case 1:
        print("Opcion 1")
    case 2:
        print("Opcion 2")
    case 3:
        print("Opcion 3")
    case _:
        print("Opcion no valida")


# ---------------- DIFICULTAD EXTRA (opcional): -----------------------------
#
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

numeros = range(10, 56)
for numero in numeros:
    if numero % 2 == 0:
        if numero == 16:
            continue
        if numero % 3 == 0:
            continue
        print(numero)
