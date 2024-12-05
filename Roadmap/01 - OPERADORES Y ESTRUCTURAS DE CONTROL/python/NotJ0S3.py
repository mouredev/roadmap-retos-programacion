# EJERCICIO:
# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

# Operadores aritmeticos:
a = 4
b = 2

print(a + b) # Suma
print(a - b) # Resta
print(a * b) # Multiplicacion
print(a / b) # Division
print(a % b) # Modulo
print(a ** b) # Potencia o exponencia
print(a // b) # Division entera

# Operadores logicos:
c = True
d = False

print(c and d) # AND
print(c or d) # OR 
print(not c) # NOT

# Operadores de comparacion:
e = 10
f = 20

print(e == f) # Igual
print(e != f) # Distinto de
print(e > f) # Mayor que
print(e < f) # Menor que
print(e >= f) # Mayor o igal que
print(e <= f) # Menor o igual que

# Operadores de identidad:
g = [1, 2, 3]
h = g
i = [1, 2, 3]

print(g is h) # Mismo objeto
print(g is i) # Diferente objeto
print(g is not i) # Verifica que no son el mismo objeto

# Operadores de Pertenencia
listaNueva = [10, 20, 30, 40, 50]

print(30 in listaNueva) # Comprueba la existencia en la lista
print(60 not in listaNueva) # Comprueba si no esta en la lista

# Operadores a nivel de Bits
x = 4 # Binario: 0100
y = 5 # Binario: 0101

print(x & y)  # AND bit a bit
print(x | y)  # OR bit a bit
print(x ^ y)  # XOR bit a bit
print(~x)     # NOT bit a bit
print(x << 1) # Desplazamiento a la izquierda
print(x >> 1) # Desplazamiento a la derecha

# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
#   Condicionales, iterativas, excepciones...
#   Debes hacer print por consola del resultado de todos los ejemplos.

# Condicionales (if, elif, else):
if x > 8:
    print("x es mayor que 8")
elif x == 8:
    print("x es igual a 8")
else: print("x es menor que 8")

# Bucle (while):
j = 1
while j <= 5:
    print(j)
    j += 1

# Bucles (for):
for num in g: # Sobre una lista
    print(num)
   
for p in range(1, 6): # Usando un rango de números
    print(p)
    
# Bucles con break y continue:
# break:
for z in range(1, 6):
    if z == 3:
        break  # Rompera o terminara el bucle cuando z sea 3
    print(z)

# continue:
for w in range(1, 6):
    if w == 3:
        continue  #  Se salta la iteracion cuando w es igual a 3
    print(w)


# DIFICULTAD EXTRA (opcional):
# - Crea un programa que imprima por consola todos los números comprendidos
# - entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)