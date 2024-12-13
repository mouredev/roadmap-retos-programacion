# /*
#  * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

# Aritméticos
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(3 / 2)
print(3 // 2)
print(2 % 2)
print(2 ** 2)

# lógicos
print(True and True)
print(True or True)
print(not True)

# comparación
print(2 == 2)
print(2 != 2)
print(2 > 2)
print(2 < 2)
print(2 >= 2)
print(2 <= 2)

# asignación
a = 2
print(a)
a += 2
print(a)
a *= 2
print(a)
a **= 2
print(a)
a -= 2
print(a)
a /= 2
print(a)
a //= 2
print(a)
a %= 2
print(a)
if test := 5 + 5:
    print(test)

dicc = {'test': 2}
dicc2 = dicc

# identidad
print(dicc is dicc2)

# pertenencia
print('test' in dicc2)

# bits
a = 0b1010
b = 0b1101

print(~15)
print(~(-15))
print(a & b)
print(a | b)
print(a ^ b)

print(2 << 4)
print(21 >> 4)

#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.

print('\n=== if-elif-else ===\n')


def if_elif_else(value):
    if value == 1:
        print('IF')
    elif value == 2:
        print('ELIF1')
    elif value == 3:
        print('ELIF2')
    else:
        print('ELSE')


if_elif_else(1)
if_elif_else(2)
if_elif_else(3)
if_elif_else(0)

print('\n=== while-else ===\n')


def while_else(iterations_number):
    count = 1
    while count < iterations_number:
        print(f'while iteration {count}.')
        if count == 4:
            print('The iterations stop for a break sentence.')
            break
        count += 1
    else:
        print('This is a print from else related with a while.')


while_else(3)
while_else(5)

print('\n=== for-else ===\n')


def for_else(iterations_number):
    for val in range(iterations_number):
        print(f'for iteration {val}.')
        if val == 4:
            print('The iterations stop for a break sentence.')
            break
    else:
        print('This is a print from else related with a for.')


for_else(3)
for_else(5)

print('\n=== match ===\n')


def show_match(value):
    match value:
        case 1:
            print('case 1')
        case 2:
            print('case 2')
        case _:
            print('default case')


show_match(1)
show_match(2)
show_match(3)

print('\n=== try-except-else-finally ===\n')


def try_except_else_finally(value):
    try:
        print('try')
        division = 5 / value
        if division == 1:
            return 'return value from try'
    except ZeroDivisionError as error:
        print('except ZeroDivisionError', error)
        return 'return value from except ZeroDivisionError'
    except Exception as error:
        print('except Exception', error)
        return 'return value from except Exception'
    else:
        print('else from try')
        return 'return value from else'
    finally:
        print('finally')
        return 'return value from finally'


result = try_except_else_finally(5)
print(result)
result = try_except_else_finally(6)
print(result)
result = try_except_else_finally(0)
print(result)
result = try_except_else_finally('a')
print(result)


print('\n=== Dificultad extra ===\n')
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for num in (x for x in range(10, 55, 2) if not (x == 16 or x % 3 == 0)):
    print(num)

#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#  */
