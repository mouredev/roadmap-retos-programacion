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
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

# OPERADORES ARITMÉTICOS

print(3 + 4)    # Suma -> 7
print(3 - 4)    # Resta -> -1
print(3 / 4)    # División -> 0.75
print(3 // 4)   # División entera -> 0
print(3 * 4)    # Multiplicación -> 12
print(3 % 4)    # Módulo -> 3
print(3 ** 4)   # Potencia -> 81


# OPERADORES LÓGICOS

print(True and False)   # AND -> False
print(True or False)    # OR -> True
print(not True)         # NOT -> False


# OPERADORES DE COMPARACIÓN

print(3 > 4)    # Mayor que -> False
print(3 < 4)    # Menor que -> True
print(3 >= 4)   # Mayor o igual que -> False
print(3 <= 4)   # Menor o igual que -> True

print(3 == "3") # Igual que -> False
print(3 != "3") # Diferente a -> True
print(3 == 4)   # False
print(3 != 4)   # True


# OPERADORES DE ASIGNACIÓN

assign_sum = 7
assign_sum += 3                 # Suma y asignación
print(assign_sum)               # 10

assign_subtract = 7
assign_subtract -= 4            # Resta y asignación
print(assign_subtract)          # 3

assign_multiplication = 7
assign_multiplication *= 2      # Multiplicación y asignación
print(assign_multiplication)    # 14

assign_division = 7
assign_division /= 2            # División y asignación
print(assign_division)          # 3.5

assign_int_division = 7
assign_int_division //= 2       # División entera y asignación
print(assign_int_division)      # 3

assign_module = 7
assign_module %= 2              # Módulo y asignación
print(assign_module)            # 1

assign_pow = 7
assign_pow **= 2                # Potencia y asignación
print(assign_pow)               # 49


# OPERADORES DE PERTENENCIA

arr = [0, 1, 2, 3, 4]
print(3 in arr)         # True
print(11 in arr)        # False


# OPERADORES DE BITS

print(3 & 4)        # AND -> 0
print(3 | 4)        # OR -> 7
print(3 ^ 4)        # XOR -> 7
print(~3)           # NOT -> -4
print(3 << 4)       # Desplazamiento a izquierda -> 48
print(3 >> 4)       # Desplazamiento a derecha -> 0


# ESTRUCTURA DE CONTROL: if - else if - else

score = 8

if score >= 5:
    print("You have passed the exam!")
elif score < 5:
    print("You haven't passed the exam...")
else:
    print("The scores are not available yet.")


# ESTRUCTURA DE CONTROL: for
for i in range(5):
    print(i)
""" Se imprimen los siguientes números:
    0
    1
    2
    3
    4
"""


# ESTRUCTURA DE CONTROL: for (otro ejemplo con objetos)

PERSON = {
    "name": "Naia",
    "username": "nlarrea",
    "age": 25
}

for key in PERSON:
    # Se imprimen las claves:
    print(key)

    # Si quisiéramos imprimir los valores:
    # print(PERSON[key])

""" Se imprimen los siguientes strings:
    name
    username
    age
"""


# ESTRUCTURA DE CONTROL: for (otro ejemplo con listas)

NUM_LIST = ['hola', True, 7, ['a', 'b', 'c']]

for item in NUM_LIST:
    print(item)

""" Se imprime:
    'hola'
    True
    7
    [ 'a', 'b', 'c' ]
"""


# ESTRUCTURA DE CONTROL: while

i = 0
while i < 5:
    print(i)
    i += 1

""" Se imprimen los siguientes números:
    0
    1
    2
    3
    4
"""


# ESTRUCTURA DE CONTROL: try-except

try:
    print(5 / 0)                                        # Esto es un error
    raise Exception("This is another error")            # No se lanza porque hay otro error antes
    print("This is not printed")
except ZeroDivisionError as error:
    print(f"{type(error).__name__}: {error}")           # ZeroDivisionError: division by zero
except Exception as error:
    print(error)


# ESTRUCTURA DE CONTROL: try-except-finally

try:
    raise ValueError("This is a custom error message")
    print("This is not printed")
except Exception as error:
    print(f"{type(error).__name__}: {error}")           # ValueError: This is a custom error message
finally:
    print("This is always printed")                     # This is always printed

""" try-except(-finally):
En estas estructuras se puede añadir el bloque 'else' que se ejecuta
siempre que en el 'try' no haya ocurrido ningún error. """


# EJERCICIO EXTRA

""" DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 """

for num in range(10, 55 + 1):
    if (
        num % 2 == 0 and
        num != 16 and
        num % 3 != 0
    ):
        print(num)

""" Se imprimen los siguientes números:
    10 
    14 
    20 
    22 
    26 
    28 
    32 
    34 
    38 
    40 
    44 
    46 
    50 
    52
"""