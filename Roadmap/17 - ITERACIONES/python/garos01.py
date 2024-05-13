# Método 1: Utilizando un bucle for
print("Metodo 1: Utilizando un bucle for")
for i in range(1, 11):
    print(i)


# Método 2: Utilizando un bucle while
print("Metodo 2: Utilizando un bucle while")
i = 1
while i <= 10:
    print(i)
    i += 1


# Metodo 3: Simulando un bucle do while en Python
print("Metodo 3: Simulando un bucle do while en Python")
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break


# Ejercicio extra

# Bucle for con range()
print("Bucle for con range():")
for i in range(1, 11):
    print(i)

# Bucle for con elementos de una lista
print("\nBucle for con elementos de una lista:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numeros:
    print(num)

# Bucle for con elementos de una tupla
print("\nBucle for con elementos de una tupla:")
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for num in numeros:
    print(num)

# Bucle for con elementos de un conjunto (set)
print("\nBucle for con elementos de un conjunto (set):")
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
for num in numeros:
    print(num)

# Bucle for con elementos de un diccionario
print("\nBucle for con elementos de un diccionario:")
numeros = {
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve",
    10: "diez",
}
for key, value in numeros.items():
    print(key, value)

# Utilizando la función map() junto con print()
print("\nUtilizando la función map() junto con print():")
numeros = list(range(1, 11))
print(*map(str, numeros), sep="\n")

# Utilizando una comprensión de lista
print("\nUtilizando una comprensión de lista:")
[num for num in range(1, 11)]

# Utilizando el operador enumerate()
print("\nUtilizando el operador enumerate():")
for idx, num in enumerate(range(1, 11)):
    print(idx + 1, num)

# Utilizando la función itertools.count()
print("\nUtilizando la función itertools.count():")
import itertools

for num in itertools.count(start=1, step=1):
    if num > 10:
        break
    print(num)

# Utilizando un iterador personalizado
print("\nUtilizando un iterador personalizado:")


class Contador:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


contador = Contador(1, 10)
for num in contador:
    print(num)
