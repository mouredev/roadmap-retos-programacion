EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.

# Crear una lista array
mi_lista = [1, 2, 3, 4, 5]

# Agregar un elemento al final de la lista
mi_lista.append(6)

# Insertar un elemento en una posición específica
mi_lista.insert(2, 10)

# Eliminar un elemento por valor
mi_lista.remove(3)

# Eliminar un elemento por índice
del mi_lista[1]

# Actualizar un elemento por índice
mi_lista[0] = 100

# Ordenar la lista de forma ascendente
mi_lista.sort()

# Ordenar la lista de forma descendente
mi_lista.sort(reverse=True)

# Crear un conjunto de lista
mi_conjunto = {1, 2, 3, 4, 5}

# Agregar un elemento al conjunto
mi_conjunto.add(6)

# Eliminar un elemento por valor
mi_conjunto.remove(3)

# Eliminar un elemento de forma segura si existe
mi_conjunto.discard(10)

# Crear un diccionario con clave:valor
mi_diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Ciudad de México"}

# Agregar una nueva clave-valor al diccionario
mi_diccionario["ocupacion"] = "Estudiante"

# Eliminar una clave-valor por clave
del mi_diccionario["edad"]


# Actualizar el valor de una clave
mi_diccionario["nombre"] = "Carlos"

   
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.

list_peoples = []


def is_duplicate(name, lastname, phone):
    newName = name.strip().capitalize()
    newLastname = lastname.strip().capitalize()
    newPhone = phone.strip()

    for people in list_peoples:
        if (
            people["name"] == newName
            and people["lastname"] == newLastname
            and people["phone"] == newPhone
        ):
            return True
    return False


def add_people():
    name = input('Ingrese el nombre: ').strip()
    lastname = input('Ingrese el apellido: ').strip()
    phone = input('Ingrese el numero de telefono: ').strip()

    if not phone.isdigit() or len(phone) > 11:
        print('Número de teléfono no válido. Debe ser numérico y tener hasta 11 dígitos.')
        return

    if is_duplicate(name, lastname, phone):
        print('El nombre, apellido y telefono ya existen, ingrese otro.')
    else:
        newName = name.strip().capitalize()
        newLastname = lastname.strip().capitalize()
        newPhone = phone.strip()

        list_peoples.append({'name': newName, 'lastname': newLastname, 'phone': newPhone})
        print(f'El nombre {newName} y el apellido {newLastname} se han registrado.')


def show():
    print("Lista de personas:")
    for person in list_peoples:
        print(f"Nombre: {person['name']}, Apellido: {person['lastname']}, Telefono:{person['phone']}")


while True:
    add_people()

    next_input = input('Desea ingresar otro nombre y apellido? (s/n): ')
    if next_input.lower() == 'n':
        break
    elif next_input.lower() == 's':
        wish = input('¿Que desea hacer ahora? Ingresar otro nombre (i), Ver (v), actualizar(a), o borrar(b): ')

        if wish.lower() == 'v':
            show()
        elif wish.lower() == 'i':
            add_people()
        elif wish.lower() == 'a':
            show()
            input_to_update = input("¿Cuál quieres actualizar?")

            for person in list_peoples:
               if person['name'] == input_to_update:
                  print("Seleccione el campo que desea actualizar:")
                  print("1. Nombre")
                  print("2. Apellido")
                  print("3. Teléfono")
            
                  choice = input("Ingrese el número del campo a actualizar: ")
                     if choice == "1":
                        new_data = input("Ingrese el nuevo nombre: ")
                        person['name'] = new_data
                     elif choice == "2":
                        new_data = input("Ingrese el nuevo apellido: ")
                        person['lastname'] = new_data
                     elif choice == "3":
                        new_data = input("Ingrese el nuevo número de teléfono: ")
                        person['phone'] = new_data
                     else:
                         print("Opción no válida. No se realizó ninguna actualización.")


        elif wish.lower() == 'b':
            show()
            input_to_delete = input("¿Cuál quieres borrar?")
            list_peoples = [person for person in list_peoples if person['name'] != input_to_delete]
        else:
            print("La opción elegida no es correcta.")
    else:
        print("La opción elegida no es correcta.")


