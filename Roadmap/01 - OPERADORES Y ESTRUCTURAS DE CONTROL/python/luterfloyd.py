'''
  EJERCICIO:
  - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
  - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
  - Debes hacer print por consola del resultado de todos los ejemplos.
 
  DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''


print('\nOPERADOR DE ASIGNACION SIMPLE (=)') 
numero1 = 2 
numero2 = 3
lista_pares = [2,4,6]

texto1 = 'manzana'
texto2 = 'pera'
lista_frutas = ['pera','mango','platano','melon','guanabana','guayaba','patilla']

print(f'numero1 = {numero1}')
print(f'numero2 = {numero2}')
print(f'texto1 = {texto1}')
print(f'texto2 = {texto2}')

print('\nOPERADORES ARITMETICOS (+,-,*,/,%,**,//)')
print(f'suma:\t\t{numero1} + {numero2} = {numero1+numero2}')
print(f'resta:\t\t{numero2} - {numero1} = {numero2-numero1}')
print(f'multiplicacion:\t{numero1} * {numero2} = {numero1*numero2}')
print(f'division:\t{numero2} / {numero1} = {numero2/numero1}')
print(f'modulo:\t\t{numero2} % {numero1} = {numero2%numero1}')
print(f'potencia:\t{numero1} ** {numero2} = {numero1**numero2}')
print(f'div. entero:\t{numero2} // {numero1} = {numero2//numero1}')
print('concatenar texto con +\t-> mi fruta favorita es la ' + texto1)
print(f'repetir texto con *\t-> {texto1} * 3 =', texto1*3)

print('\nOPERADORES LOGICOS (and, or, not)')
print('a and b -> Si a se evalúa a falso, entonces devuelve a, si no devuelve b:' )
print(f'{numero1} and {numero2} -> {numero1 and numero2}')
print('a or b -> Si a se evalúa a falso, entonces devuelve b, si no devuelve a:' )
print(f'{numero1} or {numero2} -> {numero1 or numero2}')
print('not a -> Si a se evalúa a falso, entonces devuelve True, si no devuelve False:' )
print(f'not {numero2} -> {not numero2}')

print('\nOPERADORES DE COMPARACION (>,<,==,>=,<=,!=)')

print(f'mayor que:\t{numero1} > {numero2}  -> {numero1>numero2}')
print(f'menor que:\t{numero1} < {numero2}  -> {numero1<numero2}')
print(f'igual que:\t{numero1} == {numero2} -> {numero1==numero2}')
print(f'mayor-igual que:{numero2} >= {numero1} -> {numero1>=numero2}')
print(f'menor-igual:\t{numero2} <= {numero1} -> {numero1<=numero2}')
print(f'diferente que:\t{numero1} != {numero2} -> {numero1!=numero2}')

print('\nOPERADORES DE ASIGNACION (+=,-=,*=,/=,//=,**=)')
asignacion = numero2
asignacion += numero1
print(f'suma y asig.:\t\t{numero2} += {numero1} -> {asignacion}')
valor_anterior = asignacion
asignacion -= numero1
print(f'resta y asig.:\t\t{valor_anterior} += {numero1} -> {asignacion}')
valor_anterior = asignacion
asignacion *= numero1
print(f'multiplicacion y asig.:\t{valor_anterior} *= {numero1} -> {asignacion}')
valor_anterior = asignacion
asignacion /= numero1
print(f'division y asig.:\t{valor_anterior} /= {numero1} -> {asignacion}')
valor_anterior = asignacion
asignacion **= numero1
print(f'potenciacion y asig.:\t{valor_anterior} **= {numero1} -> {asignacion}')

print('\nOPERADORES DE IDENTIDAD (is, is not)')
print(f'{numero1} is {numero2}\t\t-> {numero1 is numero2}')
print(f'{texto1} is {texto2}\t-> {texto1 is texto2}')
print(f'{numero1} is {lista_pares}\t-> {numero1 is lista_pares}')
print(f'{numero2} is {numero2}\t\t-> {numero2 is numero2}')
print(f'{numero1} is not {numero2}\t-> {numero1 is not numero2}')

print('\nOPERADORES DE PERTENENCIA (in -> para comprobar si existe en una secuencia)')
print(f'{numero1} in {lista_pares} -> {numero1 in lista_pares}')
print(f'{numero2} in {lista_pares} -> {numero2 in lista_pares}')
print(f'{texto1}\tin {lista_frutas} -> {texto1 in lista_frutas}')
print(f'{texto2}\tin {lista_frutas} -> {texto2 in lista_frutas}')

print('\nOPERADORES BIT A BIT (&,|,^,>>,<<)')
print(f'AND:\t\t{numero1} & {numero2} = {numero1&numero2}')
print(f'OR:\t\t{numero1} | {numero2} = {numero1|numero2}')
print(f'XOR:\t\t{numero1} ^ {numero2} = {numero1^numero2}')
print(f'desplaz. der.:\t{numero1} >> {numero2} = {numero1>>numero2}')
print(f'desplaz. izq.:\t{numero1} << {numero2} = {numero1<<numero2}')

print('\nESTRUCTURAL DE CONTROL:')
print('* condicionales (if-elif-else/ while)')
if numero1 > numero2:
    print(f'{numero1} es mayor que {numero2}')
elif numero1 < numero2:
        print(f'{numero1} es menor que {numero2}')
else:
      print(f'{numero1} es igual a {numero2}')

print('\n* (while)')
contador = 0
while contador < 40:
      print(contador,'*'*contador)
      contador += numero1**numero2
      if contador==32:
            print ('ciclo interrumpido (break)')
            break
      else:
           continue
else:
      print('final sin interrupcion')
print(f'valor de la variable :',contador)

print('\n* iterables (for)')
print('lista de frutas (segun lista_pares):')
for numero in lista_pares:
     print(lista_frutas[numero])

print('\n*for - range')
for numero in range(1,11):
  print(numero)

print('\nPRUEBA EXTRA: numeros pares entre 10 y 55 (incluidos) que no sean 16, ni multiplos 3')
for numero in range(10,56):
    if numero!=16 and numero%3 and not numero%2:
      print (numero)







