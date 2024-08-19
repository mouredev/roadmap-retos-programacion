"""
Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
"""


"""
Operadores aritméticos:
    - Suma: +
    - Resta: -
    - Multiplicación: *
    - División: /
    - División entera: //
    - Módulo (resto de la división): %
    - Exponente: **
"""
num_one = 3
num_two = 2

print("Operadores aritméticos")
print(f"Suma: {num_one + num_two}")
print(f"Resta: {num_one - num_two}")
print(f"Multiplicación: {num_one * num_two}")
print(f"División: {num_one / num_two}")
print(f"División entera: {num_one // num_two}")
print(f"Módulo: {num_one % num_two}")
print(f"Exponente: {num_one ** num_two}")

"""
Operadores de asignación:
    Asignación: =
    Suma y asignación: +=
    Resta y asignación: -=
    Multiplicación y asignación: *=
    División y asignación: /=
    División entera y asignación: //=
    Módulo y asignación: %=
    Exponente y asignación: **=
"""

print("\nOperadores de asignación")

asignacion = 5
print(f"Asignación: {asignacion}")

asignacion += 3
print(f"Suma y asignación: {asignacion}")

asignacion -= 3
print(f"Resta y asignación: {asignacion}")

asignacion *= 3
print(f"Multiplicación y asignación: {asignacion}")

asignacion /= 3
print(f"División y asignación: {asignacion}")

asignacion //= 3
print(f"División entera y asignación: {asignacion}")

asignacion %= 3
print(f"Módulo y asignación: {asignacion}")

asignacion **= 3
print(f"Exponente y asignación: {asignacion}")

"""
Operadores de comparación:
    Igual a: ==
    No igual a: !=
    Mayor que: >
    Menor que: <
    Mayor o igual que: >=
    Menor o igual que: <=
"""

num_one = 3
num_two = 2
numeber_tree = 2

print("\nOperadores de comparación")

print("\nIgualdad")
# Igualdad
print(f"¿ {num_one} es igual a {num_two} ? : {num_one == num_two}")
print(f"¿ {num_two} es igual a {numeber_tree} ? : {num_two == numeber_tree}")

print("\nDiferencia")
# Diferencia
print(f"¿ {num_one} es diferente a {num_two} ? : {num_one != num_two}")
print(f"¿ {num_two} es diferente a {numeber_tree} ? : {num_two != numeber_tree}")

print("\nMayor que")
# Mayor que
print(f"¿ {num_one} es mayor a {num_two} ? : {num_one > num_two}")
print(f"¿ {num_two} es mayor a {num_one} ? : {num_two > num_one}")
print(f"¿ {num_two} es mayor a {numeber_tree} ? : {num_two > numeber_tree}")

print("\nMenor que")
# Menor que
print(f"¿ {num_two} es menor a {num_one} ? : {num_two < num_one}")
print(f"¿ {num_one} es menor a {num_two} ? : {num_one < num_two}")
print(f"¿ {num_two} es menor a {numeber_tree} ? : {num_two < numeber_tree}")

print("\nMayor o igual a")
# Mayor o igual a
print(f"¿ {num_one} es mayor o igual a {num_two} ? : {num_one >= num_two}")
print(f"¿ {num_two} es mayor o igual a {numeber_tree} ? : {num_two >= numeber_tree}")
print(f"¿ {num_two} es mayor o igual a {num_one} ? : {num_two >= num_one}")

print("\nMenor o igual a")
# Menor o igual a
print(f"¿ {num_two} es menor o igual a {num_one} ? : {num_two <= num_one}")
print(f"¿ {num_two} es menor o igual a {numeber_tree} ? : {num_two <= numeber_tree}")
print(f"¿ {num_one} es menor o igual a {num_two} ? : {num_one <= num_two}")


"""
Operadores lógicos:
    AND lógico: and
    OR lógico: or
    NOT lógico: not
"""

print("Operadores lógicos")

print("\nOperador lógico AND ")
print(True and True)
print(True and False)
print(False and False)

print("\nOperador lógico OR ")
print(True or True)
print(True or False)
print(False or False)

print("\nOperador lógico NOT")
print(not(False))
print(not(True))

"""
Operadores de identidad:
    is: devuelve True si ambas variables son el mismo objeto
    is not: devuelve True si ambas variables no son el mismo objeto
"""

print("\nOperadores de identidad")

# is
print("\nOperadores de identidad is")
print(f"{True} is {True}: {True is True}")
print(f"{True} is {False}: {True is False}")
print(f"{False} is {False}: {False is False}")

# is not
print("\nOperadores de identidad is not")
print(f"{True} is not {False}: {True is not False}")
print(f"{True} is not {True}: {True is not True}")
print(f"{False} is not {False}: {False is not False}")

"""
Operadores de Pertenencia
    in: Devuelve True si el valor está presente en la secuencia
    not in: Devuelve True si el valor no está presente en la secuencia.
"""
cadena = "Soy DGrex"

# in
print("\nOperadores de Pertenencia in")
print("DGrex" in cadena)
print("dgrex" in cadena)

# not in
print("\nOperadores de Pertenencia not in")

print("DGrex" not in cadena)
print("dgrex" not in cadena)


"""
Operadores Bit a Bit
-Se utilizan para realizar operaciones a nivel de bits.
    & (AND bit a bit): Realiza una operación AND a nivel de bits.
    | (OR bit a bit): Realiza una operación OR a nivel de bits.
    ^ (XOR bit a bit): Realiza una operación XOR a nivel de bits.
    ~ (NOT bit a bit): Invierte todos los bits del operando
    << (Desplazamiento a la izquierda): Desplaza los bits del operando a la izquierda
    >> (Desplazamiento a la derecha): Desplaza los bits del operando a la derecha.
"""

print("\nOperadores Bit a Bit")

num_one = 5
num_two = 3


#  & (AND bit a bit)
print("\nOperadores Bit a Bit & (AND bit a bit)")
print(num_one & num_two)

# | (OR bit a bit)
print("\nOperadores Bit a Bit | (OR bit a bit)")
print(num_one | num_two)

# ^ (XOR bit a bit)
print("\nOperadores Bit a Bit ^ (XOR bit a bit)")
print(num_one ^ num_two)

# ~ (NOT bit a bit)
print("\nOperadores Bit a Bit~ (NOT bit a bit)")
print(~num_two)

#  << (Desplazamiento a la izquierda)
print("\nOperadores Bit a Bit << (Desplazamiento a la izquierda)")
numero = 5  # 0101 en binario
print(numero << 1)  # 1010 en binario, que es 10 en decimal
print(numero << 2)  # 10100 en binario, que es 20 en decimal

#  >> (Desplazamiento a la derecha)
print("\nOperadores Bit a Bit >> (Desplazamiento a la derecha)")
numero = 5  # 0101 en binario
print(numero >> 1)  # 0010 en binario, que es 2 en decimal
print(numero >> 2)  # 0001 en binario, que es 1 en decimal


"""
Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
Condicionales, iterativas, excepciones...
"""

# Condicionales

#Sentencia if 

print("\nSentencia if ")
if 3 > 2:
    print("3 es mayor que 2")

#Sentencia if-else 
print("\nSentencia if-else ")
if 2 > 3:
    print("2 es mayor a 3")
else:
    print("3 es mayor que 2")

#Sentencia if-elif-else 
print("\nSentencia if-elif-else ")
if 2 > 2:
    print("2 es mayor a 3")
elif 2 == 2:
    print("Ambos numero son iguales")
else:
    print("3 es mayor que 2")


# Iteractivas

# while
print("\nIteractiva While")
i = 0 
while i <= 11:
    i += 1
    print(f"{2} X {i}: {i * 2}")


print("\nIteractiva for")
# for
lista = ["Denis", "Javier", "Goyes", "Moran"]
for elemento in lista:
    print(elemento)


# Excepciones

num_one = 5
num_two = "3"

# try-except

print("\nExcepciones")
try:
    print(num_one + num_two)
    print("No se a producido el error")
except TypeError as error: # as es reservada y error es una variable
    print(f"{error}")


"""
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

print("\nEjercicio")

for num in range(10,55):

    if num % 2 == 0:
        if num != 16 and num % 3 != 0:
            print(num) 

print("\nEjercicio")

num = 10

while num <= 55:
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
    num += 1
