'''
EJERCICIO:
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
'''
# Operadores Aritméticos

print("\n *******Operadores Aritméticos******* \n")
print(f"Suma: 5 + 5 = {5 + 5}")
print(f"Resta: 10 - 5 = {10 - 5}")
print(f"Multiplicación: 5 * 5 = {5 * 5}")
print(f"División: 10 / 2 = {10 / 2}")
print(f"División entera: 10 // 3 = {10 // 3}")
print(f"Resto: 10 % 3 = {10 % 3}")
print(f"Potencia: 2 ** 3 = {2 ** 3}")

# Operadores de Comparación

print("\n *******Operadores de Comparación******* \n")
print(f"Igualdad: 5 == 5 = {5 == 5}")
print(f"Diferente: 5 != 5 = {5 != 5}")
print(f"Mayor que: 5 > 3 = {5 > 3}")

# Operadores Lógicos

print("\n *******Operadores Lógicos******* \n")
print(f"And: True and False = {True and False}")
print(f"Or: True or False = {True or False}")
print(f"Not: not True = {not True}")

# Operadores de Asignación

print("\n *******Operadores de Asignación******* \n")
a = 5
print(f"Asignación: a = 5, a = {a}")
a += 5
print(f"Suma: a += 5, a = {a}")
a -= 5
print(f"Resta: a -= 5, a = {a}")
a *= 5
print(f"Multiplicación: a *= 5, a = {a}")
a /= 5
print(f"División: a /= 5, a = {a}")
a //= 2
print(f"División entera: a //= 2, a = {a}")
a %= 3
print(f"Resto: a %= 3, a = {a}")
a **= 2
print(f"Potencia: a **= 2, a = {a}")

# Operadores de Identidad

print("\n *******Operadores de Identidad******* \n")
a = 6
b = 5
print("Suponiendo a = 6 y b = 5")
print(f"Identidad: a is b = {a is b}")
print(f"No Identidad: a is not b = {a is not b}")

# Operadores de Pertenencia

print("\n *******Operadores de Pertenencia******* \n")
lista = [1, 2, 3, 4, 5]
print(f"Suponiendo la lista: {lista}")
print(f"Pertenencia: 2 in lista = {2 in lista}")
print(f"No Pertenencia: 2 not in lista = {2 not in lista}")

# Condicionales

print("\n *******Condicionales******* \n")

print("If, elif, else: 5>3 =\n")
if 5 > 3:
    print("5 es mayor que 3")
elif 5 < 3:
    print("5 es menor que 3")
else:
    print("5 es igual a 3")

# Iterativas
    
print("\n *******Iterativas******* \n")

print("For:\n")
for i in range(5):
    print(i)

print("\nWhile:\n")
i = 0
while i < 5:
    print(i)
    i += 1


# Dificultad Extra

print("\n *******Dificultad Extra******* \n")

for i in range (1,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)


