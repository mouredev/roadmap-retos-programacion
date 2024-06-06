'''
Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
'''

var_a = 3
var_b = 5

# aritmeticos
print('Operadores aritmeticos:')
print(f'Suma {var_a} + {var_b} = {var_a + var_b}')
print(f'Resta {var_a} - {var_b} = {var_a - var_b}')
print(f'Multiplicación {var_a} * {var_b} = {var_a * var_b}')
print(f'Division {var_a} / {var_b} = {var_a / var_b}')
print(f'Division entera {var_a} // {var_b} = {var_a // var_b}')
print(f'Modulo {var_a} % {var_b} = {var_a % var_b}')
print(f'Potencia {var_a} ** {var_b} = {var_a ** var_b}')

print()

# de asignacion
numero = 6
print('Operadores de asignacion')
print('numero = 6')
numero += 3
print(f'numero += 3 es {numero}')
numero -= 1
print(f'numero -= 1 es {numero}')
numero /=2
print(f'numero /= 2 es {numero}')
numero *= 3
print(f'numero *= 3 es {numero}')
numero **=2
print(f'numero **=2 es {numero}')
numero //=3
print(f'numero //=3 es {numero}')
numero %=2
print(f'numero %=2 es {numero}')

print()

# de comparacion
print('Operadores de comparacion')
print(f'{var_b} == {var_b} -> {var_a == var_b}')
print(f'{var_b} != {var_b} -> {var_a != var_b}')
print(f'{var_b} < {var_b} -> {var_a < var_b}')
print(f'{var_b} > {var_b} -> {var_a > var_b}')
print(f'{var_b} <= {var_b} -> {var_a <= var_b}')
print(f'{var_b} >= {var_b} -> {var_a >= var_b}')

print()

# operadores logicos
print('operadores logicos')
a = (var_a == var_b)
b = (var_a <= var_b)
c = (var_a >= var_b)

print(f'a or b es {a or b}')
print(f'a and c es {a and b}')
print(f'not a es {not a}')
print(f'not b es {not b}')
print(f'not c es {not c}')

print()

# bits
print('Operadores a nivel de bits')

var_a = 6
var_b = 4

print(f'and binario: {var_a} & {var_b} -> {var_a & var_b}')
print(f'or binario: {var_a} | {var_b} -> {var_a | var_b}')
print(f'exclusivo binario: {var_a} ^ {var_b} -> {var_a ^ var_b}')
print(f'not binario: ~{var_a} -> {~var_a}')
print(f'not binario: ~{var_b} -> {~var_b}')
print(f'desplazamiento a la izquierda: {var_a} << 2 -> {var_a << 2}')
print(f'desplazamiento a la derecha: {var_a} >> 2 -> {var_a >> 2}')
print(f'representacion binaria de un entero: bin(5) -> {bin(5)}')

print()

# Operadores de pertenencia
print('Operadores de pertenencia')
lista = [1,2,3,4,5,6,7,8]
num = 9
num_2 = 4

print(f'operador in: {num_2} in {lista} -> {num_2 in lista}')
print(f'operador not in: {num} not in {lista} -> {num not in lista}')

print()

# Operador de identidad
print('Operador de identidad')
a = 1
b = 1

print(a is b)

print()

'''
Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
'''
# condicionales if, elif y match
print('condicionales if, elif y match')
#   if
if 5 < 4:
    print('5 es menor que 4')
else: 
    print('5 es mayor que 4')

#   elif
if 4 < 3:
    print('El 3 es mayor')
elif 4 > 3:
    print('El 4 es el mayor')
else:
    print('Los numeros son iguales')

#   match
dia = 'lunes'
match dia:
    case 'lunes':
        print('Es lunes')
    case 'martes':
        print('Es martes')
    case 'miercoles':
        print('Es miercoles')
    case 'jueves':
        print('Es jueves')
    case 'viernes':
        print('Es viernes')
    case _:
        print('Ninguno')
    
print()

print('Bucles for y while')
# Bucles for y while

#   bucle for
iter = 0
for i in range(10):
    iter +=1
    print(iter)

print()

#   bucle while
iter = 0
while iter < 10:
    iter += 1
    print(iter)

print()

print('Excepciones')

try:
    div_by_0 = 3/0
    print(div_by_0)
except ZeroDivisionError as e:
    print(f'error: {e}')

'''
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''

print()

print('Programa extra')
for i in range(10, 56):
    if i == 16:
        pass
    elif not(i % 3 == 0) and i % 2 == 0:
        print(i)
