""" /*
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
 */ """

x = 5
y = 3
verdadero = True
falso = False
a = 0b0001
b = 0b1010
texto = "Esto es una cadena"
numero = 10

# OPERADORES

# Operadores aritméticos
suma = x + y
print(suma)

resta = x - y
print(resta)

multiplicacion = x * y
print(multiplicacion)

division = x / y 
print(division)

modulo = x % y
print(modulo)

exponente = x ** y
print(exponente)

cociente = x // y
print(cociente)

# Operadores de asignación
x = 7
print(x)

x += 2
print(x)

x -=  3
print(x)

x *= 5
print(x)

x /= 4
print(x)

x %= 2
print(x)

y //= 2
print(y)

x **= 3
print(x)

# Operadores lógicos
print(verdadero and  falso)

print(verdadero or falso)

print(verdadero and falso or verdadero)

print(verdadero or falso and falso)

print(not verdadero)

# Operadores de comparación
print(x==y)

print(x!=y)

print(x<y)

print(x>y)

print(x<=y)

print(x>=y)

# Operadores de identidad
print(y is x)

print(x is not y)

# Operadores de bit
print(bin(a&b))

print(bin(a|b))

print(bin(~a))

print(bin(a^b))

print(bin(a>>2))

print(bin(a<<1))

# Operadores de membresía
print(7 in [1, 2, 4, 8, 7])

print(4 not in (6, 1, 0, 3, 4))


# ESTRUCTURAS DE CONTROL

# If
if a != b:
    print(a)
# If y else
if a == b:
    print("Iguales")
else:
    print("No iguales") # Se puede esxcribir en una sóla línea de código -> print("Iguales" if a==b else "No iguales")
# If, elif y else
if x > y:
    print("Mayor x")
elif x < y:
    print("Mayor y")
else:
    print("Iguales")

# Match y case
animal = "perro"
match animal:
    case "perro": 
        print("Es un perro")
    case "gato": 
        print("Es un gato")
    case "pájaro":
        print("Es un pájaro")
    case _:
        print("Animal indeterminado")

# For
for i in range(0, 10):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in "Cadena":
    print(i)

for i in texto[::-1]:
    print(i)

for i in texto[::2]:
    print(i)
# For y break
for caracter in texto:
    if caracter == "d":
        print("Letra D encontrada")
        break
# For y continue
for caracter in texto:
    if caracter == "d":
        continue
    print(caracter)

# For, break, continue y pass
for caracter in texto:
    if caracter == "e":
        print("3")
    elif caracter == "a":
        print("Paso")
        pass
    elif caracter == "d":
        break
    elif caracter == "n":
        print("Vuelvo a empezar")
        continue 
    else:
        print(caracter)

# While
i = 0
while i < 11:
    print(i)
    i += 1
# While y else
i = 0
while i < 11:
    print(i)
    i += 1
else:
    print("i mayor que 10")
# While y break
i = 0
while i < 11:
    print(i)
    i += 1
    if i == 8:
        break
# While y continue
i = 0
while i < 11:
    i += 1
    if i == 8:
        continue
    print(i)

# While, break, continue y pass
i = 0
while i < 11:
    i += 1
    if i == 5:
        print("Paso")
        pass
    elif i == 2:
        print("Vuelvo a empezar")
        continue
    elif i == 10:
        break
    else: 
        print(i)

# Excepciones
try:
    for j in range(4,-4,-1):
        print(numero/j)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
finally:
    print("Esto se ejecuta siempre")


# DIFICULTAD EXTRA
for i in range(10, 56, 2):
    if i != 16 and i % 3 != 0:
        print(i)


