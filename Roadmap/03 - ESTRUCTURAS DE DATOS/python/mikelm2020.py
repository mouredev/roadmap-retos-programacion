# Estructuras de datos
# Diccionarios


def dictionary_structure():
    cubes = {x: x**3 for x in range(1, 11)}
    print(f"El diccionario de cubos es: {cubes}")

    # Inserción
    cubes[11] = 11**3
    print("Se inserta la llave 11 para obtener su cubo:")
    print(cubes)

    # Borrado
    # Elimina con pop la clave 5
    cubes.pop(5)
    print("Elimina con el método pop la clave 5 del diccionario cubes")
    print(cubes)

    # Elimina con popitem el último par clave: valor
    cubes.popitem()
    print(
        "Elimina con el método popitem el último par clave: valor del diccionario cubes"
    )
    print(cubes)

    # Elimina con del par clave:valor de clave 7
    del cubes[7]
    print(
        "Elimina con el método del el par clave: valor del diccionario cubes con clave 7"
    )
    print(cubes)

    # Modificación
    # Asignar el valor 50 a la clave 3
    cubes[3] = 50
    print("Asignar el valor 50 a la clave 3")
    print(cubes)

    # Ordenación
    # Orden ascendente
    print("Orden ascendente")
    print(dict(sorted(cubes.items())))

    # Orden descendente
    print("Orden descendente")
    print(dict(sorted(cubes.items(), reverse=True)))

    # Elimina todos los elementos del diccionario
    cubes.clear()
    print("Elimina todos los elementos del diccionario")
    print(cubes)


# Listas
def list_structure():
    squares = [x**2 for x in range(1, 11)]
    print(f"La lista de cuadrados es: {squares}")

    # Inserción
    # Inserta el cuadrado de 11 con append
    squares.append(11**2)
    print("Inserta el cuadrado de 11 con el método append")
    print(squares)

    # Inserta el cuadrado de 12 despues del indice 3
    squares.insert(3, 12**2)
    print("Inserta el cuadrado de 12 despues del indice 3")
    print(squares)

    # Borrado
    # Quita el item de la lista con valor 81
    squares.remove(81)
    print("Quita el item de la lista con valor 81")
    print(squares)

    # Quita el item de la posición 2 de la lista
    squares.pop(2)
    print("Quita el item de la posición 2 de la lista")
    print(squares)

    # Quita el último item de la lista
    squares.pop()
    print("Quita el último item de la lista")
    print(squares)

    # Actualización
    # Actualiza con el valor 30 el item de la posición 4 de la lista
    squares[4] = 30
    print("Actualiza con el valor 30 el item de la posición 4 de la lista")
    print(squares)

    # Ordenación
    # Odenación ascendente
    squares.sort()
    print("Odenación ascendente")
    print(squares)

    # Odenación descendente
    print("Odenación descendente")
    print(sorted(squares, reverse=True))

    # Eliminación total de los items de la lista
    squares.clear()
    print("Eliminación total de los items de la lista")
    print(squares)


def set_structure():
    # Conjuntos sets
    letters = set(["a", "b", "c", "d", "e"])
    print(f"El conjunto letters es: {letters}")

    # Inserción
    # Inserta la letra f al Conjunto con add
    letters.add("f")
    print("Inserta la letra f al Conjunto con el método add")
    print(letters)

    # Inserta las letras que no se repiten en el conjunto, de la lista siguiente:
    # ['c', 'd', 'e', 'f', 'g', 'h', 'i']
    other_list = ["c", "d", "e", "f", "g", "h", "i"]
    letters.update(other_list)
    print("Inserta las letras que no se repiten en el conjunto, de la lista siguiente:")
    print(other_list)
    print(letters)

    # Borrado
    # Borra la letra h con remove
    letters.remove("h")
    print("Borra la letra h con el método remove")
    print(letters)

    # Borra la letra e con discard
    letters.discard("e")
    print("Borra la letra e con discard")
    print(letters)

    # Borra una letra aleatoriamente
    letters.pop()
    print("Borra una letra aleatoriamente")
    print(letters)

    # Ordenación
    # Orden ascendente
    print("Orden ascendente")
    print(set(sorted(letters)))

    # Orden descendente
    print("Orden descendente")
    print(set(sorted(letters, reverse=True)))

    # Borrado total de elementos
    letters.clear()
    print("Borrado total de elementos")
    print(letters)

    # Tuplas


def tuple_structure():
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_tuple = tuple(numbers_list)
    print("Las listas son estructuras de datos mutables")
    print(numbers_list)
    print(
        "Las tuplas son estructuras de datos inmutables por lo tanto no se pueden modificar una vez creadas"
    )
    print(numbers_tuple)

    # Ordenación
    # Orden ascendente
    print("Orden ascendente")
    print(tuple(sorted(numbers_tuple)))

    # Orden descendente
    print("Orden descendente")
    print(tuple(sorted(numbers_tuple, reverse=True)))


def add_contact(name):
    phone = input("Registra el teléfono del contacto: ")
    if validate_phone(phone):
        diary_object[name] = phone
    else:
        print("El teléfono es inválido")

    print(diary_object)


def find_contact(name):
    if name in diary_object:
        print(f"Nombre: {name} Teléfono: {diary_object[name]} ")
    else:
        print("Contacto inexistente")


def update_contact(name):
    if name in diary_object:
        phone = input("Registra el nuevo teléfono del contacto: ")
        if validate_phone(phone):
            diary_object[name] = phone
        else:
            print("El teléfono es inválido")
    else:
        print("Contacto inexistente")

    print(diary_object)


def delete_contact(name):
    if name in diary_object:
        del diary_object[name]
        print("Contacto eliminado correctamente")
    else:
        print("Contacto inexistente")

    print(diary_object)


def validate_name(name):
    return name.isalpha() and len(name) >= 3


def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10


diary_object = {}


def diary():
    while True:
        print(
            """
    A G E N D A   D E   C O N T A C T O S
            Selecciona una opción:
            1. - Agregar un contacto
            2. - Buscar un contacto
            3. - Actualizar un contacto
            4. - Eliminar un contacto
            5. - Salir de la Agenda
            """
        )
        response = input("Opción deseada: ")
        match response:
            case "1":
                name = input("Introduce el nombre del contacto ")
                if validate_name(name):
                    add_contact(name.capitalize())
                else:
                    print("Nombre invalido del contacto")
            case "2":
                name = input("Introduce el nombre del contacto a buscar ")
                if validate_name(name):
                    find_contact(name.capitalize())
                else:
                    print("Nombre invalido del contacto")
            case "3":
                name = input("Introduce el nombre del contacto a actualizar ")
                if validate_name(name):
                    update_contact(name.capitalize())
                else:
                    print("Nombre invalido del contacto")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar ")
                if validate_name(name):
                    delete_contact(name)
                else:
                    print("Nombre invalido del contacto")
            case "5":
                break
            case _:
                print("Opción inválida: Debe ser del 1 al 5")


if __name__ == "__main__":
    dictionary_structure()
    list_structure()
    set_structure()
    tuple_structure()
    diary()
