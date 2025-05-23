"""
Iteraciones
"""


#For
for i in range(1,11):
    print(i)


#While
numero = 1

while numero <=10:
    print(numero)
    numero+=1


#Recursividad
def iteracion(num = 1) -> int:
    if num <=10:
        print(num)
        iteracion(num +1)

iteracion()


""" * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?"""


# Itera sobre una lista de letras y las imprime una por una
for i in ["a", "b", "c", "d"]:
    print(i)

# Itera sobre la lista al revés usando reversed()
for i in reversed(["a", "b", "c", "d"]):
    print(i)

# Itera sobre una lista ordenada alfabéticamente
for i in sorted(["C", "O", "M", "P", "L", "E", "X"]):
    print(i)

# Itera sobre una lista ordenada y a la vez muestra su índice y valor usando enumerate()
for i, e in enumerate(sorted(["C", "O", "M", "P", "L", "E", "X"])):
    print(f"indice: {i}, valor: {e}")

# Itera sobre un conjunto (set)
for i in {1, 2, 3, 4}:
    print(i)

# Itera sobre una tupla
for i in (1, 2, 3, 4):
    print(i)


# Itera sobre un diccionario, obteniendo clave y valor al mismo tiempo
dictionario: dict = {1: "a", 2: "b", 3: "c"}
for key, value in dictionario.items():
    print(key, "-", value)

# Itera solo por las claves de un diccionario
for key in {1: "a", 2: "b", 3: "c"}.keys():
    print(key)

# Itera solo por los valores de un diccionario
for value in dictionario.values():
    print(value)


# Imprime del 1 al 10 usando comprensión de lista + desempaquetado * y separador de línea
print(*[i for i in range(1, 11)], sep="\n")

# [i for i in range(1, 11)] genera una lista del 1 al 10.
# * desempaqueta la lista para pasar cada elemento como argumento a print.
# sep="\n" hace que cada elemento se imprima en una línea distinta.

# Itera sobre una cadena carácter por carácter
for i in "python":
    print(i)


