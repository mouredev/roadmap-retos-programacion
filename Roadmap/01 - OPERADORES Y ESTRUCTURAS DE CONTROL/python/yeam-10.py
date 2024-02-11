"""
Respuesta de ejercicio 01

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
"""

#Operadores de asignacion 

# El operador '=' sirve para asignar el valor de la variable Ejemplo

price = 909
print(price)

price += 1 # asigna y suma 1
print(price)
price -= 3 # asigna y resta 3
print(price)
price /= 5  # asigna y divide 5
print(price) 
price //= 6 # asigna y realiza la division entera
print(price)
price *= 7 # asigna y multiplica 7
print(price)
price %= 3 # asigna y calcula resto de 3
print(price)
price **= 2 # exponente y asignacion


#Operadores aritmeticos:
#Son aquellos que nos permiten realizar operaciones matematicas como suma, multiplicacion, division

print("La suma de 2 + 3:", 2+3) #Suma
print("La resta de 2 - 3:", 2-3) #Resta
print("La multiplicacion de 4 * 3:", 2*3) #Multiplicacion
print("La division de 2 / 3:", 2/3) #Division

#Operadores relacionales
#Permiten realizar comparaciones entre dos elementos. Son los siguientes 
# < Menor que
# > Mayor que 
# >= Mayor o igual que 
# <= Menor o igual que
# == Igual que 
# != Distinto que 

print("7 < 5", 7 < 5 ) # 7 es menor que 5 ? 
print("8 > 5", 8 > 5 ) # 8 es mayor que 5 ?
print("10 >= 15", 7 < 5 ) # 10 mayor o igual que 15 ?
print("2 <= 12", 2 <= 12 ) # 2 es menor o igual que 12 ?
print("67 == 5", 67 == 5 ) # 67 es igual que 5 ?
print("4 != 9", 4 != 9 ) # 4 es distinto que 5 ?

#Operadores logicos 
# Permiten combinar las operaciones relacionales o valores booleanos independientes para obtener un unico resultado
#Los operadores logico son AND, OR, NOT

print("Operacion (5<3) AND (4==3) es:", 5<3 and 4==3)
print("Operacion (5<3) OR (4==3) es:", 1<7 or 3==3)
print("Operacion (5<3) NOT (4==3) es:", not (5<3 and 4==3))

#Operadores de identidad

total_price = price
print("total_price is price", total_price is price)
print("total_price is price", total_price is not price)

#Operadores de pertenencia 

print(" r in request", 'r' in 'request')
print(" r in request", 'r' not in  'request')

"""
Estructuras de control 
"""
#Condicionales
# if permite generar un bloque de codigo que se ejecutara si se cumple la condicion de entrada que tiene.
# elif: permite generar un camino alternativo con una condicion de entrada. 
# else: permite generar un camino alternatuvo siempre que no se hayan cumplido las condiciones if y elif.

number_one = 2
number_two = 4

if number_one > number_two:
    print("Es mayor")
elif number_one == number_two:
    print("Son iguales")
else:
    print("El primer numero es menor")

#Iterativas
    
#Bucle for 
    
for item in range(10):
    print(item)

#Bucle while

i = 0
while i < 10:
    print(i)
    i= i + 1

"""
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

#Respuesta

for num in range(10,55):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
    




