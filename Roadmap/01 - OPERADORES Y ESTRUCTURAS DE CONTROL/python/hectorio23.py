# Autor: Héctor Adán 
# GitHub: https://github.com/hectoiro23

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
* DIFICULTAD EXTRA:
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*
* Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
'''

# Operadores aritméticos
print("******** OPERADORES ARITMÉTICOS ********")
print("SUMA: 4 + 5 =", 4 + 5)
print("RESTA: 4 - 5 =", 4 - 5)
print("MULTIPLICACIÓN: 4 * 5 =", 4 * 5)
print("DIVISIÓN: 4 / 5 =", 4 / 5)
print("DIVISIÓN ENTERA: 4 // 5 =", 4 // 5)
print("MÓDULO: 4 % 5 =", 4 % 5)
print("POTENCIA: 4 ** 5 =", 4 ** 5)

# Operadores de comparación
print("******** OPERADORES DE COMPARACIÓN ********")
print("IGUAL QUE: 4 == 5:", 4 == 5)
print("DIFERENTE DE: 4 != 5:", 4 != 5)
print("MAYOR QUE: 4 > 5:", 4 > 5)
print("MENOR QUE: 4 < 5:", 4 < 5)
print("MAYOR O IGUAL QUE: 4 >= 5:", 4 >= 5)
print("MENOR O IGUAL QUE: 4 <= 5:", 4 <= 5)

# Operadores lógicos
print("******** OPERADORES LÓGICOS ********")
print("AND: True and False:", True and False)
print("OR: True or False:", True or False)
print("NOT: not True:", not True)

# Operadores de asignación
print("******** OPERADORES DE ASIGNACIÓN ********")
x = 5
print("x =", x)
x += 2
print("x += 2 ->", x)
x -= 1
print("x -= 1 ->", x)
x *= 3
print("x *= 3 ->", x)
x /= 2
print("x /= 2 ->", x)
x %= 4
print("x %= 4 ->", x)
x **= 2
print("x **= 2 ->", x)
x //= 3
print("x //= 3 ->", x)

# Operadores de identidad
print("******** OPERADORES DE IDENTIDAD ********")
a = [1, 2, 3]
b = a
print("a is b:", a is b)
c = a[:]
print("a is c:", a is c)
print("a == c:", a == c)

# Operadores de pertenencia
print("******** OPERADORES DE PERTENENCIA ********")
print("1 in [1, 2, 3]:", 1 in [1, 2, 3])
print("4 not in [1, 2, 3]:", 4 not in [1, 2, 3])

# Operadores a nivel de bits
print("******** OPERADORES A NIVEL DE BITS ********")
print("AND: 4 & 5 =", 4 & 5)
print("OR: 4 | 5 =", 4 | 5)
print("XOR: 4 ^ 5 =", 4 ^ 5)
print("NOT: ~4 =", ~4)
print("Desplazamiento a la izquierda: 4 << 1 =", 4 << 1)
print("Desplazamiento a la derecha: 4 >> 1 =", 4 >> 1)

# Estructuras de control condicionales
print("******** ESTRUCTURAS DE CONTROL CONDICIONALES ********")
if x > 2:
    print("x es mayor que 2")
elif x == 2:
    print("x es igual a 2")
else:
    print("x es menor que 2")

# Estructuras de control iterativas
print("******** ESTRUCTURAS DE CONTROL ITERATIVAS ********")
print("Bucle for:")
for i in range(3):
    print("i =", i)

print("Bucle while:")
n = 3
while n > 0:
    print("n =", n)
    n -= 1

# Manejo de excepciones
print("******** MANEJO DE EXCEPCIONES ********")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Bloque finally ejecutado")



print("******** EJERCICIO EXTRe ********")
# Imprime los numeros del 10 al 55 siempre y cuando sean pares y no sean multiplos de 3 y 16 
print([ element for element in range(10, 56, 2) if element % 3 != 0 and element % 16 != 0])
# 10, 14, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52
