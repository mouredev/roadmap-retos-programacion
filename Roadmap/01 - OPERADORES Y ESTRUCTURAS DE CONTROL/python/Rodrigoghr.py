# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
#### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

## Ejercicio

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
# Números
numero_1 = 2
numero_2 = 10

# OPERADORES:
' Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits... '
print('Operadores Aritméticos')
print(f'\tSuma: {numero_1} + {numero_2} = {numero_1 + numero_2}')
print(f'\tResta: {numero_1} - {numero_2} = {numero_1 - numero_2}')
print(f'\tMultiplicación: {numero_1} * {numero_2} = {numero_1 * numero_2}')
print(f'\tDivision: {numero_1} / {numero_2} = {numero_1 / numero_2}')
print(f'\tDivision Entera: {numero_1} // {numero_2} = {numero_1 // numero_2}')
print(f'\tResto: {numero_2} % {numero_1} = {numero_2 % numero_1}')
print(f'\tPotencia: {numero_1} ** {numero_2} = {numero_1 ** numero_2}')

print('\n\nOperadores Lógicos')
print('\tAND: True and True = ', True and True)
print('\tOR: True or True = ', True or True)
print('\tNOT: not True =', not True)

print('\n\nOperadores de Asignación')
variable = 58
print(f'\t=  Asigna valor a una variable: variable = {variable}')
variable += 4
print(f'\t+= Incrementa el valor de la variable en {4}: variable += {4} --> variable = {variable}')
variable -= 5
print(f'\t-= Decrementa el valor de la variable en {5}: variable -= {5} --> variable = {variable}')
variable *= 2
print(f'\t*= Multiplica el valor de la variable por {2}: variable *= {2} --> variable = {variable}')
variable /= 3
print(f'\t/= Divide el valor de la variable por {3}: variable /= {3} --> variable = {variable}')
variable = int(variable)
variable %= 13
print(f'\t%= Resto o modulo del valor de la variable por {13}: variable %= {13} --> variable = {variable}')
variable //= 2
print(f'\t//= División entera del valor de la variable por {2}: variable //= {2} --> variable = {variable}')
variable **= 2
print(f'\t**= Eleva la variable al exponente {2}: variable **= {2} --> variable = {variable}')

print('\n\nOperadores Relacionales')
x, y = 5, 8
print(f'\t{x} == {y} =', x==y)
print(f'\t{x} != {y} =', x!=y)
print(f'\t{x} >  {y} =', x>y) 
print(f'\t{x} <  {y} =', x<y) 
print(f'\t{x} >= {y} =', x>=y)
print(f'\t{x} <= {y} =', x<=y)


print('\n\nOperadores de Identidad')
print('\tEl operador "is" comprueba si dos variables hacen referencia a el mismo objeto')
id1, id2 = 10, 20
print(f'\t{id1} is {id2} = {id1 is id2}')
id1, id2 = 10, 10
print(f'\t{id1} is {id2} = {id1 is id2}')
print('\tEl operador "is not" comprueba si dos variables no hacen referencia a el mismo objeto')
id1, id2 = 10, 20
print(f'\t{id1} is {id2} = {id1 is id2}')
id1, id2 = 10, 10
print(f'\t{id1} is {id2} = {id1 is id2}')


print('\n\nOperadores de Pertenencia')
print('Los operadores "in" y "not in" nos indican si un elemento esta o no contenido en una secuencia (lista, string, etc)')
numeros = [13, 17, 15]
print(f'\tLista numeros: {numeros}')
print(f'\tComprobamos si 14 está contenido en la lista de numeros: 14 in {numeros} = {14 in numeros}')
print(f'\tComprobamos si 17 está contenido en la lista de numeros: 17 in {numeros} = {17 in numeros}')
print(f'\tComprobamos si 18 no está contenido en la lista de numeros: 18 not in {numeros} = {18 not in numeros}')
print(f'\tComprobamos si 13 no está contenido en la lista de numeros: 13 not in {numeros} = {13 not in numeros}')
frase = 'Hola mundo'
print(f'\tComprobamos si "Hola" está contenido en "{frase}": "Hola" in "{frase}" = {"Hola" in frase}')

print('\n\nOperadores Bits')
x, y = 5, 3
print(f'\tAND: {x} & {y} es {x & y}') 
print(f'\tOR : {x} | {y} es {x | y}') 
print(f'\tNOT: {x} es {~x}') 
print(f'\tXOR: {x} ^ {y} es {x ^ y}') 
print(f'\tDesplazamiento a la derecha  : {x} >> {y} es {x >> y}') 
print(f'\tDesplazamiento a la izquierda: {x} << {y} es {x << y}') 

# ESTRUCTURAS DE CONTROL
' Condicionales, iterativas, excepciones...'
print('\nCondicionales:')
print('if - else:')
numero = 25
if numero % 2 == 0:
    print('\tNúmero Par')
else:
    print('\tNúmero Impar')
print('\nIterativos:')
print('1. for:')
frutas = ['pera','manzana','naranja','fresa']
print('\tLista de frutas: ')
for fruta in frutas:
    print(f'\t\t{fruta}')

print('2. while:')
intentos = 1
while intentos <= 5:
    print(f'\tIntento {intentos}')
    intentos += 1

print('\nExcepciones:')
while True:
    # Control excepcion
    try:
        number = int(input('\tInserta un numero: '))
        break # Si el valor es válido (número) finaliza la ejecucion
    
    # Si el valor es invalido (diferente a un número) --> devuelve el error controlado
    except ValueError:
        print('\tError! Valor inválido. Inténtelo de nuevo')
        
# DIFICULTAD EXTRA (opcional):
'''
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''
for numero in range(10,56,2):
    if numero != 16 and numero % 3 != 0:
        print(numero)
