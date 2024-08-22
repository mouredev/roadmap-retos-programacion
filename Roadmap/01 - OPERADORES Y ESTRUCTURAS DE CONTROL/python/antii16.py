'''
Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
'''
# OPERADORES
# Aritméticos
n1 = 10
n2 = 2
print('ARITMÉTICOS')
print(f'Suma -> 2+10= {n2+n1}')
print(f'Resta -> 10-2= {n1-n2}')
print(f'Multiplicación -> 2*10= {n2*n1}')
print(f'División -> 10/2= {n1/n2}')
print(f'Módulo -> 10%2= {n1%n2}')
print(f'Potencia -> 10**2= {n1**n2}')
print(f'División con número entero -> 10//2= {n1//n2}')

# Lógicos
print('')
print('LÓGICOS')
print(f'AND -> {n1==10 and n2==10}')
print(f'OR -> {n1==10 or n2==10}')
print(f'NOT -> {not n1==10}')

# Comparación
print('')
print('COMPARACIÓN')
print(f'10>2 -> {n1>n2}')
print(f'10<2 -> {n1<n2}')
print(f'10>=2 -> {n1>=n2}')
print(f'10<=2 -> {n1<=n2}')
print(f'10!=2 -> {n1!=n2}')

# Asignación
print('')
print('ASIGNACIÓN')
n1 += n2
print(f'n1 += n2 -> {n1}')
n1 -= n2
print(f'n1 -= n2 -> {n1}')
n1 *= n2
print(f'n1 *= n2 -> {n1}')
n1 /= n2
print(f'n1 /= n2 -> {n1}')
n1 %= 4
print(f'n1 %= n2 -> {n1}')
n1 //= n2
print(f'n1 //= n2 -> {n1}')
n1 **= n2
print(f'n1 **= n2 -> {n1}')

# Identidad
print('')
print('IDENTIDAD')
print(f'n1 is n2 -> {n1 is n2}')
print(f'n1 is not n2 -> {n1 is not n2}')

# Pertenencia
frase = 'Hola, Mundo'
palabra = 'Mundo'
print(f'¿"{palabra}" está en "{frase}" ? {palabra in frase}')

# A nivel de bits
print('')
print('A NIVEL DE BITS')
x = 4 #0100
y = 2 #0010
print(f'& -> x & y = {x&y}')
print(f'| -> x | y = {x|y}')
print(f'~ -> x ~ y = {~y}')
print(f'^ -> x ^ y = {x^y}')
print(f'>> -> x >> y = {x>>y}')
print(f'<< -> x << y = {x<<y}')

'''
Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
Condicionales, iterativas, excepciones...
'''
# Condicionales
print('')
print('CONDICIONALES')

color = 'amarillo'
if color == 'azul':
    print('El color es azul')
elif color == 'rojo':
    print('Pues a lo mejor es de color rojo')
else:
    print('No queda otra, el color es amarillo')

# Iterativas
print('')
print('ITERATIVAS')
print('WHILE')
n = 0
while n != 5:
    print(n)
    n+=1

print('')
print('FOR')
nombre = 'Lolito'
for letra in nombre:
    print(letra)

print('')
print('range(fin)')
for i in range(10):
    print(i)
print('range(inicio, fin)')
for i in range(5,10):
    print(i)
print('range(inicio, fin, salto)')
for i in range(1,20, 2):
    print(i)


# EXCEPCIONES
print('')
print('EXCEPCIONES')
a = 4
b = 0

try: 
    a/b
except ZeroDivisionError:
    print('No se puede dividir por 0')
finally:
    print('Fin')

'''
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''

# DIFICULTAD EXTRA
print('')
print('DIFICULTAD EXTRA')
for n in range(10, 56):
    if n%2 == 0 and n != 16 and n%3 != 0:
        print(n)