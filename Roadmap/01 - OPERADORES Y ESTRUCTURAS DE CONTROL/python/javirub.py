'''
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
'''

#Operadores aritméticos
def arithmetic(a, b):
    print(f'La suma de {a} + {b} es {a + b}')
    print(f'La resta de {a} - {b} es {a - b}')
    print(f'La multiplicación de {a} * {b} es {a * b}')
    print(f'La división de {a} / {b} es {a / b}')
    print(f'El módulo entre {a} y {b} es {a % b}')
    print(f'El resultado de {a}^{b} es {a ** b}')
    print(f'La división entera de {a} y {b} es {a // b}')
print('Probando función de operadores aritmeticos:')
arithmetic(5, 12)
print()

#Operadores lógicos
def logic(a, b, c):
    if a > c and b > c: print(f'{a} y {b} son mayores que {c}')
    elif a > c or b > c: print(f'{a} o {b} es mayor que {c}')
    elif not a > c and not b > c: print(f'{a} y {b} son menores que {c}')

print('Probando la función de operadores lógicos:')
logic(10, 12, 6)
logic(10, 12, 11)
logic(10, 12, 20)
print()

#Operadores de comparación
def comparison(a,b):
    if a == b: print(f'{a} es igual a {b}')
    if a != b: print(f'{a} es distinto a {b}')
    if a > b: print(f'{a} es mayor que {b}')
    if a < b: print(f'{a} es menor que {b}')
    if a >= b: print(f'{a} es mayor o igual que {b}')
    if a <= b: print(f'{a} es menor o igual que {b}')

print('Probando la función de operadores de comparación:')
comparison(16, 12)
comparison(16,16)
comparison(12, 16)
print()

#Operadores de asignación
def assignment(a,b,symbol):
    if symbol == '=': result = b
    if symbol =='+=': result = a + b
    if symbol =='-=': result = a - b
    if symbol =='*=': result = a * b
    if symbol =='/=': result = a / b
    if symbol == '%=': result = a % b
    if symbol == '//=': result = a // b
    if symbol == '**=': result = a ** b
    if symbol == '&=': result = a & b
    if symbol == '|=': result = a | b
    if symbol == '^=': result = a ^ b
    if symbol == '>>=': result = a >> b
    if symbol == '<<=': result = a << b
    print(f'a {symbol} b; a = {result}')

print('Probando la función de operadores de asignación con a=5 y b=12:')
assignment(5, 12, '=')
assignment(5, 12, '+=')
assignment(5, 12, '-=')
assignment(5, 12, '*=')
assignment(5, 12, '/=')
assignment(5, 12, '%=')
assignment(5, 12, '//=')
assignment(5, 12, '**=')
assignment(5, 12, '&=')
assignment(5, 12, '|=')
assignment(5, 12, '^=')
assignment(5, 12, '>>=')
assignment(5, 12, '<<=')
print()

#Operadores de identidad
def identity(a,b):
    print(f'{a} es lo mismo que {b}? {a is b}')
    print(f'{a} es distinto a {b}? {a is not b}')

print('Probando la función de operadores de identidad:')
identity(1,1)
print()

#Operadores de pertenencia
def membership(a, b):
    print(f'{a} pertenece a {b}? {a in b}')
    print(f'{a} no pertenece a {b}? {a not in b}')

print('Probando la función de operadores de pertenencia:')
membership('platano', ['fresa', 'manzana', 'platano'])
membership('platano', ['fresa', 'manzana', 'banana'])
print()

#Operadores de bits
def bitwise(a, b, c=2):
    print(f'El operador & (AND), devuelve 1 en la posición donde ambos bits de los distintos valores son 1: {bin(a)} & {bin(b)} = {bin(a & b)}; {a} & {b} = {a & b}')
    print(f'El operador | (OR), devuelve 1 donde al menos uno de los dos bits de los distintos valores es 1: {bin(a)} | {bin(b)} = {bin(a | b)}; {a} | {b} = {a | b}')
    print(f'El operador ^ (XOR, exclusive or), devuelve 1 solo si uno de los dos valores es 1: {bin(a)} ^ {bin(b)} = {bin(a ^ b)}; {a} ^ {b} = {a ^ b}')
    print(f'El operador ~ (NOT), invierte todos los bits: ~{bin(a)} = {bin(~a)} ; ~{bin(b)} = {bin(~b)}; ~{a} = {~a}; ~{b} = {~b}')
    print(f'El operador << (Zero fill left shift), desplaza hacia la izquierda añadiendo 0 a la derecha y deja que los bits más a la izquierda caigan: {bin(a)} << {c} = {bin(a << c)}; {bin(b)} << {c} = {bin(b << c)}; {a} << {c} = {a << c}; {b} << {c} = {b << c}')
    print(f'El operador >> (Signed right shift), desplaza hacia la derecha añadiendo 0 a la izquierda y deja que los bits más a la derecha caigan: {bin(a)} >> {c} = {bin(a >> c)}; {bin(b)} >> {c} = {bin(b >> c)}; {a} >> {c} == {a >> c}; {b} >> {c} = {b >> c}')

print('Probando la función de operadores de bits:')
bitwise(28, 31)

print()

#Ejercicio opcional

print('Ejercicio opcional; Todos los números pares que no son multiples de 3 ni son el 16 entre 10 y 55 incluidos:')
for i in range(10, 55, 2):
    if (i != 16) & (i %3 != 0):
        print(i)
