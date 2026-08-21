'''
EJERCICIO:

1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes)

2. Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje:
Condicionales, iterativas, excepciones...

3. Debes hacer print por consola del resultado de todos los ejemplos.

DIFICULTAD EXTRA (opcional):

4.Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
'''

# EJERCICIO 1
var_1 = 17
var_2 = 5

print('** Operadores aristméticos **', end='\n\n')

print(f'var1 = {var_1}',f'var2 = {var_2}', sep='\n', end='\n\n')

print(f'Suma: var_1 + var_2 = {var_1 + var_2}')   
print(f'Resta: var_1 - var_2 = {var_1 - var_2}')
print(f'Multiplicación: var_1 * var_2 = {var_1 * var_2}')
print(f'División: var_1 / var_2 = {var_1 / var_2}')
print(f'División entera: var_1 // var_2 = {var_1 // var_2}') 
print(f'Módulo: var_1 % var_2 = {var_1 % var_2}') 
print(f'Exponenciación: var_1 ** var_2 = {var_1 ** var_2}')

print('\n** Operadores de comparación **', end='\n\n')

print(f'Igual "var_1 == var_2": {var_1 == var_2}')
print(f'Distinto "var_1 != var_2": {var_1 != var_2}')
print(f'Mayor que "var_1 > var_2": {var_1 > var_2}')
print(f'Menor que "var_1 < var_2": {var_1 < var_2}')
print(f'Mayor o igual que "var_1 >= var_2": {var_1 >= var_2}')
print(f'Menor o igual que "var_1 <= var_2": {var_1 <= var_2}')

print('\n** Operadores lógicos **', end='\n\n')
'''
En python los operadores lógicos se usan para combinar expresiones boleanas y suelen
usarse con operadores de comparación.
Not invierte el valor
'''
print('Operadores lógicos por orden de prioridad: Not, And (&) y Or (|)')

print('\n· NOT: invierte el valor del resultado boleano', end='\n'*2)

print(f'not(var_1 == 17 and var_1 > var_2): {not(var_1 == 17 and var_1 > var_2)}')
print(f'not(var_1 == 17 and var_1 < var_2): {not(var_1 == 17 and var_1 < var_2)}')

print('\n· AND: Solo devuelve true si todas las condiciones son verdaderas', end='\n'*2)

print(f'var_1 == 17 and var_1 > var_2: {var_1 == 17 and var_1 > var_2}')
print(f'var_1 == 17 and var_1 < var_2: {var_1 == 17 and var_1 < var_2}')

print('\n· OR: Devuelve true si al menos una de las condiciones es verdadera', end='\n'*2)

print(f'var_1 == 17 or var_1 < var_2: {var_1 == 17 or var_1 < var_2}')
print(f'var_1 < 17 or var_1 < var_2: {var_1 < 17 or var_1 < var_2}')

print('\n** Operadores de asignación o In-place **', end='\n\n')
'''
Los operadores de asignación son aquellos que realizan dos cosas en una misma instrucción.
1. Realizan una operación
2. Guardan en resultado en la misma variable
'''
print('valor de var_1 =',var_1, end='\n\n')

var_1 += 5
print('Suma var_1 += 5: nuevo valor de var_1 =', var_1) 
var_1 -= 5
print('Resta var_1 -= 5: nuevo valor de var_1 =', var_1)
var_1 *= 5
print(f'Multiplicación var_1 *= 5: nuevo valor de var_1 =', var_1)
var_1 /= 5
print(f'División var_1 /= : nuevo valor de var_1 =', var_1)
var_1 //= 5
print(f'División entera var_1 //= 5: nuevo valor de var_1 =', var_1) 
var_1 %= 5
print(f'Módulo var_1 %= 5: nuevo valor de var_1 =', var_1) 
var_1 **= 5
print(f'Exponenciación var_1 **= 5: nuevo valor de var_1 =', var_1)

print('\n** Operadores de identidad **', end='\n\n')

'''
Los operadores de identidad sirven para comprobar si dos variables apuntan exactamente al mismo objeto en la memoria.
La diferencia clave con '==' es que este compara el valor de los objetos. 
'''
a = [1,2,3]
b = [1,2,3]
c = a
d = None

print('\nLos operadores de identidad son "is" e "is not"', end='\n\n')

print(f'a = {a}')
print(f'b = {b}')
print(f'c = a')
print(f'd = {d}')
print()
print('a == b', a==b)
print('a is b', a is b)
print('a is c', a is c)
print()
print('a is not b', a is not b)
print('a is not c', a is not c)
print()
print('d is None', d is None)
print('d is not None', d is not None)
print('a is None', a is None)

print('\n** Operadores de bits **', end='\n\n')
'''
Los operadores bit modifican y comparan los números a nivel binario (bit a bit)
'''
print('Operador "&" (AND) devuelve 1 si ambos bits son 1')
print('Ejemplo: 10110 & 10011 =',bin(0b10110 & 0b10011), end='\n\n')
print('Operador "|" (OR) devuelve 1 si al menos uno de los bit es 1')
print('Ejemplo: 10110 | 10011 =',bin(0b10110 | 0b10011), end='\n\n')
print('Operador "^" (XOR) devuelve 1 si ambos bits son distintos')
print('Ejemplo: 10110 ^ 10011 =',bin(0b10110 ^ 0b10011))

print('\n** Operadores de pertenencia **', end='\n\n')

numbers = [1,2,3,4,5]
print('Teniendo una lista de números:', numbers)

print('El número 2 esta/pertenece a la lista numbers? 2 in numbers:',2 in numbers)
print('El número 2  no esta/ no pertenece a la lista numbers? 2 not in numbers:',2 not in numbers)

# EJERCICIO 2

print('\n** Estructuras de control **', end='\n\n')
print('Condicionales', end='\n\n')

print('Veamos si puedes conducir', end='\n\n')
edad = int(input('Introduce tu edad: '))
país = input('Introduce tu país: ') 
carnet = input('Tienes carnet de conducir (si/no): ')

if edad < 16 or carnet != 'si' :
    print('No puedes conducir')
elif 16 <= edad < 18 and país == 'Estados Unidos' and carnet == 'si':
    print('Solo puedes conducir en EE.UU')
elif edad >= 18 and carnet == 'si':
    print('Puedes conducir en todo el mundo')
else:
    print('Eso no es posible') 

print('\nIteraciones', end='\n\n')

print('Bucles For', end='\n\n')
paises = ['España','Portugal','Francia','Alemania','Suiza','Chipre','Italia']
print('Lista de paises:',paises)
paises_8 = []
for pais in paises:
    if len(pais) >= 8:
        paises_8.append(pais)
print(f'Paises con 8 ó más caracteres: {paises_8}')

# bucles while
password = 00000
while password != 1234:
    password = int(input('Introduce contraseña: '))
    if password == 1234:
        print('contraseña correcta')
        break
    else:
        print('Contraseña incorrecta. Intenta de nuevo')

print('\nExcepciones', end='\n\n')

try:
    edad = int(input('Introduce tu edad: '))
    if edad >= 18:
        print('Puedes pasar')
    else:
        print('Entrada prohibida')
except ValueError:
    print('La edad debe ser un número')
finally:
    print('siguiente')