# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
#### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

## Ejercicio

#
# EJERCICIO:
# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
#   Condicionales, iterativas, excepciones...
# - Debes hacer print por consola del resultado de todos los ejemplos.
#
# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#
# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#

# OPERADORES ARITMÉTICOS
# Suma
print(2 + 3)  

# Resta
print(15 - 7)  

# Multiplicación
print(8 * 6)  

# División
print(18 / 3)  

# División entera
print(19 // 5)  

# Módulo
print(17 % 7)  

# Potencia
print(2 ** 4)  

# OPERADORES DE COMPARACION
# Igualdad
print(3 == 3)  

# Desigualdad
print(14 != 5)  

# Mayor que
print(13 > 10)  

# Menor que
print(4 < 9)  

# Mayor o igual que
print(22 >= 22)  

# Menor o igual que
print(7 <= 9)

# OPERADORES LOGICOS
# AND lógico
print(True and False)  

# OR lógico
print(True or False)  

# NOT lógico
print(not True)

# OPERADORES DE ASIGNACION
x = 7
print(x)

x += 2  # Equivalente a x = x + 3
print(x)

x -= 2  # Equivalente a x = x - 2
print(x)

x *= 4  # Equivalente a x = x * 4
print(x)

x /= 2  # Equivalente a x = x / 2
print(x)

# OPERADORES DE IDENTIDAD
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, ya que 'a' y 'b' apuntan al mismo objeto
print(a is not c)  # True, ya que 'a' y 'c' no apuntan al mismo objeto

# OPERADORES DE PERTENENCIA
lista = [1, 2, 3, 4, 5]

print(2 in lista)  # True, ya que 2 está en la lista
print(6 not in lista)  # True, ya que 6 no está en la lista

# OPERADORES A NIVEL DE BITS
# AND a nivel de bits
print(5 & 3)

# OR a nivel de bits
print(5 | 3)

# XOR a nivel de bits
print(5 ^ 3)

# Desplazamiento a la derecha
print(10 >> 1)

# Desplazamiento a la izquierda
print(10 << 1)


# ESTRUCTURAS DE CONTROL
# CONDICIONALES
# If-else
x = 10
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual que 5")

# If-elif-else
y = 20
if y > 25:
    print("y es mayor que 25")
elif y == 25:
    print("y es igual a 25")
else:
    print("y es menor que 25")

# ITERATIVAS
# Bucle for
for i in range(8):
    print(i)

# Bucle while
num = 0
while num < 8:
    print(num)
    num += 1

# EXCEPCIONES
# Bloque try-except
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("¡Error! División entre cero.")

# EJERCICIO OPCIONAL
# Imprimir los números que cumplen con las condiciones dadas
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
