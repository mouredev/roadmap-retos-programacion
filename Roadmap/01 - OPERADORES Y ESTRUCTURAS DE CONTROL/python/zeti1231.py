## Operadores Aritméticos. Utilizan valores numéricos para realizar operaciones aritméticas

# Suma (Addition)
x = 3
y = 17
print(x + y)

# Resta (Subtraction)
x = 29
y = 23
print(x - y)

# Multiplicación (Multiplication)
x = 38
y = 147
print(x * y)

# División (Division)
x = 275
y = 51
print(x / y)

# Modulo (Modulus)
x = 26
y = 14
print( x % y)

# Exponencial (Exponentiation)
x = 6
y = 5
print(x ** y)

# División al piso (Floor Division), da como resultado de la división, el valor entero más cercano redondeado hacia abajo.
x = 22
y = 7
print(x // y)


## Operadores de Asignación. Se utilizan para asignar valores a las variables

# = 
x = 10
print(x)

# += 
x = 10
x += 3
print(x), # x = x + 3

# -=
x = 10
x -= 3
print(x), # x = x - 3

# *=
x = 10
x *= 3
print(x), # x = x * 3

# /=
x = 10
x /= 3
print(x), # x = x / 3

# %=
x = 10
x %=3
print(x), # x = x % 3

# //=
x = 10 
x //=3
print(x), # x = x // 3

# **=
x = 10
x **=3
print(x), # x = x ** 3

# &=
x = 10
x &=3
print(x), # x = & 3

# x |=
x = 10
x |=3
print(x), # x = x | 3

# ^=
x = 10
x ^=3
print(x), # x = x ^ 3

# ~=
x = 10
~ 10
print(x)

# >>=
x = 10
x >>=3
print(x), # x = x >> 3

# <<=
x = 10
x <<=3
print(x), # x = x << 3

# :=
x = 10
print(x := 3), # x = 3 print(x)

## Operadores de comparación.Se utilizan para comparar dos valores 

# Igual (==)
x == y 
x = 8
y = 2
print(x==y), # False

# Diferente (!=)
x != y
x = 8
y = 2
print(x != y), # True

# Mayor que (>)
x > y
x = 8
y = 2
print(x > y), # True

# Menor que (>)
x < y
x = 8
y = 2
print(x < y), # False

# Mayor o igual que (>=)
x >= y
x = 8
y = 2
print(x >= y), # True

# Menor o igual que (<=)
x <= y
x = 8
y = 12
print(x <= y), # True

# Operadores lógicos.Se utilizan para combinar declaraciones condicionales

# and. Retorna Verdadero si ambas afirmaciones son verdaderas
x = 8
print(x > 2 and x < 14), # True

# or. Retorna Verdadero si una de las afirmaciones son verdaderas
x = 8
print(x > 2 or x < 14), # True

# not. Invierte el resultado, retornando Falso si el resultado es Verdadero
x = 8
print(not(x > 2 or x < 14)), # False


# Condicionales

# if

x = 15
y = 56

if y > x:
    print("y es mayor que x")

# elif

x = 10
y = 10
if y > x:
    print("y es mayor a x")
elif x == y:
    print("x es igual a y")    

# else

x = 48
y = 22 
if y > x:
    print("y es mayor que x")
elif x == y:
    print("x es igual a y") 
else:
    print("x es mayor que y")

# Bucles

# While. Con este bucle se ejecutan un conjunto de declaraciones, siempre que una condición sea verdadera.

i = 1
while i < 10:
    print(i)
    i += 1

# Declaración de ruptura 

i = 1
while i < 10:
    print(i)
    if i == 3:
        break
    i += 1

# Declaración de continuación

i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)


# Con el comando else se ejecuta el código, hasta que la condición ya no se cumpla

i = 1 
while i < 10:
    print(i)
    i += 1
else:
    print("i ya no es menor que 10")

# For.Este bucle se utiliza para iterar sobre listas, tuplas , diccionarios, un conjunto o una cadena       

# Iterando en una lista

marcas = ["Mazda", "Ford", "Kia"]
for x in marcas:
    print(x)


# Iterando en una cadena 

for x in "caballo de troya":
    print(x)


# Iterando con ruptura

marcas = ["Mazda", "Ford", "Kia"]
for x in marcas:
    print(x)
    if x == "Ford":
        break


marcas = ["Mazda", "Ford", "Kia"]
for x in marcas:
    if x == "Ford":
        break
    print(x)


# Iterando con la instrucción continuar

marcas = ["Mazda", "Ford", "Kia"]
for x in marcas:
    if x == "Ford":
        continue
    print(x)


# Función rango().Se utiliza para recorrer un conjunto de código, un número específico de veces.Devuelve una secuencia de números, que comienza en un valor determinado, y termina en un valor determinado.

for x in range(8):
    print(x)


for x in range(3,10):
    print(x)

# Por defecto el valor del incremento en la función range es 1, para especificar un valor de incremento diferente, se debe añadir un tercer parámetro a la función.

for x in range(2,40,6):
    print(x)  


# Utilizando el condicional else en un bucle for

for x in range(8):
    print(x)
else:
    print("Terminado")    

# Bucle anidado.Condición en la que un bucle se encuentra dentro de otro bucle.El bucle interno, se ejecuta por cada iteración del bucle externo.


colores = ["Plata", "Negro", "Azul"]
marcas = ["Mazda", "Ford", "Kia"]
for x in colores:
    for y in marcas:
        print(x,y)


# DIFICULTAD EXTRA (opcional):
"""
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""  
for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)
