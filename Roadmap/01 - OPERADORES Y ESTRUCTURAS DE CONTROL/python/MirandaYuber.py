import random

print('######  OPERADORES_ARITMETICOS  ######')
print(f'suma (1 + 1): {1 + 1}')
print(f'resta (1 - 1): {1 - 1}')
print(f'Multiplicación (10 * 2): {10 * 2}')
print(f'Division (12 / 2): {12 / 2}')
print(f'Division con resultado entero (18 // 5): {18 // 5}')
print(f'Modulo (16 % 3): {16 % 3}')
print(f'Potencia (12 ** 2): {12 ** 2}')
print()
print()


print('###### OPERADORES_RELACIONALES  ######')
print(f'Mayor que (12 > 2): {12 > 2}')
print(f'Mayor o igual que (12 >= 12): {12 >= 12}')
print(f'Menor que (2 < 2): {2 < 2}')
print(f'Menor o igual que (5 <= 5): {5 <= 5}')
print(f'Igual que (3 == "3"): {3 == "3"}')
print(f'Diferente que (1 != "1"): {1 != "1"}')
print()
print()


print('######  OPERADORES_DE_ASIGNACIÓN  ######')
a = 10
print(f'Asignación (a = 10): {a}')
a += 7
print(f'Suma y asignación (a += 7): {a}')
a -= 7
print(f'Resta y asignación (a -= 7): {a}')
a *= 7
print(f'Multiplicación y asignación (a *= 7): {a}')
a /= 7
print(f'División y asignación (a /= 7): {a}')
a //= 7
print(f'División de resultado entero y asignación (a /= 7): {a}')
a %= 7
print(f'Modulo y asignación (a %= 7): {a}')
a **= 7
print(f'Potencia y asignación (a **= 7): {a}')
print()
print()


print('######  OPERADORES_LOGICOS  ######')
a = False
b = True
print(f'And: {a and b}')
print(f'Or: {a or b}')
print(f'Not: {not b}')
print()
print()


print('######  OPERADORES_PERTENENCIA  ######')
numeros = [1, 2, 3, 4, 5, 6]
print(f'In: {2 in numeros}')
print(f'not in: {10 not in numeros}')
print()
print()


print('######  OPERADORES_IDENTIDAD  ######')
num1 = 1
num2 = 1
num3 = 2
print(f'Is: {num1 is num2}')
print(f'Is not: {num1 is not num2}')
print()
print()


print('######  CONDICIONALES  ######')
numeros = random.randint(-10, 10)
print('Condicional if else:')
if numeros > 0:
    print(f'El número {numeros} es positivo')
else:
    print(f'El número {numeros} es negativo')
print()
print()

print('######  CICLOS  ######')
print('Ciclo For:')
lenguajes = ['Python', 'PHP', 'Java', 'Ruby']
for lenguaje in lenguajes:
    print(lenguaje)

print('Ciclo While:')
contador = 0
while contador <= 10:
    print(f'Iteración {contador}')
    contador += 1

print('Excepción:')
try:
    edad = int(input('Digite su edad (en números): '))
    print(f'Su edad es {edad}')
except ValueError:
    print('Debe ingresar solo valores númericos')

print()
print()

print('######  EXTRA  ######')
for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)

