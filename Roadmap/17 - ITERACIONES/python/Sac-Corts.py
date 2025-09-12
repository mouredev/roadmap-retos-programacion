# Iterar sobre una lista con bucle for
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for elemento in mi_lista:
    print(elemento)

# Iterar con range()
for i in range(11):
    print(i)

# Iterar con while 
i = 0
while i <= 10:
    print(i)
    i += 1

### Ejercicio Extra ###

# Iterar sobre un diccionario
mi_diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for clave in mi_diccionario:
    print(clave)

for valor in mi_diccionario.values():
    print(valor)

for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

# Iterar sobre conjuntos
mi_conjunto = {1, 2, 3, 4, 5}
for elemento in mi_conjunto:
    print(elemento)

# Iterar sobre una cadena de texto
mi_cadena = "Hola Mundo"
for caracter in mi_cadena:
    print(caracter)

# Iterar sobre una lista con índices
mi_lista = [1, 2, 3, 4, 5]
for i in range(len(mi_lista)):
    print(f"Índice: {i}, Elemento: {mi_lista[i]}")

# Iterar sobre una lista con enumerate()
mi_lista = ['a', 'b', 'c', 'd', 'e']
for indice, elemento in enumerate(mi_lista):
    print(f"Índice: {indice}, Elemento: {elemento}")

# Iterar sobre varias listas usando zip()
nombres = ["Isaac", "Geovanni", "Sac"]
edades = [22, 30, 16]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# Iterar sobre archivos línea por línea
file_name = "archivo.txt"
file = open(file_name, "w")
name = "Isaac Cortés"
age = 22
language = "Python"

file.write(f"Nombre: {name}\n")
file.write(f"Edad: {age}\n")
file.write(f"Lenguaje de programación: {language}\n")

file.close()

with open('archivo.txt', 'r') as archivo:
    for linea in archivo:
        print(linea.strip())

# Iterar sobre generadores 
def generador():
    for i in range(6):
        yield i

for valor in generador():
    print(valor)

# Iterar sobre comprensiones
mi_lista = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in mi_lista]
print(cuadrados)

# Iterar con recursividad
def contador(i = 1):
    if i <= 10:
        print(i)
        contador(i + 1)

contador()