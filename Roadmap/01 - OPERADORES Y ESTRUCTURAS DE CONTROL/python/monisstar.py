# Operdadores

# Operdadores aritméticos

print(f'Suma -> 2 + 2 = {2 + 2}')
print(f'Resta -> 5 - 2 = {5 - 2}')
print(f'Multiplicación -> 4 * 8 = {4 * 8}')
print(f'División -> 10 / 2 = {10 / 2}')
print(f'Módulo -> 10 % 3 = {10 % 3}')
print(f'Potencia -> 2 ** 3 = {2 ** 3}')
print(f'División entera -> 10 // 2 = {10 // 2}')

# Operaciones de comparación
print(f'Igualdad: 25 == 43 {25 == 43}')
print(f'Desigualdad: 25 != 43 {25 != 43}')
print(f'Mayor que: 25 > 43 {25 > 43}')
print(f'Menor que: 25 < 43 {25 < 43}')
print(f'Mayor o igual que: 25 >= 43 {25 >= 43}')
print(f'Menor o igual que: 25 <= 43 {25 <= 43}')

#Operdaores lógicos
print(f'AND &&: 25 + 43 == 68 and 25 - 43 == 0 es: {25 + 43 == 68 and 25 - 43 == 0}')
print(f'OR ||: 25 + 43 == 68 or 25 - 43 == 0 es: {25 + 43 == 68 or 25 - 43 == 0}')
print(f'NOT !: not 25 + 43 == 68 es: {not 25 + 43 == 68}')

# Operadores de asignación
number = 5
print(number)
number += 1  # suma y asignación
print(number)
number -= 1  # resta y asignación
print(number)
number *= 2  # multiplicación y asignacion
print(number)
number %= 2  # módulo y asignación
print(number)
number **= 2 # potencia y asignación
number //= 2 # división entera y asignación

# Operadores de identidad
n_number = 5
print(f'n_number is number es {n_number is number}')
print(f'n_number is not number es {n_number is not number}')

# Operadores de pertenencia
print(f"'o' in 'monisstar' es {'o' in 'monisstar'}")
print(f"'j' not in 'monisstar' es {'j' not in 'monisstar'}")

# Operadores de bit
a = 10
b = 3
print(f'AND: 10 & 3 = {a & b}')
print(f'OR: 10 | 3 = {a | b}')
print(f'XOR: 10 ^ 3 = {a ^ b}')
print(f'NOT: ~10 = {~a}')
print(f'Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}')
print(f'Desplazamiento a la izquierda: 10 << 2 = {10 << 2}')

'''
Estructuras de control
'''
# Condicionales
my_string = 'monisstar'
if my_string == 'monisstar':
    print('my_string es monisstar')
elif my_string == 'Brais':
    print('my_string es Brais')
else:
    print('my_string es diferente de monisstar y Brais')

# Iterativas
for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)
except ZeroDivisionError:
    print('No se puede dividir entre 0')
finally:
    print('Finalizado, el manejo de excepciones')

'''
DIFICULTAD EXTRA
'''
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)