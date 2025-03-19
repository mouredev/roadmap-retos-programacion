numero1 = 10
numero2 = 3
numero3 = 343

cadena = "10 23 esto es una cadena"

x = True
y = False

# Aritméticos
suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1 * numero2
division = numero1 / numero2

print("Suma", suma)
print("Resta", resta)
print('Multiplicación', multi)
print('División', division)

#Lógicos And Or Not
res = x and y
print(res)

res = x or y
print(res)

res = not x
print(res)

# Operadores de asignación
suma += numero3
resta -= numero3
multi *= numero3
division /= numero3

print("Suma", suma)
print("Resta", resta)
print('Multiplicación', multi)
print('División', division)

# Operadores de Comparación
res = numero1 > numero2
print(res)

res = numero1 < numero2
print(res)

res = numero1 == numero2
print(res)

res = numero1 != numero2
print(res)

# Operadores de Identidad
"""
res = 10 is numero1
print(res)

res = "esto" is not cadena
print(res)
"""
# Operadores de pertenencia
res = "esto" in cadena
print(res)

res = "esto" not in cadena
print(res)

# Operadores de Bits
res = numero1 | numero2 # or bit a bit de x e y.
print(res)

res = numero1 & numero2 # and bit a bit de x e y.
print(res)

res = ~numero1 # not x. Obtiene los bits de x invertidos.
print(res)

# Condicionales
if numero1 == numero2:
    print("son iguales")
elif numero1 > numero2:
    print("numero1 es mayor que numero2")
else:
    print("numer1 es menor que numero 2")

# Iterativas:
for i in cadena:
    print(i)
i=1
while i < numero1:
    print("esta es la vuelta ", i)
    i += 1


#Excepciones

try:
    res = numero3 / 0
    print(res)
except ZeroDivisionError:
    print("Un numero no puede ser dividido por 0")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

for i in range(10, 56):
    if ((i % 2 == 0) and (i != 16) and not (i % 3 == 0)):
        print(i)
            
