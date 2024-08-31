# Retos de programación.
'''
NOTA:
Soy nuevo en esto, pero me pareció interesantes para aprender más. Aunque mi lenguaje no es Python, quiero hacer el reto en este lenguanje para coger experiencia despues de ver los cursos de moure, y un forma de seguir mejorando.
No sé si lo haré bien porque al ser nuevo no entendía bien lo que se pedía, y espero que lo haya hecho correctamente. Veré la correción el 8. Lo he intentado hacer lo mejor posible.
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 
 Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

 Para saber todos los tipos de operadores de tu lenguaje de Python, me he basado en la documentación de Python https://docs.python.org/es/3.11/library/operator.html?highlight=operadores. 
 Es posible que me falte o se me haya pasado algunos, aprovecharé a correccion para saber si falta o están todos.
 '''

# Aritméticos
a = 8
b = 3

suma = a + b  #operadores basaicos
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b #Operador que devuelve lo que queda del resultado de una división
potencia = a ** b #Operador que eleva a la potencia especificada
division_entera = a // b #Este operador hace la división igual que la normal pero el resultado será entero porque el residuo lo ignora, mientras que la normal puede haber numero decimal.

print(f"Aritméticos: {suma}, {resta}, {multiplicacion}, {division}, {modulo}, {potencia}, {division_entera}")

# Lógicos
x = True
y = False

and_result = x and y #Este operador es el de siempre
or_result = x or y #Este operador es el o de siempre
not_result = not x #Y este operador es peculiar porque devolverá siempre lo contrario, por ejemplo si es x es True devolverá False, y si x es False devolverá True

print(f"Lógicos: {and_result}, {or_result}, {not_result}")

# De comparación
a = 5
b = 10

igual = a == b
diferente = a != b
mayor_que = a > b
menor_que = a < b
mayor_o_igual = a >= b
menor_o_igual = a <= b

print(f"De comparación: {igual}, {diferente}, {mayor_que}, {menor_que}, {mayor_o_igual}, {menor_o_igual}")

# De asignación
x = 5

x += 2  # x = x + 2 para no tener que repetir el numero 5 = 5 + 2 --> queda 5 += 2 para condensar el codigo
x -= 3  # x = x - 3
x *= 4  # x = x * 4
x /= 2  # x = x / 2
x %= 3  # x = x % 3

print(f"De asignación: {x}")

# De identidad
''' Un apunte aparte, para explicar un detalle más (no sé muy bien si entra en la categoría),
pero quiero dar este apunte porque a mí me creo confunción respeto a otros lenguajes:
Hay diferencia entre Lista, Sets, Tuplas y Diccionarios.
- LISTA --> se utiliza []
- SETS --> se utiliza {}
- Tuplas --> se utiliza ()
- DICCIONARIO --> se utiliza {"x":"y"} lo que se denomina clave:valor
Y cada uno tiene un comportamiento distinto
'''

a = [1, 2, 3] #Es una lista
b = a #Aquí b hace referencia la lista a
c = [1, 2, 3] #Pero aquí aunque c tenga los mismos valores que a es una lista distinta.

identidad1 = a is b #Aquí devolverá True porque hace referencia a la misma lista
identidad2 = a is c #Aquí devolverá False porque aunque tenga el mismo valor son listas distintas

print(f"De identidad: {identidad1}, {identidad2}")

# De pertenencia
lista = [1, 2, 3, 4, 5]
pertenece1 = 3 in lista #Simplemente pregunta si el 3 está en lista
pertenece2 = 6 not in lista #Aquí si el 6 no está en lista

print(f"De pertenencia: {pertenece1}, {pertenece2}")

# Bits
x = 5
y = 3

#Aunque esto operadores se parezcan al and que vimos arriba, en realidad no son iguales
#Aquí se trabaja con numeros enteros, en los logicos se trabaja con booleanos
and_bits = x & y 
or_bits = x | y
xor_bits = x ^ y #Aquí es un poco peculiar porque devolverá True si uno de los numeros está en la position 1
complemento_bits = ~x #Aquí no lo sé muy bien, y no lo entiendo tampoco (la teoría es que los bits se invierten, no sé más)
shift_izquierda = x << 1 #Igual (la teoría es que los bits se desplazan a la izquierda, no sé más)
shift_derecha = x >> 1 #Igual (la teoría es que los bits se desplazan a la derecha, no sé más)

print(f"Bits: {and_bits}, {or_bits}, {xor_bits}, {complemento_bits}, {shift_izquierda}, {shift_derecha}")

# Condicionales
edad = 18

if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres mayor de edad")

#O esta otra forma también usanso mayor ">"
if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres menor de edad")

# Iterativas
for i in range(5):
    print(i)

edad = 18
while edad > 0:
    print(edad)
    edad -= 1

#Hay otra manera posible:
edad = 18 
while True:
  if edad > 0:
    print(edad)
    edad -= 1

# Excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("¡Error! División por cero.")
finally:
    print("Este bloque siempre se ejecuta.")

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''

strangeNumber = [i for i in range(10, 56) if (i != 16 and i % 2 == 0 and i % 3 != 0) or i == 55]

print(strangeNumber)

