### Operadores ###

# Operadores aritméticos

# Suma
print(2 + 2)  

# Resta
print(2 - 2)

# Multiplicación
print(2 * 2)  

# División  
print(3 / 2)

# División entera 
print(10 // 2)

# Módulo 
print(10 % 2)

# Potencia 
print(2 ** 3)

# Operadores de comparación

# Igualdad  
print(2 == 2)
print(2 == 3)

# Desigualdad
print(2 != 3)
print(2 != 2) 

# Mayor que
print(2 > 3)  
print(3 > 2)  

# Menor que
print(2 < 3)
print(3 < 2)

# Mayor o igual que 
print(2 >= 3)
print(3 >= 2)

# Menor o igual que
print(2 <= 3)
print(3 <= 2)

# Operadores lógicos

# AND comparación de dos valores booleanos o variables y devuelve True si ambos son True
print(True and True) # Imprime True
print(True and False) # Imprime False
print(3 > 2 and 2 > 3)  # Imprime False

# OR comparación de dos valores booleanos o variables y devuelve True si alguno es True
print(True or False) # Imprime True
print(False or False) # Imprime False
print(3 > 2 or 2 > 3)  # Imprime True

# NOT niega el valor booleano o variable
print(not True) # Imprime False
print(not False) # Imprime True
print(not 3 > 2) # Imprime False

# Operadores de asignación
q = 2

# Asignación simple
print(q)

# Asignación de suma
q += 2 # q = q + 2 daria el mismo resultado = 4
print(q)

# Asignación de resta
q -= 2 # q = q - 2 daria el mismo resultado = 2
print(q)

# Asignación de multiplicación
q *= 2 # q = q * 2 daria el mismo resultado = 4
print(q)

# Asignación de división
q /= 2 # q = q / 2 daria el mismo resultado = 2
print(q)

# Asignación de división entera
q //= 2 # q = q // 2 daria el mismo resultado = 1
print(q)

# Asignación de módulo
q %= 2 # q = q % 2 daria el mismo resultado = 0
print(q)

# Asignación de potencia
q **= 2 # q = q ** 2 daria el mismo resultado = 0
print(q)

# Operadores de identidad
print(2 is 2) # da True porque son el mismo objeto
print(2 is not 2) # da False porque son el mismo objeto

# is
print(2 is 2) # da True porque son el mismo objeto
print(2 is 3) # da False porque no son el mismo objeto

# is not
print(2 is not 2) # da False porque son el mismo objeto
print(2 is not 3) # da True porque no son el mismo objeto

# Operadores de pertenencia
lista = [1, 2, 3, 4, 5, 6]
print(lista)

# in
print(2 in lista) # da True porque el 2 esta en la lista
print(7 in lista) # da False porque el 7 no esta en la lista

# not in
print(2 not in lista) # da False porque el 2 esta en la lista
print(7 not in lista) # da True porque el 7 no esta en la lista

# Operadores de bits
"""
eso es para operar con bits, pero no se como se usa
son los siguientes:
AND (&) 
OR (|)
XOR (^)
NOT (~)
Desplazamiento a la izquierda (<<)
Desplazamiento a la derecha (>>)
"""

# AND
a = 5 & 3 # da 1
print(0b1010 & 0b1100) # da 8

# OR
a = 5 | 3 # da 7
print(0b1010 | 0b1100) # da 12

# XOR
a = 5 ^ 3 # da 6
print(0b1010 ^ 0b1100) # da 4

# NOT
a = ~5 # da -6
print(a)

# Desplazamiento a la izquierda
a = 5 << 3 # da 40
print(a)
# Desplazamiento a la derecha
a = 5 >> 3 # da 0
print(a)
# Operadores de precedencia
""" """

# () para agrupar operaciones
print(2 + 3 * 5) # da 17

print(2 ** 3 ** 2) # da 512

print(2 + 3 * 5) # da 17

# estructura de control

# if se usa para evaluar una condición y ejecutar un bloque de código si se cumple
if (2 + 3) * 5 == 25:
    print("Correcto")# se ejecuta si la condición es verdadera
elif (2 + 3) * 5 == 30: 
    print("Casi")# se ejecuta si la primera condición no se cumple y la segunda si
else: 
    print("Incorrecto") # se ejecuta si ninguna de las condiciones anteriores se cumple

# for se usa para iterar sobre una secuencia de elementos
    
for i in range(5): # se ejecuta 5 veces
    print( "For " + str(i)) # imprime hola y el valor de i

# while se usa para ejecutar un bloque de código mientras se cumpla una condición
i = 0
while i < 5: # se ejecuta mientras i sea menor que 5
    print( "While " + str(i)) # imprime hola y el valor de i
    i += 1 # incrementa el valor de i en 1

# try se usa para probar un bloque de código en busca de errores
try:
  print(10 / 0) # intenta dividir 10 entre 0  
except ZeroDivisionError:
  print("Error: División entre cero")
finally:
  print("Terminado")

# With se usa para ejecutar un bloque de código con un recurso externo
"""
with open("archivo.txt") as f: # abre el archivo y lo asigna a la variable f
  print(f.read()) # imprime el contenido del archivo
"""

"""
 DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

print(" ejercico con for")
for extra in range(10, 56): # extra inicia en 10 y se ejecuta mientras extra sea menor que 56
    if extra % 2 == 0 and extra != 16 and extra % 3 != 0: # si el numero es par y no es 16 y no es multiplo de 3
        print(extra)  # imprime el numero en extra

print(" ejercico con while")
extra2 = 10 # extra inicia en 10
while extra2 <= 55: # se ejecuta mientras extra sea menor que 56
    if extra2 % 2 == 0 and extra2 != 16 and extra2 % 3 != 0: # si el numero es par y no es 16 y no es multiplo de 3
        print(extra2)  # imprime el numero en extra
    extra2 += 1 # incrementa el valor de extra en 1