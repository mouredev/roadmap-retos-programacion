'''/
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
'''
Operadores
'''
#Operadores aritmeticos
print(f'La suma de 10+3 = {10+3}')
print(f'La resta de 10-3 = {10-3}')
print(f'El producto de 10*3 = {10*3}')
print(f'La división de 10+3 = {10/3}')
print(f'La modulo de 10%3 = {10%3}')
print(f'La potencia de 10**3 = {10**3}')
print(f'La división entenra de 10//3 = {10//3}')

#Operadores comparativos
print(f'Igualdad: 10 == 3 es {10==3}')
print(f'Desigualdad: 10 != 3 es {10!=3}')
print(f'Mayor que: 10 > 3 es {10>3}')
print(f'Menor que: 10 < 3 es {10<3}')
print(f'Mayor o igual a que: 10 >= 3 es {10>=3}')
print(f'Menor o igual a que: 10 <= 3 es {10<=3}')

#Operadores lógicos
#Aquí aroja un resultado True+True que nos das True
print(f'AND &&: 10 + 3 == 13 and 5 - 1 == 4 {10 + 3 == 13 and 5 - 1 == 4}')
#Or se deben cumplir una de las dos condiciones que sea true para que sea true
print(f'AND ||: 10 + 3 == 13 or 5 - 1 == 4 {10 + 3 == 13 or 5 - 1 == 4}')
#Not, se cumple la condición si ese no es.
print(f'NOT !: 10 + 3 == 14 {not 10 + 3 == 14}')


#Operadores de asigancion

number = 11 #asignación
print(number)
number += 5 #suma y asignación 
print(number)
number -1 #resta y asignación
print(number)
number *1 #producto y asignación
print(number)
number /= 3 #división y asignación
print(number)
number **=2 # Exponenete y asignación
print(number)
number //=2 #División entera y asignación
print(number)
number %= 3 #modulo y asinación


#Operadores de identidad
#Nos sirven para comparar el valor de la posición de memoria

my_number = 1.0
print(f'my_number es number es {my_number is number}') # falsoCada uno tiene una identidad de memoria diferente
#Si cambio my_number = number, nos dará true


#Operadores de pertenencia
print(f'"u" in "moure" = {"u" in "moure"}')
print(f'"u" not in "moure" = {"u" not in "moure"}')

#Operadores de bit
a = 10 # 1010, el 10 se representa en binario así
b = 3 # 11, el 3 se representan como 11 en binario

print(f'AND: 10 & 3 ={10&3}')#0010
print(f'OR: 10 | 3 ={10|3}')#0010
print(f'XOR: 10 ^ 3 ={10^3}')#0010
#print(f'NOT: 10 ~3 ={10~3}')#0010
print(f'Desplazamiento a la derecha: 10 >> 2 = {10>>2}')
print(f'Desplazamiento a la derecha: 10 << 2 = {10<<2}')


'''
Estructuras de control
'''

# Condicionales

my_string = 'Joseph'

if my_string == 'Joseph':
    print('my_string es "Joseph"')
elif my_string == 'Faster':
    print('my_string es "Faster"')
else:
    print('my_string no "Joseph"')


#Iterativas

for i in range(11):
    print(i)


i = 0

while i <= 10:
    print(i)
    i += 1

#manejo de excepciones
try:
    print(10/0)
except:
    print('Se ha producido un error')
finally:
    print('Se ha finalizado la esepción')


#EXTRA
print("Números entre 10 y 55 que son pares y no son ni 16 ni múltiplos de 3:")
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)















