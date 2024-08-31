# OPERADORES ARITMÉTICOS
print('OPERADORES ARITMÉTICOS')
first_number = 7
second_number = 2
result = 0

# Operador suma (+)
result = first_number + second_number
print(f"La suma de {first_number} + {second_number} es {result}")

# Operador resta (-)
result = first_number - second_number
print(f"La resta de {first_number} - {second_number} es {result}")

# Operador multiplicación (*)
result = first_number * second_number
print(f"La multiplicación de {first_number} * {second_number} es {result}")

# Operador división (/)
result = first_number / second_number
print(f"La división de {first_number} / {second_number} es {result}")

# Operador módulo (%)
result = first_number % second_number
print(f"El resto de la división de {first_number} / {second_number} es {result}")

# OPERADORES LÓGICOS
print('\nOPERADORES LÓGICOS')
first_bool = True
second_bool = False

# Operador lógico AND (and)
logic_and = first_bool and second_bool
print(f"AND lógico: {logic_and}")

# Operador lógico OR (or)
logic_or = first_bool or second_bool
print(f"OR lógico: {logic_or}")

# Operador lógico NOT (not)
logic_not = not first_bool
print(f"NOT lógico: {logic_not}")

# OPERADORES DE COMPARACIÓN
print('\nOPERADORES DE COMPARACIÓN')
# Operador mayor que (>)
great_than = 5 > 10
print(f"¿Es 5 mayor que 10? -> {great_than}")

# Operador menor que (<)
less_than = 5 < 10
print(f"¿Es 5 menor que 10? -> {less_than}")

# Operador mayor o igual que (>=)
great_or_equal = 5 >= 10
print(f"¿Es 5 mayor o igual que 10? -> {great_or_equal}")

# Operador menor o igual que (<=)
less_or_equal = 5 <= 10
print(f"¿Es 5 menor o igual que 10? -> {less_or_equal}")

# OPERADORES DE ASIGNACIÓN
print('\nOPERADORES DE ASIGNACIÓN')
# Operador de asignación simple (=)
number = 10
print(f"Valor asignado: {number}")

# Operador de suma y asignación (+=)
number += 5  # 10 + 5 = 15
print(f"Valor del resultado de suma y asignación: {number}")

# Operador de resta y asignación (-=)
number -= 5  # 15 - 5 = 10
print(f"Valor del resultado de resta y asignación: {number}")

# Operador de multiplicación y asignación (*=)
number *= 5  # 10 * 5 = 50
print(f"Valor del resultado de multiplicación y asignación: {number}")

# Operador de división y asignación (/=)
number /= 5  # 50 / 5 = 10
print(f"Valor del resultado de división y asignación: {number}")

# Operador de módulo y asignación (%=)
number %= 5  # 10 % 5 = 0
print(f"Valor del resultado de módulo y asignación: {number}")

# OPERADORES DE IDENTIDAD
print('\nOPERADORES IDENTIDAD')
# Operador de igualdad estricta (==)
strict_equal_comp = 5 == 5
print(f"¿Es 5 estrictamente igual a 5? -> {strict_equal_comp}")

# Operador de desigualdad estricta (!=)
strict_diff_comp = '5' != '5'
print(f"¿Es '5' estrictamente diferente a '5'? -> {strict_diff_comp}")

# OPERADORES DE PERTENENCIA
print('\nOPERADORES DE PERTENENCIA')
int_list = [1, 12, 5, 643, 3]
first_check = 3 in int_list  # Devolverá True
second_check = 65 in int_list  # Devolverá False

print(f"¿Está el número 3 en la lista de números? -> {first_check}")
print(f"¿Está el número 65 en la lista de números? -> {second_check}")

# OPERADORES DE BITS
print('\nOPERADORES DE BITS')
first_bit = 5  # Representación binaria: 0000 0101
second_bit = 3  # Representación binaria: 0000 0011

# Operador AND a nivel de bits (&)
bit_and = first_bit & second_bit  # Devuelve 1 (representación binaria: 0000 0001)
print(f"Resultado AND bit a bit -> {bit_and}")

# Operador OR a nivel de bits (|)
bit_or = first_bit | second_bit  # Devuelve 7 (representación binaria: 0000 0111)
print(f"Resultado OR bit a bit -> {bit_or}")

# Operador XOR a nivel de bits (^)
bit_xor = first_bit ^ second_bit  # Devuelve 6 (representación binaria: 0000 0110)
print(f"Resultado XOR bit a bit -> {bit_xor}")

# Operador NOT a nivel de bits (~)
bit_not = ~first_bit  # Devuelve -6 (representación binaria: 1111 1010)
print(f"Resultado NOT bit a bit -> {bit_not}")

# Operador de desplazamiento hacia la derecha (>>)
to_right_bit = first_bit >> 1  # Devuelve 2 (representación binaria: 0000 0010)
print(f"Desplazamiento hacia la derecha -> {to_right_bit}")

# Operador de desplazamiento hacia la izquierda (<<)
to_left_bit = first_bit << 1  # Devuelve 10 (representación binaria: 0000 1010)
print(f"Desplazamiento hacia la izquierda -> {to_left_bit}")

# ESTRUCTURAS DE CONTROL CONDICIONAL
print('\nESTRUCTURAS DE CONTROL CONDICIONAL')
# if-else
print('if-else')
num = 10

if num > 0:
    print('El número es positivo.')
elif num == 0:
    print('El número es cero.')
else:
    print('El número es negativo.')

# Operador ternario
print('\nOperador ternario')
print('El número es positivo.' if num > 0 else 'El número es cero o negativo.')

# ESTRUCTURAS DE CONTROL ITERATIVAS
print('\nESTRUCTURAS DE CONTROL ITERATIVAS')
# while
print('Bucle While')
counter = 0
while counter < 5:
    print(f"Iteración: {counter}")
    counter += 1

# do-while (No hay una estructura directa de do-while en Python)
print('\nBucle do-while')
counter = 0
while True:
    print(f"Iteración: {counter}")
    counter += 1
    if counter >= 5:
        break

# for
print('\nBucle for')
for counter in range(5):
    print(f"Iteración: {counter}")

# for ... in (array)
print('\nBucle for ... in para arrays')
arr_numbers = [1, 2, 5, 2, 7, 9]
for number in arr_numbers:
    print(f"Número -> {number}")

# for ... in (objeto)
print('\nBucle for ... in para objetos')
persona = {'name': 'Alberto', 'age': 33}
for att, value in persona.items():
    print(f"{att} -> {value}")

# MANEJO DE EXCEPCIONES
print('\nMANEJO DE EXCEPCIONES')
print('Bloque try-catch')
err_number = 10

try:
    if err_number == 10:
        raise ValueError('El número es igual a 10.')
    print('El número es distinto de 10.')
except Exception as error:
    print(f"Se ha producido un error debido a -> {error}")

print('\nBloque try-catch-finally')
try:
    if err_number == 10:
        raise ValueError('El número es igual a 10.')
    print('El número es distinto de 10.')
except Exception as error:
    print(f"Se ha producido un error debido a -> {error}")
finally:
    print('Bloque finally. Esto siempre se ejecuta haya o no excepción.')

# DIFICULTAD EXTRA
print("\nEJERCICIO EXTRA")
""" 
Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y
que no son ni el 16 ni múltiplos de 3.
"""
for i in range(10, 56):
    if (i % 2 == 0) and (i != 16) and (i % 3 != 0):
        print("Iteración:", i)
