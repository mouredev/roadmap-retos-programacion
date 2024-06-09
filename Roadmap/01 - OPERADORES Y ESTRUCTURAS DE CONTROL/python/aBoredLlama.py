# Operadores del lenguaje Python.

## Operadores aritméticos.

print("Suma: 2 + 2 =", 2 + 2) # sirve para sumar dos números o variables.
print("Resta: 2 - 2 =", 2 - 2) # sirve para restar dos números o variables.
print("Multiplicación: 2 * 2 =", 2 * 2) # sirve para multiplicar dos números o variables.
print("División: 2 / 2 =", 2 / 2) # sirve para dividir dos números o variables.
print("Módulo: 2 % 2 =", 2 % 2) # sirve para obtener el residuo de una división.
print("Exponente: 2 ** 2 =", 2 ** 2) # sirve para elevar un número a una potencia.
print("División entera: 2 // 2 =", 2 // 2) # sirve para obtener la parte entera de una división.

## Operadores de asignación.

print("Asignación: 2 =", 2) # sirve para asignar un valor a una variable.
print("Suma y asignación (+=): x = 2, x += 2 =", 2 + 2) # sirve para sumar un valor a una variable y asignar el resultado.
print("Resta y asignación (-=): x = 2, x -= 2 =", 2 - 2) # sirve para restar un valor a una variable y asignar el resultado.
print("Multiplicación y asignación (*=): x = 2, x *= 2 =", 2 * 2) # sirve para multiplicar un valor a una variable y asignar el resultado.
print("División y asignación (/=): x = 2, x /= 2 =", 2 / 2) # sirve para dividir un valor a una variable y asignar el resultado.
print("Módulo y asignación (%=): x = 2, x %= 2 =", 2 % 2) # sirve para obtener el residuo de una división y asignar el resultado.
print("Exponente y asignación (**=): x = 2, x **= 2 =", 2 ** 2) # sirve para elevar un número a una potencia y asignar el resultado.
print("División entera y asignación (//=): x = 2, x //= 2 =", 2 // 2) # sirve para obtener la parte entera de una división y asignar el resultado.

## Operadores de comparación.

print("Igualdad: 2 == 2 es", 2 == 2) # sirve para comparar si dos valores o variables son iguales.
print("Desigualdad: 2 != 3 es", 2 != 3) # sirve para comparar si dos valores o variables son diferentes.
print("Mayor que: 2 > 3 es", 2 > 3) # sirve para comparar si un valor es mayor que otro.
print("Menor que: 2 < 3 es", 2 < 3) # sirve para comparar si un valor es menor que otro.
print("Mayor o igual que: 2 >= 2 es", 2 >= 2) # sirve para comparar si un valor es mayor o igual que otro.
print("Menor o igual que: 2 <= 3 es", 2 <= 3) # sirve para comparar si un valor es menor o igual que otro.

## Operadores lógicos.

print("AND: 2 + 2 == 4 and 3 - 1 == 2 es", 2 + 2 == 4 and 3 - 1 == 2) # sirve para realizar una operación AND lógica.
print("OR: 2 + 2 == 4 or 3 - 1 == 2 es", 2 + 2 == 4 or 3 - 1 == 2) # sirve para realizar una operación OR lógica.
print("NOT: not 2 + 2 == 4 es", not 2 + 2 == 4) # sirve para realizar una operación NOT lógica.

## Operadores de identidad.

print("Identidad: 2 is 2 es", 2 is 2) # sirve para verificar si dos variables son el mismo objeto.
print("No identidad: 2 is not 3 es", 2 is not 3) # sirve para verificar si dos variables no son el mismo objeto.

## Operadores de membresía.

print("Membresía: 'a' in 'abc' es", 'a' in 'abc') # sirve para verificar si un elemento está presente en una secuencia.
print("No membresía: 'd' not in 'abc' es", 'd' not in 'abc') # sirve para verificar si un elemento no está presente en una secuencia.

## Operadores de bits.

print("AND bit a bit: 2 & 3 es", 2 & 3) # sirve para realizar una operación AND bit a bit.
print("OR bit a bit: 2 | 3 es", 2 | 3) # sirve para realizar una operación OR bit a bit.
print("XOR bit a bit: 2 ^ 3 es", 2 ^ 3) # sirve para realizar una operación XOR bit a bit.
print("NOT bit a bit: ~2 es", ~2) # sirve para realizar una operación NOT bit a bit.
print("Desplazamiento a la derecha: 2 >> 1 es", 2 >> 1) # sirve para realizar un desplazamiento a la derecha.
print("Desplazamiento a la izquierda: 2 << 1 es", 2 << 1) # sirve para realizar un desplazamiento a la izquierda.

# Estructuras de Control.

## Condicionales.

name = input("Introduce tu nombre: ")
letter = input("Introduce una letra: ")

if letter in name and name != "aBoredLlama":
    print(f"La letra \'{letter}' está en el nombre {name}.")
elif name == "aBoredLlama" and letter in name:
    print("¡Hola todopoderoso aBoredLlama!")
else:
    print(f"La letra \'{letter}' no está en el nombre {name}.")

## Iteraciones.

a = 0
print(f"a se inicializó en {a}")
for i in range(10):
    a += 2
    print(f"a se incrementó a {a}")

b = 2
c = 5

while b < c:
    print(f"el resultado de la operación AND entre {b} y {c} es {b & c}")
    b += 1
    c -= 1

## Excepciones.

try:
    mensaje = int(input("Introduce un número decimal: "))
except ValueError:
    print("Ingrese un número válido. No se aceptan letras ni caracteres especiales.")
else:
    print(f"El número ingresado es {mensaje}.")
finally:
    print("¡Gracias por participar!")

# Ejercicio de desafio.

a = 10
b = 55

for i in range(a,b):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
