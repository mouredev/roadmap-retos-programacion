# Operadores Aritméticos
a = 5
b = 9

print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicacion: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Division Enteros: {a} // {b} = {a // b}")
print(f"Potenciacion: {a} ** {b} = {a ** b}")

# Operadores de Comparacion
print(f"Igualdad: {a} == {b} es {a == b}")
print(f"no es igual: {a} != {b} es {a != b}")
print(f"Mayor que: {a} > {b} es {a > b}")
print(f"Mayor o igual que: {a} >= {b} es {a >= b}")
print(f"menor que: {a} < {b} es {a < b}")
print(f"Menor o igual que: {a} <= {b} es {a <= b}")

# Operadores Logicos
print(f"and: True and True es {True and True}")    # solo es true si ambas son verdaderos
print(f"and: True and False es {True and False}")

print(f"or:  True or True es {True or True}")   # sera True siempre que una opcion sea True
print(f"or: True or False es {True or False}")

print(f"not: not True es {not True}")   # retorna el valor contrario si es True retorna False o si es False retorna True

# operadores de Asignacion
a = 5   # asigna 5 al valor de la variable
a += 3  # suma 3 a la variable a
a -= 3  # resta 3 a la variable a
a *= 3  # multiplica por 3 el valor de la variable a
a /= 3  # divide entre 3 el valor de la variable a
a %= 3  # muestra el resto de la division de la variable a / 3
a **= 3 # eleva la variable a a la potencia de 3
a //= 3 # Divide entre 3 y se queda solo con la parte entera

# Operadores de Identidad
a = 10
b = 34
print(f"is: {a} is {b} es {a is b}")
print(f"is not: {a} is not {b} es {a is not b}")

# Operadores de Pertenencia
frutas = ['uva', 'pera', 'manzana']
print(f"Pertenece: uva in frutas {'uva' in frutas }")
print(f"No Pertenece: naranja not in frutas {'naranja' not in frutas }")

# Bit
#AND bit a bit (&): 
print(5 & 3)   # Imprime: 1 (001)

#OR bit a bit (|):
print(5 | 3)   # Imprime: 7 (111)

#XOR bit a bit (^):
print(4 ^ 5)   # Imprime: 1 (001)

#NOT bit a bit (~):
print(~6)      # Imprime: -7

#Desplazamiento a la izquierda (<<): 
print(5 << 2)  # Imprime: 20

#Desplazamiento a la derecha (>>): 
print(1 >> 2)  # Imprime: 0

# Estructuras de control

# if/eslse
a = 5
b = 4

if a > b:
    print(f"el {a} es mayor que {b}")
else:
    print(f"el {b} es mayor que el {a}")


# if/elif/eslse
edad = 41
if edad >= 18 and edad <= 40:
    print("Eres mayor de edad")
elif edad > 0 and edad < 18:
    print("Eres menor de edad")
else:
    print("Eres un adulto mayor")

#try-except - Excepciones
try:
    print(3 / 0)
except ZeroDivisionError:
    print("Error nose puede dividir por cero")

# Ciclo For

frutas = ['uva', 'pera', 'manzana']
for fruta in frutas:
    print(fruta)

# Ciclo while
contador = 1
while contador <= 5:
    print(contador)
    contador+= 1

# Range
for i in range(1,10):
    print(i) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# Breack
for i in range(1, 5):
    print(i)
    if i == 3:
        break # termina la ejecucion cuando i vale 3

# continue
for i in range(1, 7):
    if i == 5:
        continue # salta a la sigiente interacion cuando i vale 5 sin mostrarlo
    print(i)


#reto
"""
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)