# Ejemplo de operadores aritmeticos

a = 5
b = 2

print(f'Valor de variable a: {a}')
print(f'Valor de variable b: {b}')

print(f'a + b: {a+b}')
print(f'a - b: {a-b}')
print(f'a * b: {a*b}')
print(f'a / b: {a/b}')
print(f'a % b: {a%b}')

# Ejemplo de operadores logicos

# Operador and
print('## Operador and  ##')
print(f'True and True: {True and True}')
print(f'True and False: {True and False}')
print(f'False and True: {False and True}')
print(f'False and False: {False and False}')

# Operador or
print('## Operador or  ##')
print(f'True or True: {True or True}')
print(f'True or False: {True or False}')
print(f'False or True: {False or True}')
print(f'False or False: {False or False}')

# Operador not
print('## Operador not  ##')
print(f'not True: {not True}')
print(f'not False: {not False}')

# Operadores de comparacion

print('## Operadores de comparacion ##')
print(f'{a} == {b}: {a==b}')
print(f'{a} != {b}: {a!=b}')
print(f'{a} < {b}: {a<b}')
print(f'{a} > {b}: {a>b}')
print(f'{a} <= {b}: {a<=b}')
print(f'{a} >= {b}: {a>=b}')

# Operadores de asignacion

print('## Operadores de asignacion ##')
x = "Hola"
y = 256
z = 128
print(f'x = "Hola", valor de variable x: {x}')
print(f'y = 265, valor de variable y: {y}')
y += z
print(f'y += z, resultado: {y}')
y -= z
print(f'y -= z, resultado: {y}')
y *= z
print(f'y *= z, resultado: {y}')
y /= z
print(f'y /= z, resultado: {y}')
y %= z
print(f'y %= z, resultado: {y}')
y = 2
z = 6
y **= z
print(f'y **= z, resultado: {y}')
y //= z
print(f'y //= z, resultado: {y}')

# Operadores de identidad
a = 100
b = 100

print(f'a={a}, b={b}, a is b: {a is b}')
b = 200
print(f'a={a}, b={b}, a is b: {a is b}')

lista1 = [10, 20, 30]
lista2 = [10, 20, 30]

print(f'l1: {lista1}, l2: {lista2} l1 is l2: {lista1 is lista2}')

a = 100
b = 100

print(f'a={a}, b={b}, a is not b: {a is not b}')
b = 200
print(f'a={a}, b={b}, a is not b: {a is not b}')

# Operadores de pertenencia

lista1 = ['a', 'c', 'e']
print(f'e in {lista1}: {"e" in lista1}')
print(f'g in {lista1}: {"g" in lista1}')
print(f'e not in {lista1}: {"e" not in lista1}')
print(f'n not in {lista1}: {"n" not in lista1}')

# Operadores de bits

x = 0b0001
y = 0b1010

print(f'Operador and & bitwise: {x} & {y}: {x & y}')
print(f'Operador or | bitwise: {x} | {y}: {x | y}')
print(f'Operador not ~ bitwise: {x}: {~x}')
print(f'Operador xor ^ bitwise: {x} ^ {y}: {x ^ y}')

# Estructuras de control

# Condicionales
print(f'if {a} == {b}: {a == b}')
print(f'if {a} != {b}: {a != b}')
print(f'if {a} > {b}: {a > b}')
print(f'if {a} < {b}: {a < b}')
print(f'if {a} >= {b}: {a >= b}')
print(f'if {a} <= {b}: {a <= b}')

# Iterativas

# While
x = 0
while x < 3:
    print(f'Ciclo while, Valor de x: {x}')
    x += 1
else:
    print('Fin de ciclo while')
    
# For 
x = 3
for i in range (0, x):
    print(f'Ciclo for, Valor de i: {i}')
    
for elemento in lista1:
    print(f'Elemento de lista: {elemento}')
    
cadena = 'cadena de texto'
for c in cadena:
    print(f'Caracter de cadena de texto: {c}')
    
# Ejercicio de dificultad extra

n = 56
for i in range (10, n):
    if (i % 2 == 0) and (i != 16) and (i % 3 != 0):
        print(f'Numeros: {i}')