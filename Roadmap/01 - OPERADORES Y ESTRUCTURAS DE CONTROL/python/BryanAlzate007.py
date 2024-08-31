# Operadores Aritméticos:

# +: Suma
# -: Resta
# *: Multiplicación
# /: División
# %: Módulo (residuo de la división)
# **: Exponenciación
# //: División entera (descarta la parte decimal)

print(f"Operador + ejemplo: 1 + 3 esto da como resultado: {1 + 3}")
print(f"Operador - ejemplo: 1 - 3 esto da como resultado: {1 - 3}")
print(f"Operador * ejemplo: 1 * 3 esto da como resultado: {1 * 3}")
print(f"Operador / ejemplo: 10 / 3 esto da como resultado: {10/3}")
print(f"Operador % ejemplo: 10 / 3 esto da como resultado: {10 % 3}")
print(f"Operador ** ejemplo: 10 ** 3 esto da como resultado:{10**3}")
print(f"Operador // ejemplo: 10 // 3 esto da como resultado: {10 // 3}")



# Operadores de Comparación:

# == Igual a
# != Diferente de
# > Mayor que
# < Menor que
# >= Mayor o igual que
# <= Menor o igual que

# el resultado de estos operadores nos devuelve un valor booleano true or false

print(f"Operador comparación == ejemplo 1 == 1 esto da como resultado: {1 == 1}")
print(f"Operador de comparación != ejemplo 1 != 1 esto da como resultado {1 != 1}")
print(f"Operador de comparación > ejemplo 10 > 1 esto da como resultado {10 > 1}")
print(f"Operador de comparación < ejemplo 10 > 1 esto da como resultado {10 < 1}")
print(f"Operador de comparación <= ejemplo 10 > 1 esto da como resultado {10 <= 1}")
print(f"Operador de comparación >= ejemplo 10 > 1 esto da como resultado {10 >= 1}")

#Operadores Logicos

# and: Verdadero si ambas condiciones son verdaderas
# or: Verdadero si al menos una condición es verdadera
# not: Invierte el valor de verdad

print(f"Operador and ejemplo 1 + 3 == 4 and 2 + 2 == 4{1 + 3 == 4 and 2 + 2 == 4}")
print(f"Operador and ejemplo 1 + 3 == 4 and 2 + 2 == 4{1 + 3 == 4 or 2 + 2 == 4}")
# print(f"Operador and ejemplo 1 + 3 == 4 and 2 + 2 == 4{1 + 3 == 4 not 2 + 2 == 4}")

x = 10
y = 5


x = 10
x += 5  # Equivalente a x = x + 5
print(x)  # Salida: 15

x = 10
x -= 3  # Equivalente a x = x - 3
print(x)  # Salida: 7

x = 10
x *= 2  # Equivalente a x = x * 2
print(x)  # Salida: 20

x = 10
x /= 2  # Equivalente a x = x / 2
print(x)  # Salida: 5.0

x = 10
x %= 3  # Equivalente a x = x % 3
print(x)  # Salida: 1

x = 2
x **= 3  # Equivalente a x = x ** 3
print(x)  # Salida: 8

x = 10
x //= 3  # Equivalente a x = x // 3
print(x)  # Salida: 3



a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # Salida: True, porque 'a' y 'b' apuntan al mismo objeto
print(a is c)  # Salida: False, porque 'a' y 'c' son objetos diferentes en memoria


print(a is not b)  # Salida: False, porque 'a' y 'b' apuntan al mismo objeto
print(a is not c)  # Salida: True, porque 'a' y 'c' son objetos diferentes en memoria



# Ejemplo con listas
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Salida: True, porque "banana" está en la lista 'fruits'

# Ejemplo con cadenas
sentence = "The quick brown fox"
print("quick" in sentence)  # Salida: True, porque "quick" está en la cadena 'sentence'

# Ejemplo con diccionarios
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}
print("Bob" in ages)  # Salida: True, porque "Bob" es una clave en el diccionario 'ages'


# Ejemplo con listas
fruits = ["apple", "banana", "cherry"]
print("grape" not in fruits)  # Salida: True, porque "grape" no está en la lista 'fruits'

# Ejemplo con cadenas
sentence = "The quick brown fox"
print("slow" not in sentence)  # Salida: True, porque "slow" no está en la cadena 'sentence'

# Ejemplo con diccionarios
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}
print("David" not in ages)  # Salida: True, porque "David" no es una clave en el diccionario 'ages'


a = 12  # 1100 en binario
b = 7   # 0111 en binario

result = a & b  # 0100 en binario, que es 4 en decimal
print(result)  # Salida: 4

a = 12  # 1100 en binario
b = 7   # 0111 en binario

result = a | b  # 1111 en binario, que es 15 en decimal
print(result)  # Salida: 15


a = 12  # 1100 en binario
b = 7   # 0111 en binario

result = a ^ b  # 1011 en binario, que es 11 en decimal
print(result)  # Salida: 11


a = 12  # 1100 en binario

result = ~a  # Inversión de bits, que es -13 en decimal (en el sistema de complemento a dos)
print(result)  # Salida: -13

a = 3  # 0011 en binario

result = a << 2  # Desplaza 2 posiciones a la izquierda, resultando en 1100 en binario, que es 12 en decimal
print(result)  # Salida: 12

a = 12  # 1100 en binario

result = a >> 2  # Desplaza 2 posiciones a la derecha, resultando en 0011 en binario, que es 3 en decimal
print(result)  # Salida: 3


# * DIFICULTAD EXTRA (opcional):
# * Crea un programa que imprima por consola todos los números comprendidos
# * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

# Iterar sobre el rango de números entre 10 y 55 (incluidos)
for num in range(10, 56):
    # Verificar si el número es par
    if num % 2 == 0:
        # Verificar que el número no sea el 16 y no sea múltiplo de 3
        if num != 16 and num % 3 != 0:
            print(num)
