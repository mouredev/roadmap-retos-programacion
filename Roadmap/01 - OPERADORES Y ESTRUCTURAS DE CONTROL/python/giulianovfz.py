"""
/*
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
 */
"""

# ejemplos operadores aritmeticos
a = 5
b = 3

print(f'suma a={a} b={b} a + b = {a+b}')
print(f'resta a={a} b={b} a - b = {a-b}')
print(f'multiplicación a={a} b={b} a * b = {a*b}')
print(f'división a={a} b={b} a / b = {a/b}')
print(f'módulo a={a} b={b} a % b = {a % b}')
print(f'División entera a={a} b={b} a // b = {a // b}')

# ejemplos operadores lógicos

c = 8

# and
if c > 5 and c < 11:
    print(f'Valor de c:{c}, c < 5 = {c > 5}, c < 11 = {c < 11}')

# or
if c < 5 or c < 11:
    print(f'Valor de c:{c}, c < 5 = {c < 5}, c < 11 = {c < 11}')

# not
if not (c < 5 and c < 11):
    print(f'Valor de c:{c}, not(c < 5 = {c < 5} and c < 11 = {
          c < 11}) = {not (c < 5 and c < 11)}')


# ejemplos de comparación

x = 7
y = 15
z = 3
# == igual a
if x == 7:
    print(f'El valor de x = {x}')

# != distinto de
if x != 10:
    print(f'El valor de x = {x}')

# > mayor que
if x > z:
    print(f'x={x},z={z} x > z = {x > z}')

# < menor que
if x < y:
    print(f'x={x},y={y} x < y = {x < y}')

# >= menor o igual que
if x >= 7:
    print(f'x={x} x >= 7 = {x >= 7}')

# <= mayor o igual que
if y <= 16:
    print(f'x={x} x >= 7 = {x <= 7}')

# ejemplo asignación

h = 7
print(f'h = {h}')

h += 4
print(f'h = h + 4 → h += 4: {h}')

h -= 4
print(f'h = h - 4 → h -= 4: {h}')

h *= 4
print(f'h = h * 4 → h *= 4: {h}')

h = 8
h /= 4
print(f'División, h = h / 4 → h /= 4: {h}')

h = 8
h %= 4
print(f'Módulo, h = h % 4 → h %= 4: {h}')

h = 8
h //= 4
print(f'División entera, h = h // 4 → h //= 4: {h}')

h = 8
h **= 4
print(f'Exponente, h = h ** 4 → h **= 4: {h}')

h = 8
h &= 4
print(f"""\n\toperador and comparador de bit a bit, El operador & compara cada bit
      y lo establece en 1 si ambos son 1, de lo contrario se establece en 0. El resultado
      binario lo convierte a decimal y este valor es retornado, por ejemplo

        8 = 1000
        4 = 0100
        ----------
            0000 → en decimal: 0

       h = h & 4 → h &= 4: {h}""")

h = 8
h |= 4
print(f"""\n\toperador or:| comparador de bit a bit, El operador | compara cada bit
      y lo establece en 1 si uno o ambos son 1; de lo contrario, se establece en 0,
      El resultado binario lo convierte a decimal y este valor es retornado, por ejemplo

        8 = 1000
        4 = 0100
        ----------
            1100 → en decimal: 12

       h = h | 4 → h |= 4: {h}""")

h = 6
h ^= 3
print(f"""\n\toperador xor:^ comparador de bit a bit, El operador ^ compara cada bit
      y lo establece en 1 si solo uno es 1; de lo contrario (si ambos son 1 o ambos son 0)
      se establece en 0, El resultado binario lo convierte a decimal y este valor es
      retornado, por ejemplo

        6 = 0110
        3 = 0011
        ----------
            0101 → en decimal: 5

       h = h ^ 3 → h ^= 3: {h}""")

h = 6
h1 = -7
print(f"""\n\toperador not:~ comparador de bit a bit, El operador ~ invierte cada bit
      (0 se convierte en 1 y 1 se convierte en 0), El resultado binario lo convierte
      a decimal y este valor es retornado, por ejemplo

                         6 → 0110
                             ↓↓↓↓
        invierto los bits   -1001
                             ↓↓↓↓
        invertir nuevamente -0110
                             +  1
                           ----------
                            -0111 → en decimal: -7
      para simplificarlo puede decir el binario le sumo y al transformarlo a decimal se
      le coloca el signo negativo primero, siempre y cuando el número sea positivo.

      vale decir 6 → 0110
                     +  1
                    ------
                    -0111 → en decimal: -7

       h = 6 → ~h : {~h}

      si el número es negativo tengo que hacer el complemento a 1 mencionado ateriormente,
      esto quiere decir convertir los ceros en unos y los unos en cero, sumarle uno y luego
      convertir nuevamente el binario.
      ejemplo:

                -7 →  -(0111)
                        ↓↓↓↓
      se convierte   -(-1000)
      se le suma 1    (+   1)
                    ---------
                       (1001)
      se convierte      ↓↓↓↓
                       (0110) en decimal: 6

        h1 = -7 → ~h1 : {~h1}
        """)


# Operadores de Pertenencia

# in
g = ["booleano", "enteros", "flotantes"]

print(f"""\nflotantes se encuentra en g("flotantes" in g): {
      "flotantes" in g}\n""")

# not in
print(f"""\nstrings no se encuentra en g("strings" not in g): {
      "strings" not in g}\n""")
