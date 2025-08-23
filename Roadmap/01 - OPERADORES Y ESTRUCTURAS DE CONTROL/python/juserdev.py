'''
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
'''

print(10 + 2) 
print(10 - 2)
print(10 * 2)
print(10 / 2)
print(10 % 2)
print(10 ** 2)

a, b = False, True

result = a and b
print(result)
result = a or b
print(result)

c = not True
print(c)

a, b, c = 5, 10, 5

print(a > b)
print(a < b)
print(a <= b)
print(a >= b)
print(a == b)
print(a == c)
print(a != c)
print(a != b)

a += 4
print(a)
a -= 4
print(a)
a *= 4
print(a)
a /= 4
print(a)
a //= 4
print(a)
b %= 4
print(b)
b **= 4
print(b)

a = [a,b,c]
b = a
result = a is b
print(result)
result = a is not b
print(result)

list = {1,2,3,4}

result = (3 in list)
print(result)

result = (5 in list)
print(result)

result = (3 not in list)
print(result)

result = (6 not in list)
print(result)

if a  == b:
  print(f"a es igual a b {a}{b}") 
else:
  print(f"a no es igual a b {a}{b}")

a = 10
b = 10

if a > b:
  print("a es mayor que b")
elif a < b:
  print("a es menor que b")
else:
  print("a y b son iguales")

a = [1, 2,4,5,2]

for i in a:
  print(i)

contador = 0
while contador <= 5:
  print(f"Contador -> {contador}")
  contador += 1


try:
  result = 10/0
  print(f"El resultado es -> {result}")
except ZeroDivisionError as e:
  print(f"se genero un error -> {e}")
finally:
  print("este bloque siempre se ejecuta")


number = 10
while number < 55:
  number += 1
  if number % 2 == 0 and number != 16 and number % 3 != 0:
    print(number)