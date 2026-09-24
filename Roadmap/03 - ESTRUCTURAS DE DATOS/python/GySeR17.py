# #03 ESTRUCTURAS DE DATOS
#### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

## Ejercicio

'''
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
'''

"""
Las estructuras de datos son formas de organizar y almacenar informacion para poder:
- Acceder
- Modificar
- Buscar
- Eliminar
Informacion de manera eficiente.
Las 4 estructuras principales en python son:
1. Listas
2. Tuplas
3. Conjuntos
4. Diccionarios
"""

print("1. Listas")
# Es la estructura mas usada, esta es ordenada modificable y permite duplicados.

lista_1 = ["manzana", "banana", "cereza", "mora", "frutilla"]

print(lista_1)
print(lista_1[0])  # Acceder al primer elemento
print(lista_1[-1])  # Acceder al último elemento
print(lista_1[2])  # Acceder a un elemento específico

print("\nInsertar naranja al final")
lista_1.append("naranja")  # Inserción al final
print(lista_1) #Actualizacion de la lista

print("\nInsertar kiwi en posicion especifica")
lista_1.insert(2, "kiwi")  # Inserción en una posición específica
print(lista_1) #Actualizacion de la lista 2

print("\nActualizar informacion de la lista")
lista_1[0] = "pera"  # Actualización de un elemento específico
print(lista_1) #Actualizacion de la lista 3

print("\nEliminar banana por valor")
lista_1.remove("banana")  # Borrado de un elemento especifico por valor
print(lista_1) #Actualizacion de la lista 4


print("\nEliminar mora por indice")
lista_1.remove(lista_1[3])  # Borrado de un elemento especifico por indice
print(lista_1) #Actualizacion de la lista 5

print("\nEliminar frutilla por funcion 'del'")
del lista_1[3]  # Borrado de un elemento especifico por indice
print(lista_1) #Actualizacion de la lista 6

print("\nEliminar kiwi por funcion 'pop'")
print(lista_1.pop(1))  # Borrado de un elemento especifico por indice y retorno del elemento eliminado
print(lista_1) #Actualizacion de la lista 7

print("\nEliminar naranja por funcion 'pop 2'")
print(lista_1.pop())  # Borrado del ultimo elemento de la lista y retorno del elemento eliminado
print(lista_1) #Actualizacion de la lista 8

print("\nEliminar todos los elementos de la lista")
lista_1.clear()  # Borrado de todos los elementos de la lista
print(lista_1) #Actualizacion de la lista 9

lista_2 = ["manzana", "Banana", "bergamota", "cereza", "mora", "frutilla", "aguacate", "Albaricoque"]

print("\nOrdenar elementos de la lista")
lista_2.sort()  # Ordenación de la lista por defecto (orden alfabetico, tomando en cuenta mayusculas y minusculas por convencion ASCII)
print(lista_2) #Actualizacion de la lista 9

print("\nOrdenar elementos de la lista")
lista_2.sort(reverse=True)  # Ordenación de la lista en orden inverso (orden alfabetico, tomando en cuenta mayusculas y minusculas por convencion ASCII)
print(lista_2) #Actualizacion de la lista 10



