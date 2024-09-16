"""
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
"""
# Operadores:
# Aritméticos: +, -, *, /, %, **
suma = 2 + 3 # Suma
resta = 2 - 3 # Resta
multiplicacion = 2 * 3 # Multiplicación
division = 2 / 3 # División
modulo = 2 % 3 # Módulo
potencia = 2 ** 3 # Potencia
division_entera = 2 // 3 #División entera
print(f"Aritméticos: Suma:{suma}, Resta:{resta}, Multiplicación:{multiplicacion}, División:{division}, Módulo{modulo}, Exponenciación{potencia}, División entera:{division_entera}")

# Comparación
# ==, !=, >, <, >=, <=
print(f"Igualdad: 2 == 2: {2 == 2}") # Si se cumple, devuelve True, en caso contrario False
print(f"Diferencia: 2 != 2 {2 != 2}") # Si se cumple, devuelve True, en caso contrario False
print(f"Mayor que: 2 > 2 {2 > 2}") # Si se cumple, devuelve True, en caso contrario False
print(f"Menor que: 2 < 2 {2 < 2}") # Si se cumple, devuelve True, en caso contrario False
print(f"Mayor o igual que: 2 >= 2 {2 >= 2}") # Si se cumple, devuelve True, en caso contrario False
print(f"Menor o igual que: 2 <= 2 {2 <= 2}") # Si se cumple, devuelve True, en caso contrario False

# Lógicos 
# and, or, not
print(f"and: 2 > 2 and 2 < 2 {2 > 2 and 2 > 2}") # Ambas condiciones, derecha e izquierda deben cumplirse, de ser así, devuelve True
print(f"or: 2 > 2 or 2 < 2 {2 > 2 or 2 > 2}") # Cualquiera de las dos condiciones, derecha e izquierda deben cumplirse, de ser así, devuelve True
print(f"not: not 2 + 2 = 5 { not 2 + 2 == 5} ") # En este ejemplo si no se cumple que 2 + 2 sea igual a 5, devuelve True

#Asignación
# =, +=, -=, *=, /=, %=, **=, //=
a = 11 # A la variable a se le asigna el valor 2
print(a)
a += 2 # Se calcula la suma más 2 y se asigna
print(a)
a -= 2 # Se calcula la resta menos 2 y se asigna
print(a)
a *= 2 # Se calcula la multiplicación por 2 y se asigna
print(a)
a /= 2 # Se calcula la división por 2 y se asigna
print(a)
a %= 2 # Se calcula el módulo entre 2 y se asigna
print(a)
a **= 2 # Se calcula la exponeciación por 2 y se asigna
print(a)
a //= 2 # Se calcula la división entera por 2 y se asigna
print(a)

# Identidad
nueva_var = a
print(f"¿La variable nueva_var es la variable a?: {nueva_var is a}") # Devuelve True si ambos objetos son el mismo objeto, en este caso, se crea nueva_var y se le asigna directamente a, la variable creada anteriormente
print(f"¿La variable nueva_var es la variable a?: {nueva_var is not a}") # Devuelve False si ambos objetos no son el mismo objeto, en este caso, se crea nueva_var y se le asigna directamente a, la variable creada anteriormente

# Pertenencia
# in, not in
print(f"¿El número 2 pertenece a la lista [1, 2, 3, 4]?: {2 in [1,2,3,4]}")
print(f"¿El número 5 NO pertenece a la lista [1, 2, 3, 4]?: {5 not in [1,2,3,4]}")

# Bit
# &, |, ^, ~, <<, >>
a = 2 # 2 en binario es 10
b = 3 # 3 en binario es 11
print(f"AND: {a & b}") # 10 & 11 = 10
print(f"OR: {a | b}") # 10 | 11 = 11
print(f"XOR: {a ^ b}") # 10 ^ 11 = 1
print(f"NOT: {~ b}") # ~ 11 = -10
print(f"Desplazamiento a la izquierda: {b << 2} ") # b << 2 = 1100
print(f'Desplazamiento a la derecha: {a >> 2}') # a << 2 = 0

# Estructuras de control:
# Condicionales
# if, elif, else
if 2 > 3:
    print('2 es mayor que 3')
elif 2 == 3:
    print('2 es igual a 3')
else:
    print('2 es menor que 3')

# Iterativas
# while, for
# while
i = 0
while i < 10:
    print(i)
    i += 1

# for
for i in range(10):
    print(i)

# Manejo de excepciones
# try, except, finally
try:
    var = 3 / 0
except ArithmeticError as e:
    print(f'Error {e}')
finally:
    print('Se ejecuta siempre')
    
""" Dificultad extra """
for i in range (10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(f'número {i}')