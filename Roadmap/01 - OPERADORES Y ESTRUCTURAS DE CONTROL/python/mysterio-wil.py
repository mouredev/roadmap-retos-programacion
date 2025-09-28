# EJERCICIO:
# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, dentidad, pertenencia, bits... (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

print("### OPERADORES ###")

# Operadores Aritméticos
print("\n--- Aritméticos ---")
a = 10
b = 3
print(f"Suma: 10 + 3 = {a + b}")
print(f"Resta: 10 - 3 = {a - b}")
print(f"Multiplicación: 10 * 3 = {a * b}")
print(f"División: 10 / 3 = {a / b}")
print(f"Módulo: 10 % 3 = {a % b}")
print(f"Exponenciación: 10 ** 3 = {a ** b}")
print(f"División entera: 10 // 3 = {a // b}")

# Operadores Lógicos
print("\n--- Lógicos ---")
print(f"AND (True and False): {True and False}")
print(f"OR (True or False): {True or False}")
print(f"NOT (not True): {not True}")

# Operadores de Comparación
print("\n--- Comparación ---")
print(f"Igualdad (10 == 3): {10 == 3}")
print(f"Desigualdad (10 != 3): {10 != 3}")
print(f"Mayor que (10 > 3): {10 > 3}")
print(f"Menor que (10 < 3): {10 < 3}")
print(f"Mayor o igual que (10 >= 10): {10 >= 10}")
print(f"Menor o igual que (10 <= 3): {10 <= 3}")

# Operadores de Asignación
print("\n--- Asignación ---")
x = 5
print(f"Asignación simple: x = {x}")
x += 2
print(f"Suma y asignación: x += 2 -> x = {x}")
x -= 1
print(f"Resta y asignación: x -= 1 -> x = {x}")
x *= 3
print(f"Multiplicación y asignación: x *= 3 -> x = {x}")
x /= 2
print(f"División y asignación: x /= 2 -> x = {x}")

# Operadores de Identidad
print("\n--- Identidad ---")
y = x
z = 5.0
print(f"is (x is y): {x is y}")
print(f"is not (x is not z): {x is not z}")

# Operadores de Pertenencia
print("\n--- Pertenencia ---")
lista = [1, 2, 3, 4, 5]
print(f"in (3 in lista): {3 in lista}")
print(f"not in (6 not in lista): {6 not in lista}")

# Operadores de Bits
print("\n--- Bits ---")
p = 10  # 1010
q = 3   # 0011
print(f"AND a nivel de bits (10 & 3): {p & q}")
print(f"OR a nivel de bits (10 | 3): {p | q}")
print(f"XOR a nivel de bits (10 ^ 3): {p ^ q}")
print(f"NOT a nivel de bits (~10): {~p}")
print(f"Desplazamiento a la izquierda (10 << 2): {p << 2}")
print(f"Desplazamiento a la derecha (10 >> 1): {p >> 1}")

# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones...

print("\n### ESTRUCTURAS DE CONTROL ###")

# Condicionales
print("\n--- Condicionales (if, elif, else) ---")
edad = 18
if edad < 18:
    print("Eres menor de edad.")
elif edad == 18:
    print("Tienes 18 años.")
else:
    print("Eres mayor de edad.")

# Iterativas
print("\n--- Iterativas (for) ---")
print("Imprimiendo números del 1 al 3:")
for i in range(1, 4):
    print(i)

print("\n--- Iterativas (while) ---")
contador = 3
print("Cuenta regresiva desde 3:")
while contador > 0:
    print(contador)
    contador -= 1

# Excepciones
print("\n--- Excepciones (try, except, finally) ---")
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Se intentó dividir por cero. Error: {e}")
finally:
    print("Este bloque (finally) se ejecuta siempre.")

# - Debes hacer print por consola del resultado de todos los ejemplos.
# (Esta instrucción se cumple a lo largo de todo el código)

# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

print("\n### DIFICULTAD EXTRA ###")
print("Números entre 10 y 55, pares, no 16 y no múltiplos de 3:")
for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)
