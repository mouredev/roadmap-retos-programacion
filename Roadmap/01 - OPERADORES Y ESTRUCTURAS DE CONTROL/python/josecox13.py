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


#Aritméticos
print('\n-----Operadores aritméticos-----')
print (f'Suma: 1 + 4 = {1+4}')
print(f'Resta: 4 - 1 = {4-1}')
print(f'Multiplicación: 4 * 3 = {4*3}')
print(f'Division: 12 / 3 = {12/3}')
print(f'Potencia: 4 ** 3 = {4**3}')
print(f'Resto: 5 % 3 = {5%31}')
print(f'Parte entera: 7 // 3 = {7//3}')


#Lógicos
print('\n-----Operadores de comparación-----')
print(f'Mayor que: 5 > 3 -> {5>3}')
print(f'Mayor o igual que: 5 >= 3 -> {5>=3}')
print(f'Menor que: 6 < 3 -> {6<3}')
print(f'Menor o igual que: 6<= 6 -> {6<=6}')
print(f'Igual que: 6 == 3 -> {6==3}')
print(f'Distinto de: 6 != 3 -> {6!=3}')


#A nivel de bit
print('\n-----Operadores a nivel de bit-----')
print (f'AND bitwise: 5 & 3 = {5&3}')
print(f'OR bitwsie: 5 | 3 = {5|3}')
print(f'Negación bitwise: ~3 = {~3}')
print(f'XOR bitwsie 5 ^ 3 = {5^3}')
print(f'Desplazamiento hacia la izquierda 1 posición: 5 << 1 = {5<<1}')
print(f'Desplazamiento hacia la derecha 3 posiciones: 56 >> 3 = {56>>3}')


#Pertenencia
print('\n-----Operadores de pertenencia-----')
lista = [1,2,3]
print('lista = [1,2,3]')
print(f'Pertenencia a lista: 5 in lista = {5 in lista}')
print(f'No pertenencia a lista: 7 not in lista = {7 not in lista}')
1 in lista #pertenencia a la lista: Devolverá True
2 not in lista #no pertenece a la lista: Devolveerá False

#Asignación
print('\n-----Operadores de asignación-----')
x = 873
print(f'Asignación: x = 6873-> {x}')
x += 5
print(f'Asignación con suma: x += 5 -> {x}')
x -= 5
print(f'Asignación con resta: x -= 5 -> {x}')
x *= 2
print(f'Asignación con multiplicación: x *= 2 -> {x}')
x /= 2
print(f'Asignación con división: x /= 2 -> {x}')
x %= 46
print(f'Asignación con resto: x %= 46 -> {x}')
x //= 6
print(f'Asignación con parte entera: x //= 2 -> {x}')
x **= 4
print(f'Asignación con parte entera: x **= 2 -> {x}')


#Operadores de identidad
print('\n-----Operadores de identidad-----')
print('is : Devuelve true si los operandos se refieren al mismo objeto') 
print('is not: Devuelve true si los operandos no se refieren al mismo objeto')
x = 6
y = 9
z = 9
print('x = 6 \ny = 9 \nz = 9')
print(f'x is z -> {x is z}')
print(f'y is z -> {y is z}')
print(f'y is not z -> {y is not z}')
print(f'x is not  z -> {x is not z}')


#Operadores de lógicos
print('\n-----Operadores lógicos-----')
print(f'AND: 5 + 2 == 7 and 8 * 3 == 15 -> {5+2==7 and 8*3 == 15}')
print(f'OR: 5 + 2 == 7 or 8 * 3 == 15 -> {5+2==7 or 8*3 == 15}')
print(f'NOT: not 5 + 2 == 7 -> {not 5+2==7}')


#Estructuras de control
print('\n-----Estructuras de control-----')
print('1- Condicionales')
x = 3
if x ==5:
    print('x es 5')
elif x %2 == 0:
    print('x es divisible entre 2')
else:
    print('x no es 5 ni divisible entre 2')

print('2- Bucle for')
for i in range(6):
    print(i)

print('3- Bucle while')
x = 0
while x < 4:
    print(x)
    x += 1

#Manejo de excepciones
print('\n-----Manejo de excepciones-----')
try:
    print(6/2)
except:
    print('No se pudo realizar la división')
finally:
    print('Se terminó el tratamiento de excepciones')

print("\n======== DIFICULTAD EXTRA ========")
for i in range(10,56):
    if i%2 ==0 and i%3 == 0 and i != 16:
        print (i)
