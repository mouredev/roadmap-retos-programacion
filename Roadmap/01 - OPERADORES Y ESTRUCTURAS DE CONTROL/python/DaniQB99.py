
#  * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, logicos, de comparacion, asignacion, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

# Aritméticos
print(f'Suma: {2 + 2}')
print(f'Resta: {2 - 2}')
print(f'Multiplicacion: {2 * 2}')
print(f'Division: {3 / 2}')
print(f'Division entera: {3 // 2}')
print(f'Resto de la division: {2 % 2}')
print(f'Potencia: {2 ** 2}')

# logicos  
print(f'AND &&: 10 + 4 == 14 and 4 - 1 == 3 es {True and True}')
print(f'OR ||: 10 + 4 == 14 or 4 - 1 == 3 es {True or True}')
print(f'NOT !: 10 + 4 == 14 no es {not True}')

# Comparacion
print(f'Igual: {2 == 2}')
print(f'Diferente: {5 != 5}')
print(f'Mayor: {10 > 3}')
print(f'Menor: {2 < 7}')
print(f'Mayor o igual: {3 >= 2}')
print(f'Menor o igual: {1 <= 6}')

# Asignacion
my_number = 5
print(f'Asignacion: {my_number}')
my_number += 5
print(f'Suma y asignacion: {my_number}')
my_number *= 5
print(f'Multiplicacion y asignacion: {my_number}')
my_number **= 5
print(f'Potencia y asignacion: {my_number}')
my_number -= 5
print(f'Resta y asignacion: {my_number}')
my_number /= 5
print(f'Division y asignacion: {my_number}')
my_number //= 5
print(f'Division entera y asignacion: {my_number}')
my_number %= 5
print(f'Resto de la division y asignacion: {my_number}')


# Identidad
my_string = 'test'
my_new_string = my_string
print(f'my_string is my_new_string es: {my_string is my_new_string}')
print(f'my_string is not my_new_string es: {my_string is not my_new_string}')


# Pertenencia 
print(f"'t' in 'test' = {'t' in 'test'}")
print(f"'h' not in 'test' = {'h' not in 'test'}")

# Bits
a = 10
b = 2
print(f'AND: 10 & 2 = {a & b}') 
print(f'OR: 10 | 2 = {a | b}') 
print(f'XOR: 10 ^ 2 = {a ^ b}')
print(f'NOT: ~10 = {~a}')

print(f'Desplazamiento a la derecha: 8 >> 2 = {8 >> 2}')
print(f'Desplazamiento a la izquierda: 8 << 2 = {8 << 2}')


# ESTRUCTURAS DE CONTROL

# Condicionales
if my_string == 'DaniQB99':
    print('Hola, soy DaniQB99')
elif my_string == 'Dani':
    print('Hola, soy Dani')
else:
    print('Hola, soy otro usuario')

# Iterativas
for i in range(10): # Iteramos 10 veces
    print(i)

# While
i = 0
while i < 10: # Mientras i sea menor que 10
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(12 / 0)
except ZeroDivisionError:
    print('No se puede dividir por cero')
finally:
    print('Finalizado, el manejo de excepciones')

""" 
Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y
que no son ni el 16 ni múltiplos de 3.
"""
print('\n--- EJERCICIO EXTRA ---')
for num in range(10, 55):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)

