"""
Operadores aritméticos
"""

suma = 3 + 4
resta = 5 - 2
multiplicacion = 3 * 5
division = 8 / 3
modulo = 8 % 2
exponencial = 2 ** 2
division_entera = 7 // 2

print('El resultado de los operadores aritmeticos son: ')
print(f'El resultado de la suma 3 + 4 es: {suma}')
print(f'El resultado de la resta 5 - 2 es: {resta}')
print(f'El resultado de la multiplicacion 3 * 5 es: {multiplicacion}')
print(f'El resultado de la division 8 / 3 es: {division}')
print(f'El resultado de la modulo 8 % 2 es: {modulo}')
print(f'El resultado de la exponencial es 2 ** 2: {exponencial}')
print(f'El resultado de la division entera 7 // 2 es: {division_entera}')

"""
Operadores relacionales
"""

print(f'Mayor que: 10 > 3 es {10 > 3}')
print(f'Menor que: 3 < 10 es {3 < 10}')
print(f'Igual que: 3 = 3 es {3 == 3}')
print(f'Mayor o igual que: 10 >= 10 es {10 >= 10}')
print(f'Menor o igual que: 10 <= 3 es {10 <= 10}')
print(f'No es igual 7 a 3 es {7 != 3} ')

"""
Operadores lógicos
"""

print(f'AND &&: 10 + 3 es 13 AND 15 - 2 es 13 {10 + 3 == 13 and 15 - 2 == 13 }')
print(f'OR: 10 + 3 == 15 or 5 - 1 == 4 es {10 + 3 == 13 or 5 - 1 == 4}')
print(f'NOT: 10 + 3 == 14 es {not 10 + 3 == 14} ')


'''
Operadores de asignación
'''

mi_numero = 4
print(mi_numero)

# suma y asignación
mi_numero += 1
print(mi_numero)
# Resta y asignación
mi_numero -= 2
print(mi_numero)
# multiplicación y asignación
mi_numero *= 2
print(mi_numero)
# división y asignación
mi_numero /= 2
print(mi_numero)
# Exponencial y asignación
mi_numero **= 2
print(mi_numero)

'''Operadores 
de identidad
'''

my_new_number = mi_numero
print(f'my_new_number is my_new_number es {mi_numero is my_new_number}')
print(f'my_new_number is my_new_number es {mi_numero is not my_new_number}')

# Operadores de bit
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

"""
Estructuras de control
"""

# Condicionales

my_string = "Carlos"

if my_string == "cbuenrostrovalverde":
    print("my_string es 'cbuenrostrovalverde'")
elif my_string == "Carlos":
    print("my_string es 'Carlos'")
else:
    print("my_string no es 'cbuenrostrovalverde' ni 'Carlos'")

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
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
Extra: imprimir por pantalla números entre 10 - 55
"""

for numero in range (10, 56):
    if numero %2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)