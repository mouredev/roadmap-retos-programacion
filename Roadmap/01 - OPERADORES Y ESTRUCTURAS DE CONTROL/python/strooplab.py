"""
    EJERCICIO:
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
"""

#ejemplos de operadores aritmeticos

suma = 10+5+2
resta = 7-2
multiplicacion = 5*2
division = 10/2
residuo = suma % multiplicacion
divisionEntera = division // multiplicacion
potencia = suma ** resta
mix = (suma) + (resta) - (multiplicacion) * division / residuo
print(mix)

#ejemplos operadores logicos

var1 = True
var2  = False
print(var1 and var2)
print(var1 or var2)
print(not var1)

#ejemplos de comparacion

print(resta == suma)
print(resta != suma)
print(resta < suma)
print(resta > suma)
print(resta <= suma)
print(resta >= suma)

#ejemplos de asignacion

numero = 3
numero
numero += 3
numero -= 3
numero *= 2
numero /= 2
numero %= 2
numero //= 2
numero **= 2
print(numero)

#ejemplos de identidad

lista1 = [1, 1, 2, 3, 5, 8, 13]
lista2 = [2, 4, 6, 8, 10, 12, 14]
print(lista1 is lista2)
print(lista1 is not lista2)

#ejemplos de pertentencia

print(1 in lista2)
print(4 not in lista1)

#ejemplos de bits

numeroBits = 12
print(numeroBits << 12)
print(numeroBits >> 1)
print(numeroBits & 4)
print(numeroBits | 4)
print(numeroBits ^ 4)
print(numeroBits & ~4)
print(numeroBits | ~4)
print(numeroBits ^ ~4)

#2. Condicionales

if lista1 == lista2:
    print("Las listas son iguales")
elif lista1 != lista2:
    print("Las listas son diferentes")
else:
    print("No se cumple ninguna condicion")

#iterativas

listaIt =  [1, 2, 3, 4, 5]
for i in listaIt:
    print(i, 'Missisipi')

num1 = 30
num2 = 0
while num2 < num1:
    print(num2)
    num2 += 10

#Exceptciones

try:
    num1 = 1
    num2 = 0
    print(num1 / num2)
except ZeroDivisionError:
    print("No se puede dividir por cero")
except TypeError:
    print("Error de tipo")

#Ejercicio adicional

num1 = 10
num2 = 55

while num1 < num2:
    if num1 != 16 and (num1 % 3) != 0:
        print(num1)
    num1 += 1
        
