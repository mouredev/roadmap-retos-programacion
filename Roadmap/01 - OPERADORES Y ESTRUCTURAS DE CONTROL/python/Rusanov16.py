"""
EJERCICIO 01:
    - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    
    - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
    
    - Debes hacer print por consola del resultado de todos los ejemplos.
    
    DIFICULTAD EXTRA (opcional):
    
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

"""

#*-------------------------------------------------------------------------------------------------------------#
"""
Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, 
asignación, identidad, pertenencia, bits... 
    
"""
#Operadores Aritméticos
print("Operadores Aritméticos:")
print("------------------------------------------------------")
#Suma
print(f" -Suma: +; 55 + 24 =  {55 + 24}")
print("------------------------------------------------------")
#Resta
print(f" -Resta: -; 55 - 24 = {55 - 24}")
print("------------------------------------------------------")
#Multiplicación
print(f" -Multiplicación: *; 55 * 24 = {55 * 24}")
print("------------------------------------------------------")
#División
print(f" -División: /; 55 / 24 = {round((55 / 24),4)}")
print("------------------------------------------------------")
#Módulo
print(f" -Módulo: %; 55 % 2 = {55 % 24}")
print("------------------------------------------------------")
#Exponente
print(f" -Exponente: **; 55 ** 24 = {55 ** 24}")
print("------------------------------------------------------")
#Cociente
print(f" -Cociente: //; 55 // 24 = {55 // 24}")
print("------------------------------------------------------")
print("\n")

#Operadores Lógicos
print("Operadores Lógicos:")
print("------------------------------------------------------")
#AND
print(" -Operador AND:")
print(f" True and True =  {True and True}")
print(f" True and False =  {True and False}")
print(f" False and True =  {False and True}")
print(f" False and False =  {False and False}")
print("------------------------------------------------------")
#OR
print(" -Operador OR:")
print(f" True or True =  {True or True}")
print(f" True or False =  {True or False}")
print(f" False or True =  {False or True}")
print(f" False or False =  {False or False}")
print("------------------------------------------------------")
#NOT
print(" -Operador NOT:")
print(f" not True =  {not True}")
print(f" not False =  {not False}")
print("------------------------------------------------------")
print("\n")

#Operadores de comparación
print("Operadores de Comparación:")
print("------------------------------------------------------")
#Operador ==
print(f" -Operador ==; 5 == 2 =  {5 == 2}")
print("------------------------------------------------------")
#Operador !=
print(f" -Operador !=; 5 != 2 =  {5 != 2}")
print("------------------------------------------------------")
#Operador >
print(f" -Operador >; 5 > 2 =  {5 > 2}")
print("------------------------------------------------------")
#Operador <
print(f" -Operador <; 5 < 2 =  {5 < 2}")
print("------------------------------------------------------")
#Operador >=
print(f" -Operador >=; 5 >= 2 =  {5 >= 2}")
print("------------------------------------------------------")
#Operador >=
print(f" -Operador >=; 5 >= 2 =  {5 <= 2}")
print("------------------------------------------------------")
print("\n")

# Operadores de Identidad
print("Operadores de Identidad:")
print("------------------------------------------------------")
#Operador is
print(f" -Operador is; 5 is 2 =  {5 is 2}")
print("------------------------------------------------------")
#Operador is not
print(f" -Operador is not; 5 is not 2 =  {5 is not 2}")
print("------------------------------------------------------")
print("\n")

# Operadores de Pertenencia
print("Operadores de Pertenencia:")
print("------------------------------------------------------")
#Operador in
lista = [2,6,8,10]
print(f" -Operador in; 5 in [2,6,8,10] =  {5 in lista}")
print("------------------------------------------------------")
#Operador  not in
print(f" -Operador not in; 5 not in [2,6,8,10] =  {5 not in lista}")
print("------------------------------------------------------")
print("\n")

# Operadores de Bits
print("Operadores de Bits:")
print("------------------------------------------------------")
a = 0b1101 #Valor binario del número 27
b = 0b1011
#Operador |
print(f"-Operador |; 0b1101 | 0b1011 = {bin(a | b)}")
print("------------------------------------------------------")
#Operador &
print(f"-Operador &; 0b1101 & 0b1011 = {bin(a & b)}")
print("------------------------------------------------------")
#Operador ~
c = 40
print(f"-Operador ~; ~40 = {bin(~c)}")
print("------------------------------------------------------")
#Operador ^
x = 0b0110 ^ 0b1010
print(f" -Operador ^; x = 0b0110 ^ 0b1010 = {x}")
print("------------------------------------------------------")
#Operador >>
print(f"-Operador >>; 0b1101 >> 2 = {bin(a >> 2)}")
print("------------------------------------------------------")
#Operador <<
print(f"-Operador <<; 0b1101 << 5 = {bin(a << 5)}")
print("------------------------------------------------------")
print("\n")

#*-------------------------------------------------------------------------------------------------------------#

"""    - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
"""

print("Estructuras de Control")

#if
print("IF")
if 25 % 5 == 0:
    print("25 es múltiplo de 5")
print("------------------------------------------------------")

#if/else
print("IF/ELSE")
if 25 % 5 == 0:
    print("25 es múltiplo de 5")
else:
    print("25 no es múltiplo de 5")
print("------------------------------------------------------")

#if/elif/else
print("IF/ELIF/ELSE")
edad = 45
if edad < 13:
    print("Eres un niño.")
elif edad < 20:
    print("Eres un adolescente.")
elif edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
print("------------------------------------------------------")
print("\n")

#for
print("FOR")
for i in "Programming":
    print(i)
print("------------------------------------------------------")
#while
print("WHILE")

i = 1
while i <= 3:
    print(i)
    i += 1
print("Números del 1 al 3")

print("\n")

#*-------------------------------------------------------------------------------------------------------------#

"""       DIFICULTAD EXTRA (opcional):
    
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

for i in range(10,55):
    if i % 2 == 0 and i % 3 != 0 and i != 16 :
        print(i)
        