# EJERCICIO:
# Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
'''Aritmeticos'''
print(f'suma: 4 + 4 = {4 + 4}')
print(f'resta: 4 - 4 = {4 - 4}')
print(f'multiplicacion: 4 * 3 = {4 * 3}')
print(f'division: 10 / 5 = {10 / 5}')
print(f'modulo: 10 % 5 = {11 % 5}')
print(f'division_entera: 7 // 3 = {7 // 3}')
print(f'potencia: 4 ** 3 = {4 ** 3}')

'''De comparacion'''
print(f'igualdad: 10 == 5 es {10 == 5}')
print(f'desigualdad: 10 != 5 es {10 != 5}')
print(f'mayor que: 20 > 4 es {20 > 4}')
print(f'menor que: 20 < 4 {20 < 4}')
print(f'mayor o igual que: 15 >= 14 es {15 >= 14}')
print(f'menor o igual que: 15 <= 14 es {15 <= 14}')

'''Logicos'''
'AND, OR Y NOT'
a = True
b = False

print(a and b) # False
print(a and a) # True
print(a or b)   # True
print(not a)    # False

print(True and True)   # True
print(True and False)  # False
print(True or True)   # True
print(True or False)  # True
print(not True)  # False
print(not False) # True

"Asignacion"
asignacion = 13
print(asignacion)
asignacion += 1 # Sumamos a asignacion el valor indicado
print(asignacion)
asignacion -= 3 # Restamos a asignacion el valor indicado
print(asignacion)
asignacion *= 2 # Multiplicamos a asignacion el valor indicado
print(asignacion)
asignacion /= 2 # Dividimos a asignacion el valor indicado
print(asignacion)
asignacion %= 2 # Modulo del valor indicado a asignacion
print(asignacion)
asignacion **= 1 # Potencia del valor indicado a asignacion
print(asignacion)
asignacion //= 1 # Division entera del valor indicado a asignacion
print(asignacion)

"Identidad"
nueva_asignacion = asignacion
print(f'nueva_asignacion is asignacion {nueva_asignacion is asignacion}')
print(f'nueva_asignacion is not asignacion {nueva_asignacion is not asignacion}')

"Pertenencia"
print(f"'a' in alvaro {'a' in 'alvaro'}")
print(f"'a' not in alvaro {'a' not in 'alvaro'}")


""" Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje: Condicionales, iterativas, excepciones...
"""
# Condicionales
print('if')
n = 7
if n == 7:
    print('n es igual a 7')
elif n != 6 and n != 8:
    print('n es distinto de 6 y distinto de 8')
elif n != 4 or n == 8:
    print('n es distinto de 4 o igual a 8')
else:
    print('ninguna de las anteriores')

# Iterativas
print("for")
for i in range(1,11):
    print(i)
print("while")
while n <= 10:
    print(n)
    n += 1

# Excepciones
try:
    print(12 / 3)
except:
    print('peté')
finally:
    print('cambiaste el cero y no peté gracias!')

print('////////////////')

"""DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo"""
for i in range(10,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
