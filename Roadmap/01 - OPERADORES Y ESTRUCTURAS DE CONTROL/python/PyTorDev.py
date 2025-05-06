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
  # Operadores
#Operadores de Asignación
x = 1
a = 1
b = 3
x += 1
x -= 1
# Y así con todos los operadores aritmeticós

#Operadores Aritmeticós

a + b
a - b
a * b
a ** b
a / b
a // b
a % b

# Operadores de comparación
a == b
a != b
a < b
a > b
a <= b
a >= b

# Operadores lógicos
a and b
a or b
not b

# Operadores de Bitwise
a & b
a | b
a ^ b
~ b
a << b
a >> b

# Operadores de pertenencia

'a' in 'avion'
'a' not in 'vision'

# Operadores de Identidad

a is b
a is not b

# Operador ternario

a = a if a > b else b


  # Estructuras de control
num = 5
#Condicionales

#if
if num > 0:
  print('Es positivo')

#if-else
if num % 2 == 0:
  print('Par')
else: print('Impar')

#if_elif_else
if num > 0:
  print('Es positivo')
elif num == 0:
  print('Es cero')
else:
  print('Es negativo')

#Iterativas

#for
for i in range(3):
  print(i)

#while
i = 0
while i < 3:
   print(i)
   i += 1

# Variaciónes de estas estructuras
# Break
for i in range(5):
  if i == 3:
    break
  print(i) 

# Continue
for i in range(5):
  if i == 2:
    continue
  print(i)

#else con for
for i in range(3):
  print(i)
else:
  print('Bucle completado')

#else con while
while i < 3:
  print(i)
  i += 1
else:
  print('Bucle completado')

#Excepciones
#try-except
try:
  x = 1 / 0
except ZeroDivisionError as e:
  print('No se puede dividir por cero')

#try-except-else
try:
  x = 10 / 2
except ZeroDivisionError:
  print('Error')
else:
  print('EL calculo salio bien')

#try-except-finaly
try:
  x = 10 / 0
except:
  print("Error")
finally:
  print('Esto se ejecuta en cualquier caso')

#Ejerccio extra

def imprimir_numeros():
  for i in range(10, 55):
    if i % 2 == 0:
      if i != 16 and i % 3 != 0:
        print(i)
    

imprimir_numeros()