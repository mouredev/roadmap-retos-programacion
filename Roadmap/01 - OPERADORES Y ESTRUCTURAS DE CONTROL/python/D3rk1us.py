"""
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
"""

# Aritméticos

op1 = 2 + 2     # Suma
op2 = 3 - 2     # Resta
op3 = 4 * 2     # Multiplicación
op4 = 5 / 2     # División
op5 = 6 % 2     # Módulo
op6 = 7 ** 2    # Potencia
op7 = 8 // 2    # Divide con resultado de número entero.

print("Operadores Aritméticos:")
print(f"Suma = {op1}\nResta = {op2}\nMultiplicación = {op3}\nDivisión = {op4}\nMódulo = {op5}\nPotencia = {op6}\nResultado entero de la división = {op7}")

# Lógicos y condicional if

print("\nOperadores Lógicos:")


if True and True:
    print(f"True and True = {True and True}")    # True, si ambos elementos son verdaderos.

if True or False:
    print(f"True or False = {True or False}")    # True, si al menos un elemento es verdadero.
else:
    print(f"True or False = False")

print(f"not True = {not True}")                  # Devuelve lo contrario.

# De Comparación

a = 12
b = 7
c = 12

print("\nOperadores de Comparación:")
print(f"{a} > {b} = {a > b}")
print(f"{a} < {b} = {a < b}")
print(f"{a} == {c} = {a == c}")
print(f"{a} != {c} = {a != c}")
print(f"{a} <= {c} = {a <= c}")
print(f"{b} >= {a} = {b >= a}")


# Asignación

print("\nOperadores de Asignación:")
print("x += 2\nx -= 2\nx *= 2\nx /= 2\nx %= 2\nx //= 2\nx **= 2\nx &= 2\nx |= 2\nx ^= 2\nx >>= 2\nx <<= 2")	

# Identidad

v = "Hola"
x = 67

print("\nOperadores de Identidad:")
print(f"{v} is {x} = {v is x}")
print(f"{x} is not {v} = {x is not v}")
print(f"{x} is 67 = {x is 67}")

# Pertenencia

lista = [1, 2, 3, 4, 5, 6]

print("\nOperadores de Pertenencia:")
print(f"2 in lista = {2 in lista}")
print(f"5 not in lista = {5 not in lista}")

# Excepciones y bucle while

while True:
    try:
        num = int(input("Introduce un número: "))
        break
    
    except ValueError:
        print("No ha sido un número válido. Inténtalo de nuevo...")


# Ejercicio opcional con bucle for:

for i in range(10, 56):
    if i != 16 and i % 3 != 0 and i % 2 == 0:
        print(i)