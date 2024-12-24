'''
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
# 1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

# Operadores aritméticos: estos son los operadores que se utilizan para realizar operaciones matemáticas.
# En Python tenemos los siguientes operadores aritméticos:
# + (suma), - (resta), * (multiplicación), / (división), % (módulo), ** (exponente), // (división entera)
print(f"Suma: 1 + 2 = {1 + 2}")
print(f"Resta: 1 - 2 = {1 - 2}")
print(f"Multiplicación: 1 * 2 = {1 * 2}")
print(f"División: 1 / 2 = {1 / 2}")
print(f"Módulo: 1 % 2 = {1 % 2}")
print(f"Exponente: 1 ** 2 = {1 ** 2}")
print(f"División entera: 1 // 2 = {1 // 2}")

# Operadores de comparación: estos operadores se utilizan para comparar dos valores.
# En Python tenemos los siguientes operadores de comparación:
# == (igualdad), != (desigualdad), >
print(f"Igualdad: 1 == 2 es {1 == 2}")
print(f"Desigualdad: 1 != 2 es {1 != 2}")
print(f"Mayor que: 1 > 2 es {1 > 2}")
print(f"Menor que: 1 < 2 es {1 < 2}")

# Operadores lógicos: estos operadores se utilizan para combinar expresiones lógicas.
# En Python tenemos los siguientes operadores lógicos:
# and (y), or (o), not (no)
print(f"AND &&: 1 == 1 and 2 == 2 es {1 == 1 and 2 == 2}") #tambien el and se puede escribir como &&
print(f"OR ||: 1 == 1 or 2 == 2 es {1 == 1 or 2 == 2}") #tambien el or se puede escribir como ||
print(f"NOT !: not 1 == 2 es {not 1 == 2}") #tambien el not se puede escribir como !

# Operadores de asignación: estos operadores se utilizan para asignar un valor a una variable.
# En Python tenemos los siguientes operadores de asignación:
# = (asignación), += (suma y asignación), -= (resta y asignación), *= (multiplicación y asignación), /= (división y asignación), %= (módulo y asignación), **= (exponente y asignación), //= (división entera y asignación)
num = 2  # asignación
print(num)
num += 1  # suma y asignación
print(num)
num -= 1  # resta y asignación
print(num)
num *= 2  # multiplicación y asignación
print(num)
num /= 2  # división y asignación
print(num)
num %= 3  # módulo y asignación
print(num)
num **= 2  # exponente y asignación
print(num)
num //= 2  # división entera y asignación
print(num)

# Operadores de identidad: estos operadores se utilizan para comparar la identidad de dos objetos.
# En Python tenemos los siguientes operadores de identidad:
# is (es), is not (no es)
num2 = num
print(f"num is num2 es {num is num2}") #tambien el is se puede escribir como ==
print(f"num is not num2 es {num is not num2}") #tambien el is not se puede escribir como !=

# Operadores de pertenencia: estos operadores se utilizan para comprobar si un objeto está presente en otro objeto.
# En Python tenemos los siguientes operadores de pertenencia:
# in (en), not in (no en)
cadena = "Hola Mundo"
print(f"'a' in 'Hola Mundo' = {'a' in 'Hola Mundo'}")
print(f"'b' not in 'Hola Mundo' = {'b' not in 'Hola Mundo'}")

# Operadores de bit: estos operadores se utilizan para realizar operaciones a nivel de bits.
# En Python tenemos los siguientes operadores de bit:
# & (AND), | (OR), ^ (XOR), ~ (NOT), << (desplazamiento a la izquierda), >> (desplazamiento a la derecha)
a = 5  # 0101 en binario
b = 2  # 0010 en binario
print(f"AND: 5 & 2 = {5 & 2}")  # 0000 en binario
print(f"OR: 5 | 2 = {5 | 2}")  # 0111 en binario
print(f"XOR: 5 ^ 2 = {5 ^ 2}")  # 0111 en binario
print(f"NOT: ~5 = {~5}")  # 1010 en binario
print(f"Desplazamiento a la derecha: 5 >> 2 = {5 >> 2}")  # 0001 en binario
print(f"Desplazamiento a la izquierda: 5 << 2 = {5 << 2}")  # 10100 en binario 

# 2. Utilizando las operaciones con operadores que tú quieras, crea ejemplos 
# que representen todos los tipos de estructuras de control que existan
# en tu lenguaje: Condicionales, iterativas, excepciones...

# Condicionales
num = 5
if num == 10:
    print("num es 10")
elif num == 20:
    print("num es 20")
else:
    print("num no es ni 10 ni 20")

# Iterativas
num = 0
while num < 5:
    print(num)
    num += 1

for i in range(5):
    print(i)

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("No se puede dividir por cero")
finally:
    print("Ha finalizado el manejo de excepciones")

# 3. Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for num in range(10,56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)