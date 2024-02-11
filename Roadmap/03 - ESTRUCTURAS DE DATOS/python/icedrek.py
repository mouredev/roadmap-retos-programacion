"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""
# LISTAS (list)
# Lista de elementos, puede contener varios tipos. Ordenada, mutable y admite duplicados
variable_lista: list = [1, 2, "3"]

# - Insercion
#   - Insertar valor al final de la lista
variable_lista.append(4)
#   - Insertar otra lista al final de la lista
variable_lista.extend([5, 6])
#   - los dos anteriores se pueden hacer tambien asi:
variable_lista += [7]
#   - Inserta valor(4) en el indice indicado(6)
variable_lista.insert(6, 4)

# - Borrado
#   - Borra el primer valor que coincida
variable_lista.remove(4)
#   - Borra el valor que se encuentra en el indice indicado
del variable_lista[2]
#   - Borra el valor que se encuentra en el indice indicado.
#   - Si no se pone nada borra el último elemento
variable_lista.pop()

# - Actualizacion
#   - Se actualiza el indice(3) con el valor indicado(9)
variable_lista[3] = 9

# - Ordenacion
variable_lista.sort()  # Orden ascendente
variable_lista.sort(reverse=True)  # Orden descendente

# CONJUNTOS (set)
# Lista de elementos, puede contener varios tipos. Desordenada, inmutable y no admite duplicados
variable_set: set = {1, 3, 5}
variable_set2 = {6, 7}
variable_set3 = {2, 4}

# - Insercion
#   - Insertar un valor
variable_set.add(4)
#   - Insertar varios valores
variable_set.update([9, 8, 7])
variable_set.union(variable_set3)
#   - insertar un conjunto(set) a otro conjunto(set)
variable_set |= variable_set2

# - Borrado
#   - Elimina el valor especificado
variable_set.remove(3)
variable_set.discard(8)
#   - Elimina un valor aleatorio
variable_set.pop()
#   - Eliminar valores que existan en otro conjunto
variable_set -= variable_set2
variable_set = variable_set.difference(variable_set3)
#   - Elimina todos los valores del conjunto
variable_set.clear()
# - Actualizacion - No se hace
# - Ordenacion - No se hace


# TUPLAS (tuple)
# Lista de elementos, puede contener varios tipos. Ordenada, inmutable y admite duplicados
variable_tupla: tuple = (1, "2", 3)

# - Insercion
#   - Insertar valores al final de la tupla
variable_tupla += (4, 5, 6)
#   - Insertar valores en un lugar concreto de la tupla
variable_tupla = variable_tupla[:2] + (11,) + variable_tupla[2:]

# - Borrado
#   - Eliminar un elemento segun el indice
variable_tupla = variable_tupla[:4] + variable_tupla[4 + 1:]

# - Actualizacion
#   - Actualiza un elemento segun indice
variable_tupla = variable_tupla[:2] + (9,) + variable_tupla[2 + 1:]

#   - Ordenacion. No se hace


# DICCIONARIOS(dictionary)
# lista de clave:valor. Ordenada, mutable y no admite duplicados
variable_diccionario: dict = {"letra1": "a", "letra2": "b", "letra3": "c"}
variable_diccionario2 = dict([("numero1", 1), ("numero2", 2)])
variable_diccionario3 = dict(letra1="z", letra4="d", letra5="e")

# - Insercion
#   - Inserta un elemento en el diccionario
variable_diccionario["letra6"] = "f"
# - Borrado
#   - Borra el par asociado a la clave indicada
variable_diccionario2.pop("numero1")
#   - Borra un par aleatorio
variable_diccionario3.popitem()
#   - Borra todos los elementos
variable_diccionario2.clear()
# - Actualizacion
#   - Actualiza un valor existente
variable_diccionario["letra1"] = "h"
#   - Actualiza los valores que existen en el primer diccionario con los valores del segundo.
#   - Si alguno de los valores del segundo no esta en el primere, se añaden
variable_diccionario.update(variable_diccionario3)

# - Ordenacion
variable_diccionario = dict(sorted(variable_diccionario.items()))

# NOTA: Se puede obtener una lista de todas las claves con .keys() y de todos los valores con .values()


# EJERCICIO EXTRA
import os
import time

db_contacts: dict = {}


def contacts():
    while True:
        time.sleep(1.5)

        option = main_menu()

        if option == 0:
            continue
        elif option == 1:
            insert_contact()
        elif option == 2:
            select_contact()
        elif option == 3:
            update_contact()
        elif option == 4:
            delete_contact()
        elif option == 5:
            select_all_contacts()
        else:
            break


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    clear_screen()

    print("1-Añadir contacto")
    print("2-Consultar contacto")
    print("3-Modificar contacto")
    print("4-Borrar contacto")
    print("5-Listar todos los contactos")
    print("6-Salir\n")

    option = validate_option(input("Selecciona una opción: "))

    return option


def validate_option(option):
    if option.isnumeric():
        if int(option) in range(1, 7):
            return int(option)
        else:
            print("introduce una opcion del 1 al 6")
    else:
        print("El valor introducido no es numérico")

    return 0


def insert_contact():
    contact_name = input("Introduce nombre del contacto: ")
    contact_phone = validate_phone(input("Introduce telefono del contacto: "))

    if contact_name in db_contacts:
        print("El contacto ya existe en la agenda")
        return

    if contact_phone != 0:
        db_contacts[contact_name] = contact_phone
        print(f"Contacto añadido: {contact_name} - {contact_phone}")


def select_contact():
    contact_name = input("Introduce nombre del contacto: ")
    if contact_name not in db_contacts:
        print("No se ha encontrado el contacto")
        return

    contact_phone = db_contacts[contact_name]
    print(f"Contacto: {contact_name} - Telefono: {contact_phone}")
    time.sleep(1.5)


def update_contact():
    contact_name = input("Introduce nombre del contacto a modificar: ")
    contact_new_phone = input("Introduce nuevo telefono del contacto: ")

    contact_old_phone = db_contacts[contact_name]

    if contact_old_phone == contact_new_phone:
        print("Telefono antiguo y nuevo son el mismo, no se actualiza")
        return

    db_contacts[contact_name] = contact_new_phone
    print("Contacto modificado")


def delete_contact():
    contact_name = input("Introduce nombre del contacto a eliminar: ")

    if contact_name not in db_contacts:
        print("El contacto no existe en la agenda")
        return

    db_contacts.pop(contact_name)
    print("Contacto borrado")


def select_all_contacts():
    db_contacts_sorted = dict(sorted(db_contacts.items()))

    for contact in db_contacts_sorted:
        print(f"Contacto: {contact} - Telefono: {db_contacts[contact]}")

    time.sleep(3)


def validate_phone(contact_phone):
    if contact_phone.isnumeric():
        return int(contact_phone)
    else:
        print("Debes introducir un número válido")

    if len(contact_phone) == 9:
        print("El numero debe tener 9 dígitos")

    return 0


contacts()
