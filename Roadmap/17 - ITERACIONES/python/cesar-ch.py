"""
    * #17 ITERACIONES
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1. Bucle for
for i in range(len(numeros)):
    print(numeros[i])

# 2. Bucle while
i = 0
while len(numeros) < 10:
    print(numeros[i])
    i += 1

# 3. Bucle for with step
for i in range(0, 10, 2):
    print(numeros[i])

"""
    * DIFICULTAD EXTRA
"""

# 4. Bucle with lambda
numeros.sort(key=lambda x: x)
print(numeros)

# 5. Bucle with enumerate
for i, numero in enumerate(numeros):
    print(numero)

# 6. Bucle with zip
for i, numero in enumerate(zip(numeros, numeros)):
    print(numero)

# 7. Bucle with filter
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

# ...
