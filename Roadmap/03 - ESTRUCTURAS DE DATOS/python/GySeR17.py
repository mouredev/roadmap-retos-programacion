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

print("===============================")
print("          1. Listas")
print("===============================")
# Es la estructura mas usada, esta es ordenada modificable y permite duplicados.

lista_1 = ["manzana", "banana", "cereza", "mora", "frutilla"]

print(lista_1)
print(lista_1[0])  # Acceder al primer elemento
print(lista_1[-1])  # Acceder al último elemento
print(lista_1[2])  # Acceder a un elemento específico

print("\nInsertar naranja al final")
lista_1.append("naranja")  # Inserción al final
print(lista_1) #Actualizacion de la lista

print("\nInsertar naranja al final x2")
lista_1.append("naranja")  # Inserción al final x2
print(lista_1) #Actualizacion de la lista con duplicados

print("\nInsertar kiwi en posicion especifica")
lista_1.insert(2, "kiwi")  # Inserción en una posición específica
print(lista_1) #Actualizacion de la lista 2

print("\nActualizar informacion de la lista")
lista_1[0] = "pera"  # Actualización de un elemento específico
print(lista_1) #Actualizacion de la lista 3

print("\nContar un elemento por el numero de veces que aparece en la lista")
print(f"El numero de veces que aparece 'naranja' en la lista es: {lista_1.count('naranja')}")  # Contar el numero de veces que aparece "naranja" en la lista


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

print("\nInvertir el orden de la lista como esta")
lista_2.reverse()  # Ordenación de la lista en orden inverso (orden alfabetico, tomando en cuenta mayusculas y minusculas por convencion ASCII)
print(lista_2) #Actualizacion de la lista 10

print("\nOrdenar elementos de la lista")
lista_2.sort()  # Ordenación de la lista por defecto (orden alfabetico, tomando en cuenta mayusculas y minusculas por convencion ASCII)
print(lista_2) #Actualizacion de la lista 11

print("\nOrdenar elementos de la lista")
lista_2.sort(reverse=True)  # Ordenación de la lista en orden inverso (orden alfabetico, tomando en cuenta mayusculas y minusculas por convencion ASCII)
print(lista_2) #Actualizacion de la lista 12

print("\nBuscar elementos por su indice")
busca = lista_2.index("cereza")
print(lista_2[busca])  # Buscar el elemento por su indice
print(f"El indice de '{lista_2[busca]}' es: {busca}")  # Buscar el indice de un elemento específico

lista_3 = lista_2.copy()  # Copiar la lista
print("\nLista 3 copiada de la lista 2")
print(lista_3)

print("\n===============================")
print("          2. Tuplas")
print("===============================")
#Es una coleccion ordenada por inmutable.

coordenadas = (10.0, 20.0, 30.0)
print(coordenadas)
print(coordenadas[0])  # Acceder al primer elemento

print("\nIntentar insertar un elemento en la tupla")
try:
    print(coordenadas.append(35.5))  # No se puede insertar elementos en una tupla, ya que es inmutable
except AttributeError as e:
    print(f"Error: {e}")


print("\nActualizacion de elementos no existe en la tupla")
try:
    coordenadas[0] = 15.0  # No se puede actualizar elementos en una tupla, ya que es inmutable
except TypeError as e:
    print(f"Error: {e}")    


print("\nBorrado de elementos no existe en la tupla")
try:
    del coordenadas[0]  # No se puede borrar elementos en una tupla, ya que es inmutable
except TypeError as e:
    print(f"Error: {e}") 


print("\n===============================")
print("          3. SETS (Conjuntos)")
print("===============================")
# Es una coleccion sin elementos duplicados, desordenada y no indexada(no puedes acceder mediante indices alos valores).
# Esta coleccion soporta operaciones matematicas como union, interseccion, diferencia.

usuarios = {"Juan", "Maria", "Pedro", "Ana", "Luis", "Sergio", "Paola"}
usuarios_2 = {"Roberto", "Luis", "Sofia", "Vanessa", "Martin", "Joel"}
print(usuarios)

print("\nInsertar un elemento en el conjunto")
usuarios.add("Juan Carlos")  # Inserción de un elemento en el conjunto
print(usuarios)

print("\nIntentar insertar un elemento duplicado en el conjunto")
usuarios.add("Juan")  # No se puede insertar elementos duplicados en un conjunto
print(f"No hay doble 'Juan' en: {usuarios}")

print("\nNo existe eliminacion directa de un elemento, se debe eliminar mediante el metodo remove() o discard()")
usuarios.remove("Sergio")  # Eliminación de un elemento en el conjunto
print(usuarios)

usuarios.add("Joel")  # Inserción de un elemento en el conjunto
print(usuarios)
usuarios.discard("Joel")  # Eliminación de un elemento en el conjunto
print(usuarios)

print("\nLos sets no son ordenados, por lo que no se puede acceder a un elemento mediante su indice")
print(f"primera iteracion: {usuarios}")

print("\nPara verlos ordenados se puede crear una lista a partir del set y ordenarla")
print(sorted(usuarios))

print("\nOperaciones matematicas con conjuntos")

print(f"\nUsuarios 1: {usuarios}")
print(f"Usuarios 2: {usuarios_2}")

print(f"\nUnion: {usuarios.union(usuarios_2)}")
print(f"\nInterseccion: {usuarios.intersection(usuarios_2)}")
print(f"\nDiferencia: {usuarios.difference(usuarios_2)}")


print("\nFROZEN SETS")
print("\nVersion inmutable de un set")
set_1 = frozenset(["Juan", "Maria", "Pedro", "Ana", "Luis", "Sergio", "Paola"])
print(set_1)


print("\n===============================")
print("          4. DICCIONARIOS")
print("===============================")
# Esta coleccion guarda pares de clave-valor, ordenados desde python 3.7, modificable y no permite duplicados.

persona = {
    "nombre": "Joel",
    "edad": 30
}

print(persona)
print(f"Nombre: {persona['nombre']}")  # Acceder al valor de una clave
print(f"Edad: {persona['edad']}")    # Acceder al valor de una clave

print("\nInsertar un elemento en el diccionario")
persona["País"] = "Bolivia"
persona["ciudad"] = "Sucre"  # Inserción de elementos en el diccionario
print(persona)

print("\nActualizar un elemento en el diccionario")
persona["edad"] = 31  # Actualización de un elemento en el diccionario
print(persona)

print("\nEliminar un elemento del diccionario")
del persona["ciudad"]  # Eliminación de un elemento del diccionario
print(persona)
persona["ciudad"] = "Sucre"
persona.pop("ciudad")  # Eliminación de un elemento del diccionario con pop
print(persona)

print("\nDesde python 3.7 los diccionarios son ordenados, por lo que se puede acceder a un elemento mediante su clave")
dict_1 = {
    "a": 2,
    "j": 5,
    "x": 2,
    "d": 3
    
}

print("\nOrdenar el diccionario por clave")
for key in sorted(dict_1):  # Ordenar el diccionario por clave
    print(key, dict_1[key])


print("\nOrdenar el diccionario por valor")
for key, valor in sorted(dict_1.items(), key=lambda item: item[1]):  # Ordenar el diccionario por clave
    print(key, valor)

"""

Se deben usar segun la situacion y su requerimiento:
Situacion                               Estructura
Lista de clientes                       List
Coordenadas GPS                         Tuplas
Usuarios unicos                         set
Cliente -> datos                        diccionario

"""
