"""
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.

DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

# Operadores Aritméticos
print("Operadores Aritméticos: +, -, *, /, //, %, **")
print(f"\nLa suma de 5 + 4 es {5 + 4} ") # Suma
print(f"La resta de 5 - 4 es {5 - 4} ") # Resta
print(f"La multiplicación de 5 * 4 es {5 * 4} ") # Multiplicacion
print(f"La división de 5 / 4 es {5 / 4} ") # Division
print(f"La división entera de 5 // 4 es {5 // 4} ") # Division Entera
print(f"El módulo de 5 % 4 es {5 % 4} ") # Modulo
print(f"La exponenciación de 5 ** 4 es {5 ** 4} ") # Exponenciacion
print("-" * 50)

# Operadores de Comparación
print("\nOperadores de Comparación: ==, !=, >, <, >=, <=")
print(f"\nEl resultado de 5 == 5 es {5 == 5}") # Igual a
print(f"El resultado de 5 != 5 es {5 != 5}") # Distinto a
print(f"El resultado de 5 > 4 es {5 > 5}") # Mayor que
print(f"El resultado de 5 < 6 es {5 < 5}") # Menor que
print(f"El resultado de 5 >= 7 es {5 >= 5}") # Mayor o igual que
print(f"El resultado de 5 <= 5 es {5 <= 5}") # Menor o igual que
print("-" * 50)

# Operadores Lógicos
print("\nOperadores Lógicos: and, or, not")
print(f"Operador And/&&: {True and True}") # And: Retorna True si ambas condiciones son verdaderas
print(f"Operador Or/||: {False or True}") # Or: Retorna True si al menos una de las condiciones es verdadera
print(f"Operador Not/!: {not True}") # Not: Invierte el valor de la condicion (si es True se convierte en False, y viceversa)
print("-" * 50)

# Operadores de Asignación
print("\nOperadores de Asignación: =, +=, -=, *=, /=, //=, **=, %=")
numero1 = 1 # Asignacion
print(f"\nEl resultado de declarar una variable y asignarle un 1 es {numero1}")
numero1 += 2 # Suma y Asignacion
print(f"El resultado de sumar 2 y asignarlo a la variable es {numero1}")
numero1 -= 1 # Menos y Asignacion
print(f"El resultado de restar 1 y asignarlo a la variable es {numero1}")
numero1 *= 4 # Multiplicacion y Asignacion
print(f"El resultado de multiplicar por 4 y asignarlo a la variable es {1}")
numero1 /= 2 # Division y Asignacion
print(f"El resultado de dividir con 2 y asignarlo a la variable es {numero1}")
numero1 //= 2 # Division entera y Asignacion
print(f"El resultado de realizar una division entera con 2 y asignarlo a la variable es {numero1}")
numero1 **= 3 # Exponenciacion y Asignacion
print(f"El resultado de exponenciar por 3 y asignarlo a la variable es {numero1}")
numero1 %= 5 # Modulo y Asignacion
print(f"El resultado de modulo con 5 y asignarlo a la variable es {numero1}")
print("-" * 50)

# Operadores de Identidad
print("\nOperadores de Identidad: is, is not")
numero2 = numero1
print(f"\nnumero1 = {numero1}\nnumero2 = {numero2}")
print(f"¿Las variables numero1 y numero2 hacen referencia al mismo objeto?: {numero1 is numero2}") # is: Comprueba si dos variables hacen referencia al mismo objeto
print(f"¿Las variables numero1 y numero2 no hacen referencia al mismo objeto?: {numero1 is not numero2}") # is not: Comprueba si dos variables no hacen referencia al mismo objeto
print("-" * 50)

# Operadores de Pertenencia/membresía
print("\nOperadores de Pertenencia: in, not in")
lista = [1, 2, 3]
print(f"\nLista: {lista}")
print(f"¿El numero 2 esta en la lista? {2 in lista}") # in: Verifica si un elemento esta contenido dentro de una secuencia, como podria ser una lista
print(f"¿El numero 4 esta en la lista? {4 not in lista}") # not in: Verifica que un elemento no este contenido en una secuencia
print("-" * 50)

# Operadores de Bit a Bit/Bitwise
print("\nOperadores de Bit a Bit: &, |, ^, ~, <<, >>")
bit1 = 4 # 0100
bit2 = 2 # 0010
print(f"\nAND: 4(0100) & 2(0010) es igual a {bit1 & bit2}({bin(bit1 & bit2)})")
print(f"OR: 4 | 2 es igual a {bit1 | bit2}({bin(bit1 | bit2)})")
print(f"XOR: 4 ^ 2 es igual a {bit1 ^ bit2}({bin(bit1 ^ bit2)})")
print(f"NOT: ~4 es igual a {~bit1}({bin(~bit1)})")
print(f"Desplazamiento derecha: 4 >> 2 es igual a {bit1 >> bit2}({bin(bit1 >> bit2)})")
print(f"Desplazamiento izquierdo: 4 << 2 es igual a {bit1 << bit2}({bin(bit1 << bit2)})")
print("-" * 50)

# Estructuras de Control

# Estructuras de Control Condicional: if, elif, else
x = 10
if x > 0:
    print("\nEs positivo")
elif x == 0:
    print("\nEs cero")
else:
    print("\nEs negativo")
print("-" * 50)

# Estructuras de Control Bucles: while, for
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
print("-" * 50)

for numero in range(11):
    print(numero, end= "-")
print()
print("-" * 50)

# Estructuras de Control de Flujo: break, continue, pass
for i in range(10):
    if i == 3:
        continue # Salta a la siguiente iteracion
    if i == 7:
        break # finaliza el for
    print(i)
print("-" * 50)

# Estructuras de Control de Excepciones: try, except, finally
try: 
    x = 10 / 0
except ZeroDivisionError: # Se ejecuta si se produce un error tipo ZeroDivisionError
    print("No se puede dividir entre cero")
finally: # Siempre se ejecuta
    print("Finalizo la operación")
print("-" * 50)

# EXTRA
print("\nSe imprimiran los numeros del 10 al 55(pares incluidos), excepto los multiplos de 3 o el numero 16:")
print([x for x in range(10, 56) if x % 3 != 0 and x != 16 and x % 2 == 0])
print("-" * 50)