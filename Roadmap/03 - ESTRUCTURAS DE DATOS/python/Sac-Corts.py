"""
  EJERCICIO
"""
# Listas
mi_lista = [5, 2, 9, 1, 5, 6]
# Inserción
mi_lista.append(3)  # Añade el elemento 3 al final
print(".append:", mi_lista)
mi_lista.insert(1, 4)  # Inserta el elemento 4 en la posición 1
print(".insert:", mi_lista)
# Borrado
mi_lista.remove(5)  # Elimina la primera ocurrencia del elemento 5
print(".remove:", mi_lista)
elemento = mi_lista.pop(2)  # Elimina el elemento en la posición 2 y lo retorna
print(".pop", mi_lista)
# Actualización
mi_lista[0] = 10  # Actualiza el primer elemento a 10
print("Actualización:", mi_lista)
# Ordenación
mi_lista_ordenada = sorted(mi_lista)  # Retorna una nueva lista ordenada
print("Lista ordenada:", mi_lista_ordenada)
mi_lista.sort()  # Ordena la lista en su lugar
print(".sort:", mi_lista)

# Tuplas
mi_tupla = (5, 2, 9, 1, 5, 6)
# Las tuplas son inmutables, por lo que no se pueden modificar directamente. Sin embargo, se pueden crear nuevas tuplas combinando otras. ###
# Actualización (crear una nueva tupla)
nueva_tupla = mi_tupla[:2] + (10,) + mi_tupla[3:]
# Ordenación
tupla_ordenada = tuple(sorted(mi_tupla))
print("Tupla original:", mi_tupla)
print("Nueva tupla:", nueva_tupla)
print("Tupla ordenada:", tupla_ordenada)

# Conjuntos o Sets
mi_conjunto = {5, 2, 9, 1, 5, 6}
print("Conjunto:", mi_conjunto)
# Inserción
mi_conjunto.add(3)  # Añade el elemento 3
print(".add:", mi_conjunto)
# Borrado
mi_conjunto.remove(5)  # Elimina el elemento 5
print(".remove:", mi_conjunto)
mi_conjunto.discard(7)  # Elimina el elemento 7 si existe, si no, no hace nada
print(".discard:", mi_conjunto)
### Actualización ###
# No se puede actualizar un elemento específico en un conjunto, pero se pueden añadir y eliminar elementos.
# Ordenación (crear una lista ordenada a partir del conjunto)
conjunto_ordenado = sorted(mi_conjunto)
print("Conjunto ordenado:", conjunto_ordenado)

# Diccionarios
mi_diccionario = {'a': 5, 'b': 2, 'c': 9, 'd': 1}
print("Diccionario:", mi_diccionario)
# Inserción
mi_diccionario['e'] = 6  # Añade un nuevo par clave-valor
print("Inserción:", mi_diccionario)
# Borrado
del mi_diccionario['b']  # Elimina el par con clave 'b'
print("del:", mi_diccionario)
valor = mi_diccionario.pop('c')  # Elimina el par con clave 'c' y retorna su valor
print(".pop:", mi_diccionario)
# Actualización
mi_diccionario['a'] = 10  # Actualiza el valor asociado a la clave 'a'
print("Actualización:", mi_diccionario)
# Ordenación (crear una lista de claves ordenadas)
claves_ordenadas = dict(sorted(mi_diccionario.items()))
print("Claves ordenadas:", claves_ordenadas)

"""
DIFICULTAD EXTRA
"""
contactos = {}

# Función para mostrar menú
def mostrar_menu():
    print("\nAgenda de Contactos")
    print("1. Insertar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    return input("Selecciona una opción: ")

# Función para validar el número de teléfono
def validar_numero(telefono):
    if telefono.isdigit() and 1 <= len(telefono) <= 11:
        return True
    else: 
        return False 

# Función para insertar un contacto
def insertar_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce el número de teléfono del contacto (máximo 11 dígitos): ")
    if validar_numero(telefono):
        contactos[nombre] = telefono
        print(f"Contacto {nombre} añadido.")
    else: 
        print("Número de teléfono no válido. Debe ser numérico y no exceder 11 dígitos.")
     
# Función para buscar un contacto
def buscar_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in contactos:
        print(f"Nombre: {nombre}, Teléfono: {contactos[nombre]}")
    else:
        print(f"El contacto {nombre} no está en la agenda.`")

# Función para actualizar un contacto
def actualizar_contacto():
    nombre = input("Introduce el nombre del contacto que deseas actualizar: ")
    if nombre in contactos: 
        nuevo_telefono = input("Introduce el nuevo número de teléfono (máximo 11 dígitos): ")
        if validar_numero(nuevo_telefono):
            contactos[nombre] = nuevo_telefono
            print(f"Contacto {nombre} actualizado.")
        else: 
            print("Número de teléfono no válido. Debe ser numérico y no exceder 11 dígitos.")
    else: 
        print(f"El contacto {nombre} no está en la agenda.")

# Función para eliminar un contacto
def eliminar_contacto():
    nombre = input("Introduce el nombre del contacto que deseas eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print(f"El contacto {nombre} no está en la agenda.")

# Función principal
def principal():
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            insertar_contacto()
        elif opcion == '2':
            buscar_contacto()
        elif opcion == '3':
            actualizar_contacto()
        elif opcion == '4':
            eliminar_contacto()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")


principal()
print(contactos)