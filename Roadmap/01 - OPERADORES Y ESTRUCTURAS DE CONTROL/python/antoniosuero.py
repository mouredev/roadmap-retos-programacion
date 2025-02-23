#  * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *


# OPERADORES ARITMÉTICOS
print("\nOPERADORES ARITMÉTICOS: ")
print("Suma +\n5 + 2 =", 5 + 2)
print("Resta -\n5 - 2 =", 5 - 2)
print("Multiplicacíón *\n5 * 2 =", 5 * 2)
print("División /\n5 / 2 =", 5 / 2)
print("División entera //\n5 // 2 =", 5 // 2)
print("Módulo % (Residuo de la división)\n5 % 2 =", 5 % 2)
print("Exponente **\n5 ** 2=", 5 ** 2)

# OPERADORES DE COMPARACIÓN
print("\nOPERADORES DE COMPARACIÓN: ")
print("igual que ==\n5 == 2 =", 5 == 2)
print("diferente que !=\n5 != 2 =", 5 != 2)
print("mayor que >\n 5 > 2 =", 5 > 2)
print("menor que >\n 5 < 2 =", 5 < 2)
print("mayor o igual que >=\n 5 >= 2 =", 5 >= 2)
print("menor o igual que <=\n 5 <= 2 =", 5 <= 2)

# OPERADORES LÓGICOS
print("\nOPERADORES LÓGICOS: ")
print("y lógico: and\nTrue and False =", True and False)
print("o lógico: or\nTrue or False =", True or False)
print("no lógico: not\nnot False =", not False)

# OPERADORES DE ASIGNACIÓN
print("\nOPERADORES DE ASIGNACIÓN: ")
j = 1
print("asignación =\nj = 1")
j += 1
print("incremento +=\nj += 1, j =", j)
j -= 1
print("decremento -=\nj -= 1, j =", j)
j *= 4
print("multiplicación y asignación *=\nj *= 4, j =", j)
j /= 2
print("división y asignación /=\nj /= 2, j =", j)
j **= 2
print("exponente y asignación **=\nj **= 2, j =", j)
j //= 3
print("división entera y asignación //=\nj //= 3, j =", j)
j %= 1
print("módulo y asignación %=\nj %= 1, j =", j)

# OPERADORES DE IDENTIDAD
print("\nOPERADORES DE IDENTIDAD (is - is not): ")
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(f"a = {a}\nb = a\nc = {c}")
print("Es la misma identidad: a is b =", a is b)
print("Es la misma identidad: a is c =", a is c)
print("No es la misma identidad: a is not c =", a is not c)

# OPERADORES DE PERMANENCIA
print("\nOPERADORES DE PERMANENCIA (in - not in): ")
texto = "Campus MoureDevpro"
print("texto = \"Campus MoureDevpro\"")
print("Campus in texto =", "Campus" in texto)
print("Mundo in texto =", "Mundo" in texto)
print("Mundo not in texto =", "Mundo" not in texto)

# OPERADORES BIT A BIT O NIVEL DE BITS
print("\nOPERADORES BIT A BIT: ")
x = 12  # 0b1100
y = 6  # 0b0110
print(f"x = {x} # 1100\ny = {y}  # 0110")
print("AND (&) 1 si ambos bits son 1\nx & y =", x & y, "   # 0100")
print("OR (|) 1 si al menos un bit es 1\nx | y =", x | y, "  # 1110")
print("XOR (^) 1 si los bits son diferentes\nx ^ y =", x ^ y, "  # 1100")
print("NOT (~) Invierte los bits\n~x =", ~x,"    # 0011 complemento a 2")
print("<< Desplazamiento a la izquierda cada desplazamiento multiplica por 2\nx << 1 =", x << 1, " # 11000")
print(">> Desplazamiento a la derecha cada desplazamiento divide entre 2\nx >> 1 =", x >> 1, "  # 1100")

#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

for numero in range(10, 56):
  if numero == 16 or numero % 3 == 0 or numero % 2 != 0:
    continue
  print(numero)