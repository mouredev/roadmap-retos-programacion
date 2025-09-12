# TIPOS DE ESTRUCTURAS DE DATOS

## LISTAS -> colección de elementos ordenados y modificables
''' 
- Son accesibles por el indice 
- se pueden modificar 
- No tienen porque ser homogéneas
- No tienen un tamaño fijo (podemos añadir elementos)
- Se pueden iterar
- Se pueden ordenar
'''

mi_lista = [27, 13, 14, 66, 21]
print(mi_lista) 

# 1. Inserción
mi_lista.append(88) # con append añade un elemento en la ultima posicion de la lista
print(mi_lista)

mi_lista.insert(2, 30) # con insert podemos indicar el índice donde queremos introducir un elemento y el elemento a introducir
print(mi_lista)

# 2. Borrado
elemento_borrado = mi_lista.pop(2) # con pop eliminamos el elemento indicándole el índice
mi_lista.remove(13) # con remove eliminamos el elemento indicando su valor, no el índice
print(mi_lista)
print(elemento_borrado)

# 3. Actualización (modificación del elemento)
mi_lista[4] = 77
print(mi_lista)

# 4. Ordenación
lista_ordenada = sorted(mi_lista) # con sorted y guardándola en una nueva variable, evitamos modificar la original. 
# con sort -> mi_lista.sort() -> modificariamos la lista original
print(lista_ordenada)
print(mi_lista)


## TUPLAS -> colección de elementos ordenados e inmutables
''' 
- Son accesibles por el indice 
- No se pueden modificar 
- No tienen porque ser homogéneas
- Tienen un tamaño fijo 
- Se pueden iterar
- Se pueden ordenar
'''

mi_tupla = (44, 11, 77, 55, 99)
print(mi_tupla)

# 1. Inserción -> No se puede, una tupla es inmutable
# 2. Borrado -> No se puede, una tupla es inmutable. La única manera es eliminar la tupla completa con la palabra reservada ( del )
# 3. Actualización -> No se puede, una tupla es inmutable

# 4. Ordenación 
tupla_ordenada = sorted(mi_tupla)
print(tuple(tupla_ordenada))


## SETS (conjuntos) -> Una colección de elementos únicos e inmutables
''' 
- Son accesibles iterandolo 
- Se pueden modificar 
- No tienen porque ser homogéneas
- No tienen un tamaño fijo 
- Se pueden iterar
- No se pueden ordenar
'''

mi_set = {22, 88, 33, 66}
print(mi_set)

# 1. Inserción
mi_set.add(99) # con add se añade el elemento, pero no tiene una posicion (índidce) fijo
print(mi_set)
mi_set.update([1,2,3]) # con upadate([elementos]) podemos añadir varios elementos a la vez
print(mi_set)

# 2. Borrado
mi_set.remove(33) # se elimina el elemento indicado. Si no se encuentra arroja un error
print(mi_set)
mi_set.discard(3) # se elimina el elemento indicado. Este no arroja error si no se encuentra
print(mi_set)

# 3. Actualización -> no se puede modificar directamente indicando el elemento. Se debe borrar primero, y agregar el nuevo
# 4. Ordenación -> No se pueden ordenar ya que los conjuntos son no indexados e inmutables


## DICCIONARIOS -> Una colección modificable de pares clave-valor
''' 
- Son accesibles por claves 
- Se pueden modificar 
- No tienen porque ser homogéneas
- No tienen un tamaño fijo 
- Se pueden iterar
- No se pueden ordenar como tal, si no como una lista de tuplas ( lo ordena alfabeticamente por las claves )
'''

mi_diccionario = {
    "nombre": "Alejandro",
    "edad": 30,
    "ciudad": "Palma",
    "puntuacion": 27.27
}
print(mi_diccionario)

# 1. Inserción
mi_diccionario['ocupacion'] = 'Programador' # añadimos entre [] la clave, y igualamos al valor
print(mi_diccionario)

# 2. Borrado
del mi_diccionario['ciudad'] # con del eliminamos la clave, en consecuencia se elimina el par clave-valor
print(mi_diccionario)

# 3. Actualización
mi_diccionario['puntuacion'] = 95.27 # indicamos la clave de la cual queremos modificar el valor
print(mi_diccionario)

# 4. Ordenación
print("Diccionario ordenado:", sorted(mi_diccionario.items()))



# EJERCICIO EXTRA
import re

agenda = {}

while True:
    print("\n--- OPERACIONES AGENDA ---")
    print("1. Buscar contacto")
    print("2. Añadir contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")

    opcion = input("\nIngrese el número de la operación que desea realizar: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        if nombre in agenda:
            print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
        else:
            print(f"El contacto {nombre} no existe en la agenda.")

    elif opcion == '2':
        nombre = input("Ingrese el nombre del contacto: ")
        telf = input("Ingrese el número de teléfono: ")
        if re.match(r'^\d{1,11}$', telf):
            agenda[nombre] = telf
            print(f"Contacto {nombre} añadido correctamente.")
        else:
            print("Número de teléfono no válido. Debe ser numérico y tener entre 1 y 11 dígitos.")

    elif opcion == '3':
        nombre = input("Ingrese el nombre del contacto a actualizar: ")
        if nombre in agenda:
            telf = input("Ingrese el nuevo número de teléfono: ")
            if re.match(r'^\d{1,11}$', telf):
                agenda[nombre] = telf
                print(f"Contacto {nombre} actualizado correctamente.")
            else:
                print("Número de teléfono no válido. Debe ser numérico y tener entre 1 y 11 dígitos.")
        else:
            print(f"El contacto {nombre} no existe en la agenda.")

    elif opcion == '4':
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"Contacto {nombre} eliminado correctamente.")
        else:
            print(f"El contacto {nombre} no existe en la agenda.")

    elif opcion == '5':
        print("\n--- Lista de Contactos ---")
        for nombre, telf in agenda.items():
            print(f"Nombre: {nombre}, Telf: {telf}")

    elif opcion == '6':
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 6.")