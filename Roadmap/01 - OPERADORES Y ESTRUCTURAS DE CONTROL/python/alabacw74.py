'''
# 01 OPERADORES Y ESTRUCTURAS DE CONTROL
Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24
Author: Alfredo Aburto Alcudia https://github.com/alabacw74
Propuesto por: Brais Moure https://github.com/mouredev
## Ejercicio


EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia,
    bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...

- Debes hacer print por consola del resultado de todos los ejemplos.
 
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
Seguro que al revisar detenidamente las posibilidades has descubierto algo 
nuevo.

'''

# Tipos de operadores

# Asignacion
a = 29
print(a)

# Añadir el valor de la derecha al valor actual de la variable
a += 1
print(a)

# Restar el valor de la derecha al valor actual de la variable
a -= 26
print(a)

# Dividir el valor actual de la variable por el valor de la derecha
a /= 2
print(a)

# Calcular el modulo del valor actual de la variable por el valor de la derecha
a %= 0.45
print(a)

# Calcula division entera del valor actual de la variable por el valor de la
# derecha
b = 26
b //= 11
print(b)

# Elevar el valor actual de la variable a la potencia del valor de la derecha
b **= 3
print(b)

# Aritmeticos
print(f'5 + 3 = {5 + 3}') # Suma
print(f'5 - 3 = {5 - 3}') # Resta
print(f'5 * 3 = {5 * 3}') # Multiplicación
print(f'5 / 5 = {5 / 5}') # Division (siempre retorna un float)
print(f'5 % 3 = {5 % 3}') # Modulo
print(f'5 // 3 = {5 // 3}') # Division entera
print(f'5 ** 3 = {5 ** 3}') # Exponente

# Logicos y relacionales
print("Logicos y relacionales")
a = True
b = False

print(f'a = {a} y b = {b}')

print("a and b")
print(a and b)
print("a or b")
print(a or b)
print("not a")
print(not a)

print("--------------------------")
x = 5
y = 1
z = 5.01
print(f'x = {x}, y = {y}, z = {z}')

print(f'x > y = {x > y}')
print(f'x < y = {x < y}')
print(f'x >= z = {x >= z}')
print(f'x <= z = {x <= z}')
print(f'x == z = {x == z}')
print(f'x != z = {x != z}')

# De pertenencia
print('De pertenencia')
lista = [1, 2, 3, 4, 5]
print(lista)
resultado_in = 3 in lista
print(f'resultado_in = 3 in lista --> {resultado_in}')

# De identidad
print("De identidad")
x = 5
y = 5
resultado_is = x is y

print(f'x = {x}, y = {y}')
print(f'x is y --> {resultado_is}')

# De bits
print("De bits")
'''
Los operadores de bits en Python trabajan a nivel de bits en números enteros. 
Estos operadores realizan operaciones en los bits individuales de los números,
 lo que puede ser útil en situaciones donde se necesita manipular datos a un 
 nivel más bajo.
'''

a = 5
b = 3

resultado_and_bits = a & b
resultado_or_bits = a | b
resultado_xor_bits = a ^ b
resultado_complemento = ~a
resultado_desplazamiento_izquierda = a << 1
resultado_desplazamiento_derecha = a >> 1

print("Operador AND a nivel de bits:", resultado_and_bits)
print("Operador OR a nivel de bits:", resultado_or_bits)
print("Operador XOR a nivel de bits:", resultado_xor_bits)
print("Complemento a uno:", resultado_complemento)
print("Desplazamiento a la izquierda:", resultado_desplazamiento_izquierda)
print("Desplazamiento a la derecha:", resultado_desplazamiento_derecha)
print("---------------------------------------------")
# Estructuras de control
print("Estructuras de control")

print("if-else")
print('''x = 10
if x > 5:
    print("x es mayor que 5")
else:
    print("x no es mayor que 5")''')

x = 10
if x > 5:
    print("x es mayor que 5")
else:
    print("x no es mayor que 5")
print('-------------------')
print("for")
print('''
for i in range(5):
    print(i)

      ''')
for i in range(5):
    print(i)
print('-------------------')
print("while")
print('''
    y = 0
while y < 5:
    print(y)
    y += 1
'''
)

y = 0
while y < 5:
    print(y)
    y += 1

print('-------------------')
print("break")
print('''
for i in range(10):
    if i == 5:
        break
    print(i)
''')

for i in range(10):
    if i == 5:
        break
    print(i)

print('-------------------')
print("continue")
print('''
for i in range(5):
    if i == 2:
        continue
    print(i)
''')
for i in range(5):
    if i == 2:
        continue
    print(i)

print('-------------------')
print("try-except")

print('''
La estructura try-except en Python se utiliza para manejar excepciones o errores
durante la ejecución del código. Consiste en un bloque try que contiene
el código propenso a generar una excepción, y uno o más bloques except 
que manejan específicamente esas excepciones.
''')
print('''
try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("¡División por cero!")
''')
try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("¡División por cero!")

print('-------------------')
print("width")

print('''
La estructura with se utiliza para trabajar con objetos que requieren una 
configuración y limpieza específica, como archivos, sockets, conexiones 
a bases de datos, entre otros. Proporciona un manejo más limpio de los
recursos, ya que garantiza que los recursos se liberen adecuadamente 
después de su uso, incluso si ocurren excepciones.
''')
print('''
with open('archivo.txt', 'r') as file:
    contenido = file.read()
    print(contenido)
# En este punto, el archivo se cierra automáticamente, incluso si ocurren excepciones

''')
print('-------------------')
print("DIFICULTAD EXTRA")
'''
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''

print('''
for i in range(10,56):
    if i % 2 == 0:
        if i == 16 or i % 3 == 0:
            continue
        else:
            print(i)
''')

for i in range(10,56):
    if i % 2 == 0:
        if i == 16 or i % 3 == 0:
            continue
        else:
            print(i)