# EJERCICIO:
# 1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
# Ten en cuenta que cada lenguaje puede poseer unos diferentes)
"""
Operadores
"""
print(10 + 5)   # Suma → 15
print(10 - 5)   # Resta → 5
print(10 * 5)   # Multiplicación → 50
print(10 / 5)   # División → 2.0
print(10 % 3)   # Módulo (resto) → 1
print(10 ** 2)  # Potencia → 100
print(10 // 3)  # División entera → 3

# Operadores de comparación
print(10 == 5)  # Igual a → False
print(10 != 5)  # Diferente de → True
print(10 > 5)   # Mayor que → True
print(10 < 5)   # Menor que → False
print(10 >= 10) # Mayor o igual → True
print(10 <= 5)  # Menor o igual → False

# Operadores lógicos
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
edad = 33

print(edad >= 18 and edad < 65)

# Operadores de asignación
numero = 10

numero += 5   # Equivale a: numero = numero + 5
numero -= 2   # Equivale a: numero = numero - 2
numero *= 3   # Equivale a: numero = numero * 3
numero /= 2   # Equivale a: numero = numero / 2
numero %= 3
numero **= 2
numero //= 2
print(numero)

# Operadores de identidad
# is
# is not
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]

print(lista1 is lista2)      # True
print(lista1 is lista3)      # False
print(lista1 is not lista3)  # True

# Operadores de pertenencia
# in
# not in
lenguajes = ["Python", "Java", "JavaScript"]

print("Python" in lenguajes)      # True
print("C++" in lenguajes)         # False
print("C++" not in lenguajes)     # True

# Operadores de bits
print(10 & 3)   # AND
print(10 | 3)   # OR
print(10 ^ 3)   # XOR
print(~10)      # NOT
print(10 << 2)  # Desplazamiento izquierda
print(10 >> 2)  # Desplazamiento derecha

# Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)
        

    
