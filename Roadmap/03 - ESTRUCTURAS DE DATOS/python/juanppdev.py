# Listas

## Creación
mi_lista = [1, 2, 3, 4, 5]

## Inserción
mi_lista.append(6) # Agrega el elemento 6 al final de la lista
mi_lista.insert(2, 10) # Inserta el elemento 10 en la posición 2

## Borrado
mi_lista.pop() # Elimina y devuelve el último elemento de la lista
mi_lista.pop(2) # Elimina y devuelve el elemento en la posición 2
del mi_lista[1] # Elimina el elemento en la posición 1

## Actualización
mi_lista[0] = 20 # Actualiza el valor del elemento en la posición 0 a 20

## Ordenación
mi_lista.sort() # Ordena los elementos de la lista de menor a mayor
mi_lista.sort(reverse=True) # Ordena los elementos de la lista de mayor a menor

# Tuplas

## Creación
mi_tupla = (1, 2, 3, 4, 5)

"""
    Inserción y borrado:

Como las tuplas son inmutables, no se pueden realizar operaciones de inserción o borrado directamente. Sin embargo, se pueden crear nuevas tuplas a partir de las existentes.

Actualización:

Como las tuplas son inmutables, no se pueden realizar operaciones de actualización directamente.

Ordenación:

Como las tuplas son ordenadas, se pueden ordenar de la misma manera que las listas.
"""

# Conjuntos

## Creación
mi_conjunto = {1, 2, 3, 4, 5}

## Inserción
mi_conjunto.add(6) # Agrega el elemento 6 al conjunto

## Borrado
mi_conjunto.remove(3) # Elimina el elemento 3 del conjunto

"""
    Actualización:

No se pueden realizar operaciones de actualización directamente en los conjuntos, ya que solo pueden contener elementos únicos.

Ordenación:

Los conjuntos no están ordenados, pero se pueden convertir en listas y ordenarlas.
"""

# Diccionarios

## Creación
mi_diccionario = {'clave1': 1, 'clave2': 2, 'clave3': 3}

## Inserción
mi_diccionario['clave4'] = 4 # Agrega la clave-valor ('clave4', 4) al diccionario

## Borrado
del mi_diccionario['clave2'] # Elimina la clave-valor ('clave2', 2) del diccionario

## Actualización
mi_diccionario['clave1'] = 20 # Actualiza el valor de la clave 'clave1' a 20

"""
    Ordenación:

Los diccionarios no están ordenados, pero se pueden convertir en listas de tuplas y ordenarlas.
"""

## Ejercicio Extra
# Agenda de contactos

import json

def cargar_contactos():
    """Carga los contactos desde un archivo JSON."""
    try:
        with open("contactos.json", "r") as f:
            contactos = json.load(f)
    except FileNotFoundError:
        contactos = {}
    return contactos

def guardar_contactos(contactos):
    """Guarda los contactos en un archivo JSON."""
    with open("contactos.json", "w") as f:
        json.dump(contactos, f)

def agregar_contacto():
    """Agrega un nuevo contacto a la agenda."""
    nombre = input("Nombre del contacto a agregar: ")
    if nombre not in contactos:
        telefono = input("Número de teléfono del contacto: ")
        contactos[nombre] = telefono
        guardar_contactos(contactos)
        print(f"\nSe ha agregado el contacto {nombre} a la agenda.")
    else:
        print(f"\nEl contacto {nombre} ya existe en la agenda.")

def buscar_contacto():
    """Busca un contacto por su nombre y muestra su número de teléfono."""
    nombre = input("Nombre del contacto a buscar (o deje en blanco para mostrar todos los contactos): ")
    if nombre == "":
        print("\nNombre\t\tTeléfono")
        print("----------------------------------")
        for nombre, telefono in contactos.items():
            print(f"{nombre}\t\t{telefono}")
    elif nombre in contactos:
        print(f"\nEl número de teléfono de {nombre} es {contactos[nombre]}")
    else:
        print(f"\nNo se encontró ningún contacto con el nombre {nombre}.")

def actualizar_contacto():
    """Actualiza el número de teléfono de un contacto existente."""
    nombre = input("Nombre del contacto a actualizar: ")
    if nombre in contactos:
        telefono = input("Nuevo número de teléfono del contacto: ")
        contactos[nombre] = telefono
        guardar_contactos(contactos)
        print(f"\nSe ha actualizado el contacto {nombre} en la agenda.")
    else:
        print(f"\nNo se encontró ningún contacto con el nombre {nombre}.")

def eliminar_contacto():
    """Elimina un contacto existente."""
    nombre = input("Nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        guardar_contactos(contactos)
        print(f"\nSe ha eliminado el contacto {nombre} de la agenda.")
    else:
        print(f"\nNo se encontró ningún contacto con el nombre {nombre}.")

contactos = cargar_contactos()

while True:
    print("\nAgenda de contactos")
    print("----------------------------------")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        agregar_contacto()
    elif opcion == 2:
        buscar_contacto()
    elif opcion == 3:
        actualizar_contacto()
    elif opcion == 4:
        eliminar_contacto()
    elif opcion == 5:
        break
    else:
        print("Opción inválida. Intente de nuevo.")

guardar_contactos(contactos)