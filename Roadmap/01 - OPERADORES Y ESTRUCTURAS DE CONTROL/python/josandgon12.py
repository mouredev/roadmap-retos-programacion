"""
EJERCICIO: Operadores y Estructuras de Control en Python
"""

print("=" * 60)
print("OPERADORES EN PYTHON")
print("=" * 60)

# 1. OPERADORES ARITMÉTICOS
print("\n--- OPERADORES ARITMÉTICOS ---")
a = 15
b = 4
print(f"a = {a}, b = {b}")
print(f"Suma (a + b): {a + b}")
print(f"Resta (a - b): {a - b}")
print(f"División (a / b): {a / b}")
print(f"División entera (a // b): {a // b}")
print(f"Módulo (a % b): {a % b}")
print(f"Potencia (a ** b): {a ** b}")

# 2. OPERADORES DE COMPARACIÓN
print("\n--- OPERADORES DE COMPARACIÓN ---")
x = 10
y = 20
print(f"x = {x}, y = {y}")
print(f"Igual (x == y): {x == y}")
print(f"Diferente (x != y): {x != y}")
print(f"Mayor que (x > y): {x > y}")
print(f"Menor que (x < y): {x < y}")
print(f"Mayor o igual (x >= y): {x >= y}")
print(f"Menor o igual (x <= y): {x <= y}")

# 3. OPERADORES LÓGICOS
print("\n--- OPERADORES LÓGICOS ---")
verdadero = True
falso = False
print(f"verdadero = {verdadero}, falso = {falso}")
print(f"AND (verdadero and falso): {verdadero and falso}")
print(f"OR (verdadero or falso): {verdadero or falso}")
print(f"NOT (not verdadero): {not verdadero}")

# 4. OPERADORES DE ASIGNACIÓN
print("\n--- OPERADORES DE ASIGNACIÓN ---")
numero = 10
print(f"Asignación inicial: numero = {numero}")
numero += 5
print(f"Suma y asignación (+=): {numero}")
numero -= 3
print(f"Resta y asignación (-=): {numero}")
numero *= 2
print(f"Multiplicación y asignación (*=): {numero}")
numero //= 3
print(f"División entera y asignación (//=): {numero}")
numero %= 5
print(f"Módulo y asignación (%=): {numero}")
numero **= 2
print(f"Potencia y asignación (**=): {numero}")

# 5. OPERADORES DE IDENTIDAD
print("\n--- OPERADORES DE IDENTIDAD ---")
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
print(f"lista1: {lista1} (id: {id(lista1)})")
print(f"lista2: {lista2} (id: {id(lista2)})")
print(f"lista3: {lista3} (id: {id(lista3)})")
print(f"lista1 is lista2: {lista1 is lista2}")
print(f"lista1 is lista3: {lista1 is lista3}")
print(f"lista1 is not lista2: {lista1 is not lista2}")

# 6. OPERADORES DE PERTENENCIA
print("\n--- OPERADORES DE PERTENENCIA ---")
frutas = ["manzana", "pera", "naranja"]
print(f"Lista de frutas: {frutas}")
print(f"'manzana' in frutas: {'manzana' in frutas}")
print(f"'uva' in frutas: {'uva' in frutas}")
print(f"'uva' not in frutas: {'uva' not in frutas}")

# 7. OPERADORES DE BITS
print("\n--- OPERADORES DE BITS ---")
num1 = 10  # 1010 en binario
num2 = 4   # 0100 en binario
print(f"num1 = {num1} ({bin(num1)}), num2 = {num2} ({bin(num2)})")
print(f"AND bit a bit (num1 & num2): {num1 & num2} ({bin(num1 & num2)})")
print(f"OR bit a bit (num1 | num2): {num1 | num2} ({bin(num1 | num2)})")
print(f"XOR bit a bit (num1 ^ num2): {num1 ^ num2} ({bin(num1 ^ num2)})")
print(f"NOT bit a bit (~num1): {~num1} ({bin(~num1)})")
print(f"Desplazamiento izquierda (num1 << 2): {num1 << 2} ({bin(num1 << 2)})")
print(f"Desplazamiento derecha (num1 >> 2): {num1 >> 2} ({bin(num1 >> 2)})")

print("\n" + "=" * 60)
print("ESTRUCTURAS DE CONTROL")
print("=" * 60)

# 1. CONDICIONALES (if, elif, else)
print("\n--- CONDICIONALES ---")
edad = 25
print(f"Edad: {edad}")
if edad < 18:
    print("Eres menor de edad")
elif edad < 65:
    print("Eres adulto")
else:
    print("Eres adulto mayor")

# Operador ternario
mensaje = "Par" if edad % 2 == 0 else "Impar"
print(f"La edad es: {mensaje}")

# 2. BUCLE FOR
print("\n--- BUCLE FOR ---")
print("Números del 1 al 5:")
for i in range(1, 6):
    print(f"  {i}")

print("Iterando sobre una lista:")
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(f"Color: {color}")

# 3. BUCLE WHILE
print("\n--- BUCLE WHILE ---")
contador = 0
print("Contando hasta 3:")
while contador < 3:
    contador += 1
    print(f"Contador: {contador}")

# 4. BREAK Y CONTINUE
print("\n--- BREAK Y CONTINUE ---")
print("Usando break (detener en 5):")
for i in range(1, 10):
    if i == 5:
        break
    print(f"{i}")

print("Usando continue (saltar números pares):")
for i in range(1, 8):
    if i % 2 == 0:
        continue
    print(f"{i}")

# 5. MANEJO DE EXCEPCIONES
print("\n--- MANEJO DE EXCEPCIONES ---")
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Error capturado: {e}")
except Exception as e:
    print(f"Otro error: {e}")
else:
    print("No hubo errores")
finally:
    print("Este bloque siempre se ejecuta")


# 6. MATCH-CASE
print("\n--- MATCH-CASE ---")
dia = 3
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4 | 5:
        print("Jueves o Viernes")
    case _:
        print("Fin de semana")

print("\n" + "=" * 60)
print("\nNúmeros entre 10 y 55 (incluidos), pares, que NO son 16 ni múltiplos de 3:")
print()

for numero in range(10, 56):
    # Debe ser par
    if numero % 2 != 0:
        continue
    
    # No debe ser 16
    if numero == 16:
        continue
    
    # No debe ser múltiplo de 3
    if numero % 3 == 0:
        continue
    
    print(numero)

# for i in range(10,56):
#     if i % 2 == 0 and i != 16 and i % 3 != 0:
#         print(i)