"""
Operadores
"""

# Aritméticos

print(f'Suma -> 10 + 5 = {10 + 5}')  # Adición
print(f'Resta -> 10 - 5 = {10 - 5}')  # Sustracción
print(f'Multiplicación -> 10 * 5 = {10 * 5}')  # Multiplicación
print(f'División -> 10 / 5 = {10 / 5}')  # División
print(f'Módulo -> 10 % 5 = {10 % 5}')  # Módulo
print(f'Exponente -> 10 ** 5 = {10 ** 5}')  # Exponenciación
print(f'División entera -> 10 // 5 = {10 // 5}')  # División entera

# Asignación

x = 0
print(f'Valor asignado: {x}')

x += 10
print(f'Suma y asignación: {x}')

x -= 5
print(f'Resta y asignación: {x}')

x *= 10
print(f'Multiplicación y asignación: {x}')

x /= 5
print(f'División y asignación: {x}')

x %= 1
print(f'Módulo y asignación: {x}')

x **= 2
print(f'Exponente y asignación: {x}')

# Comparación

print(f'Igualdad: 10 == 3 -> {10 == 3}')
print(f'Desigualdad: 10 != 3 -> {10 != 3}')
print(f'Mayor que: 10 > 3 -> {10 > 3}')
print(f'Menor que: 10 < 3 -> {10 < 3}')
print(f'Mayor o igual que: 10 >= 3 -> {10 >= 3}')
print(f'Menor o igual que: 10 <= 3 -> {10 <= 3}')

# Lógicos

print('and: Este operador devuelve True si ambas comparaciones son True, de lo contrario devolverá False')
print(f'10 == 3 and 10 != 3 -> {10 == 3 and 10 != 3}\n')

print('''or: Este operador devuelve True si al menos una de las comparaciones es True,
en caso de que ambas comparaciones sean False, devolverá False''')
print(f'10 == 3 or 10 != 3 -> {10 == 3 or 10 != 3}')

print('''not: Sirve para negar(invertir) el valor de una comparación booleana.
En el caso de que una comparación esté evaluada en True, este operador hará que evalue en False, y viceversa.''')
print(f'10 != 3 and not 10 == 3 -> {10 != 3 and not 10 == 3}')

# Identidad

x = True
y = False

# Devuelve True si ambas variables son el mismo objeto
print(f'x is y -> {x is y}')
# Devuelve True si ambas variables no son el mismo objeto
print(f'x is not y -> {x is not y}')

# Pertenencia

lista = [1, 32, 7, 10]
# Devuelve True si el dato especificado se encuentra dentro del objeto
print(f'32 in lista {32 in lista}')
# Devuelve True si el dato especificado no se encuentra dentro del objeto
print(f'2 not in lista {2 not in lista}')

"""
Estructuras de control
"""

# Condicionales

nombre = 'Juan'

if nombre == "Juan":
    print(f'Tu nombres es {nombre}')
elif nombre == 'Pedro':
    print(f'Tu nombre es {nombre}')
else:
    print('Tu nombre no es Juan ni Pedro')

# Iterativas

for x in range(16):
    print(x)

lista = ['Mouredev', 'Juan', 'Pedro', 'Chanchito']
for name in lista:
    print(name)

diccionario = {'nombre': 'Lucas', 'profesion': 'Médico'}
for clave, valor in diccionario.items():
    print(f'{clave} : {valor}')

x = 0

while x <= 10:
    print(x)
    x += 1

# Excepciones

try:
    print(1 / 0)
except:
    print("Se produjo un error")
finally:
    print("Terminó el manejo de expeciones")

"""Ejercicio extra"""

for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
