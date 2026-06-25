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
# *
# * DIFICULTAD EXTRA (opcional):
# * Crea un programa que imprima por consola todos los números comprendidos
# * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
# *
# * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
# */

# Aritmeticos
suma = 1 + 1
print("Suma: ", suma)
resta = 1 - 1
print("Resta: ", resta)
multiplicacion = 1 * 1
print("Multiplicacion: ", multiplicacion)
division = 1 / 1
print("Division: ", division)
modulo = 1 % 1
print("Modulo: ", modulo)
exponenciacion = 1 ** 1
print("Exponenciacion: ", exponenciacion)

# Logicos
and_operador = True and True
print("And: ", and_operador)
or_operador = True or True
print("Or: ", or_operador)
not_operador = not True
print("Not: ", not_operador)

# Comparacion
igualdad = 1 == 1
print("Igualdad: ", igualdad)
desigualdad = 1 != 1
print("Desigualdad: ", desigualdad)
mayor = 1 > 1
print("Mayor: ", mayor)
menor = 1 < 1
print("Menor: ", menor)
mayor_igual = 1 >= 1
print("Mayor o igual: ", mayor_igual)
menor_igual = 1 <= 1
print("Menor o igual: ", menor_igual)

# Asignacion
asignacion = 1
print("Asignacion: ", asignacion)
asignacion_suma = 1 + 1
print("Asignacion suma: ", asignacion_suma)
asignacion_resta = 1 - 1
print("Asignacion resta: ", asignacion_resta)
asignacion_multiplicacion = 1 * 1
print("Asignacion multiplicacion: ", asignacion_multiplicacion)
asignacion_division = 1 / 1
print("Asignacion division: ", asignacion_division)
asignacion_modulo = 1 % 1
print("Asignacion modulo: ", asignacion_modulo)
asignacion_exponenciacion = 1 ** 1
print("Asignacion exponenciacion: ", asignacion_exponenciacion)

# Identidad
is_operador = suma is resta
print("Is: ", is_operador)
is_not_operador = suma is not resta
print("Is not: ", is_not_operador)

# Pertenencia
in_lista = 1 in [1, 2, 3]
print("In: ", in_lista)
not_in_lista = 1 not in [1, 2, 3]
print("Not in: ", not_in_lista)

# Bit
binario = bin(25)
print("Binario: ", binario)
and_bit = 1 & 1
print("And bit: ", and_bit)
or_bit = 1 | 1
print("Or bit: ", or_bit)
not_bit = ~1
print("Not bit: ", not_bit)
xor_bit = 1 ^ 1
print("Xor bit: ", xor_bit)
left_bit = 1 << 1
print("Left bit: ", left_bit)
right_bit = 1 >> 1
print("Right bit: ", right_bit)

# Ejemplos de condicionales
if suma > resta:
    print("Suma es mayor a resta")
elif suma == resta:
    print("Suma es igual a resta")
else:
    print("Resta es mayor a suma")

# Ejemplos de iterativas
for i in range(suma, resta + 1):
    print(i)

# Ejemplos de excepciones
try:
    print(suma / resta)
except ZeroDivisionError:
    print("Error: Division por cero")

# Dificultad extra
for i in range(10, 55 + 1):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
