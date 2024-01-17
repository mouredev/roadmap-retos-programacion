#/*
# * EJERCICIO:
# * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
# *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
# * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
# *   que representen todos los tipos de estructuras de control que existan
# *   en tu lenguaje:
# *   Condicionales, iterativas, excepciones...
# * - Debes hacer print por consola del resultado de todos los ejemplos.

# ====== >> Operadores aritméticos << ======
# suma (+)
suma = 3 + 4
print(suma) # result: 7

# resta (-)
resta = 3 - 4
print(resta) # result: -1

# multiplicacion (*)
mult = 3 * 4
print(mult) # result: 12

# división (/)
division = 3 / 4
print(division) # result: 0.75

# división interna (//)
division_interna = 3 // 4
print(division_interna) # result: 0

# módulo (%)
modulo = 3 % 4
print(modulo) # result: 3

# exponenciación (**)
expo = 3 ** 4
print(expo) # result: 81

# ====== >> Operadores de comparación << ======
# igual (==)
comp1 = 3 == 4
print(comp1) # result: False

# diferente (!=)
comp2 = 3 != 4
print(comp2) # result: True

# más grande que (>)
comp3 = 3 > 4
print(comp3) # result: False

# mayor o igual (>=)
comp3 = 3 >= 4
print(comp3) # result: False

# menos que (<)
comp4 = 3 < 4
print(comp4) # result: True

# menos o igual (<=)
comp4 = 3 <= 4
print(comp4) # result: True

# ====== >> Operadores lógicos << ======
# and (and)
comp_log1 = 3 == 4 and "rojo" == "rojo"
print(comp_log1) # result: False

# or (or)
comp_log2 = 3 == 4 or "rojo" == "rojo"
print(comp_log2) # result: True

# not (not)
comp_log3 = not (3 == 4 or "rojo" == "rojo")
print(comp_log3) # result: False

# ====== >> Operadores de asignación << ======
# = 	x = 1
a, b, c, d, e, f = 10, 10, 10, 10, 10, 10
print(a) # result: 10
# +=	x = x + 1
b += 2
print(b) # result: 12
# -=	x = x - 1
c -= 3
print(c) # result: 7
# *=	x = x * 1
d *= 4
print(d) # result: 40
# /=	x = x / 1
e /= 5
print(e) # result: 2.0
# %=	x = x % 1
f %= 6
print(f) # result: 4

# ====== >> Operadores de identidad << ======
pokemon = ["Bulbasaur", "Charmander", "Squirtle"]
pokemon2 = ["Bulbasaur", "Charmander", "Squirtle"]
pokemon3 = pokemon

# is
print(pokemon is pokemon2) # result: False
print(pokemon is pokemon3) # result: True

# is not
print(pokemon is not pokemon2) # result: True
print(pokemon is not pokemon3) # result: False

# ====== >> Operadores de pertenencia << ======
# in
print("Pikachu" in pokemon) # result: False
# not in
print("Pikachu" not in pokemon) # result: True

# ====== >> Operadores bitwise << ======
# Ejemplos de equivalencias entre números decimales y binarios:
# 0 = “0”
# 1 = “1”
# 2 = “10”
# 3 = “11”
# 4 = “100”
# 5 = “101”
# 1029 es “10000000101” == 2**10 + 2**2 + 2**0 == 1024 + 4 + 1

# x << y    (x = x * 2 ** y)
x = 5 # equivalente a "101" en binario
y = 3 # equivalente a "11" en binario

result = x << y
print(result) # result: 40 (equivalente a "101000" en binario)
# es decir, aumentó 3 ceros a la derecha del binario

# x >> y    (x = x / 2 ** y)
x = 40 # equivalente a "101000" en binario
y = 3 # equivalente a "11" en binario

result = x >> y
print(result) # result: 5 (equivalente a "101" en binario)
# es decir, disminuyó 3 ceros a la derecha del binario

# x & y (and bit-a-bit)
# tabla verdad de "AND"
# False + False = False
# False + True = False
# True + False = False
# True + True = True

x = 5 # "101" en binario
y = 3 # "011" en binario
result = x & y
print(result) # result: 1 (equivalente a "001" en binario)

# x | y (or bit-a-bit)
# tabla verdad de "OR"
# False + False = False
# False + True = True
# True + False = True
# True + True = True

x = 5 # "101" en binario
y = 3 # "011" en binario
result = x | y
print(result) # result: 7 (equivalente a "111" en binario)

# x ^ y (xor bit-a-bit)
# tabla verdad de "XOR"
# False + False = False
# False + True = True
# True + False = True
# True + True = False

x = 5 # "101" en binario
y = 3 # "011" en binario
result = x ^ y
print(result) # result: 6 (equivalente a "110" en binario)

# ~x (devuelve el complemento)
x = 5 # "101" en binario
result = ~x
print(result) # result: -6 ("1111 1111 1111 1010" en binario [numero negativo])

# ====== >> Estructura de control (condicionales) << ======
elemento = "tierra"

# if-else
if elemento == "agua":
    print("El elemento es agua")
else:
    print("El elemento no es agua")

# elif
if elemento == "agua":
    print("El elemento es agua")
elif elemento == "tierra":
    print("El elemento es tierra")
elif elemento == "fuego":
    print("El elemento es fuego")
elif elemento == "aire":
    print("El elemento es aire")

# match-case
match elemento:
    case "agua":
        print("El elemento es agua")
    case "tierra":
        print("El elemento es tierra")
    case "fuego":
        print("El elemento es fuego")
    case "aire":
        print("El elemento es aire")
    case _:
        print("No es elemento")

# ====== >> Estructura de control (iterativas) << ======
# while
count = 5
while count > 0:
    print("count down:", count)
    count -= 1

# for-in
for counting in range(5):
    print("count up:", counting)

# ====== >> Estructura de control (excepciones) << ======
# try-except
try:
    x = 2
    y = 0
    result = x / y # result: ZeroDivisionError (division by zero)
    print(result)
except:
    print("ocurrió un error")

# * DIFICULTAD EXTRA (opcional):
# * Crea un programa que imprima por consola todos los números comprendidos
# * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
# *
# * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
# */
    
def dificultad_extra():
    """
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
    """
    for numero in range(56):
        if numero >= 10 and numero <= 55:
            if numero % 2 == 0:
                if numero != 16:
                    if not numero % 3 == 0:
                        print(numero)

dificultad_extra()