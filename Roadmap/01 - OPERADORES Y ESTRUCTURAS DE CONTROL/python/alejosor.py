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
import random
# OPERADORES ARITMÉTICOS
print("\nOperadores Aritméticos")
print(f'    - La suma de 10 + 5 es igual a {10 + 5}')
print(f'    - La resta de 10 - 5 es igual a {10 - 5}')
print(f'    - La multiplic de 10 x 5 es igual a {10 * 5}')
print(f'    - La división de 10 entre 5 es igual a {10 / 5}')
print(f'    - El resto de 10 entre 5 es igual a {10 % 5}')
print(f'    - La división de piso de 10 entre 5 es igual a {10 // 5}')
print(f'    - La potencia de 10 elevado a 5 es igual a {10 ** 5}\n')

# OPERADORES LÓGICOS
print("Operadores Lógicos")
print(f"    - AND -> True and True = {True and True}") # Operador AND
print(f"    - OR -> True or False = {True or False}") # Operador OR
print(f"    - NOT = not True = {not True}\n") # Operador NOT

# OPERADORES DE COMPARACIÓN
print("Operadores de Comparación")
print(f"    - Mayor > -> 5 es mayor(>) a 3 = {5>3}") #Operador de comparación >
print(f"    - Menor < -> 5 es menor(<) a 3 = {5<3}") #Operador de comparación <
print(f"    - Mayor o Igual >= -> 5 es mayor o igual (>=) a 3 = {5>3}") #Operador de comparación >=
print(f"    - Menor o Igual <= -> 5 es menor o igual (<=) a 3 = {5>3}") #Operador de comparación <=
print(f"    - Igual == -> 5 es igual(==) a 5 = {5==5}") #Operador de comparación ==
print(f"    - No igual != -> 5 no es igual(!=) a 3 = {5!=3}\n") #Operador de comparación !=

# OPERADORES DE ASIGNACIÓN
print("Operadores de Asignación")
print(f"    -> x = 5")
print(f"    - x+=3 -> x = x + 3 = {5+3}") # Suma
print(f"    - x-=3 -> 5 - 3 = {5-3}") # Resta
print(f"    - x*=3 -> 5 * 3 = {5*3}") # Multiplicación
print(f"    - x/=3 -> 5 / 3 = {5/3}") # División
print(f"    - x%=3 -> 5 % 3 = {5%3}") # Resto
print(f"    - x//=3 -> 5 // 3 = {5//3}") # División de piso
print(f"    - x**=3 -> 5 ** 3 = {5**3}\n") # Potencia

# OPERADORES DE IDENTIDAD
num_1 = 5
num_2 = num_1
print("Operadores de Identidad")
print(f'    - num_1 is num_2 = {num_1 is num_2}')
print(f'    - num_1 is not num_2 = {num_1 is not num_2}\n')

# OPERADORES DE PERTENENCIA
print("Operadores de Pertenencia")
print(f"    - 'a' in 'alejandro' = {"a" in "alejandro"}")
print(f"    - 'u' not in 'alejandro' = {"u" not in "alejandro"}\n")

# OPERADORES DE BITS
a = 5
b = 3
print("Operadores de Bits")
print("a = 5") # 0101
print("b = 3") # 0011
print(f'AND: a & b = {a & b}')
print(f'OR: a | b = {a | b}')
print(f'XOR: a ^ b = {a ^ b}')
print(f'NOT: ~a = {~a}')
print(f"Desplazamiento a la derecha a >> b = {a >> b}")
print(f"Desplazamiento a la izquierda a << b = {a >> b}\n")

# ESTRUCUTURAS DE CONTROL
print("Estructuras de control")
# CONDICIONALES
print("Condicionales")
my_number = random.randint(1,10)
if my_number > 5:
    print("Mi número es mayor a 5")
elif my_number < 9:
    print("Mi número es menor a 9")
else:
    print("Mi número no es ninguna de las condiciones anteriores")

# INTERATIVOS
print("\nCondicionales: FOR")
for i in range(6):
    print(i)

i = 10

print("\nCondicionales: WHILE")
while i <= 6:
    print(f'El número es {i} y es menor igual a 6\n')
    
# MANEJO DE EXCEPCIONES
print("Manejo de excepciones")
try:
    print(a/0)
except Exception as e:
    print(f"Ups.. Hay un error, {e}")
finally:
    print("Secuencia terminada")

# Extras
# Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
print("\nExtra")
for i in range(10,56):
    if i & 2 == 0 and i != 16 and i % 3 != 0:
        print(i)