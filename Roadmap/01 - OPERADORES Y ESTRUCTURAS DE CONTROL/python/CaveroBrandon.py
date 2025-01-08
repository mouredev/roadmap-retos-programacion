# Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:

# ************************************************************
# OPERADORES ARITMETICOS
# ************************************************************
val1 = 20
val2 = 10

addition = val1 + val2  # Addition
subtraction = val1 - val2  # Subtraction
multiplication = val1 * val2  # Multiplication
division = val1 / val2  # Division
modulus = val1 % val2  # Modulus
floor_division = val1 // val2  # floor division
exponentiation = val1 ** val2  # Exponentiation

# ************************************************************
# OPERADORES LOGICOS
# ************************************************************
a = True
b = False

c = a and b  # AND, return False
d = a or b  # OR, return True
e = not a  # NOT, return False

# ************************************************************
# OPERADORES DE IDENTIDAD
# ************************************************************
name = 'Brandon'
lastname = 'Cavero'

is_equal = name is lastname  # returns False
is_not_equal = name is not lastname  # returns True

# ************************************************************
# OPERADORES DE COMPARACION
# ************************************************************
small_volume = 5
big_volume = 10

is_equal = (small_volume == big_volume)  # return False
is_not_equal = (small_volume != big_volume)  # return True
is_less = (small_volume < big_volume)  # return True
is_greater = (small_volume > big_volume)  # return False
is_less_than = (small_volume <= big_volume)  # return True
is_greater_than = (small_volume >= big_volume)  # return False

# ************************************************************
# OPERADORES DE PERTENENCIA
# ************************************************************
language = 'Python'
syllabus = 'Py'

a = syllabus in language  # return True, 'Py' is in 'Python'
b = 'Xo' in language  # return True, 'Xo' is not in 'Python'

"""
Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
"""

# ************************************************************
# IF
# ************************************************************
print('********* If statement *********')
condition = True

if condition:
    print('The condition is True so this will be printed')
else:
    print('This should be printed if none of the conditions are True')

# ************************************************************
# FOR LOOP
# ************************************************************
print('********* For loop *********')
fruits = ['bananas', 'apples', 'grapes']

for fruit in fruits:
    print(fruit)

# ************************************************************
# WHILE LOOP
# ************************************************************
print('********* While loop *********')
counter = 3

while counter > 0:
    print('While loop')
    counter -= 1

# ************************************************************
# TRY - EXCEPT
# ************************************************************
print('********* Try - Except *********')
try:
    a = 1 + _  # This should raise an exception
except Exception as e:
    print('This is being printed because of the error: ', e)

"""
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
print('********* DIFICULTAD EXTRA *********')
for number in range(10, 56):
    if number == 16 or (number % 3) == 0:
        pass
    elif number % 2 == 0:
        print(number, end=' ')
