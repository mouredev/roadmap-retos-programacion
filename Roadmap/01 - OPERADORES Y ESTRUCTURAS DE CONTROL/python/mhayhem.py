# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

print("Operadores Aritméticos:")
print(f"suma: 5 + 6 = {5 + 6}")
print(f"resta: 10 - 4 = {10 - 4}")
print(f"multiplicacion: 3 x 20 = {3 * 20}")
print(f"división: 245 / 3 = {245 / 3}")
print(f"división entera: 245 // 3 = {245 // 3}")
print(f"módulo (resto): 34 % 3 = {34 % 3}")
print(f"exponente: 2 ** 3 = {2 ** 3}")
print("\nOperadores de Comparación: (retornán un booleano)")
print(f"igualdqad: 5 == 5 = {5 == 5}")
print(f"diferencia: 6 != 4 = {6 != 4}")
print(f"mayor que: 3 < 10 = {3 < 10} también puede ser mayor o igual que: 3 <= 10 = {3 <= 10}")
print(f"menor que: 20 > 2 = {20 > 2} también puede ser menor o igual que: 20 >= 2 = {20 >= 2}")
print("\nOperadores Lógicos: (retornán un booleano)")
print(f"operador AND: verdadadero y falso =  {True and False}")
print(f"operador OR: verdadero o falso = {True or False}")
print(f"operador NOT: negación de verdadero = {not True}")
print("\nOperadores de Asignación:")
x = 5
print(f"operador de asignacion: x = 5, donde x es una variable que almacena el valor {x}")
x += 3
print(f"operador de asignacion mas suma: x += 3, x ahora es {x}")
x -= 2
print(f"operador de asignacion mas suma: x -= 2, x ahora es {x}")
x *= 5
print(f"operador de asignacion mas suma: x *= 5, x ahora es {x}")
x /= 2
print(f"operador de asignacion mas suma: x /= 2, x ahora es {x}")
x //= 3
print(f"operador de asignacion mas suma: x //= 3, x ahora es {x}")
x %= 4
print(f"operador de asignacion mas suma: x %= 4, x ahora es {x}")
x **= 2
print(f"operador de asignacion mas suma: x **= 2, x ahora es {x}")
print("\nOperadores de Identidad: (retornán un booleano)")
x = "python"
print(f"operador is: x is 'python' = {x is 'python'}")
print(f"operador is not: x is not 'java' = {x is not 'java'}")
print("\nOperadores de Pertenencia: (retornán un booleano)")
lista = [1, 2, 3, 4, 5]
print(f"operador in: 3 in lista = {3 in lista}")
print(f"operador not in: 6 not in lista = {6 not in lista}")
print("\nOperadores Bit a Bit:")
print(f"AND bit a bit: 5 & 3 = {5 & 3}")
print(f"OR bit a bit: 5 | 3 = {5 | 3}")
print(f"XOR bit a bit: 5 ^ 3 = {5 ^ 3}")
print(f"NOT bit a bit: ~5 = {~5}") # NOT invierte todos los bits y no lo puse en ele pull request
print(f"Desplazamiento a la izquierda: 5 << 1 = {5 << 1}")
print(f"Desplazamiento a la derecha: 5 >> 1 = {5 >> 1}")

# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
#   Condicionales, iterativas, excepciones...
print("\nEstructuras de Control Condicionales:")
"""condicionalonales 'if' y 'else': con ellos podemos ejecutar un bloque de código si se cumple una condición. Además, podemos añadirle otro condicional 'elif'
para evaluar múltiples condiciones."""

x = 17
if x > 10:
    print("es mayor")
elif x > 10 and x < 20:
    print("es mayor que 10 pero menor a 20")
else:
    print("es menor")
print("\nEstructuras de Control Iterativas:")

"""con las estructuras de control iterativas podemos ejecutar un bloque de código varias veces, ya sea un número determinado de veces o mientras se cumpla una condición.
Con un bucle 'for' podemos iterar sobre una lista de números e imprimir cada uno de ellos."""

for n in range(6):
    print(n)
"""Con un bucle 'while' podemos seguir ejecutando un bloque de código mientras una condición sea verdadera."""
while x < 5:
    print(x)
    x += 1  
print("\nEstructuras de Control de Excepciones:")
"""con la estructura de control de excepciones 'try-except' podemos manejar errores que podrían ocurrir en nuestro programa, también podemos usar 'finally'
para ejecutar un bloque de código al final, independientemente de si se produjo un error o no."""
x = None
try:
    print(x + 5)
except TypeError:
    print("Error: No se puede sumar None a un número.")
finally:
    print("Este bloque se ejecuta siempre, haya o no un error.")
# - Debes hacer print por consola del resultado de todos los ejemplos.
#
# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

print("\nDIFICULTAD EXTRA:")
for n in range(10, 56):
    if n % 2 == 0 and n != 16 and n % 3 != 0:
        print(n)