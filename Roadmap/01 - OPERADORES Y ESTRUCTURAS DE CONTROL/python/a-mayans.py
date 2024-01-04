'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''

#---  OPERADORES  ---#

# Aritmeticos ( +, -, *, /, %, **, // )
operando_1 = 10
operando_2 = 7
print(f'Suma: {operando_1 + operando_2}')               # devuelve la suma
print(f'Resta: {operando_1 - operando_2}')              # devuelve la resta
print(f'Multiplicacion: {operando_1 * operando_2}')     # devulve la multiplicacion
print(f'Division: {operando_1 / operando_2}')           # devuelve el cociente (inclye decimales)
print(f'Modulo: {operando_1 % operando_2}')             # devuelve el resto/residuo
print(f'Potencia: {operando_1 ** operando_2}')          # devuelve el numero en potencia
print(f'Division entero: {operando_1 // operando_2}')   # devuelve el cociente entero


# Logicos ( para trabajar con valores de tipo bool ) -> AND, OR, NOT
print(True and True)        # devuelve True
print(True and False)       # devuelve False
print(True or False)        # devuelve True
print(not True)             # devuelve False
print(not False)            # devuelve True
print(not 0)                # cero es igual a False, entonces devuelve True
print(not 1)                # uno es igual a True, entonces devuelve False


# Comparacion ( >, <, ==, >=, <=, !=, ) -> devuelve un valor booleano
print(f'Mayor que: {operando_1 > operando_2}')              # devuelve True
print(f'Menor que: {operando_1 < operando_2}')              # devuelve False
print(f'Igual que: {operando_1 == operando_2}')             # devuelve False
print(f'Mayor o igual que: {operando_1 >= operando_2}')     # devuelve True
print(f'Menor o igual que: {operando_1 <= operando_2}')     # devuelve False
print(f'Distinto que: {operando_1 != operando_2}')          # devuelve True


# Asignacion ( =, +=, -=, *=, /=, %=, **=, //= ) -> asignar valores a una variable
a = 5
print(f'Variable a: {a}')
a += 10 # es lo mismo que a = a + 10
print(f'Sumando 10 a la variable a: {a}')
a -= 10 # es lo mismo que a = a - 10
print(f'Restando 10 a la variable a: {a}')
a *= 10 # es lo mismo que a = a * 10
print(f'Multiplicando 10 a la variable a: {a}')
a /= 10 # es lo mismo que a = a / 10
print(f'Dividiendo 10 a la variable a: {a}')
b = 45
b %= 10 # es lo mismo que a = a % 10
print(f'Modulo 10 a la variable b: {b}')
b **= 10
print(f'Potencia 10 a la variable b: {b}')
b //= 5
print(f'Division entera 10 a la variable b: {b}')


# Indentidad ( is, is not) -> comprobar si dos variables emplean la misma ubicacion en memoria
a = 3
b = 3
c = 4
print(a is b)               # devuelve True
print(a is not b)           # devuelve False
print( a is c)              # devuelve False
print( a is not c)          # devuelve True


# Pertenencia ( in, not it) -> para indicar pertenencia a alguna secuencia (listas, tuplas, strings)
lista = [1, 2, 3, 4, 5]
print(3 in lista)           # devuelve True
print(15 not in lista)      # devuelve True

string = 'Hola, que tal'
print('que' in string)      # devuelve True
print('de' in string)       # devuelve False
print('Ho' in string)       # devuelve True
print('ho' in string)       # devuelve False, distingue entre mayusculas y minusculas, es case sensitive



#---  ESTRUCTURAS DE CONTROL ( Condicionales, iterativas, excepciones... )  ---#

# CONDICIONAL
# If, elif, else ( controlar si se cumple 1 o varias condiciones -> utilizar operadores de comparacion y logicos)
total_compra = 120

if total_compra <= 100:
    print('Pago en efectivo')
elif total_compra > 100 and total_compra < 500:
    print('Pago con targeta de debito')
else:
    print('Pago con targeta de credito')


# ITERATIVA
# While ( ejecuta una misma accion mientras una condicion se cumpla. Dejara de ejecutarse cuando la condicion se incumpla)
numero = 0
while numero <= 10:
    print(numero)
    numero += 1


# For ( permite iterar sobre una variable compleja - Listas o Tuplas)
tupla = ('verde', 'rojo', 'amarillo', 'azul', 'naranja')
for color in tupla:
    print(color)


# EXCEPCION
while True:
    # control de la excepcion
    try:
        number = int(input('Inserta un numero: '))
        break # si introduce un valor valido termina la ejecucion
    
    # si no introduce un valor valido, devuelve el error controlado
    except ValueError:
        print('Error! No ha insertado un valor valido. Intentelo de nuevo')


#---  Reto Extra  ---#
# Iterando con un bucle For sobre el rango, y utilizando el condicional If con operadores de comparacion
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
