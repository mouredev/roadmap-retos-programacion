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