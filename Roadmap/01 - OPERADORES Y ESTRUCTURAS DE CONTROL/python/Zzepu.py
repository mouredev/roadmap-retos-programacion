# Declarando operadores aritmeticos

print(f'Suma: 15 + 15 = {15 + 15}')
print(f'Resta: 50 - 15 = {50 - 15}')
print(f'Multiplicacion: 5 * 5 = {5 * 5}')
print(f'Division: 50 / 2 = {50 / 2}')
print(f'Modulo: 50 % 2 = {50 % 2}')
print(f'Exponente: 50 ** 2 = {50 ** 2}')
print(f'Division entera: 50 // 2 = {50 // 2}')

# Declarando operadores de comparacion
print(f'Igualdad: 10 == 3 es {10 == 3}')
print(f'Desigualdad: 10 != 3 es {10 != 3}')
print(f'Mayor que: 10 > 3 es {10 > 3}')
print(f'Menor que: 10 < 3 es {10 < 3}')
print(f'Mayor o igual que: 10 >= 3 es {10 >= 3}')
print(f'Menor o igual que: 10 <= 3 es {10 <= 3}')

# Declarando operadores logicos
print(f'AND: 30 + 5 == 35 and 10 + 10 == 20 es: {30 + 5 == 35 and 10 + 10 == 20}')
print(f'OR: 30 + 5 == 35 or 10 + 10 == 20 es: {30 + 5 == 35 or 10 + 10 == 20}')
print(f'NOT: not 20 + 5 == 31 es {not 20 + 5 == 31}')

# Declarando operadores de asignacion
sweet_number = 50 # Asignacion
print(sweet_number)
sweet_number += 5 # suma y asignacion
print(sweet_number)
sweet_number -= 5 # Resta y asignacion
print(sweet_number)
sweet_number *= 5 # Multiplicacion y asignacion
print(sweet_number)
sweet_number /= 6 # Division y asignacion
print(sweet_number)
sweet_number %= 5 # Modulo y asignacion
print(sweet_number)
sweet_number **= 9 # Exponente y asignacion
print(sweet_number)
sweet_number //= 6 # Division entera y asignacion
print(sweet_number)

# Declarando operadores de identidad
new_sweet_number = 16.0
print(f'sweet_number is new_sweet_number es {sweet_number is new_sweet_number}')
print(f'sweet_number is not new_sweet_number es {sweet_number is not new_sweet_number}')

# Operadores de pertenencia
print(f"'e' in 'zzepu' es {'e' in 'zzepu'}")
print(f"'s' not in 'zzepu' es {'s' not in 'zzepu'}")

# Operadores de bit
y = 10 # 1010
z = 3 # 0011
print(f'AND: 10 & 3 es {10 & 3}')
print(f'OR: 10 | 3 es {10 | 3}')
print(f'XOR: 10 ^ 3 es {10 ^ 3}')
print(f'NOT: ~10 es {~10}')
print(f'Desplazamiento a la derecha: 10 >> 2 es {10 >> 2}')
print(f'Desplazamiento a la izquierda: 10 << 2 es {10 << 2}')

"""
Estructuras de control
"""

sweet_string = 'Zzepu'

if sweet_string == 'Zzepu':
    print('sweet_string es Zzepu')
else:
    print('sweet_string no es Zzepu')

# Ciclos iterativos

for i in range(11):
    print(i)

i = 0
while i <=10:
    print(i)
    i += 1


# Manejo de expepciones

try:
    print(10 / 0)
except:
    print('Ups! Hay un falloooo')
finally:
    print('Ha concluido el manejo de excepciones')


# Ejercicio extra!


for numbers in range(10,56):
    if numbers % 2 == 0 and numbers != 16 and numbers % 3 != 0:
        print(numbers)






