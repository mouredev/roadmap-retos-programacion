#01: OPERADORES Y ESTRUCTURAS DE CONTROL
# Lenguaje: Python

"""
En este ejercicio exploro los principales operadores que ofrece Python 
(aritméticos, comparación, lógicos, asignación, identidad, pertenencia y bits) 
junto con sus diferentes estructuras de control (condicionales, bucles y 
manejo de excepciones). El objetivo es poner en práctica la sintaxis básica 
y comprender cómo se comporta el lenguaje en cada caso.
"""

print("operadores aritméticos:")

a = 17
b = 5

print(f"suma (17 + 5): {a + b}") # = 22, ya que suma dos valores 
print(f"resta (17 - 5): {a - b}") # = 12, ya que resta dos valores
print(f"multiplicación (17 * 5): {a * b}") # = 85, ya que multiplica dos valores
print(f"división (17 / 5): {a / b}") # = 3.4, ya que divide dos valores y devuelve un número decimal
print(f"módulo (17 % 5): {a % b}") # = 2, ya que devuelve el residuo de la división
print(f"exponenciación (17 ** 5): {a ** b}") # = 5 veces 17, ya que eleva un valor a la potencia de otro
print(f"división entera (17 // 5): {a // b}") # = 3, ya que divide dos valores y devuelve un número entero

print("operadores de comparación:")

print(f"igual a (17 == 5): {a == b}") # = False, ya que compara si dos valores son iguales
print(f"distinto a (17 != 5): {a != b}") # = True, ya que compara si los valores son distintos
print(f"mayor que (17 > 5): {a > b}") # = True, ya que compara si un valor es mayor que otro
print(f"menor que (17 < 5): {a < b}") # = False, ya que compara si un valor es menor que otro
print(f"mayor o igual que (17 >= 5): {a >= b}") # = True, ya que compara si un valor es mayor o igual que otro
print(f"menor o igual que (5 <= 17): {b <= a}") # = True, ya que compara si un valor es menor o igual que otro

print("operadores lógicos:")

x = 12
y = 4

print(f"AND && (True and True): {x == x and y == y}") # = true, ya que ambos valores son verdaderos
print(f"OR || (True or False): {x == x or y == x}") # = True, ya que al menos uno de los valores es verdadero
print(f"NOT ! (not True): {not y + x == x + y}") # = False, ya que el valor es verdadero y debe contrariarse

print("operadores de asignación:")

c = 10

print(f"asignación simple (c = 10): {c}") # = 10, ya que asigna un valor a una variable
print(f"asignación suma (c += 5): {c + 5}") # = 15, ya que suma un valor a la variable
print(f"asignación resta (c -= 3): {c - 3}") # = 7, ya que resta un valor a la variable
print(f"asignación multiplicación (c *= 2): {c * 2}") # = 20, ya que multiplica un valor a la variable
print(f"asignación división (c /= 4): {c / 4}") # = 2.5, ya que divide un valor a la variable
print(f"asignación módulo (c %= 3): {c % 3}") # = 1, ya que devuelve el residuo de la división
print(f"asignación exponenciación (c **= 2): {c ** 2}") # = 100, ya que eleva un valor a la potencia de otro
print(f"asignación división entera (c //= 3): {c // 3}") # = 3, ya que divide un valor a la variable y devuelve un número entero

print("operadores de identidad:")   

d = 5 + 5

print(f"identidad (d is 10): {d is 10}") # = True, ya que compara si dos valores son idénticos
print(f"no identidad (d is not 10): {d is not 10}") # = False, ya que compara si dos valores no son idénticos

print("operadores de pertenencia:")

print(f"pertenencia (10 in [10, 20, 30]): {10 in [10, 20, 30]}") # = True, ya que comprueba si un valor pertenece a una lista
print(f"'r' in 'rodriguez' = { 'r' in 'rodriguez' }") # = True, ya que comprueba si un valor pertenece a una cadena de texto

print(f"no pertenencia (40 not in [10, 20, 30]): {40 not in [10, 20, 30]}") # = True, ya que comprueba si un valor no pertenece a una lista
print(f"'x' not in 'rodriguez' = { 'x' not in 'rodriguez' }") # = True, ya que comprueba si un valor no pertenece a una cadena de texto

print("operadores de bits:")

num1 = 12 # en binario: 1100
num2 = 4 # en binario: 0100

print(f"AND & (12 & 4): {num1 & num2}") # = 4, ya que realiza una operación AND a nivel de bits (0100)
print(f"OR | (12 | 4): {num1 | num2}") # = 12, ya que realiza una operación OR a nivel de bits (1100)
print(f"XOR ^ (12 ^ 4): {num1 ^ num2}") # = 8, ya que realiza una operación XOR a nivel de bits (1000)
print(f"NOT ~ (~12): {~num1}") # = -13, ya que invierte los bits de un número (complemento a uno)
print(f"Desplazamiento a la derecha >> (12 >> 2): {num1 >> 2}") # = 3, ya que desplaza los bits a la derecha (0011)
print(f"Desplazamiento a la izquierda << (12 << 2): {num1 << 2}") # = 48, ya que desplaza los bits a la izquierda (110000)

"""
 Estructuras de control en Python
"""
print("condicionales:")

my_age = 38

if my_age < 12:
    print("my_age es 'menor de edad.'") 
elif my_age >= 15 and my_age < 17:
    print("my_age es 'adolescente.'")
else:
    print("my_age es 'mayor de edad.'")

"""
con la anterior demostramos el uso de condicionales if, elif y else,
que nos permiten ejecutar diferentes bloques de código según se cumpla o no una condición.
"""

print("interactivas bucles:")

for i in range(20): # range(5) genera una secuencia de números del 0 al 4
    print(f"iteración {i}") # imprime el valor de i en cada iteración

i = 0

while i <= 20: # mientras i sea menor o igual a 20, se ejecuta el bucle
    print(f"iteración {i}") # imprime el valor de i en cada iteración
    i += 2 # incrementa el valor de i en 2 en cada iteración (pares)

"""
manejo de excepciones
"""

# Ejemplo de validación al ingresar la edad
entrada_usuario = "veinticinco"  # Texto que causará un error al convertir a entero
entrada_usuario2 = 25
try:
    edad = int("entrada_usuario") # Intentamos convertir el texto a entero
except ValueError: # Captura el error específico (ValueError en este caso) para evitar que el programa se detenga bruscamente.
    print("Error: Debes ingresar un número entero válido (ej. 25).") # Se ejecuta si el usuario ingresó texto en lugar de números
else:
    print(f"Registro exitoso. Tu edad es: {edad}") # Se ejecuta SOLO si la conversión fue exitosa (sin errores)
finally:
    print("Proceso de validación finalizado.") # Se ejecuta SIEMPRE, haya o no haya ocurrido un error


"""
EXTRA 
"""

print("Forma con Condicionales")

"""
Esta es la forma tradicional donde el bucle recorre todos los números,
 y la estructura condicional evalúa si cumple o no las reglas.
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0: # Evalúa que sea par, diferente de 16 y no múltiplo de 3
        print(number)


"""
Práctica de Bucle WHILE
"""

"""
En esta solución exploro el uso de bucles iterativos WHILE 
para filtrar números según las condiciones del reto
"""

print("Forma con bucle while")

i = 10 # definimos la variable de control en el límite inferior (10)

while i <= 56: # Mientras i sea menor o igual a 56, el bucle continuará ejecutándose

    i += 1 # Incrementamos i de 1 en 1 para avanzar a la siguiente iteración

    if i % 2 == 0 and i != 16 and i % 3 != 0: # Evaluamos las condiciones de filtro en cada ciclo
        print (f"interaccion {i}")


# con estos razonamientos y ejercicios completo mejor mi aprensaje e interes de python gracias 'MoureDev'