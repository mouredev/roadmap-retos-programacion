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
#Aritmeticos
print(5 + 3)  # Suma
print(5 - 3)  # Resta
print(5 * 3)  # Multiplicación
print(5 / 3)  # División
print(5 // 3) # División entera
print(5 % 3)  # Módulo
print(5 ** 3) # Potencia

#logicos
print(True and False) # AND
print(True or False)  # OR
print(not True)       # NOT

#comparacion
print(5 == 3)  # Igualdad
print(5 != 3)  # Diferente
print(5 > 3)   # Mayor que
print(5 < 3)   # Menor que
print(5 >= 3)  # Mayor o igual que
print(5 <= 3)  # Menor o igual que

#asignacion
a = 5
print(a)
a += 3  # Suma y asignación
print(a)
a -= 3  # Resta y asignación
print(a)
a *= 3  # Multiplicación y asignación
print(a)
a /= 3  # División y asignación
print(a)

#identidad
print(a is 5)  # Identidad
print(a is not 5)  # No identidad

#pertenencia
lista = [1, 2, 3, 4, 5]
print(3 in lista)  # Pertenencia
print(6 not in lista)  # No pertenencia

#bits
print(5 & 3)  # AND bit a bit
print(5 | 3)  # OR bit a bit
print(5 ^ 3)  # XOR bit a bit
print(~5)     # NOT bit a bit
print(5 << 1) # Desplazamiento a la izquierda
print(5 >> 1) # Desplazamiento a la derecha

#Estructuras de control
#Condicionales
if (5 > 3):
    print("5 es mayor que 3")
elif (5 < 3):
    print("5 es menor que 3")
else:
    print("5 es igual a 3")

#Iterativas
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)

while (a < 20):
    print(a)
    a += 1

#excepciones
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Se ha ejecutado el manejo de error")

# DIFICULTAD EXTRA 
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)