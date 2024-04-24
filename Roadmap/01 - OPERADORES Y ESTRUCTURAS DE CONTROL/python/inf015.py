#EJERCICIO:
#1 - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...(Ten en cuenta que cada lenguaje puede poseer unos diferentes)


#Operadores Aritméticos:
num1 = 5
num2 = 15

#Suma: +
print(f'Suma de {num1} + {num2} = {num1 + num2}')

#Resta: -
print(f'Resta de {num1} - {num2} = {num1 - num2}')

#Multiplicación: *
print(f'Multiplicacion de {num2} * {num1} = {num2 * num1}')

#División: /
print(f'Division de {num2} / {num1} = {num2 / num1}')

#División entera: //
print(f'Division de {num2} // {num1} = {num2 // num1}')

#Módulo (resto de la división): %
print(f'Modulo de {num2} / {num1} = {num2 % num1}')

#Potenciación: **
print(f'Potencia de {num2} ** {num1} = {num2 ** num1}')

#Operadores de Comparación (Relacionales):
#Igual a: ==
print(f'Es igual  {num2} y {num1}?:  {num2 == num1}')

#No igual a: !=
print(f'Es diferente  {num2} y {num1}?:  {num2 != num1}')

#Mayor que: >
print(f'Es mayor  {num2} que {num1}?:  {num2 > num1}')

#Menor que: <
print(f'Es menor  {num2} que {num1}?:  {num2 < num1}')

#Mayor o igual que: >=
print(f'Es mayor o igual {num2} que {num1}?:  {num2 > num1}')

#Menor o igual que: <=
print(f'Es menor o igual {num2} que {num1}?:  {num2 < num1}')

#Operadores Lógicos:
x = True
y = False

#Y lógico: and
and_result = x and y
print(f"AND: {and_result}")

#O lógico: or
or_result = x or y
print(f"OR: {or_result}")


#No lógico: not
not_result = not x
print(f"NOT: {not_result}")

#Operadores de Asignación:
#Asignación simple: =

asig = 10
print(f"asgnacion = {asig}")
#Suma y asignación: +=
asig += 10
print(f"asgnacion += {asig}")

#Resta y asignación: -=
asig -= 5
print(f"asgnacion -= {asig}")

#Multiplicación y asignación: *=
asig *= 10
print(f"asgnacion *= {asig}")

#División y asignación: /=
asig /= 10
print(f"asgnacion /= {asig}")

#División entera y asignación: //=
asig //= 3.4
print(f"asgnacion //= {asig}")

#Módulo y asignación: %=
asig %= 100
print(f"asgnacion %= {asig}")

#Potenciación y asignación: **=
asig **= 3
print(f"asgnacion **= {asig}")


#Operadores de Pertenencia:
list = [1,2,3,4,5]
#Pertenencia en: in
print(4 in list)
print(7 in list)

#No pertenencia en: not in
print(4 not in list)
print(7 not in list)
#2 - Utilizando las operaciones con operadores que tú quieras, crea ejemplosque representen todos los tipos de estructuras de control que existanen tu lenguaje:Condicionales, iterativas, excepciones...
x = 10
y = 5

#Estructuras de control condicionales:
if x == y:
    print(f"{x} es igual que {y}")

elif x > y:
    print(f"{x} es mayor que {y}")

else:
    print(f"{x} es menor que {y}")

#Bucles (Estructuras de control iterativas):
#while
while y <= x:
    print(f"imprimiendo con while {y}")
    y += 1

#for
for list in list:
    print(f"lista usando for {list}")    


#3- Debes hacer print por consola del resultado de todos los ejemplos.


'''
 DIFICULTAD EXTRA (opcional):
 Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

 Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 '''

for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)
