# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
'''
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
'''

print('>>Arithmetic operators / Operadores aritméticos')
print(f'(+) Addition / Suma: 2 + 3 = {2 + 3}')
print(f'(-) Subtraction / Resta: 5 - 7 = {5 - 7}')
print(f'(*) Multiplication / Multiplicación: 6 * 8 = {6 * 8}')
print(f'(/) Division / División: 10 / 6 = {10 / 6}')
print(f'(%) Modulus / Módulo: 5 % 2 = {5 % 2}')
print(f'(**) Exponentiation / Potencia: 2 ** 32 = {2 ** 32}')
print(f'(//) Floor Division / División entera : 10 // 6 = {10 // 6}')

print()
print('>>Assignment operators / Operadores de asignación')
x = 1000
print(f'(=) x = 5 => {x}')
x += 3
print(f'(+=) x += 3  lo mismo que  x = x + 3 => {x}')
x -= 3 
print(f'(-=) x -= 3  lo mismo que  x = x - 3 => {x}')
x *= 3
print(f'(*=) x *= 3  lo mismo que  x = x * 3 => {x}')
x /= 3
print(f'(/=) x /= 3  lo mismo que  x = x / 3 => {x}')
x %= 3
print(f'(%=) x %= 3  lo mismo que  x = x % 3 => {x}')

x = 1000
print(f"x=1000")
x //= 3
print(f'(//=) x //= 3  lo mismo que  x = x // 3 => {x}')
x **= 3
print(f'(**=) x **= 3  lo mismo que  x = x ** 3 => {x}')
x &= 3
print(f'(&=) x &= 3  lo mismo que  x = x & 3 => {x}')
x |= 3
print(f'(|=) x |= 3  lo mismo que  x = x | 3 => {x}')
x = 10
print(f"x=10")
x ^= 3
print(f'(^=) x ^= 3  lo mismo que  x = x ^ 3 => {x}')
x >>= 3
print(f'(>>=) x >>= 3  lo mismo que  x = x >> 3 => {x}')
x <<= 3
print(f'(<<=) x <<= 3  lo mismo que  x = x << 3 => {x}')
print(f'(:=) print(x := 44)  lo mismo que y luego print')
print(x := 44)

print()
print('>>Comparison operators / Operadores de comparación')
x = 10
y = 5
print(f"x=10, y=5")
print(f'(==) Equal/Igual x == y => {x == y}')
print(f'(!=) Not equal/Distinto x != y => {x != y}')
print(f'(>)  Greater than/Mayor que x > y => {x > y}')
print(f'(<)  Less than/Menor que x < y => {x < y}')
print(f'(>=) Greater than or equal to/Mayor o igual que x >= y => {x >= y}')
print(f'(<=) Less than or equal to/Menor o igual que x <= y => {x <= y}')

print()
print('>>Logical operators / Operadores lógicos')
x = 10
y = 5
print(f"x=10, y=5")
print(f'(and) Retorna True si ambas sentencias son True  x < 5 and  x < 10 => {x < 5 and  x < 10}')
print(f'(or)  Retorna True si una de las sentencias es True  x < 5 or x < 4 => {x < 5 or x < 4}') 
print(f'(not) Revierte el resultado, Retorna False si el resultado es True  not(x < 5 and x < 10) => {not(x < 5 and x < 10)}')

print()
print('>>Identity operators / Operadores de Identidad')
x = ["manzana", "banana"]
y = ["manzana", "banana"]
z = x
print('x = ["manzana", "banana"]')
print('y = ["manzana", "banana"]')
print('z = x')

print(f'(is)  Retorna True si ambas variables son el mismo objeto x is y => {x is y}, x is z => {x is z}')
print(f'(is not) Retorna True si ambas variables no son el mismo objeto x is not y => {x is not y}, x is not z => {x is not z}')

print()
print('>>Membership operators / Operadores de Membresía')
x = ["sol", "luna"]
print('x = ["sol", "luna"]')
print(f'(in)     Retorna True si una secuencia con el valor especificado está presente en el objeto    "sol" in x        => {"sol" in x}')
print(f'(not in) Retorna True si una secuencia con el valor especificado no está presente en el objeto "asteroide"" in x => {"asteroide" in x}')

print()
print('>>Bitwise operators / Operadores bit a bit')
x = 6
y = 3
print(f"x=6, 6 = 0000000000000110")
print(f"y=3, 3 = 0000000000000011")
print(f'(&) AND Establece cada bit en 1 si ambos bits son 1 x & y => {x & y} (2 = 0000000000000010)')
x = 6
y = 3
print(f"x=6, 6 = 0000000000000110")
print(f"y=3, 3 = 0000000000000011")
print(f'(|) OR Establece cada bit en 1 si uno de los dos bits es 1 x | y => {x | y} (7 = 0000000000000111)')
x = 6
y = 3
print(f"x=6, 6 = 0000000000000110")
print(f"y=3, 3 = 0000000000000011")
print(f'(^) XOR Establece cada bit en 1 si solo uno de los dos bits es 1 x ^ y => {x ^ y} (5 = 0000000000000101)')
x = 3
print(f"x=3, 3 = 0000000000000011")
print(f'(~) NOT Invierte todos los bits ~x => {~x} (-4 = 1111111111111100)')
x = 3
print(f"x=3, 3 = 0000000000000011")
print(f'(<<) Zero fill left shift: Desplaza hacia la izquierda empujando ceros desde la derecha')
print(f'y deja que los bits más a la izquierda caigan')
print(f'x << 2 => {x << 2} (12 = 0000000000001100)')

x = 8
print(f"x=8, 8 = 0000000000001000")
print(f'(>>) Signed right shift: Desplaza a la derecha empujando copias del bit más a la izquierda desde la izquierda,', end = ' ' )
print(f'y deja que los bits más a la derecha se caigan x >> 2 => {x >> 2} ( 2 = 0000000000000010)')

print()
print('Estructuras de control')
print('Condicionales, iterativas, excepciones...')

print('>>If statement')
a = 4
b = 8
print ('a = 4\nb = 8 \nif a < b :\n print("a es menor que b")')
print ('Resultado: ')
if a < b:
  print("a es menor que b")

print()
print('>>If statement - Elif')
a = 4
b = 4
print ('a = 4\nb = 4 \nif b < a: :\n print("b es menor que a")\nelif a == b :\n print("a y b son iguales")  ')
print ('>Resultado: ')
if b < a:
  print("b es menor que a")  
elif a == b :
  print("a y b son iguales") 

print()
print('>>If statement - Else')
a = 400
b = 40
print ('a = 400\nb = 40 \nif b > a:\n print("b es mayor que a")\nelif a == b:\n print("a y b son iguales")\nelse:\n print("a es mayor que b")')
print ('>Resultado: ')
if b > a:
  print("b es mayor que a")
elif a == b:
  print("a y b son iguales")
else:
  print("a es mayor que b")

print()
print('>>If statement - Short Hand if (en una linea)')
a = 256
b = 255
print('a = 256\nb = 255 \nif a > b: print("a es mayor que b")')
print ('>Resultado: ')
if a > b: print("a es mayor que b")

print()
print('>>If statement - Short Hand if ... Else (en una linea)')
a = 6
b = 110
print('a = 6\nb = 110 \nprint("A") if a > b else print("B")')
print ('>Resultado: ')
print("A") if a > b else print("B")

print()
print('>>If statement - Short Hand if ... Else con 3 condiciones(en una linea)')
a = 4444
b = 4444
print('a = 4444\nb = 4444 \nprint("A") if a > b else print("=") if a == b else print("B")')
print ('>Resultado: ')
print("A") if a > b else print("=") if a == b else print("B")

print()
print('>>If statement - Nested if (if anidados)')
x = 41
print('x = 41\nif x > 10:\n print("Above ten,")\n if x > 20:\n  print("and also above 20!")\n else:\n  print("but not above 20.")')
print ('>Resultado: ')
if x > 10:
  print("Más que 10,")
  if x > 20:
    print("y también más que 20!")
  else:
    print("pero no más que 20.")

print()
print('>>If statement - The pass Statement (evitar error en sentencias if sin contenido)')
a = 1
b = 2
print('a = 1\nb = 2\nif b > a:\n pass')
print ('>Resultado: ')
if b > a:
  pass


print('\n\n')
print('>>The while Loop')

print('i = 1\nwhile i < 6:\n print(i)\n i += 1')
print ('>Resultado: ')
i = 1
while i < 6:
  print(f'iteracion: {i}')
  i += 1

print()
print('>>The break Statement')
print('i = 1\nwhile i < 6:\n print(i)\n if i == 3:\n  break\n i += 1')
print ('>Resultado: ')
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print()
print('>>The continue Statement')
print('i = 1\nwhile i < 6:\n i += 1\n if i == 3:\n  continue\n print(i)')
print ('>Resultado: ')
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print()
print('>>The else Statement')
print('i = 1\nwhile i < 6:\n print(i)\n i += 1\nelse:\n  print("i is no longer less than 6")')
print ('>Resultado: ')
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i ya no es menor que 6")


print('\n\n')
print('>>For Loops')

print('mascotas = ["Luna", "Ash", "Alma"]\nfor x in mascotas:\n print(x)')
print ('>Resultado: ')
mascotas = ["Luna", "Ash", "Alma"]
for x in mascotas:
  print(x)

print('\n>>Loop en un String')  
print('for x in "Python":\n print(x)')
print ('>Resultado: ')
for x in "Python":
  print(x)

print('\n>>The break Statement')  
print('planetas = ["Tierra", "Marte", "Plutón", "Júpiter"]\nfor x in planetas:\n print(x) \n if x == "Plutón":\n  break')
print ('>Resultado: ')
planetas = ["Tierra", "Marte", "Plutón", "Júpiter"]
for x in planetas:
  print(x)
  if x == "Plutón":
    break

print('\n>>The continue Statement')  
print('planetas = ["Tierra", "Marte", "Plutón"]\nfor x in planetas:\n if x == "Marte":\n  continue\n print(x)')
print ('>Resultado: ')
planetas = ["Tierra", "Marte", "Plutón"]
for x in planetas:  
  if x == "Marte":
    continue
  print(x)

print('\n>>The range() Function')  
print('con 1 solo parámetro comienza en 0 y termina antes que el valor pasado')
print('for x in range(6):\n print(x)')
print ('>Resultado: ')
for x in range(6):
  print(x)

print('\ncon 2 parámetros comienza en el valor del primero y termina antes que el segundo valor')  
print('for x in range(2, 6):\n print(x)')
print ('>Resultado: ')
for x in range(2, 6):
  print(x)  

print('\nsi se agrega un 3er parámetro, este indica los incrementos')  
print('for x in range(2, 30, 3):\n print(x)')
print ('>Resultado: ')
for x in range(2, 30, 3):
  print(x)

print('\nElse in For Loop')  
print('for x in range(6):\n print(x)\nelse:\n print("Finally finished!")')
print ('>Resultado: ')
for x in range(6):
  print(x)
else:
  print("Finally finished!")

print('\nNested Loops')  
print('color = ["azul", "verde", "dorado"]\nobjeto = ["violeta", "manzana", "sol"]\nfor x in color:\n for y in objeto:\n  print(x, y)')
print ('>Resultado: ')
color = ["azul", "verde", "dorado"]
objeto = ["piedra", "manzana", "sol"]
for x in color:
  for y in objeto:
    print(x, y)

print('\nThe pass Statement (evitar error en loop for sin contenido)')  
print('for x in [0, 1, 2]:\n pass')
print ('>Resultado: ')
for x in [0, 1, 2]:
  pass

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
'''

for i in range(10, 56):
  if i % 2 == 0 and i != 16 and i % 3 != 0:
    print(i)