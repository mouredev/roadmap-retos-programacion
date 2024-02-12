"""
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
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""
# OPERADORES DE ASIGNACION - Asignan un valor a una variable
a = 1  # El valor 1 es asignado a la variable a
print(a)
a += 5  # Es equivalente a: a = a + 5
print(a)
a -= 3  # Es equivalente a: a = a - 2
print(a)
a *= 3  # Es equivalente a: a = a * 2
print(a)
a /= 3  # Es equivalente a: a = a / 3
print(a)
a %= 3  # Es equivalente a: a = a % 3
print(a)
a **= 3  # Es equivalente a: a = a ** 3
print(a)
a //= 3  # Es equivalente a: a = a // 3
print(a)

a = 5
a &= 3  # Es equivalente a: a = a & 3
print(a)
a |= 3  # Es equivalente a: a = a | 3
print(a)
a ^= 3  # Es equivalente a: a = a ^ 3
print(a)
a >>= 3  # Es equivalente a: a = a >> 3
print(a)
a <<= 3  # Es equivalente a: a = a << 3
print(a)


# OPERADORES ARITMETICOS - Devuelven un cálculo
# Suma(+)
print(1 + 2)
# Resta(-)
print(2 - 1)
# Multiplicación (*)
print(2 * 3)
# División (/)
print(6 / 2)
# División parte entera (//)
print(5 // 2)
# Módulo o Resto de la división(%)
print(5 % 2)
# Potencia (**)
print(3**2)


# OPERADORES DE COMPARACION - Devuelven True o False
# Igual (==)
print(1 == 1)
# No igual (!=)
print(1 != 2)
# Mayor (>)
print(3 > 2)
# Mayor o igual (>=)
print(2 >= 2)
# Menor (<)
print(2 < 3)
# Menor o igual (<=)
print(3 <= 3)

# OPERADORES LOGICOS - Devuelven True o False
# AND - True si se cumplen ambas condiciones
if 1 == 1 and 2 == 2:
    print("AND - True")
# OR - True si se cumple alguna de las condiciones
if 1 == 0 or 1 == 1:
    print("OR - True")
# NOT - True si alguno de los operandos es False
if not 1 == 2:
    print("NOT - True")


# OPERADORES DE BIT
print(1 & 2)  # Binario: 01 AND 10 = 00
print(1 | 2)  # Binario: 01 OR 10 = 11
print(1 ^ 2)  # Binario: 01 XOR 10 = 11
value1 = int("01", 2)
print(bin(~value1))  # Binario NOT (invierte cada bit) ~(01) = -10
# Desplaza bits de operador de la izquierda a derecha los bits que indica operador de la derecha
print(3 >> 1)
# Desplaza los bits del operando de la izquierda a la izquierda tantos bits como especifique el operador de la derecha
print(2 << 1)


# OPERADORES DE PERTENENCIA - Devuelven True o False
lista = [1, 2, 3, 4, 5]
# IN - True si el valor especificado se encuentra en una secuencia
if 5 in lista:
    print("el 5 está en la lista")
# NOT IN - True si el valor especificado no se encuentra en una secuencia
if 6 not in lista:
    print("el 6 NO está en la lista")

# OPERADORES DE IDENTIDAD - Devuelven True o False
lista2 = lista
lista3 = [1, 2, 3, 4, 5]
# IS - True si los operandos hacen referencia al mismo objeto
print(lista is lista2)
# IS NOT - True si los operandos no hacen referencia al mismo objeto
print(lista is not lista3)
# NOTA: lista y lista2 son el mismo objeto, lista y lista3 son iguales, pero no son el mismo objeto

# ESCTRUCTURAS CONDICIONALES
# IF-ELIF-ELSE
if 5 in lista:
    print("primer condicion")
elif 6 in lista:
    print("primer condicion")
else:
    print("Si no se cumple nada de lo anterior, se sale por aqui")

# MATCH-CASE - A partir de la version 3.10
condicion = 10
match condicion:
    case 11:
        print("Si se cumple, entra aqui")
    case 10:
        print("En este caso, entrara aqui")
    case _:
        print("Si no se cumple nada de lo anterior, se sale por aqui")


# ESTRUCTRUAS ITERATIVAS
# Bucle FOR
for elemento in lista:
    print(elemento)
# Bucle WHILE
contador = 0
while contador < 10:
    print(contador)
    contador += 1

# CONTROL DE ERRORES
# TRY-EXCEPT
try:
    a = 2 + "a"
except TypeError:
    print("Tipos no soportados para la operacion +")
else:
    print(a)  # Si no da error, se ejecuta esta parte [OPCIONAL]
finally:
    print("Se sale del try")  # Si se incluye este bloque, se ejecuta siempre [OPCIONAL]


# EJEMPLOS EXTRA
for _ in range(10, 55):
    if _ % 2 == 0:
        if _ != 16:
            if _ % 3 != 0:
                print(f"{_}, ", end="")

print("\n")

for _ in range(10, 55, 2):
    if _ != 16 and _ % 3 != 0:
        print(f"{_}, ", end="")

print("\n")

a = 10
while a <= 55:
    if a != 16 and a % 3 != 0:
        print(f"{a}, ", end="")

    a += 2
