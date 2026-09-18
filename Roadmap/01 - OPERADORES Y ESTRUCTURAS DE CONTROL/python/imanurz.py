# Operadores Aritmeticos

a = 5
b = 8
print("--- Operadores Aritmeticos ---")
print(f"Valor de a: {a}  Valor de b: {b}")
# Suma
print("Suma: ", a + b)

# Resta
print("Resta: ", a - b)

# Multiplicacion
print("Multiplicacion: ", a * b)

# Division
print("Division: ", b / a) # El resultado siempre sera un float si la division no es exacta

# Division entera
print("Division entera: ", b // a) # El resultado siempre sera entero

# Modulo o Residuo
print("Modulo: ", b % a) 

# Exponente o Potencia
print("Exponente: ", b ** a)

# Operadores de Comparacion

c = 7
d = 10
print("--- Operadores de Comparacion ---")
print(f"Valor de c: {c} Valor de d: {d}")

# Igual que
print("c es igual a d: ", c == d)

# Distindo de
print("c es distindo a d: ", c != d)

# Mayor que
print("c es mayor que d: ", c > d)

# Menor que
print("c es menor que d: ", c < d)

# Mayor o igual que
print("c es mayor o igual que d: ", c >= d)

# Menor o igual que
print("c es menor o igual que d: ", c <= d)

# Operadores Logicos

x = True
y = False
print("--- Operadores Logicos ---")

# AND
print("Son X y Y verdaderos: ", x and y)

# OR
print("Al menos uno entre X y Y es verdadero: ", x or y)

# NOT
print("Negacion de X: ", not x)

# Operadores de Asignacion

print("--- Operadores de Asignacion ---")
# Asignacion simple
i = 15
print(f"Valor de i: {i}")

# Asignacion Compuesta Suma
i += 2
print(f"i mas 2: {i}") # Es como i = i + 2

# Asignacion Compuesta Resta
i -= 3
print(f"i menos 3: {i}")

# Asignacion Compuesta Multiplicacion
i *= 2
print(f"i por 2: {i}")  

# Puede aplicarse con todos los operadores aritmeticos.

# Operadores de Identidad

caja1 = [1, 2, 3]
caja2 = [1, 2, 3]
caja3 = caja1
print("--- Operadores de Identidad ---")
# IS
print("Es caja1 la misma que la caja3: ", caja1 is caja3) # True, ya que caja3 apunta a la misma direccion de memoria que caja1

# IS NOT
print("Es la caja1 distinta que la caja2: ", caja1 is not caja2) # True, is verifica si son el mismo objeto en memoria


# Operadores de Pertenencia

nombres = ["Pedro", "Juan", "Maria", "Rosa"]
print("--- Operadores de Pertenencia ---")
# IN
print("¿Esta Rosa en la lista de nombres?: ", "Rosa" in nombres)

# NOT IN
print("Diego no esta en la lista de nombres: ", "Diego" not in nombres)

# Operadores de Bits

a = 6  #  0110
b = 3  #  0011
print("--- Operadores de Bits ---")

# AND (&) Devuelve 1 en cada bit si ambos bits son 1.
print("AND &: ", a & b)  # Resultado: 2 en binaio 0010

# OR (|) Devuelve 1 en cada bit si al menos uno de los bits es 1.
print("OR |: ", a | b)  # Resultado: 7 en binario 0111

# XOR (^) Devuelve 1 en cada bit si los bits son diferentes.
print("XOR ^: ", a ^ b)  # Resultado: 5 en binario 0101

# NOT (~) Invierte todos los bits basicamente es el numero negativo de x + 1. Por ejemplo, ~6 = -7
print("NOT ~: ", ~a)  # Resultado: -7 

# Desplazamiento a la izquierda (<<) Desplaza los bits a la izquierda y rellena con ceros.
print("Desplazamiento a la izquierda <<: ", a << 1)  # Resultado: 12 en binario 1100

# Desplazamiento a la derecha (>>) Desplaza los bits a la derecha y rellena con ceros.
print("Desplazamiento a la derecha >>: ", a >> 1)  # Resultado: 3 en binario 0011

# Estructuras de Control
print("--- Estructuras de Control Condicionales---")

a = 12
b = 3
c = 8
d = 33

# IF, ELIF, ELSE
if a > b and c > d:
    print(f"Soy un print que nunca va a salir porque la condicion es falsa")
elif c > b or d < a:
    print(f"Soy un print que representa la Estructura de Control IF, ELIF, ELSE")
else:
    print(f"La opcion d es {d}")

# MATCH CASE 
match b:
    case 12:
        print("Soy el 12")
    case 8:
        print("Soy el 8")
    case 3:
        print("Soy el 3 y represento la Estructura de Control MATCH CASE")
    case _:
        print("No soy ninguno de los anteriores")

# Bucles
print("--- Estructuras de Control Bucles---")

# WHILE
contador = 1
print("Soy un bucle while y voy a contar hasta 7")

while contador <= 7:
    print(contador)
    contador += 1
else: 
    print("He terminado de contar")

# FOR
paises = ["Colombia", "Peru", "Ecuador", "Venezuela"]
print("Soy un bucle for y voy a recorrer la lista de paises")

for pais in paises:
    print(pais)

# Excepciones
print("--- Estructuras de Control Excepciones---")

# TRY, EXCEPT
try:
    operacion = 5 / 0
except ZeroDivisionError:
    print("No se puede dividir entre 0")

# EJERCICIO EXTRA
"""
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

print("--- Ejercicio Extra ---")
print("Vamos a imprimir los numeros pares entre 10 y 55, incluidos, excepto el 16 y los multiplos de 3")

for i in range(10, 56):
    if (i % 2 == 0 or i == 55) and (i != 16 and i % 3 != 0):
        print(i)
    