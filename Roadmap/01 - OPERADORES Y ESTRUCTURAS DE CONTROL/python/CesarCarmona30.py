'''
  OPERADORES
'''

# Operadores Aritméticos:
print(f"Suma: 8 + 5 = {8 + 5}")
print(f"Resta: 8 - 5 = {8 - 5 }")
print(f"Multiplicación: 8 * 5 = {8 * 5}")
print(f"División: 8 / 5 = {8 / 5}")
print(f"División entera: 8 // 5 = {8 // 5}")
print(f"Módulo: 8 % 5 = {8 % 5}")
print(f"Potencia: 8 ** 5 = {8 ** 5}")

# Operadores Lógicos:
print(f"AND (and):") 
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and False = {False and False}")
print(f"OR (or):") 
print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or False = {False or False}")
print(f"NOT (not):") 
print(f"not True = {not True}")
print(f"not False = {not False}")

# Operadores de Comparación:
print(f"Igualdad: 15 == 5 es {15 == 5}")
print(f"Desigualdad: 15 != 5 es {15 != 5}")
print(f"Mayor que: 15 > 5 es {15 > 5}")
print(f"Menor que: 15 < 5 es {15 < 5}")
print(f"Mayor o igual que: 15 >= 155 es {15 >= 155}")
print(f"Menor o igual que: 155 <= 155 es {155 <= 155}")

# Operadores de Asignación:
numero = 50
print(f"Asignación: numero = {numero}")
numero += 1
print(f"Suma y asignación: numero += 1 ({numero})")
numero -= 3
print(f"Resta y asignación: numero -= 3 ({numero})")
numero *= 3
print(f"Multiplicación y asignación: numero *= 3 ({numero})")
numero /= 4
print(f"División y asignación: numero /= 4 ({numero})")
numero //= 5
print(f"División entera y asignación: numero //= 5 ({numero})")
numero %= 5
print(f"Módulo y asignación: numero %= 5 ({numero})")
numero **= 8
print(f"Potencia y asignación: numero **= 8 ({numero})")

# Operadores de Identidad:
a = 85
b = a
c = b

print(f"a = 85 y b = a, entonces b is a es: {b is a}")
print(f"b = a y c = b, entonces c not is a es: {c is not a}")

# Operadores de Pertenencia:
print(f"'Hola' in 'Hola Mundo' es: {'Hola' in 'Hola Mundo'}")
print(f"'Hello' not in 'Hola Mundo' es: {'Hello' not in 'Hola Mundo'}")

# Operadores Bit a Bit:
x = 10
y = 12

print(f"AND: 10 & 12 = {10 & 12}") 
print(f"OR: 10 | 12 = {10 | 12}")  
print(f"XOR: 10 ^ 12 = {10 ^ 12}")  
print(f"NOT: ~2 = {~2}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") 
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")

'''
  ESTRUCTURAS DE CONTROL
'''

# Condicionales

mi_lenguaje = "Python"

print('Ejecutando estructura if: ')
if mi_lenguaje == "JavaScript":
  print("Estoy programando en JavaScript")
elif mi_lenguaje == "Python":
  print("Estoy programando en Python")
else:
  print("No estoy programando en JavaScript ni en Python")

#Iterativas

print('Ejecutando estructura for: ')   

for n in range(1, 11):
  print(n, end=' ')

print('\nEjecutando estructura while: ')

m = 0
while m <= 10:
  print(m, end=', ')
  m += 1

# Manejo de Excepciones

print('\nEjecutando estructura try-except: ')

print('5 / 0 = ...')
try:
  print(5 / 0)
except ZeroDivisionError as err:
  print(f"Se produjo un error de tipo: {type(err).__name__}")
finally:
  print("*Nota: Recuerda que la división por cero no esta definida")

'''
  EJERCICIO EXTRA
'''

for number in range(10, 56):
    if number % 2 != 0 or number == 16 or number % 3 == 0:
      continue
    print(number, end=' ')