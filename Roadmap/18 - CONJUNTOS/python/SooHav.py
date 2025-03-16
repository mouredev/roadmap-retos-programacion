# 18 CONJUNTOS
"""Ejercicio"""

# Crear un conjunto de datos
mi_conjunto = []

# Añadir un elemento al final
mi_conjunto.append(1)
print(mi_conjunto)

# Añadir un elemento al principio
mi_conjunto.insert(0, 0)
print(mi_conjunto)

# Añadir varios elementos en bloque al final
mi_conjunto.extend([2, 3, 6])
print(mi_conjunto)

# Añadir varios elementos en bloque en una posición concreta
mi_conjunto[4:4] = [4, 5]
print(mi_conjunto)

# Eliminar un elemento en una posición concreta
del mi_conjunto[6]
print(mi_conjunto)

# Actualizar el valor de un elemento en una posición concreta
mi_conjunto[0] = "a"
print(mi_conjunto)

# Comprobar si un elemento está en un conjunto
elemento = 4
try:
    mi_conjunto.index(elemento)
    print(f"{elemento} está en el conjunto")
except ValueError:
    print(f"{elemento} no está en el conjunto")

# Eliminar todo el contenido del conjunto
mi_conjunto.clear()

print(mi_conjunto)

"""Extra"""
# Unión de conjuntos en Python
a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print(a | b)

# Intersección de conjuntos en Python
a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print(a & b)

# Diferencia de conjuntos en Python
a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print(a - b)

# Diferencia simétrica de conjuntos en Python
a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print(a ^ b)

"""Prueba de programa con el primer ejercicio"""
while True:
    print("\nMenú:")
    print("0. Crea un conjunto de elementos")
    print("1. Inserta elemento/s al final")
    print("2. Inserta elemento/s al inicio")
    print("3. Inserta elemento/s en una posición")
    print("4. Elimina elemento en una posición")
    print("5. Actualiza elemento en una posición")
    print("6. Comprueba si un elemento está")
    print("7. Elimina todo el contenido")
    print("8. Sale del programa")

    opcion = input("Seleccione una opción: ")

    if opcion == "0":
        mi_conjunto = list()
        opcion_conjunto = type(mi_conjunto)
        print(f"Se ha creado un conjunto de tipo {opcion_conjunto}")

    elif opcion == "1":
        elementos = input(
            "Ingresa el/los elemento/s separados por comas:\n").split(",")
        nuevo_elemento = []
        for i in elementos:
            i = i.strip()
            if i.isdigit():
                nuevo_elemento.append(int(i))
            elif i.replace('.', '', 1).isdigit():
                nuevo_elemento.append(float(i))
            else:
                nuevo_elemento.append(i)
        mi_conjunto.extend(nuevo_elemento)
        print(mi_conjunto)

    elif opcion == "2":
        elemento = input(
            "Ingresa el/los elemento/s separados por comas:\n").split(",")
        nuevo_elemento = []
        for i in elemento:
            i = i.strip()
            if i.isdigit():
                nuevo_elemento.append(int(i))
            elif i.replace('.', '', 1).isdigit():
                nuevo_elemento.append(float(i))
            else:
                nuevo_elemento.append(i)
        mi_conjunto = nuevo_elemento + mi_conjunto
        print(mi_conjunto)

    elif opcion == "3":
        elemento = input("Ingresa el/los elemento/s:\n").split(",")
        nuevo_elemento = []
        for i in elemento:
            i = i.strip()
            if i.isdigit():
                nuevo_elemento.append(int(i))
            elif i.replace('.', '', 1).isdigit():
                nuevo_elemento.append(float(i))
            else:
                nuevo_elemento.append(i)
        indice = int(input("Ingresa la posición:\n"))
        mi_conjunto[indice:indice] = nuevo_elemento
        print(mi_conjunto)

    elif opcion == "4":
        indice = int(input("Ingresa la posición:\n"))
        mi_conjunto.pop(indice)
        print(mi_conjunto)

    elif opcion == "5":
        elemento = input("Ingresa el elemento a actualizar:\n")
        try:
            elemento_num = int(elemento)
        except ValueError:
            try:
                elemento_num = float(elemento)
            except ValueError:
                elemento_num = elemento
        indice = int(input("Ingresa la posición:\n"))
        mi_conjunto[indice] = elemento_num
        print(mi_conjunto)

    elif opcion == "6":
        elemento = input("Ingresa el elemento:\n")
        try:
            mi_conjunto.index(elemento)
            print(f"{elemento} está en el conjunto")
        except ValueError:
            print(f"{elemento} no está en el conjunto")

    elif opcion == "7":
        mi_conjunto.clear()
        print(mi_conjunto)

    elif opcion == "8":
        print("Saliendo del programa")
        break
