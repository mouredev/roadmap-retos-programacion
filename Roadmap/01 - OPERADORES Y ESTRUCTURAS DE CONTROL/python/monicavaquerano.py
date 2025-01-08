# Mónica Vaquerano
# https://monicavaquerano.dev

# EJERCICIO 01:
# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
# (Ten en cuenta que cada lenguaje puede poseer unos diferentes)


print("\nOperadores Aritméticos:")
x, y = 2, 2

suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y
modulo = x % y
exponencial = x**y
floor_division = x // y

print("Suma: x + y =", suma)
print("Resta: x - y =", resta)
print("Multiplicación: x * y =", multiplicacion)
print("División: x / y =", division)
print("Modulo: x % y =", modulo)
print("Exponencial: x ** y =", exponencial)
print("Floor division: x // y =", floor_division)

print("\nOperadores de Asignación:")
print("X = 10")
print("x += 2")
print("x -= 3")
print("x *= 8")
print("x /= 6")
print("x %= 2")
print("x %= 3")
print("x //= 1")
print("x **= 5")
print("x &= 0")
print("x |= 3")
print("x ^= 3")
print("x >>= 3")
print("x <<= 3")


print("\nOperadores de Comparación:")
x, y = 12, 6
if x == 12:
    print("X es igual a 12 (x == 12)")
if x != y:
    print("X no es igual a Y (x != y)")
if x > y:
    print("X es mayor a Y (x > y)")
if y < x:
    print("Y es menor a X (y < x)")
if y >= 4:
    print("Y es mayor o igual que 4 (y >= 4)")
if x <= 20:
    print("X es menor o igual que 20 (x <= 20)")

print("\nOperadores de Lógicos:")
if x > y and x == 12:
    print("X es mayor que Y, y X es igual a 12 (x > y and x == 12)")
if x != 12 or y == 6:
    print("X es diferente a 12 o Y es igual a 6 (x != 12 or y == 6)")
if not (x != 12 and y != 6):
    print("No es X diferente a 12 y Y diferente a 6 (not (x != 12 and y != 6))")

print("\nOperadores de Identidad:")
x, y = 5, 10
print(f"X is Y?: {x is y}")
print(f"X is not Y?: {x is not y}")

print("\nOperadores de Pertenencia:")
list = [5, 10, 20, 55, 75]
print(f"20 is in List?: {20 in list}")
print(f"20 is not in List?: {20 not in list}")

# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
# que representen todos los tipos de estructuras de control que existan
# en tu lenguaje:
# Condicionales, iterativas, excepciones...
# Debes hacer print por consola del resultado de todos los ejemplos.
print("\nEstructuras de Control Condicional:")
list = [-3, 0, 1, 6]
for item in list:
    item *= 2
    if item < 0:
        print("Soy un número negativo:", item, end=". ")
    elif item == 0:
        print("Soy cero!", end=". ")
    elif 0 < item < 4:
        print("Soy un número entre 0 y 5:", item, end=". ")
    else:
        print("Soy un número mayor a 5:", item, end=". ")
print()

print("\nEstructuras de Control Ternario:")
for i in range(len(list)):
    print(
        "Soy un número negativo" if list[i] <= 0 else "Soy un número positivo", end=". "
    )
print()

print("\nEstructuras de Control Iterativas:")
print("While loop:")
counter = 0
while counter < 3:
    print("Counter es menor a 3: counter =", counter, end=". ")
    counter += 1
print()

print("\nDo-While loop:")
counter = 3
while True:
    print("Counter es mayor a 0: counter =", counter, end=". ")
    counter -= 1
    if counter <= 0:
        break
print()

print("\nFor loop:")
for i in range(10, -1, -1):
    if i == 0:
        print("Boom!")
    else:
        print(i, end=", ")

print("\nFor in loop:")
for item in list:
    print("Item:", item, end=". ")
print()

print("\nFor in loop en objeto:")
contactos = {
    "Alice": {"telefono": "0123456"},
    "Bob": {"telefono": "0123456"},
    "Charlie": {"telefono": "0123456"},
}
for key, value in contactos.items():
    print(f"{key.capitalize()} -> ", end="")
    for subkey, subvalue in value.items():
        print(f"{subkey.capitalize()} | {subvalue}", end=" |")
    print()

print("\nExcepciones:")
print("Try and except:")
x = 0
try:
    if x == 0:
        raise ValueError
except:
    print("Ocurrió una excepción.")

print("\nMuchas excepciones:")
try:
    if x == 0:
        raise NameError
except NameError:
    print("La excepción NameError fue llamada.")
except:
    print("NameError salio bien, pero algo más salio mal")


print("\nExcepciones con Else:")
try:
    print("Hola, me ejecutaron con éxito!")
except:
    print("Algo salió mal")
else:
    print("Nada salió mal")


print("\nExcepciones con Finally:")
try:
    if x == 0:
        raise NameError
except:
    print("Algo salió mal: NameError fue llamado", end=". ")
finally:
    print("El bloque 'try except' terminó y ahora el bloque 'finally' se ejecuta.")


extra = """
                DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3:
"""
print(f"{extra}")
print("> ", end="")
for i in range(10, 56):
    if i % 2 == 0 and not i % 3 == 0 and i != 16:
        print(i, end=", ")
print()
