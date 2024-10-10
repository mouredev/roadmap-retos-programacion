# Estructuras de datos

# Listas

# Crear una lista de numeros del 0 al 4
my_list = list(range(5))
print(my_list)

my_list.append(5)  # Añadir un elemento a la lista al final
my_list.insert(8, 0)  # Añadir elemento en la posición indexada
print(my_list)

print(my_list[2])  # Llama al elemento en el indice 2

print(my_list.count(0))  # Funcion para contar cuantos elementos n hay

my_list.remove(0)  # Elimina el primer elemento en la lista con ese valor
print(my_list)

my_list.pop()  # Devuelve y saca de la lista el ultimo elemento
print(my_list)

my_list.sort()  # Ordena la lista
print(my_list)

# Tuplas
# Crear una tupla
my_tuple: tuple = ("Diego", "DevsDav")
print(my_tuple[1])  # Acceso
index_devsdav = my_tuple.index("DevsDav")  # Acceder al indice del argumento
print(index_devsdav)
my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)

# Set
my_set: set = {"Diego", "Arenas", "Devsdav", "27"}
print(my_set)
my_set.add("DAVstudy")  # Inserción
my_set.add("DAVstudy")
print(my_set)
my_set.remove("Arenas")  # Eliminación
print(my_set)

# Dict
my_dict: dict = {
    "name": "Diego",
    "surname": "Arenas",
    "alias": "Devsdav",
    "age": 27
    }
print(my_dict)
name = my_dict["name"]  # Acceso al valor de la key "name"
print(name)
my_dict["email"] = "devsdav@devsdav.dev"  # Inserción
print(my_dict)
print(my_dict.keys())  # Acceso a una lista con todas las llaves
print(my_dict.values())  # Acceso a una lista con todos los valores
print(my_dict.items())  # Acceso a una lista con tuplas de pares llave-valor

my_dict = dict(sorted(my_dict.items()))  # Ordenacion
print(my_dict)
del my_dict  # Eliminación


"""
Ejercicio extra
"""


def agenda():

    agenda = {}

    def insert_contact():

        contact_name = input("Ingrese el nombre del nuevo contacto: ")
        if contact_name in agenda:
            print("Error el nombre ya existe, intente nuevamente")
        else:
            phone = input("Ingrese el número de contacto: ")

            if phone.isalnum and len(phone) < 11:
                agenda[contact_name] = phone
            else:
                print("Error al ingresar el numero")

    def delete_contact():

        contact_name = input("""
        Ingrese el nombre del contacto que desea eliminar:
        """)
        if contact_name in agenda:
            del agenda[contact_name]
        else:
            print("Error no existe contacto con ese nombre")

    def update_contact():

        option = input("""
Presione la opcion que desea actualizar:
1. Actualizar nombre de contacto.
2. Actualizar número de contacto.
        """)

        match option:

            case "1":
                contact_name = input("Ingrese el nombre actual del contacto: ")

                if contact_name in agenda:
                    new_name = input("Ingrese el nuevo nombre: ")
                    agenda[new_name] = agenda[contact_name]
                    del agenda[contact_name]
                else:
                    print("Error contacto no existe")

            case "2":
                contact_name = input("Ingrese el nombre actual del contacto: ")

                if contact_name in agenda:

                    phone = input("Ingrese el nuevo número: ")

                    if phone.isalnum and len(phone) < 11:
                        agenda[contact_name] = phone
                        return
                    else:
                        print("Error al ingresar el numero")
                        return

    def search_contact():
        contact_name = input("Ingrese el nombre del contacto que busca: ")
        if contact_name in agenda:
            print(f"Se encontro el contacto {contact_name} y su numero es: {agenda[contact_name]}")
        else:
            print("Error contacto no existe")

    close = False

    while (not close):
        option = input("""
    Presione la opcion que desea:
    1. Ingresar nuevo contacto
    2. Actualizar contacto
    3. Buscar contacto
    4. Eliminar contacto
    5. Mostrar todos los contactos
    6. Salir
        """)

        match option:

            case "1":
                insert_contact()
            case "2":
                update_contact()
            case "3":
                search_contact()
            case "4":
                delete_contact()
            case "5":
                print(agenda)
            case "6":
                close = True
            case _:
                continue


agenda()
