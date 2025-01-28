# #01 OPERADORES Y ESTRUCTURAS DE CONTROL

"""
1.
 - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
"""

'''# OPERADORES ARITMÉTICOS'''

a = 4
b = 6

print(a + b) # suma
print(a - b) # resta
print(a * b) # multiplicación
print(a / b) # división
print(a // b) # división entera
print(a % b) # Môdulo, devuelve el resto de la división
print(a ** b) # Elevado a...
print(-a) # Negación, cambiar el valor positivo o negativo 

# ==================================================================

'''OPERADORES LÓGICOS'''
# Utlizados para combinar o invertir expresiones condicionales (booleanos)

a = True
b = False
x = 10

#AND (Y lógico)
print(a and b) # imprime False

#Ejemplo
print(x > 5 and x < 20) # True
print(x < 11 and x != 10) # False

#=================================
#OR (O lógico)
print( a or b) # Imprime True
print(x < 5 or x > 8) # True

#=================================
#NOT (Negación lógica)
print(not a) # False
print(not(x > 5)) # False

#===============================================

'''OPERADORES DE COMPARACIÓN'''

# IGUAL A...
a = 5
b = 12
print(a == b) # False

# DISTINTO DE...
print(a != b) # True

# MAYOR QUE...
print( a > b) # False

# MENOR QUE...
print(a < b) # True

# MAYOR O IGUAL QUE...
print(a >= b) # False

# MENOR O IGUAL QUE...
print(a <= b) # True

#=====================================
'''OPERADORES DE ASIGNACIÓN'''

# Asignaciôn simple
x = 20

# Suma y asigna
x += 1
print(x) # 4

# Resta y asigna
x -= 2
print(x)

# Multiplica y asigna
x *= 5
print(x)

# Divide y asigna
x /= 2
print(x)

#División entera y asigna
x //= 2
print(x)

# Módulo y asigna
x %= 5
print(x)

# Potencia y asigna
x **= 4
print(x)

#========================================

'''Operadores Bit a Bit'''
c = 5 # 0101
d = 3 # 0011

# AND bit a bit; devuelve 1 solo si ambos bits son 1.
print(c & d) 

# OR bit a bit; devuelve 1 si al menos uno de los bits es 1.
print(c | d)

# XOR bit a bit; devuelve 1 solo so los bits son diferentes
print(c ^ d)

#NOT bit a bit; invierte todos los bits de un número.
print(~c) 

# Desplazamiento a la izquierda; desplaza los bits de un número hacia la izq, añadiendo ceros al final.
print(c << 1)

# Desplazamiento a la derecha; desplaza los bits de un número a la derecha, descartando los bits finales.
print(c >> 1)

#=======================================================

'''OPERADORES DE MEMBRESÍA'''

# IN; devuelve True si el elemento está en la secuencia

mi_lista = [1, 2, 3, 4]
print(3 in mi_lista) # True

texto = "Python"
print("Py" in texto) # True

# NOT IN; devuelve True si el elemento NO está en la secuencia

print(5 not in mi_lista) # True
print("Java" not in texto) # True

#=========================================================

'''OPERADORES DE INDENTIDAD'''

# IS; Devuelve True si dos variables apuntan al mismo objeto

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) # True
print(a is c) # False, son objetos diferentes, aunque iguales

# IS NOT; Devuelve True si dos variables NO apuntan al mismo objeto

print(a is not c)

#===========================================================

'''OPERADORES ESPECIALES'''

# OPERADOR TERNARIO (Condicional en una línea)
# forma compacta de escribir condiciones

x = 10
y = 20
mayor = x if x > y else y 
print(mayor) # 20

# OPERADOR LAMBDA (Función anónima)
# Define una función en una sola línea

suma = lambda x, y: x + y
print(suma(5, 3)) # 8

es_par = lambda x: "Par" if x % 2 == 0 else "Impar"
print(es_par(10)) # Par

#==================================================

'''ESTRUCTURAS DE CONTROL'''

# CONDICIONALES IF, ELIF, ELSE

num = 10

if num % 2 == 0:
    print(f"{num} es un número par.")
elif num > 10:
    print(f"{num} es mayor que 10.")
else:
    print(f"{num} es impar o menor que 10.")

# ESTRUCTURAS ITERATIVAS

# FOR
for i in range(1,6):
    print(f"El cuadrado de {i} es {i **2}")

# WHILE

n = 0
limite = 5

while n <= limite:
    print(f"n = {n}")
    n += 1

# EXCEPCIONES TRY, EXCEPT, ELSE, FINALLY

try:
    resultado = 10 / 0 # generará una excepción 
except ZeroDivisionError as e:
    print("Error: División por cero no permitida.")
else:
    print(f"El resultado es {resultado}")
finally:
    print("Bloque finally ejecutado.")

# COMPREHENSIONS (estructura de control implícita en Python)

# lista de números pares utilizando if dentro de una lista
numeros = [x for x in range(10) if x % 2 == 0]
print(numeros) # salida: [0, 2, 4, 6, 8]

# lista con una operación utilizando FOR y CONDICIONALES
#(lista con cuadrados de números pares y un mensaje para impares)
resultado = [x ** 2 if x % 2 == 0 else "Impar" for x in range (1, 6)]
print(resultado) # salida: ['Impar', 4, 'Impar', 16, 'Impar']

# OPERADORES DENTRO DE FUNCIONES
# Función con operadores aritméticos
def calcular_area(base, altura):
    return base * altura / 2

area = calcular_area(10, 5)
print(f" El área del triángulo es: {area}")

# Función con operadores lógicos
def es_mayor_de_edad(edad):
    return edad >= 18

print(es_mayor_de_edad(20))
print(es_mayor_de_edad(16))

#===================================================

'''EJERCICIO EXTRA

 * Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''

for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)








