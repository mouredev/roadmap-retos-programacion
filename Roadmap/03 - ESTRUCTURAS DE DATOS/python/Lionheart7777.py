"""
ESTRUCTURAS
"""

# listas
my_list = ["Brais", "Bl4ck", "Wolfy", "Visions"]
print(my_list)
my_list.append("Castor")  # Inserción
my_list.append("Castor")
print(my_list)
my_list.remove("Brais")  # Eliminación
print(my_list)
print(my_list[1])  # acceso
my_list[1] = "Cuervillo"  # Actualización
print(my_list)
my_list.sort()  # Ordenación
print(my_list)


# TUPLAS
my_tuple: tuple = ("Brais", "Moure", "@mouredev", "36")
print(my_tuple[1])  # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)
print(type(my_tuple))

# SETS
my_set = {"Brais", "Moure", "@mouredev", "36"}
print(my_set)
my_set.add("mouredev@gmail.com")  # Inserción
my_set.add("mouredev@gmail.com")  # NO admite duplicados
print(my_set)
my_set.remove("Moure")  # Eliminación
print(my_set)
my_set = set(sorted(my_set))  # NO se puede ordenar
print(my_set)
print(type(my_set))

# DICTIONARY
my_dict: dict = {"name": "Brais", "surname": "Moure", "alias": "@mouredev", "age": "36"}

my_dict["email"] = "mouredev@gmail.com"  # Inserción
print(my_dict)
del my_dict["surname"]  # Eliminación
print(my_dict)
print(my_dict["name"])  # Acceso
my_dict["age"] = "37"  # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # Ordenación
print(my_dict)
print(type(my_dict))

"""
EXTRA
"""


def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el número del contacto : ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print("Debes introducir un # con menos de 12 dígitos")

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input(" Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f" El número de teléfono de {name} es {agenda[name]}")
                else:
                    print(f"El contacto {name} no existe ")
            case "2":
                name = input("Introduce el nombre del contacto : ")
                insert_contact()
            case "3":
                name = input(" Introduce el nombre del contacto : ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe ")
            case "4":
                name = input(" Introduce el nombre del contacto a eliminar : ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe ")
            case "5":
                print("Saliendo de la Agenda")
                break
            case _:
                print("Opción no válida. Elije una opción del 1 al 5")


my_agenda()
