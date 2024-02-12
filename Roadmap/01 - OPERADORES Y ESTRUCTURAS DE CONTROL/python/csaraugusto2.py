#01 OPERADORES Y ESTRUCTURAS DE CONTROL

# Ejercicios

# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:

# ARITMETICOS

print('\nOperaciones Aritmeticas\n')
print('----------------------------Inicio-------------------------------------\n')
# Suma (+)
n1 = 5
n2 = 3

suma = n1 + n2

print(f'Suma: {n1} + {n2} = {suma}\n')

# Resta (-)

resta = n1 - n2

print(f'Resta: {n1} - {n2} = {resta}\n')

# multiplicacion (*)

mult = n1 * n2

print(f'Multiplicacion: {n1} x {n2} = {mult}\n')

# Division (/)

div = n1 / n2

print(f'Division: {n1} / {n2} = {div}\n')

# Modulo (%)

modulo = n1 % n2

print(f'Residuo: {n1} % {n2} = {modulo}\n')

# Potencia (**)

potencia = n1 ** n2

print(f'Potencia: {n1}^{n2} = {potencia}\n')

# Cociente (//)

cociente = n1 // n2

print(f'Cociente: {n1} // {n2} = {cociente}\n')

print('----------------------------Fin----------------------------------------\n')

# Concatenacion de cadenas de caracteres
print('Concatenacion de cadenas de caracteres\n')

print('----------------------------Inicio-------------------------------------\n')

c1 = 'Hola'
c2 = 'Pyton'

concat = 'Unimos esta frase para decir: "' + c1 + ' ' + c2 + '"'
print(f'Concatenaremos una frase con: ({c1}) y ({c2}) en la linea siguente:')
print(concat,'\n')

print('----------------------------Fin----------------------------------------\n')

# Logicos (and, or, not) y Booleanos (true/False)

A = True
B = False
print(f'Manejo de los Operadores logicos con resultados Booleanos {A} y {B}\n')
print('----------------------------Inicio-------------------------------------\n')

resultado = A and B #Falso
print(f'AND: {A} Y {B} = {resultado}') 

resultado = A or B #Verdadero
print(f'OR: {A} O {B} = {resultado}')

resultado = not B # Cambia Falso por Verdadero
print(f'NOT: NO {B} = {resultado}\n') # Cambia Verdadero por Falso

print('----------------------------Fin----------------------------------------\n')

# Operadores de Comparacion ( mayor > , mayor o igual >= , menor < , menor o igual <= , igual ==)

print('Operadores de Comparacion\n')
print('----------------------------Inicio-------------------------------------\n')

resultado = n1 < n2
print(f'{n1} es menor a {n2} ? --> {resultado}')

resultado = n1 <= n2
print(f'{n1} es menor o igual a {n2} ? --> {resultado}')

resultado = n1 == n2
print(f'{n1} es igual a {n2} ? --> {resultado}')

resultado = n1 >= n2
print(f'{n1} es mayor o igual a {n2} ? --> {resultado}')

resultado = n1 > n2
print(f'{n1} es mayor a {n2} ? --> {resultado}\n')

print('----------------------------Fin----------------------------------------\n')

# Operadores de asignacion (=)
print('Operadores de asignacion\n')
print('----------------------------Inicio-------------------------------------\n')

concat = 'Aqui estamos asignando esta cadena de caracteres a la variable "concat" para luego mostrarla en el print'
print(concat,'\n')

print('----------------------------Fin----------------------------------------\n')

# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:

print('Ejemplos de operaciones con estructuras de control\n')

# Condicionales
print('Condicionales if/elif/else\n')
print('----------------------------Inicio-------------------------------------\n')

print(f'Si {n1} es menor a {n2} mostrar la suma de ambos, sino mostrar la resta')
if n1 < n2:
    p = n1 + n2
    print(f'La suma es: {n1} + {n2} = {p}\n')
elif n1 > n2:
    p = n1 - n2
    print(f'La resta es: {n1} - {n2} = {p}\n')

print('----------------------------Fin----------------------------------------\n')

# Iterativas
print('Iteraciones con Wile y For\n')

i = 0
# Wile
print('iteracion de 1 a 5 con Wile\n')
print('----------------------------Inicio-------------------------------------\n')

while i != n1:
    i += 1
    print(i)

print('----------------------------Fin----------------------------------------\n')

# For

print('5 iteraciones de solo numero pares con For\n')
print('----------------------------Inicio-------------------------------------\n')
for i in range(5):
    i *= 2
    print(i)

print('----------------------------Fin----------------------------------------\n')

# Excepciones
print('Excepciones\n')
print('----------------------------Inicio-------------------------------------\n')

var1 = 5
var2 = "Cinco"

print(f'Intentamos sumar ({var1} + {var2}) y capturaremos el error')

try:
    resultado = var1 + var2
except Exception as ex:
    print(f'Ha ocurrido un error: {ex}')

print('\n----------------------------Fin----------------------------------------\n')




# Dificultad extra
'''    
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''
print('Ejercicio adicional propuesto como Dificultad Extra\n')
print('----------------------------Inicio-------------------------------------\n')

print('Números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3')

for i in range(10,55):
    if i != 16 and i % 2 == 0 and i % 3 != 0:
        print(i)

print('----------------------------Fin----------------------------------------\n')
