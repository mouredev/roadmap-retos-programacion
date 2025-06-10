# 03 - Python

# Estructuras de datos y operaciones básicas

# List - conjunto de elementos
list = [1, 2, 3, 4, 5]
list.append(6) # Operación de inserción
list.insert(0, 0) # Operación de inserción
list.remove(6) # Operación de borrado
list[0] = 0 # Operación de actualización
list.sort() # Operación de ordenación
list.reverse() # Operación de ordenación inversa

# Turple - conjunto inmutable de elementos, sin operaciones
tuple = (1, 2, 3, 4, 5)
sorted(tuple) # Operación de ordenación

# Set - conjunto único de elementos, sin duplicados
set_element = {1, 2, 3, 4, 5}
set_element.add(6) # Operación de inserción
set_element.discard(6) # Operación de borrado

# Dictionary - conjunto de elementos tipo key,value
dictionary = {"one": 1, "two": 2, "three": 3}
dictionary["four"] = 4 # Operación de inserción
dictionary.pop("four") # Operación de borrado
dictionary["one"] = 0 # Operación de actualización
dictionary.update({"five": 5}) # Operación de actualización

from collections import deque

# Heap - Binary Tree
heap = [1, 5, 3, 4, 2, 8, 7, 9]

# Stacks and queues
stack = deque([1, 2, 3, 4, 5])



# EXTRA: Agenda de contactos

# Crear contacto; dictionary con nombre y número de teléfono
contactos = {}
# Menú de opciones
run = True
while run:
    print("*** Agenda de contactos ***")
    print("Elija una opción:")
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    try:
        opcion = int(input())
        if opcion == 1:
            nombre = input("Ingrese el nombre del contacto: ")
            if nombre in contactos:
                print(f"{nombre}: {contactos[nombre]}")
            else:
                print("Contacto no encontrado.")
        elif opcion == 2:
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            if telefono.isdigit() and len(telefono) <= 11:
                contactos[nombre] = int(telefono)
                print("Contacto agregado.")
            else:
                print("Número de teléfono inválido.")
        elif opcion == 3:
            nombre = input("Ingrese el nombre del contacto: ")
            if nombre in contactos:
                telefono = input("Ingrese el nuevo número de teléfono: ")
                if telefono.isdigit() and len(telefono) <= 11:
                    contactos[nombre] = int(telefono)
                    print("Contacto actualizado.")
                else:
                    print("Número de teléfono inválido.")
            else:
                print("Contacto no encontrado.")
        elif opcion == 4:
            nombre = input("Ingrese el nombre del contacto: ")
            if nombre in contactos:
                del contactos[nombre]
                print("Contacto eliminado.")
            else:
                print("Contacto no encontrado.")
        elif opcion == 5:
            print("Saliendo...")
            run = False
        else:
            print("Opción no válida.")
    except ValueError:
        print("Por favor, ingrese un número válido.")